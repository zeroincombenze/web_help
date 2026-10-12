.. help-version:: <13

   .. help-page:: account_invoice_form
      :title: Invoice
      :model: account.invoice
      :view: account.invoice_form, account.invoice_supplier_form
      :view-type: form

.. help-version:: 13

   .. help-page:: account_invoice_form
      :title: Invoice
      :model: account.move
      :view: account.view_move_form
      :view-type: form
      :when: type != entry

.. help-version:: >=14

   .. help-page:: account_invoice_form
      :title: Invoice
      :model: account.move
      :view: account.view_move_form
      :view-type: form
      :when: move_type != entry

Invoice
=======

.. _description:

Description
-----------

.. help-version:: <13

   An invoice asks the :field:`customer <partner_id>` to pay for goods or
   services; a **vendor bill** records what a vendor asks you to pay. Their
   corrections are the :version:`10|**refunds**;*|**credit notes**`. Products,
   quantities, prices and taxes are listed in the **Invoice Lines** tab.

   The :field:`status <state>` bar at the top shows where the invoice stands:

   * *Draft*: the invoice can be freely changed; it has no number and no
     effect on the accounts.
   * *Open*: validated. Odoo assigned the :field:`number <number>` and wrote
     the journal entry; the invoice waits for its payment.
   * *Paid*: the payments cover the whole amount.
   * *Cancelled*: the invoice no longer counts.

   .. help-version:: 10

      With the *Allow pro-forma invoices* setting a draft can become
      *Pro-forma*: a draft sent to the customer before validation.

   .. help-version:: 12

      Between *Open* and *Paid* the invoice is *In Payment*: paid, waiting for
      the payment to be matched with the bank statement.

.. help-version:: >=13

   An invoice asks the :field:`customer <partner_id>` to pay for goods or
   services; a **vendor bill** records what a vendor asks you to pay. Their
   corrections are the **credit notes** (for vendors, *refunds*). Products,
   quantities, prices and taxes are listed in the **Invoice Lines** tab, the
   resulting debits and credits in the **Journal Items** tab.

   An invoice is a journal entry with an invoice type: the same form also shows
   the plain journal entries, which have no partner, no invoice lines and no
   payment.

   The :field:`status <state>` bar at the top shows the accounting status:

   * *Draft*: the invoice can be freely changed and has no effect on the
     accounts.
   * *Posted*: confirmed. Odoo assigned the :field:`number <name>` and the
     invoice counts in the accounts.
   * *Cancelled*: the invoice no longer counts.

   .. help-version:: 13

      A ribbon shows the :field:`payment status <invoice_payment_state>`:
      *Not Paid*, *In Payment* or *Paid*.

   .. help-version:: >=14

      A ribbon shows the :field:`payment status <payment_state>`: *Not Paid*,
      *Partially Paid*, *In Payment* (paid, waiting for the bank statement),
      *Paid* or *Reversed* (cancelled by a credit note).

.. help-include:: account_invoice_fields.rst

.. help-include:: account_invoice_new.rst

.. help-include:: account_invoice_update.rst

.. help-include:: account_invoice_configure.rst

.. help-include:: account_invoice_report.rst

.. help-include:: account_invoice_example.rst

.. _faq:

FAQ
---

.. help-question:: Why can't I change the invoice?

   .. help-version:: <13

      A validated invoice is locked. Cancel it with **Cancel Invoice** and
      press **Reset to Draft**: the journal must allow cancelling entries, see
      *Configure*. If it is paid, remove the payment first.

   .. help-version:: >=13

      A posted invoice is locked: press **Reset to Draft**, change it and
      confirm it again. If the button is missing, the invoice is in a locked
      period or its journal secures the entries; issue a credit note instead.

.. help-question:: Why can't I delete the invoice?

   .. help-version:: <13

      Only draft or cancelled invoices that never received a number can be
      deleted. A validated invoice keeps its number: cancel it, or issue a
      credit note.

   .. help-version:: >=13

      Only draft invoices can be deleted, and only if their number is the last
      of the sequence, so that no gap is left. Reset it to draft and cancel it,
      or issue a credit note.

.. help-question:: How do I register a partial payment?

   Press :version:`<18|**Register Payment**;*|**Pay**`
   and lower the amount. Choose *Keep open* to wait for the rest, or
   :version:`<14|*Mark invoice as fully paid*;*|*Mark as fully paid*` to write
   the difference off to an account, e.g. for bank fees.

.. help-question:: How do I cancel a paid invoice?

   Remove the payment first: in the payments under the totals, click the
   ⓘ icon of the payment and press **Unreconcile**. Then cancel the invoice,
   or issue a credit note.

.. help-question:: Why is the invoice still waiting for a payment I already registered?

   The payment was registered without the invoice, e.g. from the bank
   statement: the invoice shows it under the totals as an *outstanding
   credit*. Press **Add** next to the payment to use it.

   .. help-version:: >=12

      *In Payment* means the payment is registered but not yet matched with
      the bank statement: the invoice becomes *Paid* after the reconciliation.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-10-02 07:23 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
