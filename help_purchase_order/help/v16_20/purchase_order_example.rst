.. _example:

Example
-------

**Order above the approval amount**

#. With *Purchase Order Approval* set to 5,000, a buyer confirms an order of
   8,000: its status becomes *To Approve*.
#. The purchase manager opens it from the *To Approve* filter and presses
   **Approve Order**: the order becomes a *Purchase Order* and the receipt is
   created.

**Bill only what has been received**

#. The product has *Received quantities* as control policy; 100 units are
   ordered and 60 arrive: validate the receipt with 60.
#. Press **Create Bill**: the draft bill has 60 units. When the other 40
   arrive, validate the backorder and press **Create Bill** again.

**The vendor raises the price after the confirmation**

Change the unit price on the line of the confirmed order; bills already
created keep the old price.

**The vendor cannot deliver**

Press **Cancel**; the order stays in the list with status *Cancelled* and its
receipt is cancelled too.
