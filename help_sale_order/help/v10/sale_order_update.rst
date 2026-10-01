.. _update_record:

Update record
-------------

#. Open the order from **Sales ‣ Sales ‣ Quotations** or **Sales ‣ Sales ‣
   Sales Orders**, press **Edit**, change the fields and press **Save**
   (**Discard** drops the changes). Every change of status is logged in the
   chatter.
#. **Quotation** or **Quotation Sent**: every field can be changed. Changing
   the :field:`pricelist <pricelist_id>` does not recompute the lines already
   entered: pick their product again. Press **(update)** next to the total to
   recompute taxes and totals. Changing a sent quotation does not resend it:
   press **Send by Email** again.
#. **Sales Order**: customer, addresses, pricelist and expiration date become
   read-only. You can still change quantities and add lines: Inventory updates
   the delivery and the :field:`invoice status <invoice_status>` is recomputed.
   The product of a line cannot be changed once it is invoiced or sent to the
   warehouse. Lines cannot be deleted: set their quantity to 0.
#. **Create Invoice** invoices what is due: choose *Invoiceable lines*,
   *Invoiceable lines (deduct down payments)* or a down payment (percentage or
   fixed amount), then **Create Invoices** or **Create and View Invoices**.
#. **Lock** (or the *Sale Order Modification* setting set to *Never allow to
   modify a confirmed sales order*) sets the status to *Locked*: products,
   quantities, prices and taxes cannot be changed any more, but the order can
   still be delivered and invoiced. A locked order cannot be unlocked.
#. To change a confirmed order a lot: press **Cancel**, then **Set to
   Quotation**, change it and press **Confirm Sale** again.
#. To delete a quotation select it in the list and use **Action ‣ Delete**:
   only quotations not yet sent and cancelled orders can be deleted.
