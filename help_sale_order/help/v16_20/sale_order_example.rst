.. _example:

Example
-------

**30% down payment before production**

#. Create the quotation and press **Confirm** when the customer accepts.
#. Press **Create Invoice**, choose *Down payment (percentage)*, type 30 and
   create the invoice: post it and send it to the customer.
#. When the goods are delivered press **Create Invoice** again with *Regular
   invoice*: the down payment is deducted from the final invoice.

**The customer wants 2 more units after the confirmation**

#. Open the order and raise the quantity of the line from 10 to 12.
#. Inventory adds the 2 units to the delivery not yet done, or creates a new
   delivery; the invoice status becomes *To Invoice* again.

**Wrong product on a confirmed order**

* Not yet delivered nor invoiced: change the product on the line.
* Already delivered or invoiced: set the quantity of the wrong line to 0 and
  add a line with the right product.

**The customer refuses the quotation**

Press **Cancel**: the wizard proposes an email to the customer; press
**Send and cancel** or **Cancel** to cancel without email.
