.. help-page:: tax_form
   :title: Taxes
   :model: account.tax
   :view: account.view_tax_form
   :view-type: form
   :priority: 96

Taxes
=====

.. _description:

Description
-----------

Click on button [`Ready`] for help about how to use this help; click on
button [`FAQ`] for the most common solved questions.

A tax tells Odoo how to compute the tax of an invoice line (e.g. the VAT) and
where to post it. Taxes are chosen on the products, proposed by the fiscal
position of the partner and written on the invoice lines.

Every tax has a :field:`name <name>`, a :field:`computation
<amount_type>` (percentage, fixed, percentage tax included or group of
taxes), a :field:`type <type_tax_use>` (*Sales*, *Purchases* or *None*), an
optional :field:`scope <tax_scope>` (*Services* or *Goods*) and the
:field:`amount <amount>`. The tab **Definition** holds the distribution of the
tax on the accounts and on the tax grids, for the invoices and for the
refunds; the tab **Advanced Options** the label on invoices, the tax group,
the country and the accounting options (e.g. *Affect Base of Subsequent
Taxes*, *Tax Exigibility*). With the Italian localization it shows also
:field:`Exoneration <l10n_it_exempt_reason>` (the nature code N1...N7) and
:field:`Law Reference <l10n_it_law_reference>`.

.. help-include:: tax_new.rst

.. help-include:: tax_new_duplicate.rst

.. help-if:: module = l10n_it

   .. help-include:: tax_new_vat.rst

   .. help-include:: tax_new_novat.rst

   .. help-include:: tax_new_split.rst

   .. help-include:: tax_new_rc.rst

.. help-include:: tax_update.rst

.. help-include:: tax_cancel.rst

.. help-include:: tax_configure.rst

.. help-include:: tax_report.rst

.. help-include:: tax_example.rst

.. _faq:

FAQ
---

Click on button [`Topic`] to return to the specific help page.

.. help-question:: Why can't I save a tax with 0%?

   With the Italian localization a tax with Tax Computation *Percentage* and
   amount 0 needs :field:`Exoneration <l10n_it_exempt_reason>` and
   :field:`Law Reference <l10n_it_law_reference>`: Odoo says *If the tax
   amount is 0%, you must enter the exoneration code and the related law
   reference.*

.. help-question:: Why does Odoo say "Tax names must be unique!"?

   Two taxes of the same company cannot have the same name, type, scope and
   country. Change the name, e.g. add a letter, or the scope.

.. help-question:: Why does Odoo say the distribution should have a total factor of 100?

   The lines *of tax* of **Distribution for Invoices** must add up to +100%
   (and, when there are negative lines, as in the reverse charge, to -100%);
   **Distribution for Refunds** must have the same lines in the same order,
   and each table exactly one *Base* line.

.. help-question:: Why can't I choose children for my group tax?

   The :field:`Children Taxes <children_tax_ids>` table is shown when Tax
   Computation is *Group of Taxes* and the tax type is not *None*. The
   children must be of type *None* or of the same type of the group, and not
   groups themselves.

.. help-question:: Why does the tax not appear on the invoice line?

   An archived tax is not proposed. Check also the :field:`Tax Type
   <type_tax_use>` (sales taxes are not proposed on vendor bills) and the
   *Fiscal Position* of the partner, which may replace the tax of the product.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-11-22 16:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
