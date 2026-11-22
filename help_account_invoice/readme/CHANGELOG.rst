18.0.1.0.8 (2026-11-22)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Module category changed from Hidden/Tools to Tutorial, as the apps of odoo.com

18.0.1.0.7 (2026-11-20)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages split in customer invoices (account_invoice_out_*, move types out_invoice / out_refund / out_receipt) and vendor bills (account_invoice_in_*, move types in_invoice / in_refund / in_receipt; before 13.0 the views invoice_form / invoice_supplier_form): list and form, new record, update, cancel, set up, report, examples, FAQ and e-invoice FAQ rewritten for each side
* [IMP] Vendor bills: new chapter Invoice from supplier order (only with purchase): control policy of the product, Confirm Order, Receive Products, Create Bill, Auto-Complete, partial billing, billing status of the order
* [IMP] Vendor bills: vendor reference, bill date, payment to the vendor, credit note requested to the vendor (Ask Refund / Ask for a Credit Note up to 12.0), import of e-invoices of the vendors (only with l10n_it_edi_extension)
* [IMP] Vendor bills: new chapter How to create invoice from xml (Odoo 18.0, with l10n_it_edi): Upload from the bills list or the purchase journal card, what is imported (vendor, lines, taxes, due date, bank, attachments), duplicate check, checks before Confirm, import detail level and validation message with l10n_it_edi_extension
* [FIX] Credit note button of the invoice: Add Credit Note up to 16.0, Credit Note from 17.0; customer credit notes menu of 11.0

18.0.1.0.6 (2026-11-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice form and list: new section How to cancel or delete record (Cancel Journal Entries up to 12.0, Reset to Draft then Cancel from 13.0, sequence and audit trail limits on deletion); journal dashboard: new section How to archive or delete record
* [IMP] Invoice list: new sections How to insert a new record (button Create / New) and How to update a record (click on a line); journal dashboard: the same sections (cards are not created here, ⋮ ‣ Configuration)
* [IMP] Buttons written [`Label`], shown inside a frame (menu paths, tabs and titles stay bold)

18.0.1.0.5 (2026-11-08)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice form and invoice list: 25 e-invoice FAQ (FAQ fattura elettronica) adapted from the 10.0 helpdesk FAQ to l10n_it_edi; the cases handled automatically by Odoo 18.0 are left out
* [IMP] Every help page starts with the hint to the Ready and FAQ buttons; every FAQ page starts with the hint to the Topic button
* [IMP] Invoice FAQ: negative quantity on an invoice line and negative invoice total (Odoo 10.0 does not stop it, 11.0+ refuses it, 13.0+ can switch the draft into a credit note)
* [FIX] New invoice: Odoo 10.0 does not refuse an invoice with a negative total

18.0.1.0.4 (2026-11-06)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Report and export file: export of several invoices in a ZIP file (Export ZIP in 17.0, Print ‣ XML FatturaPA with l10n_it_edi in 18.0) and import of a ZIP of e-invoices made outside Odoo (only with l10n_it_edi_extension)
* [IMP] Invoice list: new chapter Other actions (Altre azioni), before How to set up: confirm invoices, register a payment, create a debit note (with account_debit_note; TD05 with l10n_it_edi_ndd_account_dn)
* [IMP] Invoice form: new chapter Other actions (Altre azioni), before How to set up: confirm the invoice, register a payment (moved here from How to update a record), create a debit note

18.0.1.0.3 (2026-11-01)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice form: new section Invoicing from sale order (Fatturazione da ordine di vendita), shown only when the sale module is installed
* [NEW] Accounting Dashboard (journal kanban) help page: cards of sales, purchase, bank, cash, credit card and miscellaneous journals, the ⋮ menu, search, set up and FAQ

18.0.1.0.2 (2026-10-31)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages in the standard layout: sections renamed How to insert a new record, How to update a record, Suggestions for search, How to set up, Report and export file (Italian titles too); the Report section explains how to export the records to a file

18.0.1.0.1 (2026-10-25)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages declared with :priority: 96, the priority of the module pages: the last fallback after the pages of the administrator (requires web_context_help 18.0.1.0.6)

18.0.1.0.0 (2026-10-02)
~~~~~~~~~~~~~~~~~~~~~~~

* [NEW] Help pages for invoice list and form, English and Italian, Odoo 10 to 18 (account.invoice before 13.0, account.move since 13.0, journal entries excluded)
