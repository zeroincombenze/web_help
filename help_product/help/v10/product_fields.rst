.. _fields:

Main fields
~~~~~~~~~~~

* :field:`Product type <type>`: *Consumable*, *Service* or, with Inventory,
  *Stockable Product*.
* :field:`Internal category <categ_id>`: groups the products and gives the
  default income and expense accounts and the costing method.
* :field:`Internal reference <default_code>` and :field:`barcode <barcode>`:
  printed on documents and read by barcode scanners (on each variant when the
  product has several).
* :field:`Sale price <list_price>`: the base price, changed by pricelists;
  :field:`cost <standard_price>`: used for margins and stock valuation.
* :field:`Unit of measure <uom_id>` and :field:`purchase unit of measure
  <uom_po_id>` (*Units of Measure* setting), e.g. sold by unit, bought by box.
* **Sales** tab: the :field:`invoicing policy <invoice_policy>`, *Ordered
  quantities* or *Delivered quantities*, and the prices of the pricelists.
* **Inventory** tab: the routes (*Buy*, *Make To Order*, …), customer lead
  time, weight, volume, lots and serial numbers, and the **Vendors** with
  their price and delivery lead time.
* **Invoicing** tab: :field:`customer taxes <taxes_id>`, :field:`vendor taxes
  <supplier_taxes_id>`, income and expense accounts.
* **Notes** tab: the descriptions printed on quotations, purchase orders and
  pickings.
