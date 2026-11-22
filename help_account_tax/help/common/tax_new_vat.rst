.. _new_record_vat:

How to insert a tax with VAT
----------------------------

The package *Italy* loads, for the sales, the taxes *22%*, *10%*, *5%* and
*4%* and, for the purchases, the same rates in two series: *22% G*, *10% G*,
*5% G*, *4% G* with :field:`Tax Scope <tax_scope>` *Goods* (in Italian *M* for
*merci*) and *22% S*, *10% S*, *5% S*, *4% S* with scope *Services*. The
default taxes of the company are *22%* on the sales and *22% G* on the
purchases.

#. Open **Invoicing ‣ Configuration ‣ Accounting ‣ Taxes** and search for the
   rate, e.g. ``22%``.
#. The taxes *5%* and *4%*, sales and purchases, are archived when the package
   is installed: click the **Active** toggle of the ones you need.
#. Open a tax to check it. In the tab **Advanced Options** the :field:`Tax
   Group <tax_group_id>` is the one of the rate (*22% VAT*, *10% VAT*, *5% VAT*
   or *4% VAT*) and the :field:`Country <country_id>` is *Italy*. In the tab
   **Definition** the distribution has the base line and a line *of tax* on
   the account *VAT debt* (sales) or *VAT credit* (purchases), with the tax
   grids of the VAT report.
#. For another rate (the package has the tax groups also for 2%, 12%, 20% and
   21%) follow *How to insert a new record by duplicate*, duplicating
   the tax of the same type, e.g. *22%* for a sale at 21%.

