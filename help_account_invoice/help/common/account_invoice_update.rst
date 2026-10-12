.. _update_record:

Update record
-------------

.. help-version:: <13

   #. Open the invoice from the list and press **Edit**. A *Draft* invoice can
      be changed freely; press **Save** when done.
   #. A validated (*Open*) invoice cannot be changed. To correct it, press
      **Cancel Invoice**, then **Reset to Draft**, change it and press
      **Validate** again: it keeps its number. Cancelling needs the
      *Allow Cancelling Entries* option of the journal, see *Configure*.
   #. To register a payment press **Register Payment**: check the payment
      journal (bank or cash), the amount, the date and the memo, then press
      **Validate**. A lower amount leaves the rest open (*Keep open*) or writes
      it off (*Mark invoice as fully paid*).
   #. A payment already received, e.g. from the bank statement, is shown under
      the totals as an *outstanding credit*: press **Add** next to it.
   #. To refund the customer, press :version:`10|**Refund Invoice**;*|**Add
      Credit Note**`, write the reason and the date, choose the method and
      press :version:`10|**Create Refund**;*|**Add Credit Note**`:

      * :version:`10|*Create a draft refund*;*|*Create a draft credit note*`:
        a draft to change, e.g. for a partial refund;
      * :version:`10|*Cancel: create refund and reconcile*;*|*Cancel: create
        credit note and reconcile*`: the whole invoice is cancelled;
      * :version:`10|*Modify: create refund, reconcile and create a new draft
        invoice*;*|*Modify: create credit note, reconcile and create a new
        draft invoice*`: as *Cancel*, plus a new draft to correct.

   #. A draft invoice that never received a number can be deleted from
      **Action ‣ Delete**; a validated invoice is cancelled or refunded, never
      deleted.

.. help-version:: >=13

   #. Open the invoice from the list. :version:`<17|Press **Edit**: a *Draft*
      invoice can be changed freely, then press **Save**.;*|A *Draft* invoice
      can be changed freely and is saved automatically.`
   #. A *Posted* invoice cannot be changed: press **Reset to Draft**, change
      it and press :version:`13|**Post**;*|**Confirm**` again; it keeps its
      number. The button is missing in a locked period and on secured
      journals: issue a credit note instead.
   #. To register a payment press :version:`<18|**Register Payment**;*|**Pay**`:
      check the journal, the payment method, the amount, the date and the memo,
      then press **Create Payment**. A lower amount leaves the rest to pay
      (*Keep open*) or writes it off (:version:`13|*Mark invoice as fully
      paid*;*|*Mark as fully paid*`).
   #. A payment already received, e.g. from the bank statement, is shown under
      the totals as an *outstanding credit*: press **Add** next to it.
   #. To refund the customer, press :version:`<18|**Add Credit Note**;*|**Credit
      Note**`, write the reason and check the reversal date and the journal.

      .. help-version:: <17

         Choose the credit method and press **Reverse**:

         * *Partial Refund*: a draft credit note to change and confirm;
         * *Full Refund*: the credit note is posted and matched with the
           invoice, which becomes paid;
         * *Full refund and new draft invoice*: as *Full Refund*, plus a new
           draft invoice to correct.

      .. help-version:: >=17

         Press **Reverse** for a draft credit note to change and confirm, or
         **Reverse and Create Invoice** to cancel the whole invoice with a
         posted credit note and open a new draft invoice to correct.

   #. To drop a draft invoice press :version:`<15|**Cancel Entry**;*|**Cancel**`;
      it can also be deleted from :version:`<17|**Action ‣
      Delete**;*|the gear icon ‣ **Delete**` when its number is the last one
      of the sequence.

   .. help-version:: >=15

      An invoice marked *To Check*, e.g. created from an email or a scanned
      PDF, shows **Set as Checked**: press it after reviewing the invoice.

   .. help-version:: >=17

      An electronic invoice already sent to the tax authority shows **Request
      Cancel**: the cancellation is asked through the electronic invoicing
      service.
