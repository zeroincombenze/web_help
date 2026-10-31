.. _update_record:

How to update a record
----------------------

#. Open the order from its list (**Requests for Quotation** or **Purchase
   Orders**), press **Edit**, change the fields and press **Save**
   (**Discard** drops the changes). Every change of status is logged in the
   chatter.
#. **RFQ** or **RFQ Sent**: every field can be changed. Changing a sent RFQ
   does not resend it: press :version:`11|**Re-Send RFQ by Email**;*|**Re-Send
   by Email**`.
#. **To Approve**: a purchase manager presses **Approve Order** to confirm it.
#. **Purchase Order**: vendor, order date, currency and the product of the
   lines become read-only. You can still change quantities, prices and add
   lines: Inventory updates the receipt. Lines cannot be deleted: set their
   quantity to 0. **Send PO by Email** sends the confirmed order to the
   vendor.
#. :version:`<=14|**Receive Products** (or the receipt smart button)
   opens;*|The **Receipt** smart button opens` the receipt: set the received
   quantities and press **Validate**. A partial receipt creates a backorder
   for the remaining goods.
#. :version:`11|The **Vendor Bills** smart button creates the vendor bill from
   the order, or opens the existing ones;*|**Create Bill** creates the vendor
   bill from the order, and the **Vendor Bills** smart button opens the existing
   ones`. In a new vendor bill, the :version:`<=12|**Add Purchase
   Order**;*|**Auto-Complete**` field loads the lines of an order. The
   quantities proposed depend on the *Control Policy* of the product; the
   :field:`billing status <invoice_status>` is then recomputed.
#. **Lock** (or the *Lock Confirmed Orders* setting) sets the status to
   *Locked*: the lines cannot be changed any more, but the goods can still be
   received and billed. A purchase manager can press **Unlock**.
#. **Cancel** cancels the order and its receipts; it is refused when some goods
   are received or a vendor bill is not cancelled. **Set to Draft** turns a
   cancelled order back into an RFQ.
#. To delete an order select it in the list and use **Action ‣ Delete**: only
   cancelled orders can be deleted.
