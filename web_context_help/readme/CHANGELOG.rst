10.0.1.0.7 (2026-10-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Migrated from 18.0 to 10.0: Python 2.7, Odoo 10 ORM, list views as tree and attrs, assets and QWeb templates of the Odoo 10 web client
* [IMP] Odoo 10 adapter of the control panel: the [?] button opens the help of the view shown, the help window follows the views and the records (pager, save), highlights the fields and runs the tours
* [IMP] Odoo 10: the Insert video button of the page form inserts a video of the video directory at the end of the page or after a paragraph, in place of the editor plugin of 18.0
* [IMP] Odoo 10: the selection values of a help rule are written as their keys, comma separated, checked against the allowed values shown in the rule form
* [IMP] Odoo 10: help page of the Help pages form in help/v10
* [IMP] Odoo 10: the Help Editor menus are in the left bar of the Help menu, Odoo 10 having no apps menu; the Help menu still opens the help window
* [FIX] Videos streamed with HTTP range support without the 18.0 Stream class
* [FIX] Page keys quoted in the URLs: a duplicated page (key ending with " (copy)") opens
* [QUA] Test coverage 90% (1241: 120+1121) [0 TestPoints] - quality rating 51 (target 100)
* [FIX] RST engine on Python 2: byte strings accepted, icons out of the basic plane (e.g. U+1F6DF) rendered on narrow builds, global search text copied without the docutils 0.16 system messages

18.0.1.0.6 (2026-10-22)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] help-page :when: condition on many2one fields too, the record named by xmlid or id, e.g. type_id = sale_order_type.normal_sale_type
* [IMP] Help rules (Settings ‣ Technical ‣ Context Help ‣ Help Rules, or the Rules tab of a page): the administrator chooses which page is shown by a selection, boolean or many2one field of the record, no RST source needed; several rules of a page are alternatives; in the rule form field, operator and value are shown together
* [IMP] Help lookup by page Priority (1 the highest) and Clear cut flag: the clear cut pages come first, the first one with a rule met is shown; otherwise the general page (not clear cut, its rules ignored) with the highest priority: pages of the administrator (default 32) before the pages of the modules (96), the last fallback; same priority, the page meeting more :when: conditions wins
* [IMP] Help pages created by the administrator are kept by the rebuild of the pages and their sections are built from their content
* [IMP] Help Editor group: writes the help pages, their rules and reads the questions asked, with no administrator rights, from the new Help Editor app; the administrators are help editors too
* [IMP] help-page :priority: option, the priority of a module page (96 when missing)
* [IMP] Help window: Loose help button on a clear cut page or a page of priority 64 or less: opens the general page of priority 64 or more with the highest priority, for the same record (usually the page of the module)
* [FIX] Odoo 18 form views: the help sees the fields of the open record (the form view did not share its record with the control panel), so the :when: conditions and the rules work on the record; the help window follows the record when it is saved or the pager moves to another one
* [FIX] Help pages: Duplicate no longer fails on the duplicate key: the copy key ends with " (copy)" (" (copy 2)" and so on for further copies); the copy has no source file, so it is a page of the administrator kept by the rebuild

18.0.1.0.5 (2026-10-14)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages: Help video button in the floating toolbar of the editor (and /Help video command): inserts a video of the directory set by the system parameter web_help_video_path (default ~/Video), played on click; Backspace or Delete next to a video removes it
* [UPD] Help pages: HTML code view (</>) shown only in developer mode, as in standard Odoo; the custom field widget is removed
* [FIX] Help pages: the Sections of a page edited by the administrator (editor or HTML code view) are rebuilt from its content, so the added headings and text are listed and found by the search; a reset to source rebuilds them too

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
