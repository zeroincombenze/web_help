.. _update_record:

How to update a record
----------------------

.. help-version:: <13

   #. Open the bill from the list and press [`Edit`]. A *Draft* bill can be
      changed freely; press [`Save`] when done.
   #. A validated (*Open*) bill cannot be changed. To correct it, cancel it
      (see *How to cancel or delete record*), press [`Set to Draft`], change
      it and press [`Validate`] again: it keeps its number.
   #. To pay it, see *Other actions*.
   #. To ask the vendor a credit note, press :version:`10|[\`Ask Refund\`];*|[\`Ask
      for a Credit Note\`]`, write the reason and the date, choose the method
      and press :version:`10|[\`Create Refund\`];*|[\`Add Credit Note\`]`:

      * :version:`10|*Create a draft refund*;*|*Create a draft credit note*`:
        a draft to change and to match with the credit note received from the
        vendor, e.g. for a partial refund;
      * :version:`10|*Cancel: create refund and reconcile*;*|*Cancel: create
        credit note and reconcile*`: the whole bill is cancelled;
      * :version:`10|*Modify: create refund, reconcile and create a new draft
        invoice*;*|*Modify: create credit note, reconcile and create a new
        draft invoice*`: as *Cancel*, plus a new draft bill to correct.

.. help-version:: >=13

   #. Open the bill from the list. :version:`<17|Press [\`Edit\`]: a *Draft*
      bill can be changed freely, then press [\`Save\`].;*|A *Draft* bill can
      be changed freely and is saved automatically.`
   #. A *Posted* bill cannot be changed: press [`Reset to Draft`], change it
      and press :version:`13|[\`Post\`];*|[\`Confirm\`]` again; it keeps its
      number. The button is missing in a locked period and on secured
      journals: record a credit note instead.
   #. To pay it, see *Other actions*.
   #. To record a credit note received from the vendor press
      :version:`<17|[\`Add Credit Note\`];*|[\`Credit Note\`]` on the posted
      bill, write the reason and check the reversal date and the journal.

      .. help-version:: <17

         Choose the credit method and press [`Reverse`]:

         * *Partial Refund*: a draft credit note to change and confirm;
         * *Full Refund*: the credit note is posted and matched with the bill,
           which becomes paid;
         * *Full refund and new draft invoice*: as *Full Refund*, plus a new
           draft bill to correct.

      .. help-version:: >=17

         Press [`Reverse`] for a draft credit note to change and confirm, or
         [`Reverse and Create Invoice`] to cancel the whole bill with a posted
         credit note and open a new draft bill to correct.

   .. help-version:: >=15

      A bill marked *To Check*, e.g. created from an email or a scanned PDF,
      shows [`Set as Checked`]: press it after reviewing the bill.
