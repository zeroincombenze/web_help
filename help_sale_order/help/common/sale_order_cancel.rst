.. _cancel:

How to cancel or delete record
------------------------------

#. [`Cancel`] is shown on *Quotation*, *Quotation Sent* and *Sales Order*.
   :version:`10|A *Locked* order cannot be cancelled, nor unlocked.;<=16|On a
   *Locked* order press [\`Unlock\`] first.;*|On a locked order (lock icon) press
   [\`Unlock\`] first.`

   .. help-version:: 10

      The order becomes *Cancelled*. Invoices already created are not changed:
      cancel them from the invoice.

   .. help-version:: 11-12

      The order becomes *Cancelled* and, with Inventory, its deliveries are
      cancelled: the order cannot be cancelled once a delivery is done.
      Invoices already created are not changed: cancel them from the invoice.

   .. help-version:: 13

      The order becomes *Cancelled* and, with Inventory, the deliveries not
      yet done are cancelled. Invoices already created are not changed:
      cancel them from the invoice.

   .. help-version:: 14-15

      When the order has draft invoices a window asks to confirm: press
      [`Confirm`]. The order becomes *Cancelled*, its draft invoices are
      cancelled and, with Inventory, the deliveries not yet done are
      cancelled. Posted invoices are not changed: issue a credit note.

   .. help-version:: 16-18

      On an order that is no longer a draft quotation a window proposes an
      email to the customer: press [`Send and cancel`] to send it, [`Cancel`]
      to cancel without email, [`Discard`] to stop. The order becomes
      *Cancelled*, its draft invoices are cancelled and, with Inventory, the
      deliveries not yet done are cancelled. Posted invoices are not changed:
      issue a credit note.

   .. help-version:: >=19

      Confirm with :version:`19|**Ok**;*|[\`Yes, cancel order\`]`. The order
      becomes *Cancelled*, its draft invoices are cancelled and, with
      Inventory, the deliveries not yet done are cancelled. Posted invoices
      are not changed: issue a credit note.

#. [`Set to Quotation`] turns a *Cancelled* order back into a *Quotation*, to
   change it and confirm it again.
#. Only quotations (never sent) and cancelled orders can be deleted: in the
   form use :version:`<17|**Action ‣ Delete**;*|the gear icon ‣ **Delete**`,
   in the list select the orders and use :version:`<17|**Action ‣
   Delete**;*|**Actions ‣ Delete**`. A sent quotation or a confirmed order is
   cancelled first.
#. Sale orders cannot be archived: cancelled orders stay in the list, and the
   :version:`10|*Quotations* and *Sales*;*|*Quotations* and *Sales Orders*`
   filters hide them.
