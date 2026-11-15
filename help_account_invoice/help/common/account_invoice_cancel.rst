.. _cancel:

How to cancel or delete record
------------------------------

.. help-version:: <13

   #. Cancelling an invoice needs the *Cancel Journal Entries* module, which
      adds the :version:`<12|[\`Cancel Invoice\`];*|[\`Cancel\`]` button.

      .. help-if:: module != account_cancel

         The administrator installs it from the **Apps** menu.

         .. help-version:: 10

            Without it, [`Cancel Invoice`] on customer invoices is shown only
            in developer mode, and [`Cancel Bill`] cancels only draft vendor
            bills.

   #. :version:`10|[\`Cancel Invoice\`] is shown on *Draft*, *Pro-forma* and
      *Open* invoices.;11|[\`Cancel Invoice\`] is shown on *Draft* and *Open*
      invoices.;*|[\`Cancel\`] is shown on *Draft*, *Open*, *In Payment* and
      *Paid* invoices.` A validated invoice can be cancelled only when the
      *Allow Cancelling Entries* option of its journal is set (developer
      mode). :version:`<12|An invoice paid even in part cannot be cancelled:
      unreconcile its payments first.;*|The payments of the invoice are
      unreconciled and stay open.` The journal entry is deleted and the
      invoice becomes *Cancelled*, keeping its number.
   #. [`Reset to Draft`] ([`Set to Draft`] on vendor bills) turns a
      *Cancelled* invoice back into a *Draft*: change it and validate it
      again, with the same number.
   #. Only a draft or cancelled invoice that never received a number can be
      deleted, from **Action ‣ Delete** in the form, or by selecting it in the
      list and using **Action ‣ Delete**. A validated invoice is cancelled or
      refunded, never deleted.
   #. Invoices cannot be archived.

.. help-version:: >=13

   #. :version:`<15|[\`Cancel Entry\`];*|[\`Cancel\`]` is shown on *Draft*
      invoices: the invoice becomes *Cancelled* and keeps its lines, but no
      longer counts in the accounts or in the amounts due.
   #. A *Posted* invoice is cancelled in two steps: press [`Reset to Draft`]
      (its payments are unreconciled and stay open), then
      :version:`<15|[\`Cancel Entry\`];*|[\`Cancel\`]`. [`Reset to Draft`] is refused
      in a locked period and is missing on journals whose entries are hashed
      (inalterability): issue a credit note instead, see *How to update a
      record*.

      .. help-version:: >=17

         An electronic invoice already sent to the tax authority shows
         [`Request Cancel`] instead: the cancellation is asked through the
         electronic invoicing service.

   #. [`Reset to Draft`] also turns a *Cancelled* invoice back into a
      *Draft*, to change it and confirm it again.
   #. Only draft or cancelled invoices can be deleted: in the form use
      :version:`<17|**Action ‣ Delete**;*|the gear icon ‣ **Delete**`, in the
      list select them and use :version:`<17|**Action ‣
      Delete**;*|**Actions ‣ Delete**`.

      .. help-version:: <15

         An invoice that was posted once can no longer be deleted: cancel it
         instead.

      .. help-version:: >=15

         An invoice that received a number can be deleted only when its
         number is the last one of the journal sequence, so as not to leave a
         gap; cancel the others instead.

      .. help-version:: >=16

         A user with the :version:`<18|*Billing Administrator*;*|accounting
         *Administrator*` right can delete it anyway, after a warning.

      .. help-version:: >=18

         With the :version:`18|*Audit Trail*;*|*Restrictive Audit Trail*`
         option of the accounting settings, an invoice that was posted once
         can never be deleted: cancel it instead.

   #. Invoices cannot be archived.
