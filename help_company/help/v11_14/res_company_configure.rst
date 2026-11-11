.. _configure:

How to set up
-------------

**Settings ‣ General Settings**, section **Multi-companies**: *Manage
multiple companies* enables several companies, then press **Save**; the
**Companies** button lists them. With several companies the form shows the
*Parent Company*, the company switcher appears in the top bar and the users
get *Allowed Companies* and *Current Company* in the **Access Rights** tab of
their form (**Settings ‣ Users & Companies ‣ Users**); the current company is
the one the user works in. The section **Business Documents** sets the paper
*Format* and the *Document Template* of the reports. **Settings ‣
Dashboard**, box of the company, **Set Up** opens the current company.

With Invoicing, every company has its own chart of accounts and taxes,
chosen in **Invoicing ‣ Configuration ‣ Settings** (*Package* of the
**Fiscal Localization**) while working in that company.

Electronic invoicing (Italy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Italian companies send and receive invoices as XML files (*FatturaPA*)
through the *Sistema di Interscambio* (SdI) of the Agenzia delle Entrate.
The chart of accounts is **Italy - Accounting** (``l10n_it``), or **ITA -
Fiscal localization by Zeroincombenze(R)** (``l10n_it_coa``), more detailed.
For the e-invoice there are two alternatives, which cannot be installed
together; install one of them from **Apps**.

**Odoo module: Italy - E-invoicing** (``l10n_it_edi``). When an invoice of
an Italian company is validated, it builds the XML and sends it by PEC to the
SdI; it reads the vendor bills and the notices of the SdI from the PEC
mailbox. It adds to the company the *Codice Fiscale*, the *Tax System*, the
PEC fields and the **Electronic Invoicing** tab, and to the contacts the *PEC
e-mail*, the *Codice Fiscale* and the *PA index*. Its labels are not
translated. To activate it:

#. Set the :field:`country <country_id>` of the company to *Italy* and fill
   in the complete address (street, ZIP of 5 digits, city), the :field:`Tax
   ID <vat>`, the *Codice Fiscale* and the *Tax System*: validating an
   invoice stops when one of them is missing.
#. In developer mode, set up the PEC mailbox of the company in **Settings ‣
   Technical ‣ Email ‣ Outgoing Mail Servers**, and in **Settings ‣ Technical
   ‣ Email ‣ Incoming Mail Servers** (IMAP) with *PEC server* checked.
#. On this form, under the address, choose the *Server PEC* and fill in the
   *Company PEC-mail* and the *Government PEC-mail* (the PEC address of the
   SdI, e.g. *sdi01@pec.fatturapa.it*).
#. In the **Electronic Invoicing** tab, check *Company listed on the register
   of companies* and fill in its data, if the company is listed; check
   *Company have a tax representative* for a foreign company with a tax
   representative in Italy.
#. On every customer fill in the *PA index* (the 7 characters destination
   code) or the *PEC e-mail*; for a private person the Codice Fiscale. The
   invoices to the Public Administration (6 characters PA index) are not
   sent: download the XML and send it yourself.

**OCA modules: ITA - Fattura elettronica - Base** (``l10n_it_fatturapa``) of
the repository *l10n-italy*, with **ITA - Fattura elettronica - Emissione**
(``l10n_it_fatturapa_out``) for the customer invoices, **ITA - Fattura
elettronica - Ricezione** (``l10n_it_fatturapa_in``) for the vendor bills,
and the channel to the SdI: **ITA - Fattura elettronica - Supporto PEC**
(``l10n_it_fatturapa_pec``) or **ITA - Fattura elettronica - Supporto
SDICoop** (``l10n_it_fatturapa_sdicoop``), both on ``l10n_it_sdi_channel``.
They install the Fiscal Code (``l10n_it_fiscalcode``) and the REA data
(``l10n_it_rea``); optional ``l10n_it_fatturapa_export_zip`` exports several
e-invoices in a ZIP file. To activate them:

#. Set the :field:`country <country_id>` of the company to *Italy* and fill
   in the complete address, the :field:`Tax ID <vat>`, the *Fiscal Code* and,
   in the **REA Data** tab, the REA data, if the company is listed.
#. Set up the channel in **Invoicing ‣ Configuration ‣ Accounting ‣ ES
   Channels**.
#. In the **E-invoice** tab of this form choose the *Fiscal Position* (the
   Regime fiscale) and the *ES channel*, both required.
#. In **Invoicing ‣ Configuration ‣ Settings**, section **Electronic
   Invoices**, check the *Fiscal Position* and fill in, when needed, *Art.
   73*, the *Legal Tax Representative*, the *Stable Organization* and the
   *Third Party/Sender*. Press **Save**.
#. On every customer, in the **Electronic Invoice** tab, check *Enable
   electronic invoicing* and fill in the *Addressee Code* (7 characters) or
   the *Addressee PEC*.

.. help-if:: module = l10n_it_edi

   .. important::

      The invoices of the company cannot be validated while its **Tax
      System** is empty: check it now in the **General Information** tab.

.. help-if:: module != l10n_it_edi and module != l10n_it_fatturapa

   No e-invoicing module is installed in this database: the fields of the
   Regime fiscale and of the e-invoice appear once one of them is installed.
