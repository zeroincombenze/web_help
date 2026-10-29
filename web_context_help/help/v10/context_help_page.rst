.. help-page:: context_help_page
   :title: Help pages
   :model: context.help.page
   :view: web_context_help.context_help_page_tree, web_context_help.context_help_page_form

Help pages
==========

Every module can explain its forms with RST files in its ``help/`` directory.
They are read at every server start and turned into the pages listed here.
Press the |sos| button in the control panel to open the help of the current view
in a separate window: the Odoo tab stays usable and, with *Follow Odoo* checked,
the help window follows you from view to view.

.. |sos| unicode:: U+1F6DF

.. _page_fields:

Fields
------

:field:`Key <key>` is ``<module>.<name>``; :field:`Views <view_xmlid>`,
:field:`Model <model>` and :field:`View type <view_type>` decide which view
opens the page.

.. _rules:

Rules
-----

The **Rules** tab chooses the page by a field of the open record, with no RST
source: field (selection, boolean or many2one), *is* or *is not*, and the value.
The values of a selection field are written as their keys, comma separated
(e.g. ``draft, sent``): the *Allowed values* of the rule form lists them.
The Rules tab is shown on the **Clear cut** pages: a clear cut page is shown
only when one of its rules is met, e.g. the help of an order type. Which page
wins is set by its **Priority** (1 is the highest):

* the clear cut pages come first, in priority order: the first one with a rule
  met is shown;
* with no rule met, the general page (not clear cut) with the highest priority
  is shown: your own pages (default 32) come before the pages of the modules
  (96), which are the last fallback.

A clear cut page, or a page of priority 64 or less, shows the **Loose help**
button: it opens the general help of the same record, i.e. the general page
of priority 64 or more with the highest priority, usually the page of the
module.

All the rules are also listed in *Help Rules*. A page created with **New** or
**Duplicate** has no source and is kept by **Rebuild all pages**; a duplicate
gets the key of the page followed by " (copy)".

.. help-include:: editing.rst

Press **Edit** to change the page and **Save** when done. The
**Insert video** button lists the videos of the video directory (system
parameter ``web_help_video_path``): the chosen one is added at the end of the
page, or after the paragraph containing the text written in *After the text*.

.. _faq:

Questions
---------

.. help-question:: Why doesn't my change to the RST file appear?

   Pages are rebuilt at server start when a source checksum changes.
   Restart the server or press **Rebuild all pages**.

.. help-question::
   :auto:
