.. _update_record:

Update record
-------------

#. Open the order from **Purchases ‣ Purchase ‣ Requests for Quotation** or
   **Purchases ‣ Purchase ‣ Purchase Orders**, press **Edit**, change the
   fields and press **Save** (**Discard** drops the changes). Every change of
   status is logged in the chatter.
#. **RFQ** or **RFQ Sent**: every field can be changed. Changing a sent RFQ
   does not resend it: press **Re-Send RFQ by Email**.
#. **To Approve**: a purchase manager presses **Approve Order** to confirm it.
#. **Purchase Order**: vendor, order date, currency and the product of the
   lines become read-only. You can still change quantities, prices and add
   lines: Inventory updates the receipt. Lines cannot be deleted: set their
   quantity to 0. **Send PO by Email** sends the confirmed order to the
   vendor.
#. **Receive Products** (or the **Shipment** button) opens the receipt: set
   the received quantities and press **Validate**. A partial receipt creates a
   backorder for the remaining goods.
#. **Vendor Bills** button: creates the vendor bill from the order, or opens
   the existing ones. A bill can also be created in **Purchases ‣ Control ‣
   Vendor Bills** choosing the order in the **Add Purchase Order** field. The
   quantities proposed depend on the *Control Purchase Bills* policy of the
   product; the :field:`billing status <invoice_status>` is then recomputed.
#. **Lock** (or the *Purchase Order Modification* setting set to *Confirmed
   purchase orders are not editable*) sets the status to *Locked*: the lines
   cannot be changed any more, but the goods can still be received and billed.
   A purchase manager can press **Unlock**.
#. **Cancel** cancels the order and its receipts; it is refused when some goods
   are received or a vendor bill is validated. **Set to Draft** turns a
   cancelled order back into an RFQ.
#. To delete an order select it in the list and use **Action ‣ Delete**: only
   cancelled orders can be deleted.
