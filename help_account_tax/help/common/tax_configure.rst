.. _configure:

How to set up
-------------

* The taxes are in **Invoicing ‣ Configuration ‣ Accounting ‣ Taxes**, for
  the users who see the **Configuration** menu.
* The taxes of a country are loaded by the fiscal localization:
  **Invoicing ‣ Configuration ‣ Settings**, block **Fiscal Localization**,
  field *Package*. The package can be chosen only while
  the company has no accounting entries.
* In the same page the block **Default Taxes** has the fields *Sales Tax* and
  *Purchase Tax*: choose the taxes proposed on the new products (the Italian
  package sets *22%* on the sales and *22% G* on the purchases). On the
  product, tab **General Information**, the fields *Sales Taxes* and *Purchase
  Taxes* hold the taxes of that product.
* The **Fiscal Positions** (**Invoicing ‣ Configuration ‣ Accounting ‣ Fiscal
  Positions**) replace the taxes of the products: in the tab **Tax Mapping**,
  *Tax on Product* is replaced by *Tax to Apply*. A position is chosen on the
  partner, tab **Invoicing**, group **Fiscal Information**, field *Fiscal
  Position*, or detected automatically.
* The **Tax Groups** (menu **Invoicing ‣ Configuration ‣ Accounting ‣ Tax
  Groups**, in developer mode only) set the accounts of the total of every
  tax and the title under which it is printed.

**How to activate a tax of the package**

#. Open **Invoicing ‣ Configuration ‣ Accounting ‣ Taxes** and search the tax
   by name or by amount: the archived taxes are in the list, in grey.
#. Click the **Active** toggle of the line.

.. help-if:: module = l10n_it

   **Other Italian charts**

   The module ``l10n_it_coa`` (**Italia - Piano dei conti (Zeroincombenze)**)
   brings its own taxes, with Italian names such as *IVA 22% su vendite*,
   *Art. 17ter - split-payment* or *Acq. (RC 22%) N.I. art.17 c.2 DPR633*,
   and no nature code: the steps above to activate or duplicate a tax are the
   same, the names of the chapters *How to insert a tax ...* are those of ``l10n_it``.
