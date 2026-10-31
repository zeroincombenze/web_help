.. _update_record:

How to update a record
----------------------

#. Open the order from **Sales ‣ Orders ‣ Quotations** or **Sales ‣ Orders ‣
   Orders**, press **Edit**, change the fields and press **Save**
   (**Discard** drops the changes). Every change of status is logged in the
   chatter.
#. **Quotation** or **Quotation Sent**: every field can be changed. Changing
   the :field:`pricelist <pricelist_id>` does not recompute the lines already
   entered: :version:`<=13|pick their product again;*|press **Update Prices**`.
   Changing a sent quotation does not resend it: press **Send by Email**
   again.
#. **Sales Order**: customer, addresses, pricelist and expiration date become
   read-only. You can still change quantities and add lines: Inventory updates
   the delivery and the :field:`invoice status <invoice_status>` is recomputed.
   The product of a line cannot be changed once it is invoiced or sent to the
   warehouse. Lines cannot be deleted: set their quantity to 0.
#. **Create Invoice** invoices what is due: :version:`<=12|choose *Invoiceable
   lines*, *Invoiceable lines (deduct down payments)* or a down payment
   (percentage or fixed amount), then **Create Invoices** or **Create and View
   Invoices**;*|choose *Regular invoice* (with *Deduct down payments* when
   there are some) or a down payment (percentage or fixed amount), then
   **Create Invoice** or **Create and View Invoice**`.
#. **Lock** (or the :version:`11|*Lock Confirmed Orders*;*|*Lock Confirmed
   Sales*` setting) sets the status to *Locked*: the order can no longer be
   changed, but it can still be delivered and invoiced. **Unlock** makes it
   editable again.
#. To change a confirmed order a lot: press **Cancel**, then **Set to
   Quotation**, change it and press :version:`11|**Confirm Sale**;*|**Confirm**`
   again.
#. To delete a quotation select it in the list and use **Action ‣ Delete**:
   only quotations not yet sent and cancelled orders can be deleted.
