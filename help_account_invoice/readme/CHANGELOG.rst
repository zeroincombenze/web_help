12.0.1.0.6 (2026-11-22)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages split in customer invoices (account_invoice_out_*, types out_invoice / out_refund) and vendor bills (account_invoice_in_*, types in_invoice / in_refund, view invoice_supplier_form): list and form, new record, update, cancel, set up, report, examples, FAQ and e-invoice FAQ (v11_14) rewritten for each side; the old account_invoice_* files are removed
* [IMP] Vendor bills: new chapter Invoice from supplier order (only with purchase): Control Policy of the product, Confirm Order, Receive Products, Create Bill, Auto-Complete, partial billing, Billing Status of the order
* [IMP] Vendor bills: vendor reference, bill date, payment to the vendor, credit note requested to the vendor (Ask for a Credit Note, Add Credit Note); the Bill tab of the vendor form and the vendor set up (Sales & Purchases and Invoicing tabs of the partner) as in Odoo 12.0; no cash rounding on the vendor bills
* [FIX] Italian labels of Odoo 12.0: Multi valuta, Modifica: crea nota di credito, riconcilia e genera nuova fattura in bozza, Cancel Journal Entries

12.0.1.0.5 (2026-11-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice form and list: new section How to cancel or delete record (Cancel Journal Entries up to 12.0, Reset to Draft then Cancel from 13.0, sequence and audit trail limits on deletion); journal dashboard: new section How to archive or delete record
* [IMP] Invoice list: new sections How to insert a new record (button Create / New) and How to update a record (click on a line); journal dashboard: the same sections (cards are not created here, ⋮ ‣ Configuration)
* [IMP] Buttons written [`Label`], shown inside a frame (menu paths, tabs and titles stay bold)

12.0.1.0.4 (2026-11-07)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice form and invoice list: 27 e-invoice FAQ (FAQ fattura elettronica) adapted from the 10.0 helpdesk FAQ to l10n_it_fatturapa (OCA 12.0); the 10.0-only cases are left out
* [IMP] Invoice list: new chapter Other actions (Altre azioni), before How to set up: confirm invoices, register payments for several invoices (one per invoice, or grouped with Group Invoices); no debit note function in 12.0
* [IMP] Invoice form: new chapter Other actions (Altre azioni), before How to set up: confirm the invoice, register a payment (moved here from How to update a record; In Payment with Post At Bank Reconciliation), outstanding credits, debit note
* [IMP] Report and export file: aligned with 18.0 (the new paragraphs apply to 17.0 and later only)
* [IMP] Every help page starts with the hint to the Ready and FAQ buttons; every FAQ page starts with the hint to the Topic button
* [IMP] Invoice FAQ: negative quantity on an invoice line and negative invoice total (Odoo 10.0 does not stop it, 11.0+ refuses it, 13.0+ can switch the draft into a credit note)
* [FIX] New invoice: Odoo 10.0 does not refuse an invoice with a negative total

12.0.1.0.3 (2026-11-01)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Migrated from 18.0 to 12.0 (requires web_context_help 12.0.1.0.10)
* [IMP] Invoice form: new section Invoicing from sale order (Fatturazione da ordine di vendita), shown only when the sale module is installed
* [NEW] Accounting Overview (journal kanban) help page: cards of sale, purchase, bank, cash and miscellaneous journals, the ⋮ menu, search, set up and FAQ
* [FIX] Italian invoice search: label of Add Custom Filter as translated by each Odoo version

18.0.1.0.2 (2026-10-31)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages in the standard layout: sections renamed How to insert a new record, How to update a record, Suggestions for search, How to set up, Report and export file (Italian titles too); the Report section explains how to export the records to a file

18.0.1.0.1 (2026-10-25)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages declared with :priority: 96, the priority of the module pages: the last fallback after the pages of the administrator (requires web_context_help 18.0.1.0.6)

18.0.1.0.0 (2026-10-02)
~~~~~~~~~~~~~~~~~~~~~~~

* [NEW] Help pages for invoice list and form, English and Italian, Odoo 10 to 18 (account.invoice before 13.0, account.move since 13.0, journal entries excluded)
