.. _example:

Example
-------

**The customer wants the invoices sent to its head office**

Open the company, in **Contacts & Addresses** press **Create**, choose
:version:`<=12|*Invoice address*;*|*Invoice Address*`, type the head office
address and **Save & Close**: new orders propose it as invoice address.

**A person moves to another company**

Open the person, press **Edit**, change the :field:`company <parent_id>` and
**Save**: the address and the commercial data now come from the new company;
old documents keep the old ones.

**A customer was created twice**

Open the copy that is not used yet, check that it has no documents (smart
buttons) and delete it; if it has documents, archive it.

.. help-version:: <=12

   **A customer is also a vendor**

   Check :field:`Is a Vendor <supplier>` in the **Sales & Purchases** tab: the
   same contact is proposed on purchase orders and vendor bills.

.. help-version:: >=13

   **A customer is also a vendor**

   Nothing to set: the same contact can be chosen on sale and purchase
   documents; it appears among the vendors after its first purchase order or
   vendor bill.
