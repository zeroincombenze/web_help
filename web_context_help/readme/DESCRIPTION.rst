Adds a |sos| button to the control panel of every view: it opens the help of the
current view in a separate window, so the Odoo tab stays usable.

* Help pages are written in RST by each module, in its ``help/`` directory
* The help window follows the navigation (*Follow Odoo*), highlights the fields
  named by the page and can start a guided tour
* Questions are answered by a full-text search over the help sections; every
  question is logged for the administrator
* Administrators can edit a page; the edited version survives the upgrades and
  a warning appears when the original source changes
* A page can be chosen by a field of the open record, many2one included: by
  the ``:when:`` of its RST source or by rules set by the administrator, e.g. a
  different sale order help for each order type
* Views without a page get an automatic page built from the fields help
* The **Help** menu opens the help home page; its **Summary** button lists the
  pages of every installed help module (e.g. help_account_invoice,
  help_sale_order)

.. |sos| unicode:: U+1F6DF
