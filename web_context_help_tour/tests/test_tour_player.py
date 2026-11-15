# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
import os
from unittest import mock

from odoo.tests import HttpCase, common, tagged
from odoo.tools import config

# Chrome of the browser tests: tests/chrome_bin/google-chrome, see before_test.sh
CHROME_BIN_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "chrome_bin"
)
os.environ["PATH"] = CHROME_BIN_DIR + os.pathsep + os.environ.get("PATH", "")

# Plays a tour in the real web client: the steps are those the help window
# sends, the checks read the player DOM. The harness of Odoo 12 ends on
# console.log("ok"), or on a console line starting with "error": anything else
# is a timeout
PLAYER_JS = r"""
(async () => {
    const fail = (msg) => { throw new Error("tour player: " + msg); };
    const until = async (check, what) => {
        for (let i = 0; i < 100; i++) {
            if (check()) {
                return;
            }
            await new Promise((r) => setTimeout(r, 100));
        }
        fail("timeout waiting for " + what);
    };
    const $ = (sel) => document.querySelector(sel);
    const service = window.wchHelpTour;
    await until(() => $(".o-kanban-button-new, .o_list_button_add"), "New button");
    service.start("t", [
        {target: "new", click: true, position: "auto",
         html: "<p>Press <strong>New</strong><script>window.bad = 1</script>"
             + "<a class='wch-field' href='#'>here</a></p>"},
        {target: "field:name", click: false, position: "right", html: "<p>Name</p>"},
        {target: "css:.no_such_element", click: false, position: "auto", html: "x"},
    ]);
    await until(() => $(".o_wcht .o_wcht_ring"), "player");
    if ($(".o_wcht_count").textContent !== "Step 1 of 3") {
        fail("counter " + $(".o_wcht_count").textContent);
    }
    const body = $(".o_wcht_body");
    if (body.querySelector("script, a") || body.textContent !== "Press Newhere") {
        fail("text not sanitized: " + body.innerHTML);
    }
    if (!body.querySelector("strong") || !$(".o_wcht_prev").disabled) {
        fail("markup or Previous");
    }
    await until(() => !$(".o_wcht").classList.contains("o_wcht_waiting"), "New found");
    // :click: Next presses New, the step waits for the form
    $(".o_wcht_next").click();
    await until(() => $(".o_form_view .o_field_widget[name='name']"), "form");
    await until(() => !$(".o_wcht").classList.contains("o_wcht_waiting"), "name field");
    // the ring slides to its target in 0.2s
    await new Promise((r) => setTimeout(r, 500));
    const ring = $(".o_wcht_ring").getBoundingClientRect();
    const field = $(".o_form_view .o_field_widget[name='name']")
        .getBoundingClientRect();
    if (ring.left > field.left || ring.right < field.right
            || ring.top > field.top || ring.bottom < field.bottom) {
        fail("ring does not surround the field: " + JSON.stringify([ring, field]));
    }
    if ($(".o_wcht_pop").dataset.side === undefined) {
        fail("popover not placed");
    }
    // a missing target waits, Next becomes Finish on the last step
    $(".o_wcht_next").click();
    await until(() => $(".o_wcht").classList.contains("o_wcht_waiting"), "waiting");
    if ($(".o_wcht_next").textContent !== "Finish") {
        fail("Finish label");
    }
    $(".o_wcht_prev").click();
    await until(() => $(".o_wcht_count").textContent === "Step 2 of 3", "Previous");
    $(".o_wcht_stop").click();
    if ($(".o_wcht")) {
        fail("Stop left the player");
    }
    // Esc stops too
    service.start("t2", [{target: "save", click: false, html: "<p>x</p>"}]);
    await until(() => $(".o_wcht"), "second tour");
    document.dispatchEvent(
        new KeyboardEvent("keydown", {key: "Escape", bubbles: true})
    );
    if ($(".o_wcht")) {
        fail("Esc did not stop the tour");
    }
    if (window.bad) {
        fail("script of a step was run");
    }
    console.log("ok");
})().catch((err) => console.log("error " + err.message));
"""


@tagged("post_install", "-at_install")
class TestTourPlayer(HttpCase):
    def setUp(self):
        # odoo.tests.common reads PORT when odoo is imported, before the
        # configuration is parsed: it stays 8069 whatever http_port the test
        # server listens on, and the browser opens a page nobody serves
        patcher = mock.patch.object(common, "PORT", config["http_port"])
        patcher.start()
        self.addCleanup(patcher.stop)
        super(TestTourPlayer, self).setUp()

    def test_player(self):
        self.browser_js(
            "/web#action=base.action_partner_form",
            PLAYER_JS,
            ready="Boolean(window.wchHelpTour)",
            login="admin",
            timeout=120,
        )
