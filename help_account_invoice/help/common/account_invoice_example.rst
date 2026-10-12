.. _example:

Example
-------

**Wrong price on an invoice already sent**

.. help-version:: <13

   If the customer has not paid yet and the journal allows cancelling entries,
   press **Cancel Invoice**, **Reset to Draft**, correct the price and press
   **Validate**: the invoice keeps its number. Otherwise press
   :version:`10|**Refund Invoice**;*|**Add Credit Note**`, choose the *Modify*
   method and correct the new draft invoice.

.. help-version:: >=13

   If the period is open, press **Reset to Draft**, correct the price and
   press :version:`13|**Post**;*|**Confirm**`: the invoice keeps its number.
   When the invoice must stay as it was sent (e.g. an electronic invoice
   already delivered), press :version:`<18|**Add Credit Note**;*|**Credit
   Note**` and choose :version:`<17|*Full refund and new draft
   invoice*;*|**Reverse and Create Invoice**`, then correct the new draft.

**Payment in two instalments**

Create the payment terms *50% now, balance in 30 days* in **Invoicing ‣
Configuration ‣** :version:`<13|**Management**;*|**Invoicing**` **‣ Payment
Terms** and choose them on the invoice: the journal entry has two due dates.
When the first half arrives, register it with *Keep open*: the invoice stays
:version:`<13|*Open*;13|*Not Paid*;*|*Partially Paid*` until the balance is
paid.

**Partial refund of a returned product**

Press :version:`10|**Refund Invoice**;<18|**Add Credit Note**;*|**Credit
Note**`, write the reason (e.g. *Damaged goods*) and create a draft
:version:`10|refund;*|credit note`; keep only the returned line with its
quantity and :version:`<13|validate;13|post;*|confirm` it. The customer owes
the difference, or you pay back the amount of the credit note.
