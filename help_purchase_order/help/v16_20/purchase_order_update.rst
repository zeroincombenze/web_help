.. _update_record:

Update record
-------------

#. Open the order from **Purchase ‣ Orders ‣ Requests for Quotation** or
   **Purchase ‣ Orders ‣ Purchase Orders** and change the fields; the record
   is saved when you leave it, or press the cloud icon. Every change of status
   is logged in the chatter.
#. **RFQ** or **RFQ Sent**: every field can be changed. Changing a sent RFQ
   does not resend it: press **Re-Send by Email**.
#. **To Approve**: a purchase manager presses **Approve Order** to confirm it,
   or **Cancel** to refuse it.
#. **Purchase Order**: vendor and currency become read-only. You can still
   change quantities and prices and add lines: Inventory updates the receipt
   and the :field:`billing status <invoice_status>` is recomputed. Lines
   cannot be deleted: set their quantity to 0. **Send PO by Email** sends the
   confirmed order to the vendor. The **Received** quantity of services is
   typed on the line.
#. With Inventory installed, **Receive Products** (or the **Receipt** smart
   button) opens the receipt to validate when the goods arrive.
#. **Create Bill** creates the draft vendor bill of what is due, according to
   the *Bill Control* of each product (ordered or received quantities); the
   **Vendor Bills** smart button opens the bills.
#. **Lock** (or the *Lock Confirmed Orders* setting) sets the status to
   *Locked*: the lines cannot be changed any more, but the order can still be
   received and billed. A purchase manager presses **Unlock** to change it
   again.
#. To change the vendor or a lot of the order: press **Cancel** (bills must be
   cancelled first), then **Set to Draft**, change it and **Confirm Order**
   again.
#. To delete an order select it in the list and use **Actions ‣ Delete**: only
   cancelled orders can be deleted.
