.. help-if:: module = purchase

   .. _purchase_order:

   Invoice from supplier order
   ---------------------------

   With the Purchase app the vendor bills are usually created from the
   confirmed purchase orders: Odoo copies the vendor, the payment terms, the
   fiscal position and the lines, and keeps track of what is already billed.

   What can be billed depends on the :version:`10|*Control Purchase
   Bills*;*|*Control Policy*` of each product, set on the product\ :version:`>=11|, in the **Purchase**
   tab`:

   * *On ordered quantities*: the whole ordered quantity, as soon as the
     order is confirmed;
   * *On received quantities*: only the quantity already received, e.g. after
     the validation of the receipt.

   The :field:`Billing Status <invoice_status>` of an order shows what is left:
   *Nothing to Bill*, *Waiting Bills* and
   :version:`10|*Bills Received*;11-12|*No Bill to Receive*;*|*Fully Billed*`.

   #. Open :version:`<13|**Purchase ‣ Purchase ‣ Purchase Orders**;*|**Purchase ‣
      Orders ‣ Purchase Orders**` and open the order (a request for quotation becomes an
      order with [`Confirm Order`]).
   #. If the control policy of the products is *On received quantities*,
      receive the goods first with [`Receive Products`]\
      :version:`>=14|, or the **Receipt** smart button`, and validate the
      receipt: nothing can be billed before.
   #. :version:`<12|Press the **Vendor Bills** smart button of the order and
      create a new bill there: the order is already chosen in the *Add Purchase
      Order* field and its lines are added.;*|Press [\`Create Bill\`] on the order (also the **Vendor
      Bills** smart button opens its bills): the new bill opens as a draft,
      with the quantities still to be billed.`
   #. Write the vendor reference of the bill (:version:`<13|*Vendor
      Reference*;13|*Reference*;*|*Bill Reference*`) and the bill date.
   #. Check quantities, prices and taxes against the order: change the
      quantity of a line to bill only a part of it.
   #. Press :version:`<13|[\`Validate\`];13|[\`Post\`];*|[\`Confirm\`]`: the bill
      is confirmed and the *Billing Status* of the order is updated.

   *Alternative*: create the bill by hand, as described in *How to insert a
   new record*, choose the vendor and then the order in the
   :version:`<12|*Add Purchase Order*;*|*Auto-Complete*` field of the bill
   (it is shown on a draft bill, to the users of the Purchase app): the lines
   of the order are loaded in the bill. :version:`>=13|The same field can also
   copy the lines of an old bill of the vendor.`

   *Partial billing*: bill only a part of the order (change the quantity of the
   lines, or receive the goods in several steps with the policy *On received
   quantities*): the order stays *Waiting Bills*. Press
   :version:`<12|the **Vendor Bills** smart button;*|[\`Create Bill\`]` again
   when the rest is to be billed: only the quantities not yet billed are
   proposed.

   The bill is linked to the order: the **Vendor Bills** smart button of the
   order opens its bills. :version:`>=18|On the bill, the **Purchases** smart
   button opens the orders and **Purchase Matching** matches the bill lines
   with the order lines, and on the order **Bill Matching** does the same.`
