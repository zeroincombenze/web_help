10.0.1.0.6 (2026-11-08)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Every help page starts with the hint to the Ready and FAQ buttons; every FAQ page starts with the hint to the Topic button
* [IMP] Invoice FAQ: negative quantity on an invoice line and negative invoice total (Odoo 10.0 does not stop it, 11.0+ refuses it, 13.0+ can switch the draft into a credit note)
* [FIX] New invoice: Odoo 10.0 does not refuse an invoice with a negative total

10.0.1.0.5 (2026-11-07)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice form and invoice list: 33 e-invoice FAQ (FAQ fattura elettronica, sending and receiving) from the helpdesk tickets, 10.0 only, shown when the l10n_it_einvoice modules are installed
* [IMP] Invoice list: new chapter Other actions (Altre azioni), before How to set up: confirm invoices, register one payment for several invoices of the same partner, type and currency; no debit note function in 10.0
* [IMP] Invoice form: new chapter Other actions (Altre azioni), before How to set up: confirm the invoice, register a payment (moved here from How to update a record), outstanding credits, debit note
* [IMP] Report and export file: aligned with 18.0 (the new paragraphs apply to 17.0 and later only)

10.0.1.0.4 (2026-11-01)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice form: new section Invoicing from sale order (Fatturazione da ordine di vendita), shown only when the sale module is installed
* [NEW] Accounting Dashboard (journal kanban) help page: cards of sale, purchase, bank, cash and miscellaneous journals, the More menu, search, set up and FAQ

10.0.1.0.3 (2026-10-31)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages in the standard layout: sections renamed How to insert a new record, How to update a record, Suggestions for search, How to set up, Report and export file (Italian titles too); the Report section explains how to export the records to a file

10.0.1.0.2 (2026-10-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Migrated from 18.0 to 10.0 (requires web_context_help 10.0.1.0.7)

18.0.1.0.1 (2026-10-25)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages declared with :priority: 96, the priority of the module pages: the last fallback after the pages of the administrator (requires web_context_help 18.0.1.0.6)

18.0.1.0.0 (2026-10-02)
~~~~~~~~~~~~~~~~~~~~~~~

* [NEW] Help pages for invoice list and form, English and Italian, Odoo 10 to 18 (account.invoice before 13.0, account.move since 13.0, journal entries excluded)
