/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * VERSION-DEPENDENT: Odoo 10 adapter (widgets of the web client).
 * [?] button of the control panel: opens the help window of the view shown
 * and serves its postMessage requests (see common/help_window.js).
 */
odoo.define("web_context_help.context_help", function (require) {
    "use strict";

    var ajax = require("web.ajax");
    var core = require("web.core");
    var pyeval = require("web.pyeval");
    var ControlPanel = require("web.ControlPanel");
    var FormView = require("web.FormView");
    var ViewManager = require("web.ViewManager");

    var WINDOW_NAME = "odoo_help";
    var FOLLOW_KEY = "web_context_help.follow";
    var HIGHLIGHT_CLASS = "o_wch_highlight";
    var RE_FIELD = /^\w+$/;

    var helpWindow = null;
    var lastContext = null;
    // View manager of the main action: dialogs and x2many keep its help
    var current = null;

    function isFollowing() {
        try {
            return window.localStorage.getItem(FOLLOW_KEY) !== "0";
        } catch (e) {
            return true;
        }
    }

    function isOpen() {
        return Boolean(helpWindow && !helpWindow.closed);
    }

    function isMain(vm) {
        return Boolean(
            vm &&
                vm.action_manager &&
                vm.action_manager.get_inner_widget() === vm &&
                !(vm.action && vm.action.target === "new")
        );
    }

    /**
     * Values checked by the "when" condition and the rules of the help pages:
     * the default_<name> keys of the action context (as <name>), overridden
     * by the selection, boolean and many2one (its id) fields of the open
     * record (form view).
     */
    function contextValues(vm) {
        var values = {};
        var context = {};
        try {
            context = pyeval.eval("context", vm.dataset.get_context());
        } catch (e) {
            context = (vm.action && vm.action.context) || {};
        }
        _.each(context, function (value, key) {
            var scalar = ["string", "number", "boolean"].indexOf(typeof value) >= 0;
            if (key.indexOf("default_") === 0 && scalar) {
                values[key.slice(8)] = value;
            }
        });
        var view = vm.active_view;
        var form = view && view.type === "form" && view.controller;
        if (!form || !form.fields_view) {
            return values;
        }
        _.each(form.fields_view.fields || {}, function (desc, name) {
            var value;
            var widget = form.fields && form.fields[name];
            try {
                value = widget ? widget.get_value() : (form.datarecord || {})[name];
            } catch (e) {
                value = (form.datarecord || {})[name];
            }
            if (value === undefined) {
                return;
            }
            if (desc.type === "selection" || desc.type === "boolean") {
                values[name] = value;
            } else if (desc.type === "many2one") {
                // [id, display_name], id or false
                values[name] = (_.isArray(value) ? value[0] : value) || false;
            }
        });
        return values;
    }

    function getContext(vm) {
        var view = vm && vm.active_view;
        if (!vm || !view) {
            return {};
        }
        var controller = view.controller;
        return {
            model: vm.dataset && vm.dataset.model,
            viewType: view.type,
            viewId: controller && controller.fields_view && controller.fields_view.view_id,
            values: contextValues(vm),
        };
    }

    function lookup(ctx, looseFrom) {
        return ajax.jsonRpc("/web_context_help/lookup", "call", {
            model: ctx.model || false,
            view_type: ctx.viewType || false,
            view_id: ctx.viewId || false,
            values: ctx.values || {},
            loose_from: looseFrom || false,
        });
    }

    // Loose help button of the help window: the general page of the open
    // record, the page shown being clear cut or of high priority
    function loose(pageKey) {
        if (!isOpen()) {
            return;
        }
        if (!lastContext) {
            helpWindow.location =
                "/web_context_help/loose/" + encodeURIComponent(pageKey);
            return;
        }
        lookup(lastContext, pageKey).then(function (result) {
            if (result.url && isOpen()) {
                helpWindow.location = result.url;
            }
        });
    }

    function open(ctx) {
        lastContext = ctx;
        // Open synchronously in the click handler, or popup blockers bite
        helpWindow = window.open("", WINDOW_NAME);
        lookup(ctx).then(function (result) {
            if (helpWindow) {
                helpWindow.location = result.url || "/web_context_help/home";
                helpWindow.focus();
            }
        });
    }

    // Help menu: the home page, in the same window as the context help
    function openHome() {
        helpWindow = window.open("/web_context_help/home", WINDOW_NAME);
        if (helpWindow) {
            helpWindow.focus();
        }
    }

    function notify(ctx) {
        lastContext = ctx;
        if (!isOpen() || !isFollowing()) {
            return;
        }
        lookup(ctx).then(function (result) {
            if (!result.url || !isOpen()) {
                return;
            }
            // The FAQ and Fields pages of the current page are not left
            var current_url = "";
            try {
                var location = new URL(helpWindow.location.href);
                location.searchParams.delete("view");
                current_url = location.pathname + location.search;
            } catch (e) {
                current_url = "";
            }
            if (result.url !== current_url) {
                helpWindow.location = result.url;
            }
        });
    }

    function fieldElements(field) {
        var view = current && current.active_view;
        var controller = view && view.controller;
        if (!controller || !RE_FIELD.test(field)) {
            return $();
        }
        var $elements = controller.$(
            'th[data-id="' + field + '"], td[data-field="' + field + '"]'
        );
        var widget = view.type === "form" && controller.fields && controller.fields[field];
        if (widget) {
            $elements = $elements.add(widget.$el).add(widget.$label || $());
        }
        return $elements.filter(":visible");
    }

    function highlight(field) {
        var $elements = fieldElements(field);
        $elements.addClass(HIGHLIGHT_CLASS);
        setTimeout(function () {
            $elements.removeClass(HIGHLIGHT_CLASS);
        }, 3000);
        if ($elements.length && $elements[0].scrollIntoView) {
            $elements[0].scrollIntoView({block: "center", behavior: "smooth"});
        }
    }

    function runTour(name) {
        var services = (window.odoo && odoo.__DEBUG__ && odoo.__DEBUG__.services) || {};
        var tour = services["web_tour.tour"];
        if (tour && tour.run) {
            tour.run(name);
        }
    }

    window.addEventListener("message", function (ev) {
        if (ev.origin !== window.location.origin || !ev.data || !ev.data.type) {
            return;
        }
        if (isOpen() && ev.source !== helpWindow) {
            return;
        }
        if (!isOpen() && ev.source && ev.source.name === WINDOW_NAME) {
            // Odoo tab reloaded: take the help window back
            helpWindow = ev.source;
        }
        switch (ev.data.type) {
            case "wch_highlight":
                highlight(ev.data.field);
                break;
            case "wch_tour":
                runTour(ev.data.tour);
                break;
            case "wch_loose":
                loose(ev.data.page_key);
                break;
            case "wch_follow":
                if (ev.data.value && lastContext) {
                    notify(lastContext);
                }
                break;
        }
    });

    function notifyView(vm) {
        if (isMain(vm)) {
            current = vm;
            notify(getContext(vm));
        }
    }

    ViewManager.include({
        // A view shown: new action, switch of view, breadcrumb back
        _display_view: function () {
            var self = this;
            return $.when(this._super.apply(this, arguments)).then(function (result) {
                notifyView(self);
                return result;
            });
        },
    });

    FormView.include({
        // The help follows the record: pager, save, discard
        load_record: function () {
            var self = this;
            return $.when(this._super.apply(this, arguments)).then(function (result) {
                var vm = self.getParent();
                if (vm === current && vm.active_view && vm.active_view.controller === self) {
                    notifyView(vm);
                }
                return result;
            });
        },
    });

    ControlPanel.include({
        events: _.extend({}, ControlPanel.prototype.events, {
            "click .o_wch_button": "on_context_help_click",
        }),
        on_context_help_click: function (ev) {
            ev.preventDefault();
            // a client action (no view) has no context: the home page
            open(isMain(current) ? getContext(current) : {});
        },
    });

    // Client action of the Help menu: opens the window, the current view stays
    core.action_registry.add("web_context_help.home", function () {
        openHome();
    });

    return {
        open: open,
        openHome: openHome,
        notify: notify,
        isOpen: isOpen,
        contextValues: contextValues,
    };
});
