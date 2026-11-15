# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
import os
from odoo.tests import HttpCase, tagged

# Chrome of the browser tests: tests/chrome_bin/google-chrome, see before_test.sh
CHROME_BIN_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "chrome_bin"
)
os.environ["PATH"] = CHROME_BIN_DIR + os.pathsep + os.environ.get("PATH", "")

# Plays a tour in the real web client: the steps are those the help window
# sends, the checks read the player DOM
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
    const service = odoo.__WOWL_DEBUG__.root.env.services.context_help_tour;
    if (!service) {
        fail("service context_help_tour not started");
    }
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
    const field = $(
            ".o_form_view .o_field_widget[name='name']").getBoundingClientRect();
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
    document.dispatchEvent(new KeyboardEvent(
            "keydown", {key: "Escape", bubbles: true}));
    if ($(".o_wcht")) {
        fail("Esc did not stop the tour");
    }
    if (window.bad) {
        fail("script of a step was run");
    }
    console.log("test successful");
})();
"""


# Plays the steps of the contact search tour (help_res_partner): the Filters
# menu opened by the tour must stay open while the user presses Next
SEARCH_JS = r"""
(async () => {
    const fail = (msg) => { throw new Error("search tour: " + msg); };
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
    const found = () => !$(".o_wcht").classList.contains("o_wcht_waiting");
    // a real press: pointerdown first (the click-away of the dropdowns), then click
    const press = (el) => {
        el.dispatchEvent(new PointerEvent("pointerdown", {
            bubbles: true, cancelable: true
        }));
        el.click();
    };
    const surrounds = async (sel) => {
        await new Promise((r) => setTimeout(r, 500)); // the ring slides in 0.2s
        const ring = $(".o_wcht_ring").getBoundingClientRect();
        const box = $(sel).getBoundingClientRect();
        if (ring.left > box.left + 1 || ring.right < box.right - 1
                || ring.top > box.top + 1 || ring.bottom < box.bottom - 1) {
            fail("ring does not surround " + sel);
        }
    };
    const service = odoo.__WOWL_DEBUG__.root.env.services.context_help_tour;
    await until(() => $(".o_searchview_dropdown_toggler"), "search bar");
    service.start("res_partner_search", [
        {target: "filters", click: true, position: "auto", html: "<p>Open</p>"},
        {target: "css:.o_filter_menu",
         click: false, position: "auto", html: "<p>Companies</p>"},
        {target: "css:.o_add_custom_filter",
         click: false, position: "auto", html: "<p>Custom</p>"},
        {target: "search", click: false, position: "bottom", html: "<p>Type</p>"},
    ]);
    await until(() => $(".o_wcht .o_wcht_ring") && found(), "filters toggler");
    if ($(".o_filter_menu")) {
        fail("Filters menu open before Next");
    }
    // step 1, :click: Next opens the Filters menu
    press($(".o_wcht_next"));
    await until(() => $(".o_filter_menu"), "Filters menu");
    await until(() => $(
            ".o_wcht_count").textContent === "Step 2 of 4" && found(), "step 2");
    await surrounds(".o_filter_menu");
    // the user chooses Companies: the facet is shown, the menu stays open
    const companies = [...document.querySelectorAll(".o_filter_menu .o_menu_item")]
        .find((el) => el.textContent.trim() === "Companies");
    if (!companies) {
        fail("no Companies filter");
    }
    companies.click();
    await until(() => [...document.querySelectorAll(".o_searchview_facet")]
        .some((el) => el.textContent.includes("Companies")), "Companies facet");
    // Next on the popover is not a click away: the menu stays open
    press($(".o_wcht_next"));
    await until(() => $(".o_wcht_count").textContent === "Step 3 of 4", "step 3");
    if (!$(".o_filter_menu")) {
        fail("Next closed the Filters menu");
    }
    await until(found, "Add Custom Filter");
    await surrounds(".o_add_custom_filter");
    press($(".o_wcht_next"));
    await until(() => $(
            ".o_wcht_count").textContent === "Step 4 of 4" && found(), "step 4");
    await surrounds(".o_searchview");
    if ($(".o_wcht_next").textContent !== "Finish") {
        fail("Finish label");
    }
    // a press outside the popover still closes the menu
    press(document.body);
    await until(() => !$(".o_filter_menu"), "menu closed by a click away");
    press($(".o_wcht_next"));
    if ($(".o_wcht")) {
        fail("Finish left the player");
    }
    console.log("test successful");
})();
"""


@tagged("post_install", "-at_install")
class TestTourPlayer(HttpCase):
    def test_player(self):
        self.browser_js(
            "/odoo/action-base.action_partner_form",
            PLAYER_JS,
            ready="Boolean(odoo.__WOWL_DEBUG__ && odoo.__WOWL_DEBUG__.root)",
            login="admin",
            timeout=120,
        )

    def test_search_tour(self):
        self.browser_js(
            "/odoo/action-base.action_partner_form",
            SEARCH_JS,
            ready="Boolean(odoo.__WOWL_DEBUG__ && odoo.__WOWL_DEBUG__.root)",
            login="admin",
            timeout=120,
        )
