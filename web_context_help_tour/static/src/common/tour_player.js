/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * Tour player of the help pages, played in the Odoo tab (legacy web client:
 * odoo.define, no ES modules). The help window sends the steps written in
 * the page (target, text); each step dims the screen around its target,
 * rings it and explains it in a popover with the Previous / Next / Stop
 * buttons. The dimmed screen still takes clicks: the user does the work, the
 * tour only shows where.
 *
 * The selectors of the short targets (new, save, ...) are written for the
 * web client of Odoo 10 and 12, both listed: the first one on screen is used.
 */
odoo.define("web_context_help_tour.tour_player", function (require) {
    "use strict";

    var core = require("web.core");
    var _t = core._t;

    // Name of the help window, set by web_context_help
    var HELP_WINDOW_NAME = "odoo_help";
    var MESSAGE_TYPE = "wch_help_tour";
    // Sent back to the help window when a tour stops (Finish, Stop, Esc)
    var END_TYPE = "wch_tour_end";
    // Room around the target and between the target and the popover
    var PADDING = 6;
    var GAP = 12;
    var MARGIN = 8;
    // A missing target is looked for again every RESOLVE_MS
    var RESOLVE_MS = 250;

    // Short targets of help-step: the control panel buttons
    var ALIASES = {
        new: ".o_list_button_add, .o-kanban-button-new, .o_form_button_create",
        save: ".o_form_button_save",
        discard: ".o_form_button_cancel",
        search: ".o_searchview",
        filters: ".o_searchview_more",
        actions: ".o_cp_buttons .dropdown-toggle",
        breadcrumb: ".o_breadcrumb",
        statusbar: ".o_statusbar_status",
    };

    // Inline markup kept in the text of a step; any other tag is dropped and
    // its text kept, e.g. the :field: links of the help page
    var ALLOWED_TAGS = {
        P: true,
        STRONG: true,
        EM: true,
        B: true,
        I: true,
        CODE: true,
        KBD: true,
        BR: true,
        UL: true,
        OL: true,
        LI: true,
        SPAN: true,
    };
    var DROPPED_TAGS = {SCRIPT: true, STYLE: true, TEMPLATE: true};

    function isVisible(el) {
        if (!el.isConnected || el.closest(".o_wcht")) {
            return false;
        }
        var rect = el.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0;
    }

    function visibleIn(selector) {
        var found;
        try {
            found = document.querySelectorAll(selector);
        } catch (e) {
            return []; // invalid css: target of the help page
        }
        return [].filter.call(found, isVisible);
    }

    // Label of a form field: through the id of its focusable element, or the
    // label cell of the same group row (a readonly widget has no id)
    function fieldLabels(widget) {
        var labels = [];
        var candidates = [widget].concat([].slice.call(widget.querySelectorAll("[id]")));
        candidates.forEach(function (el) {
            if (el.id) {
                [].push.apply(
                    labels,
                    document.querySelectorAll('label[for="' + CSS.escape(el.id) + '"]')
                );
            }
        });
        var cell = widget.closest(".o_wrap_input");
        var labelCell = cell && cell.previousElementSibling;
        if (labelCell && labelCell.classList.contains("o_wrap_label")) {
            [].push.apply(labels, labelCell.querySelectorAll("label"));
        }
        return labels.filter(isVisible);
    }

    /**
     * Elements shown by a help-step target, the main one first: [] when the
     * target is not on screen
     */
    function resolveTarget(target) {
        if (ALIASES[target]) {
            return visibleIn(ALIASES[target]).slice(0, 1);
        }
        var sep = target.indexOf(":");
        var kind = target.slice(0, sep);
        var value = target.slice(sep + 1).trim();
        var name = CSS.escape(value);
        var widget;
        switch (kind) {
            case "field":
                widget = visibleIn('.o_field_widget[name="' + name + '"]')[0];
                if (widget) {
                    return [widget].concat(fieldLabels(widget));
                }
                // list view: the column header
                return visibleIn('th[data-name="' + name + '"]').slice(0, 1);
            case "button":
                return visibleIn('button[name="' + name + '"]').slice(0, 1);
            case "tab":
                return visibleIn(
                    '.o_notebook .nav-link[name="' + name + '"]'
                ).slice(0, 1);
            case "menu":
                return visibleIn('[data-menu-xmlid="' + name + '"]').slice(0, 1);
            case "css":
                return visibleIn(value).slice(0, 1);
        }
        return [];
    }

    function sanitize(html) {
        var doc = new DOMParser().parseFromString(
            "<div>" + html + "</div>",
            "text/html"
        );
        var out = document.createElement("div");
        var copy = function (src, dst) {
            [].forEach.call(src.childNodes, function (node) {
                if (node.nodeType === Node.TEXT_NODE) {
                    dst.appendChild(document.createTextNode(node.textContent));
                } else if (node.nodeType === Node.ELEMENT_NODE) {
                    if (ALLOWED_TAGS[node.tagName]) {
                        var el = document.createElement(node.tagName);
                        copy(node, el);
                        dst.appendChild(el);
                    } else if (!DROPPED_TAGS[node.tagName]) {
                        copy(node, dst);
                    }
                }
            });
        };
        copy(doc.body.firstElementChild || doc.body, out);
        return out;
    }

    function unionRect(elements) {
        var top = Infinity;
        var left = Infinity;
        var bottom = -Infinity;
        var right = -Infinity;
        elements.forEach(function (el) {
            var r = el.getBoundingClientRect();
            top = Math.min(top, r.top);
            left = Math.min(left, r.left);
            bottom = Math.max(bottom, r.bottom);
            right = Math.max(right, r.right);
        });
        return {
            top: top - PADDING,
            left: left - PADDING,
            bottom: bottom + PADDING,
            right: right + PADDING,
        };
    }

    function make(tag, className, parent) {
        var el = document.createElement(tag);
        if (className) {
            el.className = className;
        }
        if (parent) {
            parent.appendChild(el);
        }
        return el;
    }

    function place(el, top, left, width, height) {
        el.style.top = Math.round(top) + "px";
        el.style.left = Math.round(left) + "px";
        el.style.width = Math.max(0, Math.round(width)) + "px";
        el.style.height = Math.max(0, Math.round(height)) + "px";
    }

    // Text of "Step x of y", translated with its two placeholders in order
    function stepCounter(current, total) {
        return _t("Step %s of %s").replace("%s", current).replace("%s", total);
    }

    function TourPlayer(name, steps) {
        this.name = name;
        this.steps = steps;
        this.index = -1;
        this.elements = [];
        this.lastResolve = 0;
        this.scrolled = false;
        this.frame = null;
        this.onStop = null;
        this.onKeydown = this.onKeydown.bind(this);
        this.onPress = this.onPress.bind(this);
        this.loop = this.loop.bind(this);
        this.build();
    }

    TourPlayer.prototype.build = function () {
        var root = make("div", "o_wcht");
        root.dataset.tour = this.name;
        var self = this;
        this.masks = ["top", "bottom", "left", "right"].map(function (side) {
            return make("div", "o_wcht_mask o_wcht_mask_" + side, root);
        });
        this.ring = make("div", "o_wcht_ring", root);
        var pop = make("div", "o_wcht_pop", root);
        pop.setAttribute("role", "dialog");
        this.arrow = make("div", "o_wcht_arrow", pop);
        var header = make("div", "o_wcht_header", pop);
        this.counter = make("span", "o_wcht_count", header);
        this.closeBtn = make("button", "close o_wcht_close", header);
        this.closeBtn.type = "button";
        this.closeBtn.innerHTML = "&times;";
        this.closeBtn.title = _t("Stop the tour");
        this.closeBtn.setAttribute("aria-label", _t("Stop the tour"));
        this.body = make("div", "o_wcht_body", pop);
        this.note = make("p", "o_wcht_note", pop);
        this.note.textContent = _t(
            "Waiting for this step: open the screen it refers to, or do what the previous step asks."
        );
        var footer = make("div", "o_wcht_footer", pop);
        this.stopBtn = make("button", "btn btn-link o_wcht_stop", footer);
        this.stopBtn.textContent = _t("Stop");
        this.prevBtn = make("button", "btn btn-default o_wcht_prev", footer);
        this.prevBtn.textContent = _t("Previous");
        this.nextBtn = make("button", "btn btn-primary o_wcht_next", footer);
        [this.stopBtn, this.prevBtn, this.nextBtn].forEach(function (btn) {
            btn.type = "button";
        });
        // run by onPress, before the click reaches the Odoo listeners
        this.actions = [
            [this.closeBtn, function () { self.stop(); }],
            [this.stopBtn, function () { self.stop(); }],
            [this.prevBtn, function () { self.go(self.index - 1); }],
            [this.nextBtn, function () { self.next(); }],
        ];
        this.root = root;
        this.pop = pop;
    };

    TourPlayer.prototype.actionOf = function (btn) {
        for (var i = 0; i < this.actions.length; i++) {
            if (this.actions[i][0] === btn) {
                return this.actions[i][1];
            }
        }
        return null;
    };

    TourPlayer.prototype.start = function () {
        document.body.appendChild(this.root);
        window.addEventListener("keydown", this.onKeydown, true);
        // registered before any dropdown opens, so they run before the
        // click-away listeners of the Odoo dropdowns
        window.addEventListener("pointerdown", this.onPress, true);
        window.addEventListener("click", this.onPress, true);
        this.go(0);
        this.frame = window.requestAnimationFrame(this.loop);
    };

    TourPlayer.prototype.stop = function () {
        if (this.frame) {
            window.cancelAnimationFrame(this.frame);
            this.frame = null;
        }
        window.removeEventListener("keydown", this.onKeydown, true);
        window.removeEventListener("pointerdown", this.onPress, true);
        window.removeEventListener("click", this.onPress, true);
        this.root.remove();
        if (this.onStop) {
            this.onStop(this);
        }
    };

    TourPlayer.prototype.onKeydown = function (ev) {
        if (ev.key === "Escape") {
            ev.preventDefault();
            ev.stopPropagation();
            this.stop();
        }
    };

    // A press on the popover is not a click away: an Odoo dropdown opened by
    // the tour, e.g. the Filters menu, stays open for the next step. Odoo
    // closes it on pointerdown and on a keyboard click (Enter on Next), so
    // both stop here, at window capture, and the button action runs here.
    TourPlayer.prototype.onPress = function (ev) {
        var pop =
            ev.target instanceof Element && ev.target.closest(".o_wcht_pop");
        if (!pop) {
            return;
        }
        ev.stopImmediatePropagation();
        if (ev.type === "click") {
            var btn = ev.target.closest("button");
            var action = btn && !btn.disabled && this.actionOf(btn);
            if (action) {
                action();
            }
        }
    };

    TourPlayer.prototype.step = function () {
        return this.steps[this.index];
    };

    TourPlayer.prototype.isLast = function () {
        return this.index === this.steps.length - 1;
    };

    TourPlayer.prototype.go = function (index) {
        if (index < 0 || index >= this.steps.length) {
            return;
        }
        this.index = index;
        this.elements = [];
        this.lastResolve = 0;
        this.scrolled = false;
        this.counter.textContent = stepCounter(index + 1, this.steps.length);
        var content = sanitize(this.step().html || "");
        this.body.innerHTML = "";
        while (content.firstChild) {
            this.body.appendChild(content.firstChild);
        }
        this.prevBtn.disabled = index === 0;
        this.nextBtn.textContent = this.isLast() ? _t("Finish") : _t("Next");
        this.resolve(true);
        this.layout();
        this.nextBtn.focus({preventScroll: true});
    };

    TourPlayer.prototype.next = function () {
        // :click: the tour presses the target for the user, e.g. New
        if (this.step().click && this.elements.length) {
            this.elements[0].click();
        }
        if (this.isLast()) {
            this.stop();
        } else {
            this.go(this.index + 1);
        }
    };

    TourPlayer.prototype.resolve = function (force) {
        var now = Date.now();
        var lost = this.elements.some(function (el) {
            return !isVisible(el);
        });
        if (!force && !lost && this.elements.length) {
            return;
        }
        if (!force && !lost && now - this.lastResolve < RESOLVE_MS) {
            return;
        }
        this.lastResolve = now;
        var found = resolveTarget(this.step().target);
        if (found[0] !== this.elements[0]) {
            this.scrolled = false;
        }
        this.elements = found;
    };

    TourPlayer.prototype.loop = function () {
        this.resolve(false);
        this.layout();
        this.frame = window.requestAnimationFrame(this.loop);
    };

    TourPlayer.prototype.layout = function () {
        var vw = document.documentElement.clientWidth;
        var vh = document.documentElement.clientHeight;
        var waiting = !this.elements.length;
        this.root.classList.toggle("o_wcht_waiting", waiting);
        if (waiting) {
            // Nothing to show: the whole screen is dimmed, popover centered
            place(this.masks[0], 0, 0, vw, vh);
            this.masks.slice(1).forEach(function (mask) {
                place(mask, 0, 0, 0, 0);
            });
            var pw = this.pop.offsetWidth;
            var ph = this.pop.offsetHeight;
            this.pop.style.top = Math.round((vh - ph) / 2) + "px";
            this.pop.style.left = Math.round((vw - pw) / 2) + "px";
            return;
        }
        if (!this.scrolled) {
            this.scrolled = true;
            var first = this.elements[0].getBoundingClientRect();
            if (
                first.top < 0 ||
                first.bottom > vh ||
                first.left < 0 ||
                first.right > vw
            ) {
                this.elements[0].scrollIntoView({
                    block: "center",
                    inline: "nearest",
                });
            }
        }
        var r = unionRect(this.elements);
        var top = Math.max(0, r.top);
        var bottom = Math.min(vh, r.bottom);
        var left = Math.max(0, r.left);
        var right = Math.min(vw, r.right);
        place(this.masks[0], 0, 0, vw, top);
        place(this.masks[1], bottom, 0, vw, vh - bottom);
        place(this.masks[2], top, 0, left, bottom - top);
        place(this.masks[3], top, right, vw - right, bottom - top);
        place(this.ring, r.top, r.left, r.right - r.left, r.bottom - r.top);
        this.placePopover(r, vw, vh);
    };

    TourPlayer.prototype.placePopover = function (r, vw, vh) {
        var pw = this.pop.offsetWidth;
        var ph = this.pop.offsetHeight;
        var room = {
            bottom: vh - r.bottom - GAP,
            top: r.top - GAP,
            right: vw - r.right - GAP,
            left: r.left - GAP,
        };
        var fits = function (side) {
            return side === "top" || side === "bottom"
                ? room[side] >= ph
                : room[side] >= pw;
        };
        var wanted = this.step().position;
        var side = "bottom";
        ["bottom", "top", "right", "left"].some(function (s) {
            if (fits(s)) {
                side = s;
                return true;
            }
            return false;
        });
        if (wanted && wanted !== "auto" && fits(wanted)) {
            side = wanted;
        }
        var cx = (r.left + r.right) / 2;
        var cy = (r.top + r.bottom) / 2;
        var top;
        var left;
        if (side === "bottom" || side === "top") {
            top = side === "bottom" ? r.bottom + GAP : r.top - GAP - ph;
            left = cx - pw / 2;
        } else {
            left = side === "right" ? r.right + GAP : r.left - GAP - pw;
            top = cy - ph / 2;
        }
        left = Math.min(Math.max(MARGIN, left), vw - pw - MARGIN);
        top = Math.min(Math.max(MARGIN, top), vh - ph - MARGIN);
        this.pop.style.top = Math.round(top) + "px";
        this.pop.style.left = Math.round(left) + "px";
        this.pop.setAttribute("data-side", side);
        // The arrow points at the middle of the target
        if (side === "bottom" || side === "top") {
            this.arrow.style.left =
                Math.round(Math.min(Math.max(16, cx - left), pw - 16)) + "px";
            this.arrow.style.top = "";
        } else {
            this.arrow.style.top =
                Math.round(Math.min(Math.max(16, cy - top), ph - 16)) + "px";
            this.arrow.style.left = "";
        }
    };

    // The tour being played, one at a time
    var current = null;

    function startTour(name, steps, helpWindow) {
        if (current) {
            current.stop();
        }
        current = new TourPlayer(name, steps);
        current.onStop = function (player) {
            if (current === player) {
                current = null;
            }
            // the help window gives its tour button back its label
            try {
                if (helpWindow && !helpWindow.closed) {
                    helpWindow.postMessage(
                        {type: END_TYPE, tour: player.name},
                        window.location.origin
                    );
                }
            } catch (e) {
                // help window gone
            }
        };
        current.start();
        return current;
    }

    function stopTour() {
        if (current) {
            current.stop();
        }
    }

    window.addEventListener("message", function (ev) {
        if (
            ev.origin !== window.location.origin ||
            !ev.data ||
            ev.data.type !== MESSAGE_TYPE ||
            !ev.source ||
            ev.source === window
        ) {
            return;
        }
        var sourceName;
        try {
            sourceName = ev.source.name;
        } catch (e) {
            return; // another origin
        }
        if (sourceName !== HELP_WINDOW_NAME) {
            return;
        }
        var steps = (Array.isArray(ev.data.steps) ? ev.data.steps : []).filter(
            function (step) {
                return step && typeof step.target === "string";
            }
        );
        if (steps.length) {
            startTour(String(ev.data.tour || ""), steps, ev.source);
        }
    });

    // Used by the tests of the module: the player started without the help
    // window
    window.wchHelpTour = {start: startTour, stop: stopTour};

    return {start: startTour, stop: stopTour};
});
