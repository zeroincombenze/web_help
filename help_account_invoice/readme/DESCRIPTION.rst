Context help pages for the invoice list and form, shown by web_context_help:
customer invoices, vendor bills and their credit notes.

The model depends on the Odoo version: before 13.0 the pages follow
``account.invoice``, from 13.0 ``account.move``, where an invoice is a journal
entry with an invoice type.

Every page follows the help rule of web_context_help:

* **Description**: what invoices are, their statuses and the main fields
* **New record** (form): step-by-step guide to create, validate and send an
  invoice or a vendor bill
* **Update record** (form): changing an invoice, registering payments, credit
  notes, cancelling and deleting
* **How to search** (list): menus, search, filters and groupings
* **Configure**: the Invoicing settings, journals, payment terms and taxes
* **Report**: the invoice PDF, sending and the invoice analysis
* **Example**: common cases, e.g. partial payments or correcting a posted invoice
* **FAQ** and **Footer**

Pages are in English and Italian, with the menus, buttons and statuses of the
running Odoo version.
