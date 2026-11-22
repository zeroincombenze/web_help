.. _actions:

Other actions
-------------

The buttons at the top of the bill; each one appears only when the status of
the bill allows it.

Confirm the bill
~~~~~~~~~~~~~~~~

.. help-version:: <13

   On a *Draft* bill press [`Validate`]: Odoo checks the bill, assigns the
   :field:`number <number>`, writes the journal entry and the status becomes
   *Open*. From now on the bill cannot be changed: see *How to update a record*
   to correct it.

.. help-version:: >=13

   On a *Draft* bill press :version:`13|[\`Post\`];*|[\`Confirm\`]`: Odoo
   checks the bill, assigns the :field:`number <name>` from the sequence of the
   journal and the status becomes *Posted*. From now on the bill cannot be
   changed: press [`Reset to Draft`] to correct it.

   .. help-version:: >=14

      With :version:`<16|*Post Automatically*;*|*Auto-post*` set in the
      **Other Info** tab and a date in the future, the button is hidden: Odoo
      confirms the bill by itself on that date.

Pay the vendor
~~~~~~~~~~~~~~

.. help-version:: <13

   On an *Open* bill press [`Register Payment`]: check the payment journal
   (bank or cash), the payment method, the amount, the date and the memo, then
   press [`Validate`]. A lower amount leaves the rest open (*Keep open*) or
   writes it off on a difference account (*Mark invoice as fully paid*). When
   the payments cover the whole amount the status becomes *Paid*.

.. help-version:: >=13

   On a *Posted* bill\ :version:`13| not yet paid;*| not yet paid, or paid
   only in part,` press :version:`<18|[\`Register Payment\`];*|[\`Pay\`]`: check
   the journal (bank or cash), the payment method, the amount, the date and
   the memo, then press [`Create Payment`]. A lower amount leaves the rest to
   pay (*Keep open*) or writes it off on a difference account
   (:version:`13|*Mark invoice as fully paid*;*|*Mark as fully paid*`). When
   the payments cover the whole amount the bill is *Paid*, or *In Payment*
   until the payment is matched with the bank statement.

A payment already made, e.g. from the bank statement, is shown under the
totals as an *outstanding debit*: press [`Add`] next to it to use it for this
bill.

How to create a debit note
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   A debit note records an extra amount that the vendor asks on a bill already
   received (e.g. a price increase or an omitted charge). This version has no
   specific function: create a new bill for the extra amount, and write the
   number of the original bill in its reference.

.. help-version:: >=13

   A debit note records an extra amount that the vendor asks on a bill already
   received (e.g. a price increase or an omitted charge).

   .. help-if:: module != account_debit_note

      The function needs the *Debit Notes* module: the administrator installs
      it from the **Apps** menu.

   .. help-if:: module = account_debit_note

      On a *Posted* bill that is not itself a debit note, press
      :version:`<17|[\`Add Debit Note\`];*|the gear icon next to the record
      name ‣ **Debit Note**`. Fill in the *Reason*, the *Debit Note Date*, the
      *Journal* and, to start from a copy of the bill lines, *Copy Lines*;
      then press [`Create Debit Note`]. The new debit note opens as a draft:
      correct its lines and amounts, then confirm it. It shows the original
      bill in *Original Invoice Debited*, while the original bill gets the
      *Debit Notes* button to open its debit notes.
