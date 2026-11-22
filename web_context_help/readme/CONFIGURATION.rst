No configuration is needed. Pages are rebuilt at server start when a help source
changes; a help editor can force it with **Rebuild all pages** in *Help > Help
Editor > Help Pages*.

Help level of the users
~~~~~~~~~~~~~~~~~~~~~~~

Every internal user reads the help. The help level of a user is set in the user
form (*Settings > Users*, field **Context Help** in the *Application* section):

* empty: no edit, the help is only read;
* **No help**: the help is not shown to the user: no |sos| button in the
  views, no **Help** menu, and the help pages are refused;
* **User**: edits the help pages of priority lower than 64 and their rules.
  Editing a page of priority 64 or more, e.g. a page of a module (96), creates a
  copy of it with the default priority (32), and the copy is edited: being of
  higher priority, it is shown in place of the original;
* **System**: edits all the help pages.

The levels **User** and **System** need no administrator rights: they get the
*Help Editor* section in the left bar of the **Help** menu (pages, rules,
questions asked) and the [`Edit`] button of the help window.

The field sets the level of the administrators too: they start as **System**
(when the module is installed, or already had it before this version), and can
be lowered to **User**, to no edit or to **No help**. A user made administrator
later gets no help level by default.

Videos
~~~~~~

The videos inserted in the help pages are read from the directory of the system
parameter ``web_help_video_path`` (default ``~/Video``, the home of the user
running Odoo), subdirectories included; change it in *Settings > Technical >
System Parameters*.
