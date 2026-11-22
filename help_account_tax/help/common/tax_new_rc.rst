.. _new_record_rc:

How to insert a tax for reverse charge
--------------------------------------

In the reverse charge the VAT is not charged by the supplier: the buyer
integrates the document with the VAT and records it both in credit and in
debit. The nature of the operation is one of *[N6.1] ... [N6.9]*. The package
*Italy* loads, for each nature, the taxes of both sides:

.. list-table::
   :header-rows: 1

   * - Nature
     - Operation
     - Law reference of the sales tax
   * - N6.1
     - Scrap and recovery materials
     - art.74, comma 7-8, D.P.R. 633/1972
   * - N6.2
     - Gold (*N6.2b*: investment gold)
     - art.17, comma 5, D.P.R. 633/1972
   * - N6.3
     - Construction subcontractors
     - art.17, comma 6, lett. a, D.P.R. 633/1972
   * - N6.4
     - Investments in construction (buildings)
     - art.17, comma 6, lett. a-bis, D.P.R. 633/1972
   * - N6.5
     - Cellphones
     - art.17, comma 6, lett. b, D.P.R. 633/1972
   * - N6.6
     - Electronics
     - art.17, comma 6, lett. c, D.P.R. 633/1972
   * - N6.7
     - Construction services
     - art 17, comma 6, lett. a-ter, D.P.R. 633/1972
   * - N6.8
     - Energy
     - art.17, comma 6, lett. d-bis, d-ter, d-quater, D.P.R. 633/1972

* **Sales taxes** *0% RC N6.1* ... *0% RC N6.8*: 0% on the invoices of the
  supplier who sells in reverse charge, with the nature and the law reference
  of the table (for N6.9 *Inversione contabile - altri casi* there is none:
  duplicate one and choose the nature).
* **Purchase taxes**, one for each rate and nature: *22% RC N6.3*, *10% RC
  N6.3*, *5% RC N6.3*, *4% RC N6.3*... (in Italian *IC* for *inversione
  contabile*). Only *22% RC N6.7* and *10% RC N6.7* (and the sales *0% RC N6.7*) are active
  when the package is installed: activate the others as in *How to activate a tax of the package*.
* **Purchase taxes outside Italy**: *22% S RC* (services) and *22% G RC*
  (goods) and the same for 10%, 5% and 4% (the 0% ones have nature N1), used
  for the supplies from the EU by the fiscal position *Intra-Community*,
  and *22% G D*, for the goods in a VAT deposit.

The purchase taxes have two lines *of tax* in the table **Distribution for
Invoices** (and in the refunds, with the opposite signs): +100% on the account
*VAT credit* and -100% on the account *VAT debt*, with the tax grids of the
VJ section of the VAT report. So the total of the vendor bill does not change
and the VAT is both credited and due.

#. Open **Invoicing ‣ Configuration ‣ Accounting ‣ Taxes**, search ``RC`` and
   activate the taxes of the natures and rates you use.
#. Open the purchase tax, e.g. *22% RC N6.3*, and check the :field:`Tax Type
   <type_tax_use>` (*Purchases*), the two lines of the tab **Definition** and
   the :field:`Tax Group <tax_group_id>` (*22% VAT*).
#. For a new rate or nature duplicate the nearest purchase tax: the two lines
   of the distribution are copied. Change the name, the amount and the tax
   grids when the nature changes, and do the same for the refunds table: the
   same lines in the same order.
#. For the sales in reverse charge duplicate the tax *0% RC N6.x*, set the
   :field:`Exoneration <l10n_it_exempt_reason>` and the :field:`Law Reference
   <l10n_it_law_reference>` and choose the tax on the invoice lines.
#. Fiscal position: the package has *Construction Subcontractors - RC* (in
   Italian *Subappalto Edilizia - IC*), which replaces *22% S* with *22% RC
   N6.3* (and 10%, 5%, 4%) on the purchases and *0%* with *0% RC N6.3* on the
   sales. For the other natures add the lines to a similar fiscal position.
#. Integration of the invoice: Odoo does not create a second document. The
   vendor bill with a reverse charge tax is itself the self-invoice: once
   posted, the button [`Send to SDI`] sends it to the SdI with the document
   type chosen from the tax grids (TD16 for the domestic reverse charge, TD17
   for the services from abroad, TD18 for the goods from the EU, TD19 for the
   goods in a VAT deposit). A bill with taxes of the foreign reverse charge cannot
   mix services and goods: Odoo finds no document type, so use one bill for
   each, with the right :field:`Tax Scope <tax_scope>`.


**Choosing the TD type**

The function ``_l10n_it_edi_get_document_type`` goes through the table
``_l10n_it_edi_document_type_mapping``. It uses the first entry whose
features all match:

.. list-table::
   :header-rows: 1

   * - TD
     - Case
     - Match criteria
   * - TD16
     - Domestic reverse charge
     - VJ6, VJ7, VJ8, VJ12 to VJ17
   * - TD17
     - Services from abroad
     - VJ3, services
   * - TD18
     - EU goods
     - VJ9, goods, partner in EU
   * - TD19
     - Goods in Italy / VAT deposit
     - VJ3, goods, goods_in_italy
   * - TD28
     - San Marino
     - partner country SM
