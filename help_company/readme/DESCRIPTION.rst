Context help pages for the company list and form (``res.company``), shown by
web_context_help.

Every page follows the standard layout of web_context_help: description, new
record, update record or search, set up, report, example, FAQ and footer.

The *How to set up* section of the form explains how to activate the Italian
electronic invoicing (FatturaPA through the SdI) on Odoo 12.0, with one of
the two alternatives: Odoo's ``l10n_it_edi`` (sending by PEC) or the OCA
modules ``l10n_it_fatturapa``, ``l10n_it_fatturapa_out``,
``l10n_it_fatturapa_in`` and an SdI channel (``l10n_it_fatturapa_pec`` or
``l10n_it_fatturapa_sdicoop``): what each one does, and the company, settings
and customer data to fill in.

When ``l10n_it_edi`` or ``l10n_it_fatturapa`` is installed, the page shows an
important warning: the Regime fiscale of the company (*Tax System* or
e-invoice *Fiscal Position*) must be set.

Pages are in English and Italian.
