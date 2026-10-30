.. _new_record:

New record
----------

#. Open **Sales ‣ Sales ‣ Products**, **Purchases ‣ Purchase ‣ Products** or
   **Inventory ‣ Inventory Control ‣ Products** and press **Create**.
#. Type the :field:`product name <name>` (required) and check :field:`Can be
   Sold <sale_ok>` and/or :field:`Can be Purchased <purchase_ok>`.
#. In **General Information** choose the :field:`product type <type>` and the
   :field:`internal category <categ_id>`, type the :field:`internal reference
   <default_code>`, the :field:`barcode <barcode>`, the :field:`sale price
   <list_price>` and the :field:`cost <standard_price>`, and the units of
   measure.
#. In **Sales** choose the :field:`invoicing policy <invoice_policy>`.
#. In **Inventory** choose the routes and, under **Vendors**, press **Add an
   item** to add each vendor with its price, minimal quantity and delivery
   lead time.
#. In **Invoicing** check the customer and vendor taxes.
#. To sell it in several versions (*Product Variants* setting), in the
   **Variants** tab add a line for each attribute (e.g. *Size*) with its values
   (*S, M, L*): Odoo creates one variant for each combination when you save.
#. Press **Save**.
