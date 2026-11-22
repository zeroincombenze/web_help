Adds a |sos| button to the control panel of every view: it opens the help of the
current view in a separate window, so the Odoo tab stays usable.

The help pages are on two levels:

* **Standard level**: the pages supplied by the help modules (e.g.
  help_account_invoice, help_sale_order), which show the help of the standard
  Odoo modules. They have a priority of 64 or more (96 by default), so they are
  the last fallback, always available
* **Customized level**: the pages built for the custom modules, or the copies
  of the standard pages changed to fit the company. They have a priority lower
  than 64 (32 by default), and 1 is the highest: a customized page is shown in
  place of the standard page of the same view. Editors write them in *Help ‣
  Help Editor ‣ Help Pages*, or in the ``help/`` directory of the custom module

* Administrators can edit a help page from the Odoo interface, with the editor
  of the page form: in the database a page is HTML, so no RST is needed. The
  edited version is kept when the module is upgraded, and a warning appears
  when the RST source changes afterwards, so the edit can be checked against
  the new source
* The source of a help page is an RST file, written by the developer in the
  ``help/`` directory of the module (one file per language); the server turns
  it into the HTML page of the database, when it starts and when the source
  changes
* Images are added to the RST source (``image`` directive, file in the
  ``static/`` of a module), videos by the editors in the HTML page; the guided
  tours need the *Context help tours* module (``web_context_help_tour``)
* The help window follows the navigation (*Follow Odoo*), highlights the fields
  named by the page and can start a guided tour
* Questions are answered by a full-text search over the help sections; every
  question is logged for the administrator
* A page can be chosen by a field of the open record, many2one included: by
  the ``:when:`` of its RST source or by rules set by the administrator, e.g. a
  different sale order help for each order type
* Views without a page get an automatic page built from the fields help
* The **Help** menu opens the help home page; its **Summary** button lists the
  pages of every installed help module (e.g. help_account_invoice,
  help_sale_order)

.. |sos| unicode:: U+1F6DF
