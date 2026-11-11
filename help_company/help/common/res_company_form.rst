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
logo, address, :field:`Tax ID <vat>` and :field:`currency <currency_id>` are
printed on quotations, invoices and every other report, and the accounting of
each company is kept apart. A database can hold several companies; a
company can have **Branches**, which share the accounting settings of the
main company. The address, the Tax ID and the contacts of the company are
stored on its :field:`partner <partner_id>`, a contact like any other.

.. help-if:: module = l10n_it_edi

   .. important::

      **Set the Regime fiscale.** The Italian electronic invoice requires the
      :field:`Regime fiscale <l10n_it_tax_system>` (Tax System) of the
      company, e.g. *[RF01] Ordinario* or *[RF19] Regime forfettario*: while
      it is empty Odoo does not create the e-invoices, and sending an invoice
      stops with the error *Company/ies should have a Tax System*. Choose it in the
      **General Information** tab, under the Tax ID; the field is shown when
      the country of the company is Italy.

.. help-include:: res_company_new.rst

.. help-include:: res_company_update.rst

.. help-include:: res_company_configure.rst

.. help-include:: res_company_report.rst

.. _example:

Example
-------

**An Italian company ready for e-invoicing.** In the **General Information**
tab:

* Address: *Via Roma 1*, *00100 Roma (RM)*, *Italy*
* Tax ID: *IT01234567890*

.. help-if:: module = l10n_it_edi

   * Codice Fiscale: *01234567890* (for a company it is usually the VAT
     number without *IT*)
   * Regime fiscale: *[RF01] Ordinario*

   and, in the **Electronic Invoicing** tab, *Company listed on the register
   of companies* checked, with the office, the number, the share capital and
   the liquidation state of the REA.

.. help-if:: module != l10n_it_edi

   then install the e-invoicing modules described in *How to set up* and fill
   in the Codice Fiscale and the Regime fiscale.

.. _faq:

FAQ
---

Click on button **Topic** to return to the specific help page.

.. help-question:: Why don't I see the Regime fiscale field?

   The field is added by the module *Italy - E-invoicing* (``l10n_it_edi``)
   and is shown only when the :field:`country <country_id>` of the company is
   Italy: install the module and set the country.

.. help-question:: The invoice says "Company/ies should have a Tax System".

   The :field:`Regime fiscale <l10n_it_tax_system>` of the company is empty:
   set it in this form and send the invoice again.

.. help-question:: Why can't I change the currency?

   The currency cannot be changed once the company has journal items: create
   a new company if you need another accounting currency.

.. help-question:: Where do I change the logo and the layout of the reports?

   The logo is changed here, clicking the image. The layout (fonts, colors,
   header and footer) is set in **Settings ‣ General Settings ‣ Companies ‣
   Configure Document Layout**.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-11-07 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
