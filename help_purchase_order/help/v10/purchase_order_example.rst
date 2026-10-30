.. _example:

Example
-------

**The vendor delivers in two shipments**

#. Confirm the order of 100 units and press **Receive Products**.
#. Set 60 as done quantity and press **Validate**, then choose **Create
   Backorder**: the 40 missing units stay in a new receipt.
#. With the *On received quantities* policy, the vendor bill created now
   proposes 60 units; the order stays *Waiting Bills* until the rest is
   received and billed.

**The vendor raises the price after the confirmation**

Open the order, press **Edit**, change the **Unit Price** of the line and
**Save**: the new price is proposed on the vendor bill.

**Orders over 5,000 need the manager's approval**

#. In **Purchases ‣ Configuration ‣ Settings** choose *Get 2 levels of
   approvals to confirm a purchase order* and set the amount to 5,000.
#. A purchase user confirming an order of 8,000 gets the status *To Approve*;
   the manager opens it and presses **Approve Order**.

**The vendor cannot supply the goods**

Press **Cancel**; the order stays in the list with status *Cancelled* and can
then be deleted.
