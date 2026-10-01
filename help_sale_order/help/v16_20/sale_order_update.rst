.. _update_record:

Update record
-------------

#. Open the order from **Sales ‣ Orders ‣ Quotations** or **Sales ‣ Orders ‣
   Orders** and change the fields; the record is saved when you leave it, or
   press the cloud icon. Every change of status is logged in the chatter.
#. **Quotation** or **Quotation Sent**: every field can be changed. After
   changing the :field:`pricelist <pricelist_id>` press **Update Prices** to
   recompute the prices of the lines; after changing the :field:`fiscal
   position <fiscal_position_id>` press **Update Taxes**. Changing a sent
   quotation does not resend it: press **Send by Email** again.
#. **Sales Order**: customer, pricelist, expiration date and template become
   read-only. You can still raise or lower quantities and add lines: Inventory
   updates the delivery and the :field:`invoice status <invoice_status>` is
   recomputed. The product of a line can be changed only until it is delivered
   or invoiced. Lines cannot be deleted: set their quantity to 0. The
   **Delivered** quantity of services and manual products is typed on the line.
#. **Create Invoice** invoices what is due: choose *Regular invoice* or a down
   payment (percentage or fixed amount), then :version:`16|**Create and View
   Invoice**;17|**Create Draft Invoice**;*|**Create Draft**`. The **Invoices**
   smart button opens them.
#. **Locked** order (*Lock Confirmed Sales* setting, or **Lock** pressed by a
   sales administrator): lines and delivery date cannot be changed, but the
   order can still be delivered and invoiced. A sales administrator presses
   **Unlock** to change it again. :version:`16|The status shows *Locked*.;*|A
   lock icon appears and the status stays *Sales Order*.`
#. To change a confirmed order a lot: unlock it if needed, press **Cancel** (a
   wizard proposes to inform the customer by email; draft invoices are
   cancelled), then **Set to Quotation**, change it and **Confirm** it again.
#. To delete a quotation select it in the list and use **Actions ‣ Delete**:
   only quotations not yet sent and cancelled orders can be deleted.
