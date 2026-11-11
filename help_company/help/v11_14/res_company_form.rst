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

Click on button **Ready** for help about how to use this help; click on
button **FAQ** for the most common solved questions.

A company is the legal entity that issues the documents of Odoo: its name,
logo, address and :field:`Tax ID <vat>` are printed on quotations, invoices
and every other report, and the accounting of each company is kept apart, in
its own :field:`currency <currency_id>`. A database can hold several
companies, once *Manage multiple companies* is enabled; a company of a group
can have a :field:`Parent Company <parent_id>`. The address, the Tax ID, the
phone and the email of the company are stored on its partner, a contact like
any other.

.. help-if:: module = l10n_it_edi

   .. important::

      **Set the Tax System.** The Italian electronic invoice requires the
      :field:`Tax System <l10n_it_tax_system>` (the Regime fiscale) of the
      company, e.g. *[RF01] Ordinario* or *[RF19] Regime forfettario*: while
      it is empty, validating an invoice stops with the error *The seller's
      company must have a tax system.* Choose it in the **General
      Information** tab, under the Tax ID.

.. help-if:: module = l10n_it_fatturapa

   .. important::

      **Set the Fiscal Position of the e-invoice.** The Italian electronic
      invoice requires the :field:`Fiscal Position
      <fatturapa_fiscal_position_id>` (the Regime fiscale) of the company,
      e.g. *Regime ordinario* (RF01) or *Regime forfettario* (RF19): choose it
      in the **E-invoice** tab. The field is required: the form cannot be
      saved while it is empty.

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

.. help-if:: module = l10n_it_edi

   * Codice Fiscale: *01234567890* (for a company it is usually the VAT
     number without *IT*)
   * Tax System: *[RF01] Ordinario*
   * Server PEC, Company PEC-mail and Government PEC-mail, as described in
     *How to set up*

   and, in the **Electronic Invoicing** tab, *Company listed on the register
   of companies* checked, with the office, the number, the share capital and
   the liquidation state of the register.

.. help-if:: module = l10n_it_fatturapa

   * Fiscal Code: *01234567890* (for a company it is usually the VAT number
     without *IT*)

   then, in the **REA Data** tab, the REA data and, in the **E-invoice** tab,
   the Fiscal Position *Regime ordinario* and the ES channel.

.. help-if:: module != l10n_it_edi and module != l10n_it_fatturapa

   then install the e-invoicing modules described in *How to set up* and fill
   in the Fiscal Code and the Regime fiscale.

.. _faq:

FAQ
---

Click on button **Topic** to return to the specific help page.

.. help-question:: Why don't I see the Regime fiscale field?

   It is added by the e-invoicing modules: the *Tax System* under the Tax ID
   with *Italy - E-invoicing* (``l10n_it_edi``), the *Fiscal Position* of the
   **E-invoice** tab with *ITA - Fattura elettronica - Base*
   (``l10n_it_fatturapa``). Install one of them: they cannot be installed
   together.

.. help-question:: Validating an invoice says "The seller's company must have a tax system."

   The :field:`Tax System <l10n_it_tax_system>` of the company is empty: set
   it in this form and validate the invoice again.

.. help-question:: Why can't I change the currency?

   The currency cannot be changed once the company has journal items: create
   a new company if you need another accounting currency.

.. help-question:: Why can't I duplicate a company?

   Odoo does not allow it (*Duplicating a company is not allowed. Please
   create a new company instead.*): create the new company from the list.

.. help-question:: Where do I change the logo and the layout of the reports?

   The logo is changed here: press **Edit** and click the image. The paper
   format and the layout of the reports are set in **Settings ‣ General
   Settings**, section **Business Documents**: *Format* and *Document
   Template* (**Change Document Template**).

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-11-07 18:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
