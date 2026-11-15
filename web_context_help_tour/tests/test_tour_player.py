# -*- coding: utf-8 -*-
#
# Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
#
# License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
#
import os
from odoo.tests import common

# PhantomJS of the browser tests (Odoo 10 HttpCase.phantom_js): the copy that
# before_test.sh installs in tests/.phantomjs/, run through tests/test_bin/phantomjs.
# The PATH is touched only when that local copy exists, so without it Odoo keeps
# skipping the test ("PhantomJS not found") instead of failing it.
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if os.access(os.path.join(TESTS_DIR, ".phantomjs", "bin", "phantomjs"), os.X_OK):
    os.environ["PATH"] = (
        os.path.join(TESTS_DIR, "test_bin") + os.pathsep + os.environ.get("PATH", "")
    )

# Plays a tour in the real web client (PhantomJS: ES5 only): the steps are
# those the help window sends, the checks read the player DOM. The harness of
# Odoo 10 (phantomtest.js) ends on console.log("ok"), or on a console line
# starting with "error": an exception in a timer is not always reported by
# PhantomJS, so a failure is logged before being thrown.
PLAYER_JS = r"""
(function () {
    var fail = function (msg) {
        // what is on screen: the view and its first named elements
        var view = $(".o_form_view, .o_list_view, .o_kanban_view");
        var named = view ? view.querySelectorAll("[name]") : [];
        msg += " | hash=" + window.location.hash + " view="
            + (view ? view.className : "none") + " named="
            + [].map.call([].slice.call(named, 0, 12), function (el) {
                return el.tagName + "." + el.className
                    + "[" + el.getAttribute("name") + "]";
            }).join(" ");
        console.log("error tour player: " + msg);
        throw new Error("tour player: " + msg);
    };
    var $ = function (sel) { return document.querySelector(sel); };
    var when = function (check, what, done, tries) {
        tries = tries || 0;
        if (check()) {
            return done();
        }
        if (tries > 100) {
            fail("timeout waiting for " + what);
        }
        setTimeout(function () { when(check, what, done, tries + 1); }, 100);
    };
    var service = window.wchHelpTour;
    var steps = [
        {target: "new", click: true, position: "auto",
         html: "<p>Press <strong>New</strong><script>window.bad = 1</script>"
             + "<a class='wch-field' href='#'>here</a></p>"},
        {target: "field:name", click: false, position: "right", html: "<p>Name</p>"},
        {target: "css:.no_such_element", click: false, position: "auto", html: "x"}
    ];
    when(function () { return $(".o-kanban-button-new, .o_list_button_add"); },
         "New button", function () {
        service.start("t", steps);
        when(function () { return $(".o_wcht .o_wcht_ring"); }, "player", function () {
            if ($(".o_wcht_count").textContent !== "Step 1 of 3") {
                fail("counter " + $(".o_wcht_count").textContent);
            }
            var body = $(".o_wcht_body");
            if (body.querySelector("script, a")
                    || body.textContent !== "Press Newhere") {
                fail("text not sanitized: " + body.innerHTML);
            }
            when(function () {
                return !$(".o_wcht").classList.contains("o_wcht_waiting");
            }, "New found", function () {
                $(".o_wcht_next").click();
                when(function () {
                    return $(".o_form_view [data-wch-field='name'],"
                             + " .o_form_view .o_field_widget[name='name']");
                }, "form", function () {
                    when(function () {
                        return !$(".o_wcht").classList.contains("o_wcht_waiting");
                    }, "name field", function () {
                        $(".o_wcht_next").click();
                        when(function () {
                            return $(".o_wcht").classList.contains("o_wcht_waiting");
                        }, "waiting", function () {
                            if ($(".o_wcht_next").textContent !== "Finish") {
                                fail("Finish label");
                            }
                            $(".o_wcht_prev").click();
                            when(function () {
                                return $(".o_wcht_count").textContent === "Step 2 of 3";
                            }, "Previous", function () {
                                $(".o_wcht_stop").click();
                                if ($(".o_wcht")) {
                                    fail("Stop left the player");
                                }
                                if (window.bad) {
                                    fail("script of a step was run");
                                }
                                console.log("ok");
                            });
                        });
                    });
                });
            });
        });
    });
})();
"""


class TestTourPlayer(common.HttpCase):
    def test_player(self):
        self.phantom_js(
            "/web#action=base.action_partner_form",
            PLAYER_JS,
            ready="window.wchHelpTour",
            login="admin",
            timeout=120,
        )
