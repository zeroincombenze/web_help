.. help-version:: <13

   .. help-page:: account_invoice_in_form
      :title: Vendor bill
      :model: account.invoice
      :view: account.invoice_supplier_form
      :view-type: form
      :priority: 96

.. help-version:: 13

   .. help-page:: account_invoice_in_form
      :title: Vendor bill
      :model: account.move
      :view: account.view_move_form
      :view-type: form
      :when: type = in_invoice, in_refund, in_receipt
      :priority: 96

.. help-version:: >=14

   .. help-page:: account_invoice_in_form
      :title: Vendor bill
      :model: account.move
      :view: account.view_move_form
      :view-type: form
      :when: move_type = in_invoice, in_refund, in_receipt
      :priority: 96

Vendor bill
===========

.. _description:

Description
-----------

Click on button [`Ready`] for help about how to use this help; click on
button [`FAQ`] for the most common solved questions.

.. help-version:: <13

   A vendor bill records what a :field:`vendor <partner_id>` asks you to pay
   for goods or services. Its corrections are the vendor
   :version:`10|**refunds**;*|**credit notes**`. Products, quantities, prices
   and taxes are listed in the **Invoice Lines** tab.

   The :field:`status <state>` bar at the top shows where the bill stands:

   * *Draft*: the bill can be freely changed; it has no number and no effect on
     the accounts.
   * *Open*: validated. Odoo assigned the :field:`number <number>` and wrote
     the journal entry; the bill waits for its payment.
   * *Paid*: the payments cover the whole amount.
   * *Cancelled*: the bill no longer counts.

   .. help-version:: 12

      Between *Open* and *Paid* the bill is *In Payment*: paid, waiting for the
      payment to be matched with the bank statement.

.. help-version:: >=13

   A vendor bill records what a :field:`vendor <partner_id>` asks you to pay
   for goods or services. Its corrections are the vendor **credit notes**
   (*refunds*). Products, quantities, prices and taxes are listed in the
   **Invoice Lines** tab, the resulting debits and credits in the **Journal
   Items** tab.

   A bill is a journal entry with a bill type: the same form also shows the
   customer invoices and the plain journal entries, which have their own help.

   The :field:`status <state>` bar at the top shows the accounting status:

   * *Draft*: the bill can be freely changed and has no effect on the
     accounts.
   * *Posted*: confirmed. Odoo assigned the :field:`number <name>` and the
     bill counts in the accounts.
   * *Cancelled*: the bill no longer counts.

   .. help-version:: 13

      A ribbon shows the :field:`payment status <invoice_payment_state>`:
      *Not Paid*, *In Payment* or *Paid*.

   .. help-version:: >=14

      A ribbon shows the :field:`payment status <payment_state>`: *Not Paid*,
      *Partially Paid*, *In Payment* (paid, waiting for the bank statement),
      *Paid* or *Reversed* (cancelled by a credit note).

.. help-include:: account_invoice_in_fields.rst

.. help-include:: account_invoice_in_new.rst

.. help-include:: account_invoice_in_xml.rst

.. help-include:: account_invoice_in_purchase.rst

.. help-include:: account_invoice_in_update.rst

.. help-include:: account_invoice_in_cancel.rst

.. help-include:: account_invoice_in_form_actions.rst

.. help-include:: account_invoice_in_configure.rst

.. help-include:: account_invoice_in_report.rst

.. help-include:: account_invoice_in_example.rst

.. _faq:

FAQ
---

Click on button [`Topic`] to return to the specific help page.

.. help-question:: Why can't I change the bill?

   .. help-version:: <13

      A validated bill is locked. Cancel it (the journal must allow cancelling
      entries, see *How to set up*) and press [`Set to Draft`]. If it is paid,
      remove the payment first.

   .. help-version:: >=13

      A posted bill is locked: press [`Reset to Draft`], change it and confirm
      it again. If the button is missing, the bill is in a locked period or its
      journal secures the entries; record a credit note instead.

.. help-question:: Why can't I delete the bill?

   .. help-version:: <13

      Only draft or cancelled bills that never received a number can be
      deleted. A validated bill keeps its number: cancel it, or record a
      credit note.

   .. help-version:: >=13

      Only draft bills can be deleted, and only if their number is the last of
      the sequence, so that no gap is left. Reset it to draft and cancel it,
      or record a credit note.

.. help-question:: How do I pay only a part of the bill?

   Press :version:`<18|[\`Register Payment\`];*|[\`Pay\`]` and lower the
   amount. Choose *Keep open* to pay the rest later, or
   :version:`<14|*Mark invoice as fully paid*;*|*Mark as fully paid*` to write
   the difference off to an account, e.g. for a discount of the vendor.

.. help-question:: How do I cancel a paid bill?

   Remove the payment first: in the payments under the totals, click the
   ⓘ icon of the payment and press [`Unreconcile`]. Then cancel the bill, or
   record a credit note.

.. help-question:: Why is the bill still waiting for a payment I already made?

   The payment was registered without the bill, e.g. from the bank statement:
   the bill shows it under the totals as an *outstanding debit*. Press
   [`Add`] next to the payment to use it.

   .. help-version:: >=12

      *In Payment* means the payment is registered but not yet matched with
      the bank statement: the bill becomes *Paid* after the reconciliation.

.. help-question:: The total of the bill is different from the paper bill: what do I do?

   Check the quantities, the unit prices and the taxes of every line, and the
   rounding (*How to set up*): the total of the bill must be equal to the one
   written by the vendor.

.. help-question:: What if the total of the bill is negative?

   A bill with a negative total is a credit note in disguise: the money comes
   from the vendor, not to the vendor.

   .. help-version:: 10

      Odoo 10.0 does not stop you, but do not validate it: the bill would show
      the amount as due to the vendor while the journal entry records the
      opposite. Correct the lines, or delete the draft and ask the vendor
      credit note with [`Ask Refund`] on the original bill.

   .. help-version:: 11-12

      Odoo refuses to validate it: *You cannot validate an invoice with a
      negative total amount. You should create a credit note instead.*
      Correct the lines, or delete the draft and press [`Ask for a Credit
      Note`] on the original bill.

   .. help-version:: >=13

      Odoo refuses to confirm it: *You cannot validate an invoice with a
      negative total amount. You should create a credit note instead. Use the
      action menu to transform it into a credit note or refund.* Correct the
      lines, or turn the draft into a credit note with
      :version:`<=14|**Action ‣ Switch into refund/credit note**;<=16|**Action
      ‣ Switch into invoice/credit note**;*|**Switch into invoice/credit
      note** in the menu under the gear icon`: Odoo changes the sign of the
      quantities, so the credit note has a positive total.

.. help-version:: 18

   .. help-include:: account_invoice_in_faq_einvoice.rst

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-11-20 10:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
