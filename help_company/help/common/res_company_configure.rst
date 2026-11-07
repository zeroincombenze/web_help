.. _configure:

How to set up
-------------

**Settings ‣ General Settings ‣ Companies** shows the current company:
**Update Info** opens it, **Manage Companies** lists all of them, and
**Configure Document Layout** sets the look of the reports. Each user works
for the companies in the *Allowed Companies* of the user, chosen in **Settings
‣ Users & Companies ‣ Users**; the default company is the one used at login.

With Invoicing, every company has its own *Fiscal Localization* (chart of
accounts and taxes), chosen in **Invoicing ‣ Configuration ‣ Settings** while
working in that company.

Electronic invoicing (Italy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Italian companies send and receive invoices as XML files (*FatturaPA*)
through the *Sistema di Interscambio* (SdI) of the Agenzia delle Entrate.
These modules are needed, from **Apps**:

* **Italy - Accounting** (``l10n_it``): the Italian chart of accounts and
  taxes; it is installed by choosing *Italy* as *Fiscal Localization*.
* **Italy - Accounting Zeroincombenze** (``l10n_it_coa``): alternative
  chart of accounts, more detailed, by Zeroincombenze.
* **Italy - E-invoicing** (``l10n_it_edi``): installed with ``l10n_it``. It
  builds the XML of customer invoices and credit notes, sends them to the SdI
  and imports the vendor bills received, through the Odoo proxy (module
  ``account_edi_proxy_client``, installed with it). It adds to the company
  the :field:`Codice Fiscale <l10n_it_codice_fiscale>`, the **Regime
  fiscale** (Tax System) and the **Electronic Invoicing** tab, and to the
  contacts the *Codice Fiscale*, the *Destination Code* and the *PEC
  e-mail*.
* **Italy - E-invoicing - Additional module to support the debit notes**
  (``l10n_it_edi_ndd``) and **Italy - Sale E-invoicing**
  (``l10n_it_edi_sale``): installed automatically, they add the document
  types and the data of the sale orders to the XML.
* Optional: **Italy - E-invoicing (Withholding)**
  (``l10n_it_edi_withholding``) for the withholding taxes and the pension
  funds, **Italy - Declaration of Intent** (``l10n_it_edi_doi``) for the
  regular exporters.

The OCA repository *l10n-italy* adds, if needed:

* ``l10n_it_edi_extension``: preview and download of the XML, more XML data
  (Art. 73, Public Administration reference, stable organization), better
  import of the received XML files.
* ``l10n_it_edi_pec`` (with ``l10n_it_edi_sdi``): sends and receives the
  e-invoices by PEC (certified email) instead of the Odoo proxy.
* ``l10n_it_edi_sender_partner``: the third party intermediary that issues
  the invoices for the company.
* ``l10n_it_edi_related_document``: the related documents (order,
  contract, agreement, …) written in the XML.

To activate the e-invoicing:

#. Set the :field:`country <country_id>` of the company to *Italy* and fill
   in the complete address (street, ZIP, city), the :field:`Tax ID <vat>`
   and the Codice Fiscale.
#. Set the **Regime fiscale** of the company (see the warning at the top of
   the page).
#. In the **Electronic Invoicing** tab, check *Company listed on the
   register of companies* and fill in the REA data, if the company is listed;
   check *Company have a tax representative* for a foreign company with a
   tax representative in Italy.
#. Open **Invoicing ‣ Configuration ‣ Settings ‣ Italian Electronic
   Invoicing**: choose the *Fattura Elettronica mode* (*Demo* only simulates
   the sending, *Test (experimental)* sends to the test service, *Official*
   to the SdI) and check *Allow Odoo to process invoices*. The official and
   test registration cannot be changed afterwards. With ``l10n_it_edi_pec``,
   check *PEC Channel* instead and choose the outgoing and incoming PEC
   servers and the PEC address of the SdI.
#. On every customer fill in the *Destination Code* (7 characters, 6 for the
   Public Administration) or the *PEC e-mail*; for a private person the
   Codice Fiscale.

.. help-if:: module = l10n_it_edi

   .. important::

      The e-invoices are not created while the **Regime fiscale** of the
      company is empty: check it now in the **General Information** tab.

.. help-if:: module != l10n_it_edi

   The module *Italy - E-invoicing* is not installed in this database: the
   Codice Fiscale, the Regime fiscale and the **Electronic Invoicing** tab
   appear once it is installed.
