.. _actions:

Other actions
-------------

The buttons at the top of the invoice; each one appears only when the status
of the invoice allows it.

Confirm the invoice
~~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   On a *Draft* invoice press **Validate**: Odoo checks the invoice, assigns
   the :field:`number <number>`, writes the journal entry and the status
   becomes *Open*. From now on the invoice cannot be changed: see *How to
   update a record* to correct it.

.. help-version:: >=13

   On a *Draft* invoice press :version:`13|**Post**;*|**Confirm**`: Odoo
   checks the invoice, assigns the :field:`number <name>` from the sequence of
   the journal and the status becomes *Posted*. From now on the invoice cannot
   be changed: press **Reset to Draft** to correct it.

   .. help-version:: >=14

      With :version:`<16|*Post Automatically*;*|*Auto-post*` set in the
      **Other Info** tab and a date in the future, the button is hidden: Odoo
      confirms the invoice by itself on that date.

Register a payment
~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   On an *Open* invoice press **Register Payment**: check the payment journal
   (bank or cash), the payment method, the amount, the date and the memo, then
   press **Validate**. A lower amount leaves the rest open (*Keep open*) or
   writes it off on a difference account (*Mark invoice as fully paid*). When
   the payments cover the whole amount the status becomes *Paid*.

.. help-version:: >=13

   On a *Posted* invoice\ :version:`13| not yet paid;*| not yet paid, or paid
   only in part,` press :version:`<18|**Register Payment**;*|**Pay**`: check
   the journal (bank or cash), the payment method, the amount, the date and
   the memo, then press **Create Payment**. A lower amount leaves the rest to
   pay (*Keep open*) or writes it off on a difference account
   (:version:`13|*Mark invoice as fully paid*;*|*Mark as fully paid*`). When
   the payments cover the whole amount the invoice is *Paid*, or *In Payment*
   until the payment is matched with the bank statement.

A payment already received, e.g. from the bank statement, is shown under the
totals as an *outstanding credit*: press **Add** next to it to use it for this
invoice.

How to create a debit note
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   A debit note asks the customer for an extra amount on an invoice already
   issued (e.g. a price increase or an omitted charge). This version has no
   specific function: create a new invoice for the extra amount, and write
   the number of the original invoice in its reference.

.. help-version:: >=13

   A debit note asks the customer for an extra amount on an invoice already
   issued (e.g. a price increase or an omitted charge), or records the extra
   amount asked by a vendor.

   .. help-if:: module != account_debit_note

      The function needs the *Debit Notes* module: the administrator installs
      it from the **Apps** menu.

   .. help-if:: module = account_debit_note

      On a *Posted* invoice, bill or credit note that is not itself a debit
      note, press :version:`<17|**Add Debit Note**;*|the gear icon next to
      the record name ‣ **Debit Note**`. Fill in the *Reason*, the *Debit Note
      Date*, the *Journal* and, to start from a copy of the invoice lines,
      *Copy Lines*; then press **Create Debit Note**. The new debit note opens
      as a draft: correct its lines and amounts, then confirm it. It shows the
      original invoice in *Original Invoice Debited*, while the original
      invoice gets the *Debit Notes* button to open its debit notes.

   .. help-version:: >=18

      .. help-if:: module = l10n_it_edi_ndd_account_dn

         The e-invoice of a debit note is sent with the document type
         *TD05*.
