Context help pages for the company list and form (``res.company``), shown by
web_context_help.

Every page follows the standard layout of web_context_help: description, new
record, update record or search, set up, report, example, FAQ and footer.

The *How to set up* section of the form explains how to activate the Italian
electronic invoicing (FatturaPA through the SdI) on Odoo 10.0: which modules
to install (``l10n_it`` or ``l10n_it_coa``, ``l10n_it_einvoice_base``,
``l10n_it_einvoice_out``, ``l10n_it_einvoice_in``,
``l10n_it_einvoice_send2sdi``, …), what each one does, and the company,
settings and customer data to fill in.

When ``l10n_it_einvoice_base`` is installed, the page shows an important
warning: the e-invoice *Fiscal Position* (Regime fiscale) of the company must
be set, otherwise the e-invoices are not exported.

Pages are in English and Italian.
