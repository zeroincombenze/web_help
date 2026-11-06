.. _actions:

Other actions
-------------

Select the invoices with the check boxes of the list to act on all of them at
once; each action is also available on the single invoice, from its form.

Confirm invoices
~~~~~~~~~~~~~~~~

.. help-version:: <13

   Select the draft invoices, then **Action ‣ Confirm Draft Invoices** and
   press **Confirm Invoices**: each invoice gets its number and its journal
   entry, and can no longer be changed. Only the draft invoices can be
   confirmed; on the form the button is **Validate**.

.. help-version:: >=13

   Select the draft invoices, then :version:`<=16|**Action ‣ Post
   entries**;17|**Actions ‣ Post entries**;*|**Actions ‣ Confirm Entries**`
   and press :version:`<18|**Post Journal Entries**;*|**Confirm**`: each
   invoice gets its number and its journal entry, and can no longer be
   changed; set it back to draft to correct it. On the form the button is
   :version:`13|**Post**;*|**Confirm**`.

Register a payment
~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   Select the open invoices of the same type (customer or vendor), then
   **Action ‣ Register Payment**: choose the payment journal (bank or cash),
   the payment date and press **Validate**. The invoices become *Paid*. On the
   form the button is **Register Payment**, and lets you also pay a partial
   amount.

.. help-version:: 13

   Select the posted invoices, then **Action ‣ Register Payment**: choose the
   payment journal (bank or cash), the payment date and press **Create
   Payment**. The invoices become *Paid*. On the form the button is
   **Register Payment**, and lets you also pay a partial amount.

.. help-version:: >=14

   Select the posted invoices: the :version:`<18|**Register
   Payment**;*|**Pay**` button appears above the list\ :version:`<17| (only
   for the users with the *Show Full Accounting Features* right)`. Choose the
   payment journal (bank or cash), the payment date and the amount, then press
   **Create Payment**\ :version:`>=17| (**Create Payments** when they are more
   than one)`. With several invoices of the same partner, *Group Payments*
   makes one payment for all of them. The invoices become *Paid*, or *In
   Payment* until the payment is matched with the bank statement. On the form
   the button is :version:`<18|**Register Payment**;*|**Pay**`.

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

      Select the posted invoices, then :version:`<=16|**Action ‣ Create Debit
      Note**;*|**Actions ‣ Create Debit Note**` (on the form,
      :version:`<17|the **Add Debit Note** button;*|**Debit Note** in the menu
      under the gear icon`). Fill in the *Reason*, the *Debit Note Date*, the
      *Journal* and, to start from a copy of the invoice lines, *Copy Lines*;
      then press **Create Debit Note**. A draft invoice is created, linked to
      the original one: correct its lines and amounts, then confirm it. The
      original invoice shows the *Debit Notes* button.

   .. help-version:: >=18

      .. help-if:: module = l10n_it_edi_ndd_account_dn

         The e-invoice of a debit note is sent with the document type
         *TD05*.
