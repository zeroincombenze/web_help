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
