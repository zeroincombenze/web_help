.. _update_record:

Update record
-------------

#. Open the product and change the fields; the record is saved when you leave
   it, or press the cloud icon. Orders and invoices already made keep their
   prices and descriptions.
#. **Sales price**: the new price is proposed in new quotations; pricelists
   may still change it for some customers.
#. **Cost**: with the *Standard* costing method it can be typed; with
   *Average* or *FIFO* (Inventory) it is computed from the receipts.
#. **Unit of measure**: after stock moves it can be changed only to a unit of
   the same category.
#. **Product type**: :version:`<=17|changing a *Storable Product* with stock
   to another type is refused;*|unchecking **Track Inventory** with stock on
   hand is refused`; empty the stock first.
#. **Attributes & Variants**: adding a value creates the new variants;
   removing one archives the variants using it.
#. **Actions ‣ Archive** hides a product no longer used without losing its
   history; **Actions ‣ Duplicate** copies it to create a similar one.
#. To delete a product select it in the list and use **Actions ‣ Delete**: a
   product used in documents cannot be deleted, archive it instead.
