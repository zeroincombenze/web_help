Context help pages for the invoice list and form, shown by web_context_help:
customer invoices, vendor bills and their credit notes.

The model depends on the Odoo version: before 13.0 the pages follow
``account.invoice``, from 13.0 ``account.move``, where an invoice is a journal
entry with an invoice type.

Every page follows the standard layout of web_context_help:

* **Contents**: the sections of the page, built by the help window
* **Description**: what invoices are, their statuses and the main fields
* **How to insert a new record** (form): step-by-step guide to create, validate
  and send an invoice or a vendor bill
* **Suggestions for search** (list): menus, search, filters and groupings
* **How to update a record** (form): changing an invoice, registering payments,
  credit notes, cancelling and deleting
* **How to set up**: the Invoicing settings, journals, payment terms and taxes
* **Report and export file**: the invoice PDF, sending, the invoice analysis
  and the export of the invoices to a file
* **Example** button: common cases, e.g. partial payments or correcting a
  posted invoice
* **FAQ** button and **Footer**

Pages are in English and Italian, with the menus, buttons and statuses of the
running Odoo version.
