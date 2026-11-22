.. _new_record:

How to insert a new record
--------------------------

The steps load a tax with VAT, *21%* on sales. For the Italian tax codes
with the nature (without VAT, split payment, reverse charge) see the chapters
*How to insert a tax without VAT*, *How to insert a tax for split payment* and
*How to insert a tax for reverse charge*.

.. help-version:: 18

   .. help-tour:: account_tax_new
      :label: Show me how to create a tax

      .. help-step:: new
         :click:

         Press **New** to open an empty tax form.

      .. help-step:: field:name
         :position: right

         Write the tax name, shown when the tax is chosen on a line.

      .. help-step:: field:amount_type
         :position: right

         Choose how the tax is computed: *Percentage* for the VAT.

      .. help-step:: field:type_tax_use
         :position: left

         Choose *Sales* or *Purchases*.

      .. help-step:: field:amount
         :position: left

         Write the rate.

      .. help-step:: tab:advanced_options
         :position: bottom
         :click:

         Open **Advanced Options** to set the label, the tax group and the
         country.

#. Open **Invoicing ‣ Configuration ‣ Accounting ‣ Taxes** and press
   [`New`].
#. Write the :field:`tax name <name>`, e.g. *21%*: it is the text shown when
   the tax is chosen on a line. The name must be unique for the same type,
   scope and country.
#. Leave :field:`Tax Computation <amount_type>` on *Percentage*; the other
   options are *Fixed*, *Group of Taxes* and *Percentage Tax Included*.
#. Choose the :field:`Tax Type <type_tax_use>`: *Sales* for the customer
   invoices, *Purchases* for the vendor bills; *None* for the taxes used only
   as children of a group.
#. Choose the :field:`Tax Scope <tax_scope>`, *Services* or *Goods*, or leave
   it empty. The scope is needed for the reverse charge purchases, see *How to
   insert a tax for reverse charge*.
#. Write the rate in :field:`Amount <amount>`, e.g. 21.
#. In the tab **Advanced Options** the :field:`Label on Invoices
   <invoice_label>` is already filled with the rate (*21%*); choose the
   :field:`Tax Group <tax_group_id>` (e.g. *21% VAT*) and check the
   :field:`Country <country_id>` (*Italy*).
#. In the tab **Definition** the tables **Distribution for Invoices** and
   **Distribution for Refunds** have a line *Base* and a line *of tax*, 100%:
   on the line *of tax* choose the :field:`Account <account_id>` (for the
   Italian package *VAT debt* on the sales, *VAT credit* on the purchases)
   and the **Tax Grids** of the tax report. It is easier to **Duplicate** a
   similar tax of the package and change its name and rate.
#. With the Italian localization, when the amount is 0% fill
   :field:`Exoneration <l10n_it_exempt_reason>` and :field:`Law Reference
   <l10n_it_law_reference>`: see *How to insert a tax without VAT*.
#. The record is saved automatically when you leave it, or at once with the
   cloud icon next to the breadcrumb.
