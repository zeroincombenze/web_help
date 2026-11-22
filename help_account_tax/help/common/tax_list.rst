.. help-page:: tax_list
   :title: Taxes
   :model: account.tax
   :view: account.view_tax_tree
   :view-type: list
   :priority: 96

Taxes
=====

.. _description:

Description
-----------

Click on button [`Ready`] for help about how to use this help; click on
button [`FAQ`] for the most common solved questions.

The list of the taxes: the codes that Odoo applies to the invoice lines to
compute the VAT (or any other tax) and to fill the tax report. Each row shows
the :field:`tax name <name>`, the :field:`description <description>`, the
:field:`tax type <type_tax_use>` (*Sales*, *Purchases* or *None*), the
:field:`tax scope <tax_scope>` (*Services* or *Goods*), the :field:`label on
invoices <invoice_label>`, in a multi-company database the :field:`company
<company_id>`, and the **Active** toggle. The archived taxes are shown too, in
grey. Click a row to open the tax.

.. _new_record:

How to insert a new record
--------------------------

Press [`New`] at the top left: an empty form opens, see its help for the
fields to fill in.

.. help-include:: tax_list_search.rst

.. _update_record:

How to update a record
----------------------

Click on a line of the list to open its form, then follow the help of the
form to change it.

.. help-include:: tax_cancel.rst

.. help-include:: tax_configure.rst

.. help-include:: tax_report.rst

.. help-include:: tax_list_example.rst

.. _faq:

FAQ
---

Click on button [`Topic`] to return to the specific help page.

.. help-question:: Why don't I see some taxes?

   The list opens with the filters **Sale** and **Purchase**: the taxes of
   type *None*, e.g. the children of the split payment taxes, are hidden.
   Remove the filters, or search for the name, to see them. The archived taxes
   are in the list, in grey.

.. help-question:: How do I activate a tax that came with the fiscal localization?

   Click its **Active** toggle at the end of the line. Some taxes of the
   Italian package, e.g. 5% and 4% or most of the reverse charge ones, are
   archived when the package is installed. See *How to set up*.

.. help-question:: Which taxes does Odoo provide for Italy?

   Those of the module ``l10n_it`` (**Italy - Accounting**), loaded when
   *Italy* is chosen as *Package* in **Invoicing ‣ Configuration ‣ Settings**.
   See *How to set up*.

.. _footer:

Footer
------

Page created on 2026-11-22 16:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
