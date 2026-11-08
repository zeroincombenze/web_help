.. help-page:: res_company_form
   :title: Company
   :model: res.company
   :view-type: form
   :priority: 96

Company
=======

.. _description:

Description
-----------

A company is the legal entity that issues the documents of Odoo: its name,
logo, :field:`Company Tagline <rml_header1>`, address and :field:`Tax ID
<vat>` are printed on quotations, invoices and every other report, and the
accounting of each company is kept apart, in its own :field:`currency
<currency_id>`. A database can hold several companies, once *Manage multiple
companies* is enabled; a company of a group can have a :field:`Parent Company
<parent_id>`. The address, the Tax ID, the phone and the email of the company
are stored on its partner, a contact like any other.

.. help-if:: module = l10n_it_einvoice_base

   .. important::

      **Set the Fiscal Position of the e-invoice.** The Italian electronic
      invoice requires the *Fiscal Position* (the Regime fiscale) of the
      company, e.g. *Regime ordinario* (RF01) or *Regime forfettario* (RF19):
      while it is empty the export of the e-invoice stops with the error
      *E-invoice fiscal position not set.* The field is not on this form: set
      it in **Invoicing ‣ Configuration ‣ Settings**, section **Electronic
      Invoice**, together with the *Sequence* of the e-invoice files.

.. help-include:: res_company_new.rst

.. help-include:: res_company_update.rst

.. help-include:: res_company_configure.rst

.. help-include:: res_company_report.rst

.. _example:

Example
-------

**An Italian company ready for e-invoicing.** Press **Edit** and, in the
**General Information** tab, fill in:

* Address: *Via Roma 1*, *00100 Roma*, state *Roma*, country *Italy*
* Tax ID: *IT01234567890*
* Phone and Email: both are written in the e-invoice

.. help-if:: module = l10n_it_einvoice_base

   then:

   * in the **REA Data** tab, the office, the number, the capital, the member
     type and the liquidation state of the REA, if the company is listed on
     the register of companies;
   * on the contact of the company, the *Fiscal Code* (for a company it is
     usually the VAT number without *IT*);
   * in **Invoicing ‣ Configuration ‣ Settings**, section **Electronic
     Invoice**, the *Fiscal Position* *Regime ordinario* and the *Sequence*.

.. help-if:: module != l10n_it_einvoice_base

   then install the e-invoicing modules described in *How to set up*.

.. _faq:

FAQ
---

.. help-question:: Where is the Regime fiscale of the company?

   It is the *Fiscal Position* of the section **Electronic Invoice** in
   **Invoicing ‣ Configuration ‣ Settings**, added by the module *EInvoice +
   FatturaPA* (``l10n_it_einvoice_base``). The possible values are listed in
   **Invoicing ‣ Configuration ‣ Accounting ‣ Tax Authority Definitions ‣
   Posizione Fiscale Fattura Elettronica**.

.. help-question:: The export says "E-invoice fiscal position not set."

   The *Fiscal Position* of the e-invoice is empty: set it in **Invoicing ‣
   Configuration ‣ Settings**, section **Electronic Invoice**, and export the
   invoice again.

.. help-question:: Where do I write the Fiscal Code of the company?

   The *Fiscal Code* (module ``l10n_it_fiscalcode``) is stored on the contact
   of the company, not on this form: open the contact (in developer mode the
   *Partner* field of this form links to it), press **Edit** and fill in
   *Fiscal Code*, next to the Tax ID.

.. help-question:: Why can't I change the currency?

   The currency cannot be changed once the company has journal items (*You
   cannot change the currency of the company since some journal items already
   exist*): create a new company if you need another accounting currency.

.. help-question:: Where do I change the logo and the layout of the reports?

   The logo is changed here: press **Edit** and click the image. The *Company
   Tagline*, under the name, is printed in the header of the reports. The
   footer and the paper format are set in **Settings ‣ General Settings**,
   section **Report Configuration**.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-11-07 18:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
