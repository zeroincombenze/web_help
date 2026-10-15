No configuration is needed. Pages are rebuilt at server start when a help
source changes; the administrator can force it with **Rebuild all pages** in
*Settings > Technical > Context Help > Help Pages*.

The videos inserted in the help pages are read from the directory of the system
parameter ``web_help_video_path`` (default ``~/Video``, the home of the user
running Odoo), subdirectories included; change it in *Settings > Technical >
System Parameters*.
