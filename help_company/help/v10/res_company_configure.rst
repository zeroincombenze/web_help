.. _configure:

How to set up
-------------

**Settings ‣ General Settings**: **Configure your company data** opens the
current company; *Manage multiple companies*, in the **Multi Company** line,
enables several companies, then press **Apply**. With several companies the
form shows the *Parent Company*, the company switcher appears in the top bar
and the users get *Allowed Companies* and *Current Company* in the **Access
Rights** tab of their form (**Settings ‣ Users ‣ Users**); the current
company is the one the user works in. The section **Report Configuration**
sets the footer and the paper format of the reports.

With Invoicing, every company has its own chart of accounts and taxes,
chosen in **Invoicing ‣ Configuration ‣ Settings** (*Template* of the
**Chart of Accounts**) while working in that company.

Electronic invoicing (Italy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Italian companies send and receive invoices as XML files (*FatturaPA*)
through the *Sistema di Interscambio* (SdI) of the Agenzia delle Entrate. In
this version the e-invoicing comes from the Zeroincombenze modules of the
repositories *l10n-italy* and *l10n-italy-supplemental*, installed from
**Apps**:

* **Italy - Accounting** (``l10n_it``): the generic Italian chart of
  accounts and taxes; or **ITA - Fiscal localization by Zeroincombenze(R)**
  (``l10n_it_coa``), a more detailed chart of accounts.
* **EInvoice + FatturaPA** (``l10n_it_einvoice_base``): the base of the
  e-invoice. It installs with it the tables of the Agenzia delle Entrate
  (``l10n_it_ade``), the Fiscal Code (``l10n_it_fiscalcode``), the REA data
  (``l10n_it_rea``), the PEC address (``l10n_it_pec``) and the
  **Electronic Invoice** tab of the contacts (``l10n_it_fiscal_ipa``); it
  adds the section **Electronic Invoice** to **Invoicing ‣ Configuration ‣
  Settings**.
* **Italian Localization - FatturaPA - Emissione**
  (``l10n_it_einvoice_out``): builds the XML of the customer invoices:
  select them, then **Action ‣ Export Electronic Invoice**.
* **ITA - Fattura elettronica - Ricezione** (``l10n_it_einvoice_in``):
  imports the XML of the vendor bills received, from **Invoicing ‣ Purchases
  ‣ Electronic Bill**.
* **Send E-Invoice to SdI** (``l10n_it_einvoice_send2sdi``): sends the
  e-invoices to the SdI, and receives the vendor bills and the notices of
  the SdI, through an intermediary, the *Sender Channel*.
* Optional: **Fattura elettronica - Export ZIP**
  (``l10n_it_einvoice_export_zip``) exports several e-invoices in a ZIP file;
  the modules ``l10n_it_einvoice_out_*`` add to the XML the withholding tax
  (``_wt``), the reverse charge (``_rc``), the delivery documents (``_ddt``),
  the declarations of intent (``_li``); ``l10n_it_einvoice_stamp`` the stamp
  duty.

To activate the e-invoicing:

#. Set the :field:`country <country_id>` of the company to *Italy* and fill
   in the complete address (street, ZIP, city, state), the :field:`Tax ID
   <vat>`, the :field:`phone <phone>` and the :field:`email <email>`: the
   export of the e-invoice stops when one of them is missing.
#. Fill in the *Fiscal Code* on the contact of the company and, in the **REA
   Data** tab, the REA data, if the company is listed on the register of
   companies.
#. Open **Invoicing ‣ Configuration ‣ Settings**, section **Electronic
   Invoice**: choose the *Fiscal Position* (the Regime fiscale) and the
   *Sequence* of the e-invoice files, both required, the *E-Invoice Sender
   Channel* and, when needed, *Art. 73*, the *Legal Tax Representative* and
   the *Third Party/Sender*. Press **Apply**.
#. With ``l10n_it_einvoice_send2sdi``, set up the channel in **Invoicing ‣
   Configuration ‣ Accounting ‣ Tax Authority Definitions ‣ Sender Channel**
   with the data given by the intermediary.
#. On every customer, in the **Electronic Invoice** tab, check *Subjected to
   electronic invoice* and fill in the *Recipient Code* (7 characters) or the
   *PEC destinatario*.

.. help-if:: module = l10n_it_einvoice_base

   .. important::

      The e-invoices are not exported while the *Fiscal Position* of the
      section **Electronic Invoice** is empty: check it now in **Invoicing ‣
      Configuration ‣ Settings**.

.. help-if:: module != l10n_it_einvoice_base

   The module *EInvoice + FatturaPA* is not installed in this database: the
   section **Electronic Invoice** of the settings and the **REA Data** tab
   appear once it is installed.
