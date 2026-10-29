.. _fields:

Main fields
~~~~~~~~~~~

* **Product Type**: :version:`<=17|*Consumable* (no stock kept), *Service* or,
  with Inventory, *Storable Product* (stock quantities kept);*|*Goods*,
  *Service* or *Combo* (a set of choices sold as one product). For goods, with
  Inventory, **Track Inventory** keeps the stock quantities`.
* :version:`<=17|**Can be Sold** and **Can be Purchased**;*|**Sales** and
  **Purchase**` (checkboxes under the name): whether the product is proposed
  in sales and purchase documents.
* :field:`Sales price <list_price>` and :field:`cost <standard_price>`; with
  Invoicing also the **Sales Taxes** and **Purchase Taxes**.
* :field:`Internal reference <default_code>` and :field:`barcode <barcode>`:
  codes printed on documents and searched by the scanners.
* :field:`Product category <categ_id>`: groups the products and sets their
  accounts and costing method.
* :field:`Unit of measure <uom_id>` and :field:`purchase unit <uom_po_id>`
  (*Units of Measure* setting).
* **Sales** tab: the :field:`sales description <description_sale>` copied to
  quotations and invoices; with Sales the **Invoicing Policy**.
* **Purchase** tab (Purchase installed): the vendors with their prices and
  lead times, the **Control Policy** and the purchase description.
* **Inventory** tab (Inventory installed): routes, responsible, weight,
  volume, lead times and, with lots, the tracking.
* :field:`Internal notes <description>`: seen only by the users.
