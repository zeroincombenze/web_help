Context help pages for the invoice list and form, shown by web_context_help:
customer invoices, vendor bills and their credit notes.

The model depends on the Odoo version: before 13.0 the pages follow
``account.invoice``, from 13.0 ``account.move``, where an invoice is a journal
entry with an invoice type.

Customer invoices and vendor bills have separate help pages (customer invoices:
move types out_invoice, out_refund, out_receipt; vendor bills: in_invoice,
in_refund, in_receipt), each one with its own text, menus and FAQ. The vendor
bill pages include **Invoice from supplier order**, shown only when the
Purchase app is installed, and **How to create invoice from xml** (Odoo 18.0 with
l10n_it_edi): creating a vendor bill by loading an e-invoice.

Every page follows the standard layout of web_context_help:

* **Contents**: the sections of the page, built by the help window
* **Description**: what invoices are, their statuses and the main fields
* **How to insert a new record** (form): step-by-step guide to create, validate
  and send an invoice or a vendor bill
* **Invoicing from sale order** (customer invoice form, only when the Sales app is installed):
  invoicing policy, invoice status, regular invoices and down payments,
  several orders at once
* **Suggestions for search** (list): menus, search, filters and groupings
* **How to update a record** (form): changing an invoice, registering payments,
  credit notes
* **How to cancel or delete record** (form and list): cancelling a draft or
  posted invoice, resetting it to draft, which invoices can be deleted
* **How to set up**: the Invoicing settings, journals, payment terms and taxes
* **Report and export file**: the invoice PDF, sending, the invoice analysis
  and the export of the invoices to a file
* **Example** button: common cases, e.g. partial payments or correcting a
  posted invoice
* **FAQ** button and **Footer**

A page for the Accounting Dashboard (journal kanban) explains the cards of
the journals, their buttons and figures, the **⋮** menu, and how journals
are archived or deleted.

Pages are in English and Italian, with the menus, buttons and statuses of the
running Odoo version.
