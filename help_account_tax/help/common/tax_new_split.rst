.. _new_record_split:

How to insert a tax for split payment
-------------------------------------

In the split payment the customer is a public administration: it pays the
supplier the taxable amount only and the VAT goes to the tax authority. The
package *Italy* loads, for each rate, three taxes:

* *22% SP pos.*, *10% SP pos.*, *5% SP pos.*, *4% SP pos.*: type *None*, the
  positive VAT, with the tax grids of the VAT report and of the split payment
  (VE38);
* *22% SP neg.*, *10% SP neg.*, *5% SP neg.*, *4% SP neg.*: type *None*, with
  the negative amount (-22, -10, -5, -4) and :field:`Included in Price
  <price_include_override>` *Tax Excluded*, which cancel the VAT in the total
  of the invoice;
* *22% SP*, *10% SP*, *5% SP*, *4% SP*: type *Sales*, :field:`Tax Computation
  <amount_type>` *Group of Taxes*, with the two taxes above in the table
  **Children Taxes**: these are the ones to choose on the invoices.

The distribution of the two children posts the tax on the account *VAT Split
Payment*; the tax group of the group tax is *Split Payment*. Do not change
them: duplicate the whole set when you need another rate.

#. Open **Invoicing ‣ Configuration ‣ Accounting ‣ Taxes**, remove the filters
   **Sale** and **Purchase** and search ``SP``: the twelve taxes are there. They
   are active when the package is installed.
#. Open **Invoicing ‣ Configuration ‣ Accounting ‣ Fiscal Positions** and
   open *Split Payment* (in Italian *Scissione dei Pagamenti*): in the tab
   **Tax Mapping** *22%* is replaced by *22% SP*, and so for 10%, 5% and 4%.
#. On the public administration partner, tab **Invoicing**, group **Fiscal
   Information**, choose the *Fiscal Position* *Split Payment*. The invoices of the
   partner get the group taxes.
#. For a rate that is not loaded (e.g. 21%) duplicate the three taxes of a
   rate: change the names and the amounts of the two children (+21 and -21),
   the :field:`Tax Group <tax_group_id>` of the positive one (*21% VAT*), then
   on the group tax replace the :field:`Children Taxes <children_tax_ids>`
   with the two new ones. Then add the line to the *Tax Mapping* of the fiscal
   position.

