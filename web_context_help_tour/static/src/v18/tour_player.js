/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * VERSION-DEPENDENT: Odoo 18 tour player.
 * Plays the help-tour tours of the help pages in the Odoo tab. The help
 * window sends the steps written in the page (target, text); each step dims
 * the screen around its target, rings it and explains it in a popover with
 * the Previous / Next / Stop buttons. The dimmed screen still takes clicks:
 * the user does the work, the tour only shows where.
 */
import {registry} from "@web/core/registry";
import {browser} from "@web/core/browser/browser";
import {_t} from "@web/core/l10n/translation";

// Name of the help window, set by web_context_help
const HELP_WINDOW_NAME = "odoo_help";
const MESSAGE_TYPE = "wch_help_tour";
// Sent back to the help window when a tour stops (Finish, Stop, Esc)
const END_TYPE = "wch_tour_end";
// Room around the target and between the target and the popover
const PADDING = 6;
const GAP = 12;
const MARGIN = 8;
// A missing target is looked for again every RESOLVE_MS
const RESOLVE_MS = 250;

// Short targets of help-step: the control panel buttons of Odoo 18
const ALIASES = {
    new: ".o_list_button_add, .o-kanban-button-new, .o_form_button_create",
    save: ".o_form_button_save",
    discard: ".o_form_button_cancel",
    search: ".o_searchview",
    filters: ".o_searchview_dropdown_toggler",
    actions: ".o_cp_action_menus button:has(.fa-cog)",
    breadcrumb: ".o_breadcrumb",
    statusbar: ".o_statusbar_status",
};

// Inline markup kept in the text of a step; any other tag is dropped and its
// text kept, e.g. the :field: links of the help page
const ALLOWED_TAGS = new Set([
    "P",
    "STRONG",
    "EM",
    "B",
    "I",
    "CODE",
    "KBD",
    "BR",
    "UL",
    "OL",
    "LI",
    "SPAN",
]);
const DROPPED_TAGS = new Set(["SCRIPT", "STYLE", "TEMPLATE"]);

function isVisible(el) {
    if (!el.isConnected || el.closest(".o_wcht")) {
        return false;
    }
    const rect = el.getBoundingClientRect();
    return rect.width > 0 && rect.height > 0;
}

function visibleIn(selector) {
    let found;
    try {
        found = document.querySelectorAll(selector);
    } catch {
        return []; // invalid css: target of the help page
    }
    return [...found].filter(isVisible);
}

// Label of a form field: through the id of its focusable element, or the
// label cell of the same group row (a readonly widget has no id)
function fieldLabels(widget) {
    const labels = [];
    for (const el of [widget, ...widget.querySelectorAll("[id]")]) {
        if (el.id) {
            labels.push(
                ...document.querySelectorAll(`label[for="${CSS.escape(el.id)}"]`)
            );
        }
    }
    const cell = widget.closest(".o_wrap_input");
    const labelCell = cell && cell.previousElementSibling;
    if (labelCell && labelCell.classList.contains("o_wrap_label")) {
        labels.push(...labelCell.querySelectorAll("label"));
    }
    return labels.filter(isVisible);
}

/**
 * Elements shown by a help-step target, the main one first: [] when the
 * target is not on screen
 */
export function resolveTarget(target) {
    if (ALIASES[target]) {
        return visibleIn(ALIASES[target]).slice(0, 1);
    }
    const sep = target.indexOf(":");
    const kind = target.slice(0, sep);
    const value = target.slice(sep + 1).trim();
    const name = CSS.escape(value);
    switch (kind) {
        case "field": {
            const widget = visibleIn(`.o_field_widget[name="${name}"]`)[0];
            if (widget) {
                return [widget, ...fieldLabels(widget)];
            }
            // list view: the column header
            return visibleIn(`th[data-name="${name}"]`).slice(0, 1);
        }
        case "button":
            return visibleIn(`button[name="${name}"]`).slice(0, 1);
        case "tab":
            return visibleIn(`.o_notebook_headers a.nav-link[name="${name}"]`).slice(
                0,
                1
            );
        case "menu":
            return visibleIn(`[data-menu-xmlid="${name}"]`).slice(0, 1);
        case "css":
            return visibleIn(value).slice(0, 1);
    }
    return [];
}

function sanitize(html) {
    const doc = new DOMParser().parseFromString(`<div>${html}</div>`, "text/html");
    const out = document.createElement("div");
    const copy = (src, dst) => {
        for (const node of src.childNodes) {
            if (node.nodeType === Node.TEXT_NODE) {
                dst.appendChild(document.createTextNode(node.textContent));
            } else if (node.nodeType === Node.ELEMENT_NODE) {
                if (ALLOWED_TAGS.has(node.tagName)) {
                    const el = document.createElement(node.tagName);
                    copy(node, el);
                    dst.appendChild(el);
                } else if (!DROPPED_TAGS.has(node.tagName)) {
                    copy(node, dst);
                }
            }
        }
    };
    copy(doc.body.firstElementChild || doc.body, out);
    return out;
}

function unionRect(elements) {
    let top = Infinity;
    let left = Infinity;
    let bottom = -Infinity;
    let right = -Infinity;
    for (const el of elements) {
        const r = el.getBoundingClientRect();
        top = Math.min(top, r.top);
        left = Math.min(left, r.left);
        bottom = Math.max(bottom, r.bottom);
        right = Math.max(right, r.right);
    }
    return {
        top: top - PADDING,
        left: left - PADDING,
        bottom: bottom + PADDING,
        right: right + PADDING,
    };
}

function make(tag, className, parent) {
    const el = document.createElement(tag);
    if (className) {
        el.className = className;
    }
    if (parent) {
        parent.appendChild(el);
    }
    return el;
}

function place(el, top, left, width, height) {
    el.style.top = `${Math.round(top)}px`;
    el.style.left = `${Math.round(left)}px`;
    el.style.width = `${Math.max(0, Math.round(width))}px`;
    el.style.height = `${Math.max(0, Math.round(height))}px`;
}

export class TourPlayer {
    constructor(name, steps) {
        this.name = name;
        this.steps = steps;
        this.index = -1;
        this.elements = [];
        this.lastResolve = 0;
        this.scrolled = false;
        this.frame = null;
        this.onKeydown = this.onKeydown.bind(this);
        this.onPress = this.onPress.bind(this);
        this.loop = this.loop.bind(this);
        this.build();
    }

    build() {
        const root = make("div", "o_wcht");
        root.dataset.tour = this.name;
        this.masks = ["top", "bottom", "left", "right"].map((side) =>
            make("div", `o_wcht_mask o_wcht_mask_${side}`, root)
        );
        this.ring = make("div", "o_wcht_ring", root);
        const pop = make("div", "o_wcht_pop", root);
        pop.setAttribute("role", "dialog");
        this.arrow = make("div", "o_wcht_arrow", pop);
        const header = make("div", "o_wcht_header", pop);
        this.counter = make("span", "o_wcht_count", header);
        this.closeBtn = make("button", "btn-close o_wcht_close", header);
        this.closeBtn.type = "button";
        this.closeBtn.title = _t("Stop the tour");
        this.closeBtn.setAttribute("aria-label", _t("Stop the tour"));
        this.body = make("div", "o_wcht_body", pop);
        this.note = make("p", "o_wcht_note", pop);
        this.note.textContent = _t(
            "Waiting for this step: open the screen it refers to, or do what the previous step asks."
        );
        const footer = make("div", "o_wcht_footer", pop);
        this.stopBtn = make("button", "btn btn-link o_wcht_stop", footer);
        this.stopBtn.textContent = _t("Stop");
        this.prevBtn = make("button", "btn btn-secondary o_wcht_prev", footer);
        this.prevBtn.textContent = _t("Previous");
        this.nextBtn = make("button", "btn btn-primary o_wcht_next", footer);
        for (const btn of [this.stopBtn, this.prevBtn, this.nextBtn]) {
            btn.type = "button";
        }
        // run by onPress, before the click reaches the Odoo listeners
        this.actions = new Map([
            [this.closeBtn, () => this.stop()],
            [this.stopBtn, () => this.stop()],
            [this.prevBtn, () => this.go(this.index - 1)],
            [this.nextBtn, () => this.next()],
        ]);
        this.root = root;
        this.pop = pop;
    }

    start() {
        document.body.appendChild(this.root);
        browser.addEventListener("keydown", this.onKeydown, true);
        // registered before any dropdown opens, so they run before the
        // click-away listeners of the Odoo dropdowns
        browser.addEventListener("pointerdown", this.onPress, true);
        browser.addEventListener("click", this.onPress, true);
        this.go(0);
        this.frame = browser.requestAnimationFrame(this.loop);
    }

    stop() {
        if (this.frame) {
            browser.cancelAnimationFrame(this.frame);
            this.frame = null;
        }
        browser.removeEventListener("keydown", this.onKeydown, true);
        browser.removeEventListener("pointerdown", this.onPress, true);
        browser.removeEventListener("click", this.onPress, true);
        this.root.remove();
        if (this.onStop) {
            this.onStop(this);
        }
    }

    onKeydown(ev) {
        if (ev.key === "Escape") {
            ev.preventDefault();
            ev.stopPropagation();
            this.stop();
        }
    }

    // A press on the popover is not a click away: an Odoo dropdown opened by
    // the tour, e.g. the Filters menu, stays open for the next step. Odoo
    // closes it on pointerdown and on a keyboard click (Enter on Next), so
    // both stop here, at window capture, and the button action runs here.
    onPress(ev) {
        const pop = ev.target instanceof Element && ev.target.closest(".o_wcht_pop");
        if (!pop) {
            return;
        }
        ev.stopImmediatePropagation();
        if (ev.type === "click") {
            const btn = ev.target.closest("button");
            const action = btn && !btn.disabled && this.actions.get(btn);
            if (action) {
                action();
            }
        }
    }

    get step() {
        return this.steps[this.index];
    }

    get isLast() {
        return this.index === this.steps.length - 1;
    }

    go(index) {
        if (index < 0 || index >= this.steps.length) {
            return;
        }
        this.index = index;
        this.elements = [];
        this.lastResolve = 0;
        this.scrolled = false;
        this.counter.textContent = _t("Step %(current)s of %(total)s", {
            current: index + 1,
            total: this.steps.length,
        });
        this.body.replaceChildren(...sanitize(this.step.html || "").childNodes);
        this.prevBtn.disabled = index === 0;
        this.nextBtn.textContent = this.isLast ? _t("Finish") : _t("Next");
        this.resolve(true);
        this.layout();
        this.nextBtn.focus({preventScroll: true});
    }

    next() {
        // :click: the tour presses the target for the user, e.g. New
        if (this.step.click && this.elements.length) {
            this.elements[0].click();
        }
        if (this.isLast) {
            this.stop();
        } else {
            this.go(this.index + 1);
        }
    }

    resolve(force) {
        const now = Date.now();
        const lost = this.elements.some((el) => !isVisible(el));
        if (!force && !lost && this.elements.length) {
            return;
        }
        if (!force && !lost && now - this.lastResolve < RESOLVE_MS) {
            return;
        }
        this.lastResolve = now;
        const found = resolveTarget(this.step.target);
        if (found[0] !== this.elements[0]) {
            this.scrolled = false;
        }
        this.elements = found;
    }

    loop() {
        this.resolve(false);
        this.layout();
        this.frame = browser.requestAnimationFrame(this.loop);
    }

    layout() {
        const vw = document.documentElement.clientWidth;
        const vh = document.documentElement.clientHeight;
        const waiting = !this.elements.length;
        this.root.classList.toggle("o_wcht_waiting", waiting);
        if (waiting) {
            // Nothing to show: the whole screen is dimmed, popover centered
            place(this.masks[0], 0, 0, vw, vh);
            for (const mask of this.masks.slice(1)) {
                place(mask, 0, 0, 0, 0);
            }
            const pw = this.pop.offsetWidth;
            const ph = this.pop.offsetHeight;
            this.pop.style.top = `${Math.round((vh - ph) / 2)}px`;
            this.pop.style.left = `${Math.round((vw - pw) / 2)}px`;
            return;
        }
        if (!this.scrolled) {
            this.scrolled = true;
            const r = this.elements[0].getBoundingClientRect();
            if (r.top < 0 || r.bottom > vh || r.left < 0 || r.right > vw) {
                this.elements[0].scrollIntoView({block: "center", inline: "nearest"});
            }
        }
        const r = unionRect(this.elements);
        const top = Math.max(0, r.top);
        const bottom = Math.min(vh, r.bottom);
        const left = Math.max(0, r.left);
        const right = Math.min(vw, r.right);
        place(this.masks[0], 0, 0, vw, top);
        place(this.masks[1], bottom, 0, vw, vh - bottom);
        place(this.masks[2], top, 0, left, bottom - top);
        place(this.masks[3], top, right, vw - right, bottom - top);
        place(this.ring, r.top, r.left, r.right - r.left, r.bottom - r.top);
        this.placePopover(r, vw, vh);
    }

    placePopover(r, vw, vh) {
        const pw = this.pop.offsetWidth;
        const ph = this.pop.offsetHeight;
        const room = {
            bottom: vh - r.bottom - GAP,
            top: r.top - GAP,
            right: vw - r.right - GAP,
            left: r.left - GAP,
        };
        const fits = (side) =>
            side === "top" || side === "bottom" ? room[side] >= ph : room[side] >= pw;
        const wanted = this.step.position;
        let side = ["bottom", "top", "right", "left"].find(fits) || "bottom";
        if (wanted && wanted !== "auto" && fits(wanted)) {
            side = wanted;
        }
        const cx = (r.left + r.right) / 2;
        const cy = (r.top + r.bottom) / 2;
        let top;
        let left;
        if (side === "bottom" || side === "top") {
            top = side === "bottom" ? r.bottom + GAP : r.top - GAP - ph;
            left = cx - pw / 2;
        } else {
            left = side === "right" ? r.right + GAP : r.left - GAP - pw;
            top = cy - ph / 2;
        }
        left = Math.min(Math.max(MARGIN, left), vw - pw - MARGIN);
        top = Math.min(Math.max(MARGIN, top), vh - ph - MARGIN);
        this.pop.style.top = `${Math.round(top)}px`;
        this.pop.style.left = `${Math.round(left)}px`;
        this.pop.dataset.side = side;
        // The arrow points at the middle of the target
        if (side === "bottom" || side === "top") {
            this.arrow.style.left = `${Math.round(
                Math.min(Math.max(16, cx - left), pw - 16)
            )}px`;
            this.arrow.style.top = "";
        } else {
            this.arrow.style.top = `${Math.round(
                Math.min(Math.max(16, cy - top), ph - 16)
            )}px`;
            this.arrow.style.left = "";
        }
    }
}

export const contextHelpTourService = {
    start() {
        let current = null;

        function start(name, steps, helpWindow) {
            if (current) {
                current.stop();
            }
            current = new TourPlayer(name, steps);
            current.onStop = (player) => {
                if (current === player) {
                    current = null;
                }
                // the help window gives its tour button back its label
                try {
                    if (helpWindow && !helpWindow.closed) {
                        helpWindow.postMessage(
                            {type: END_TYPE, tour: player.name},
                            browser.location.origin
                        );
                    }
                } catch {
                    // help window gone
                }
            };
            current.start();
            return current;
        }

        function stop() {
            if (current) {
                current.stop();
            }
        }

        browser.addEventListener("message", (ev) => {
            if (
                ev.origin !== browser.location.origin ||
                !ev.data ||
                ev.data.type !== MESSAGE_TYPE ||
                !ev.source ||
                ev.source === window
            ) {
                return;
            }
            let sourceName;
            try {
                sourceName = ev.source.name;
            } catch {
                return; // another origin
            }
            if (sourceName !== HELP_WINDOW_NAME) {
                return;
            }
            const steps = (Array.isArray(ev.data.steps) ? ev.data.steps : []).filter(
                (step) => step && typeof step.target === "string"
            );
            if (steps.length) {
                start(String(ev.data.tour || ""), steps, ev.source);
            }
        });

        return {start, stop};
    },
};

registry.category("services").add("context_help_tour", contextHelpTourService);
