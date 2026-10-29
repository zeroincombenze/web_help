.. _update_record:

Update record
-------------

#. Open the product, press **Edit**, change the fields and press **Save**
   (**Discard** drops the changes).
#. A new :field:`sale price <list_price>` or :field:`cost <standard_price>` is
   used by the next documents only; orders and invoices already made keep
   their prices.
#. The :field:`product type <type>` and the :field:`unit of measure <uom_id>`
   should not be changed once the product has stock moves: create a new
   product instead.
#. Adding a value in the **Variants** tab creates the new variants; removing
   a value deletes the variants that use it, or archives them when they are
   already used by documents. **Variant Prices** sets the extra
   price of each attribute value: the sale price of a variant is the sale price
   of the product plus the extra prices of its values.
#. The **Variants** button opens the variants, to set their own reference,
   barcode, cost and weight.
#. **Update Qty On Hand** (stockable products) sets the quantity in stock
   after a count.
#. **Active** at the top right archives the product and all its variants: it
   is no longer proposed on new documents but stays on the old ones. Press
   **Archived** to restore it.
#. To delete a product select it in the list and use **Action ‣ Delete**: a
   product used by orders, invoices or stock moves cannot be deleted, archive
   it instead.
