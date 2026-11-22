.. _cancel:

How to cancel or delete record
------------------------------

.. help-version:: <13

   #. Cancelling a validated bill needs the *Cancel Journal Entries* module,
      which adds the :version:`<12|[\`Cancel Invoice\`];*|[\`Cancel\`]`
      button.

      .. help-if:: module != account_cancel

         The administrator installs it from the **Apps** menu.

         .. help-version:: 10

            Without it, [`Cancel Bill`] cancels only the draft and
            pro-forma bills.

   #. :version:`10|[\`Cancel Invoice\`] is shown on *Draft*, *Pro-forma* and
      *Open* bills.;11|[\`Cancel Invoice\`] is shown on *Draft* and *Open*
      bills.;*|[\`Cancel\`] is shown on *Draft*, *Open*, *In Payment* and
      *Paid* bills.` A validated bill can be cancelled only when the *Allow
      Cancelling Entries* option of its journal is set (developer mode).
      :version:`<12|A bill paid even in part cannot be cancelled: unreconcile
      its payments first.;*|The payments of the bill are unreconciled and stay
      open.` The journal entry is deleted and the bill becomes *Cancelled*,
      keeping its number.
   #. [`Set to Draft`] turns a *Cancelled* bill back into a *Draft*: change it
      and validate it again, with the same number.
   #. Only a draft or cancelled bill that never received a number can be
      deleted, from **Action ‣ Delete** in the form, or by selecting it in the
      list and using **Action ‣ Delete**. A validated bill is cancelled or
      refunded with a credit note, never deleted.
   #. Bills cannot be archived.

.. help-version:: >=13

   #. :version:`<15|[\`Cancel Entry\`];*|[\`Cancel\`]` is shown on *Draft*
      bills: the bill becomes *Cancelled* and keeps its lines, but no longer
      counts in the accounts or in the amounts due.
   #. A *Posted* bill is cancelled in two steps: press [`Reset to Draft`] (its
      payments are unreconciled and stay open), then
      :version:`<15|[\`Cancel Entry\`];*|[\`Cancel\`]`. [`Reset to Draft`] is
      refused in a locked period and is missing on journals whose entries are
      hashed (inalterability): record a vendor credit note instead, see *How
      to update a record*.
   #. [`Reset to Draft`] also turns a *Cancelled* bill back into a *Draft*,
      to change it and confirm it again.
   #. Only draft or cancelled bills can be deleted: in the form use
      :version:`<17|**Action ‣ Delete**;*|the gear icon ‣ **Delete**`, in the
      list select them and use :version:`<17|**Action ‣
      Delete**;*|**Actions ‣ Delete**`.

      .. help-version:: <15

         A bill that was posted once can no longer be deleted: cancel it
         instead.

      .. help-version:: >=15

         A bill that received a number can be deleted only when its number is
         the last one of the journal sequence, so as not to leave a gap;
         cancel the others instead.

      .. help-version:: >=16

         A user with the :version:`<18|*Billing Administrator*;*|accounting
         *Administrator*` right can delete it anyway, after a warning.

      .. help-version:: >=18

         With the :version:`18|*Audit Trail*;*|*Restrictive Audit Trail*`
         option of the accounting settings, a bill that was posted once can
         never be deleted: cancel it instead.

   #. Bills cannot be archived.
