.. _cancel:

How to cancel or delete record
------------------------------

#. [`Cancel`] is shown on *RFQ*, *RFQ Sent*, *To Approve* and *Purchase
   Order*. :version:`<=18|On a *Locked* order;*|On a locked order` a purchase
   manager presses [`Unlock`] first.

   .. help-version:: <=18

      The cancellation is refused when some goods are already received, or
      when a vendor bill of the order is neither draft nor cancelled: cancel
      the bill first. Otherwise the order becomes *Cancelled* and its
      receipts are cancelled too.

   .. help-version:: >=19

      The cancellation is refused when a vendor bill of the order is neither
      draft nor cancelled: cancel the bill first. The order becomes
      *Cancelled* and its receipts not yet done are cancelled; the receipts
      already done stay as they are, with a note about the cancelled order.

#. [`Set to Draft`] turns a *Cancelled* order back into an *RFQ*, to change
   it and confirm it again.
#. Only cancelled orders can be deleted: in the form use
   :version:`<17|**Action ‣ Delete**;*|the gear icon ‣ **Delete**`, in the
   list select the orders and use :version:`<17|**Action ‣
   Delete**;*|**Actions ‣ Delete**`. Any other order is cancelled first.
#. Purchase orders cannot be archived: cancelled orders stay in the list.
