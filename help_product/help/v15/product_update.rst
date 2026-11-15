.. _update_record:

How to update a record
----------------------

#. Open the product, press [`Edit`], change the fields and press [`Save`]
   ([`Discard`] drops the changes).
#. A new :field:`sale price <list_price>` or :field:`cost <standard_price>` is
   used by the next documents only; orders and invoices already made keep
   their prices.
#. The :field:`product type <type>` and the :field:`unit of measure <uom_id>`
   should not be changed once the product has stock moves: create a new
   product instead.
#. Adding a value in the :version:`<=14|**Variants**;*|**Attributes &
   Variants**` tab creates the new variants; removing a value deletes the
   variants that use it, or archives them when they are already used by
   documents. :version:`11|**Variant Prices**;12-14|[\`Configure
   Variants\`];*|[\`Configure\`] on an attribute line` sets the extra price of
   each attribute value: the sale price of a variant is the sale price of the
   product plus the extra prices of its values.
#. The [`Variants`] button opens the variants, to set their own reference,
   barcode, cost and weight.
#. :version:`<=12|[\`Update Qty On Hand\`];*|[\`Update Quantity\`]` (storable
   products) sets the quantity in stock after a count.
