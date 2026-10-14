18.0.1.0.4 (2026-10-14)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help menu at the top of the menu tree: opens the help home page, editable by the administrator; HTML code view (</>) on the content of the help pages, also without developer mode and as wide as the page
* [IMP] Help window: Summary button, page listing the help pages of every installed help module, each title followed by its view type (list) or (form); Home and Edit buttons
* [FIX] Help window: a malformed lang in the URL (e.g. ?lang=it_IT?debug=1) no longer falls back to the English page

18.0.1.0.3 (2026-10-02)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help window: find in page box, like the browser Ctrl+F, with previous / next buttons; several words found when near each other, phrase in quotes
* [IMP] Help window: FAQ and fields help on their own pages, opened by the FAQ and Fields buttons
* [IMP] Every list page gets the global wildcard search text at the end of its How to search section
* [IMP] help-page :when: condition on the open record or the menu context, e.g. move_type != entry
* [FIX] RST: a :field: role wrapped on two lines was printed as text; a :version: role with a stray ";" now fails on every version instead of cutting the text

18.0.1.0.2 (2026-10-01)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Version specific help: help-version directive and :version: role, pages built for the running Odoo version

18.0.1.0.1 (2026-09-27)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Field labels highlighted too, dialogs keep the help of the main view

18.0.1.0.0 (2026-09-27)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Migrated from 16.0: list views, invisible expressions, Odoo 18 control panel adapter

16.0.1.0.0 (2026-09-27)
~~~~~~~~~~~~~~~~~~~~~~~

* [NEW] Context help button, help pages built from the RST sources of each module
