.. _new_record:

How to insert a new record
--------------------------

#. Open the products menu of Sales, Purchase or Inventory and press
   **Create**.
#. Type the :field:`product name <name>` (required) and check :field:`Can be
   Sold <sale_ok>` and/or :field:`Can be Purchased <purchase_ok>`.
#. In **General Information** choose the :field:`product type <type>` and the
   :field:`internal category <categ_id>`, type the :field:`internal reference
   <default_code>`, the :field:`barcode <barcode>`, the :field:`sale price
   <list_price>` and the :field:`cost <standard_price>`, and the units of
   measure.
#. In **Sales** choose the :field:`invoicing policy <invoice_policy>`.
#. In **Purchase**, under **Vendors**, press :version:`11|**Add an
   item**;*|**Add a line**` to add each vendor with its price, minimal
   quantity and delivery lead time.
#. In **Inventory** choose the routes; in :version:`11|**Invoicing**;*|**Accounting**`
   check the customer and vendor taxes.
#. To sell it in several versions (variants setting), in the
   :version:`<=14|**Variants**;*|**Attributes & Variants**` tab add a line for
   each attribute (e.g. *Size*) with its values (*S, M, L*): Odoo creates one
   variant for each combination when you save.
#. Press **Save**.
