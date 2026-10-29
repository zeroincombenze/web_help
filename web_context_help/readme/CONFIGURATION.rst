No configuration is needed. Pages are rebuilt at server start when a help
source changes; a help editor can force it with **Rebuild all pages** in
*Help > Help Editor > Help Pages*.

Every internal user reads the help. The help pages and their rules are written
by the users of the group **Help Editor** (*Settings > Users*, section
*Context Help*), with no administrator rights: they get the *Help Editor*
section in the left bar of the **Help** menu (pages, rules, questions asked)
and the **Edit** button of the help window.
The administrators are help editors too.

The videos inserted in the help pages are read from the directory of the system
parameter ``web_help_video_path`` (default ``~/Video``, the home of the user
running Odoo), subdirectories included; change it in *Settings > Technical >
System Parameters*.
