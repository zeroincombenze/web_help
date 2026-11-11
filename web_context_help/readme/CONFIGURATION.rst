No configuration is needed. Pages are rebuilt at server start when a help
source changes; a help editor can force it with **Rebuild all pages** in
*Help > Help Editor > Help Pages*.

Every internal user reads the help. Who edits it is set in the user form
(*Settings > Users*, field **Context Help** in the *Other* section):

* empty: no edit, the help is only read;
* **User**: edits the help pages of priority lower than 64 and their rules.
  Editing a page of priority 64 or more, e.g. a page of a module (96),
  creates a copy of it with the default priority (32), and the copy is
  edited: being of higher priority, it is shown in place of the original;
* **System**: edits all the help pages, as before.

The field sets the level of the administrators too: they start as **System**
(when the module is installed, or already had it before this version), and
can be lowered to **User** or to no edit. A user made administrator later
gets no help level by default.

Both levels need no administrator rights: opening the **Help** app, they get
its *Help Editor* menu in the top bar (pages, rules, questions asked) and the
**Edit** button of the help window.

The videos inserted in the help pages are read from the directory of the system
parameter ``web_help_video_path`` (default ``~/Video``, the home of the user
running Odoo), subdirectories included; change it in *Settings > Technical >
System Parameters*.
