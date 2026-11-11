/* Copyright 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
 * License LGPL-3.0-or-later (https://www.gnu.org/licenses/lgpl).
 *
 * VERSION-DEPENDENT: Odoo 12 adapter (widgets of the web client).
 * [?] button of the control panel: opens the help window of the view shown
 * and serves its postMessage requests (see common/help_window.js).
 */
odoo.define("web_context_help.context_help", function (require) {
    "use strict";

    var ajax = require("web.ajax");
    var core = require("web.core");
    var ActionManager = require("web.ActionManager");
    var AbstractController = require("web.AbstractController");
    var ControlPanel = require("web.ControlPanel");

    var WINDOW_NAME = "odoo_help";
    var FOLLOW_KEY = "web_context_help.follow";
    var HIGHLIGHT_CLASS = "o_wch_highlight";
    var RE_FIELD = /^\w+$/;

    var helpWindow = null;
    var lastContext = null;
    // Page of the current Odoo view: the Topic button of the help window
    var topicUrl = false;
    // Action manager of the web client: its current controller is the main
    // view, the dialogs are not in its controller stack and keep its help
    var actionManager = null;

    function isFollowing() {
        try {
            return window.localStorage.getItem(FOLLOW_KEY) !== "0";
        } catch (e) {
            return true;
        }
    }

    // The Odoo client never is the help window: a help window whose
    // session expired goes to the login page and then loads Odoo in the
    // same tab, which keeps the window name. Without this reset the help
    // pages would be loaded over the Odoo views of this very tab
    if (window.name === WINDOW_NAME) {
        window.name = "";
    }

    // The window found by name, never this very tab
    function openWindow(url) {
        var win = window.open(url, WINDOW_NAME);
        return win === window ? null : win;
    }

    function isOpen() {
        return Boolean(helpWindow && !helpWindow.closed && helpWindow !== window);
    }

    // {widget, action} of the main view, or null (client action, no action)
    function currentView() {
        var controller = actionManager && actionManager.getCurrentController();
        if (!controller || !controller.widget) {
            return null;
        }
        var action = actionManager.actions[controller.actionID];
        if (!action || action.target === "new" || !controller.widget.modelName) {
            return null;
        }
        return {widget: controller.widget, action: action};
    }

    /**
     * Values checked by the "when" condition and the rules of the help pages:
     * the default_<name> keys of the action context (as <name>), overridden
     * by the selection, boolean and many2one (its id) fields of the open
     * record (form view).
     */
    function contextValues(view) {
        var values = {};
        var context = view.action.context;
        if (!_.isObject(context)) {
            context = {};
        }
        _.each(context, function (value, key) {
            var scalar = ["string", "number", "boolean"].indexOf(typeof value) >= 0;
            if (key.indexOf("default_") === 0 && scalar) {
                values[key.slice(8)] = value;
            }
        });
        var widget = view.widget;
        if (widget.viewType !== "form" || !widget.model || !widget.handle) {
            return values;
        }
        var record = widget.model.get(widget.handle, {raw: true});
        if (!record || !record.data) {
            return values;
        }
        _.each(record.fields || {}, function (desc, name) {
            var value = record.data[name];
            if (value === undefined) {
                return;
            }
            if (desc.type === "selection" || desc.type === "boolean") {
                values[name] = value;
            } else if (desc.type === "many2one") {
                // raw: the id, or false
                values[name] = (_.isArray(value) ? value[0] : value) || false;
            }
        });
        return values;
    }

    function getContext(view) {
        if (!view) {
            return {};
        }
        var widget = view.widget;
        var desc = _.findWhere(view.action.views || [], {type: widget.viewType});
        return {
            model: widget.modelName,
            viewType: widget.viewType,
            viewId: desc && desc.fieldsView && desc.fieldsView.view_id,
            values: contextValues(view),
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

    // The help window shows its Topic button when on another page
    function sendTopic() {
        if (isOpen()) {
            helpWindow.postMessage(
                {type: "wch_topic", url: topicUrl || false},
                window.location.origin
            );
        }
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
        helpWindow = openWindow("");
        lookup(ctx).then(function (result) {
            topicUrl = result.url;
            if (helpWindow) {
                helpWindow.location = result.url || "/web_context_help/home";
                helpWindow.focus();
            }
        });
    }

    // Help menu: the home page, in the same window as the context help
    function openHome() {
        helpWindow = openWindow("/web_context_help/home");
        if (helpWindow) {
            helpWindow.focus();
        }
    }

    function notify(ctx) {
        lastContext = ctx;
        if (!isOpen()) {
            return;
        }
        lookup(ctx).then(function (result) {
            if (ctx !== lastContext || !isOpen()) {
                return; // a newer view was opened meanwhile
            }
            topicUrl = result.url;
            if (!result.url || !isFollowing()) {
                sendTopic();
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
            } else {
                sendTopic();
            }
        });
    }

    function fieldElements(field) {
        var view = currentView();
        if (!view || !RE_FIELD.test(field)) {
            return $();
        }
        var $root = view.widget.$el;
        // list headers, field widgets of forms and editable lists
        var $elements = $root.find(
            'th[data-name="' + field + '"], .o_field_widget[name="' + field + '"]'
        );
        // form labels: the renderer keeps the id they point to, by field
        var ids = (view.widget.renderer && view.widget.renderer.idsForLabels) || {};
        if (ids[field]) {
            $elements = $elements.add($root.find('label[for="' + ids[field] + '"]'));
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
        if (
            !isOpen() &&
            ev.source &&
            ev.source !== window &&
            ev.source.name === WINDOW_NAME
        ) {
            // Odoo tab reloaded: take the help window back
            helpWindow = ev.source;
        }
        switch (ev.data.type) {
            case "wch_ready":
                if (!topicUrl && lastContext) {
                    // Odoo tab reloaded with the help window open
                    notify(lastContext);
                } else {
                    sendTopic();
                }
                break;
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

    function notifyView() {
        var view = currentView();
        if (view) {
            notify(getContext(view));
        }
    }

    ActionManager.include({
        // A view shown: new action, switch of view, breadcrumb back
        _pushController: function () {
            actionManager = this;
            var result = this._super.apply(this, arguments);
            notifyView();
            return result;
        },
    });

    AbstractController.include({
        // The help follows the record: pager, save, discard, reload
        _update: function () {
            var self = this;
            return $.when(this._super.apply(this, arguments)).then(function (result) {
                var view = currentView();
                if (view && view.widget === self) {
                    notifyView();
                }
                return result;
            });
        },
    });

    ControlPanel.include({
        events: _.extend({}, ControlPanel.prototype.events, {
            "click .o_wch_button": "_onContextHelpClick",
        }),
        _onContextHelpClick: function (ev) {
            ev.preventDefault();
            // a client action (no view) has no context: the home page
            open(getContext(currentView()));
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
