.. _actions:

Other actions
-------------

Select the bills with the check boxes of the list to act on all of them at
once; each action is also available on the single bill, from its form.

Confirm bills
~~~~~~~~~~~~~

.. help-version:: <13

   Select the draft bills, then **Action ‣ Confirm Draft Invoices** and press
   [`Confirm Invoices`]: each bill gets its number and its journal entry, and
   can no longer be changed. Only the draft bills can be confirmed; on the
   form the button is [`Validate`].

.. help-version:: >=13

   Select the draft bills, then :version:`<=16|**Action ‣ Post
   entries**;17|**Actions ‣ Post entries**;*|**Actions ‣ Confirm Entries**`
   and press :version:`<18|[\`Post Journal Entries\`];*|[\`Confirm\`]`: each
   bill gets its number and its journal entry, and can no longer be changed;
   set it back to draft to correct it. On the form the button is
   :version:`13|[\`Post\`];*|[\`Confirm\`]`.

Pay the vendors
~~~~~~~~~~~~~~~

.. help-version:: <13

   Select the open bills of the same type, then **Action ‣ Register
   Payment**: choose the payment journal (bank or cash), the payment date and
   press [`Validate`]. The bills become *Paid*. On the form the button is
   [`Register Payment`], and lets you also pay a partial amount.

.. help-version:: 13

   Select the posted bills, then **Action ‣ Register Payment**: choose the
   payment journal (bank or cash), the payment date and press [`Create
   Payment`]. The bills become *Paid*. On the form the button is [`Register
   Payment`], and lets you also pay a partial amount.

.. help-version:: >=14

   Select the posted bills: the :version:`<18|[\`Register
   Payment\`];*|[\`Pay\`]` button appears above the list\ :version:`<17| (only
   for the users with the *Show Full Accounting Features* right)`. Choose the
   payment journal (bank or cash), the payment date and the amount, then press
   [`Create Payment`]\ :version:`>=17| ([\`Create Payments\`] when they are more
   than one)`. With several bills of the same vendor, *Group Payments* makes
   one payment for all of them. The bills become *Paid*, or *In Payment* until
   the payment is matched with the bank statement. On the form the button is
   :version:`<18|[\`Register Payment\`];*|[\`Pay\`]`.

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

      Select the posted bills, then :version:`<=16|**Action ‣ Create Debit
      Note**;*|**Actions ‣ Create Debit Note**` (on the form,
      :version:`<17|the [\`Add Debit Note\`] button;*|**Debit Note** in the menu
      under the gear icon`). Fill in the *Reason*, the *Debit Note Date*, the
      *Journal* and, to start from a copy of the bill lines, *Copy Lines*;
      then press [`Create Debit Note`]. A draft bill is created, linked to the
      original one: correct its lines and amounts, then confirm it. The
      original bill shows the *Debit Notes* button.
