.. _example:

Example
-------

**Wrong price on a bill already confirmed**

.. help-version:: <13

   If the vendor has not been paid yet and the journal allows cancelling
   entries, cancel the bill (see *How to cancel or delete record*), press
   [`Set to Draft`], correct the price and press [`Validate`]: the bill keeps
   its number. Otherwise press :version:`10|[\`Ask Refund\`];*|[\`Ask for a
   Credit Note\`]`, choose the *Modify* method and correct the new draft bill.

.. help-version:: >=13

   If the period is open, press [`Reset to Draft`], correct the price and
   press :version:`13|[\`Post\`];*|[\`Confirm\`]`: the bill keeps its number.
   When the bill must stay as it was received, press
   :version:`<17|[\`Add Credit Note\`];*|[\`Credit Note\`]` and choose
   :version:`<17|*Full refund and new draft invoice*;*|[\`Reverse and Create
   Invoice\`]`, then correct the new draft.

**Payment in two instalments**

Create the payment terms *50% now, balance in 30 days* in **Invoicing ‣
Configuration ‣** :version:`<13|**Management**;*|**Invoicing**` **‣ Payment
Terms** and choose them on the bill: the journal entry has two due dates.
When you pay the first half, register it with *Keep open*: the bill stays
:version:`<13|*Open*;13|*Not Paid*;*|*Partially Paid*` until the balance is
paid.

**Partial credit note of a returned product**

Press :version:`10|[\`Ask Refund\`];11-12|[\`Ask for a Credit
Note\`];<17|[\`Add Credit Note\`];*|[\`Credit Note\`]`, write the reason (e.g.
*Damaged goods*) and create a draft credit note; keep only the returned line
with its quantity and :version:`<13|validate;13|post;*|confirm` it. The
vendor owes you the difference, or you pay the bill net of the credit note.
