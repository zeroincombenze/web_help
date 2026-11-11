.. help-version:: <13

   .. help-page:: account_invoice_form
      :title: Invoice
      :model: account.invoice
      :view: account.invoice_form, account.invoice_supplier_form
      :view-type: form
      :priority: 96

.. help-version:: 13

   .. help-page:: account_invoice_form
      :title: Invoice
      :model: account.move
      :view: account.view_move_form
      :view-type: form
      :when: type != entry
      :priority: 96

.. help-version:: >=14

   .. help-page:: account_invoice_form
      :title: Invoice
      :model: account.move
      :view: account.view_move_form
      :view-type: form
      :when: move_type != entry
      :priority: 96

Invoice
=======

.. _description:

Description
-----------

Click on button **Ready** for help about how to use this help; click on
button **FAQ** for the most common solved questions.

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

.. help-include:: account_invoice_sale.rst

.. help-include:: account_invoice_update.rst

.. help-include:: account_invoice_form_actions.rst

.. help-include:: account_invoice_configure.rst

.. help-include:: account_invoice_report.rst

.. help-include:: account_invoice_example.rst

.. _faq:

FAQ
---

Click on button **Topic** to return to the specific help page.

.. help-question:: Why can't I change the invoice?

   .. help-version:: <13

      A validated invoice is locked. Cancel it with **Cancel Invoice** and
      press **Reset to Draft**: the journal must allow cancelling entries, see
      *How to set up*. If it is paid, remove the payment first.

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

.. help-question:: Can I write a negative quantity on an invoice line?

   Yes: a line with a negative quantity lowers the total of the invoice, e.g.
   for a returned item, a down payment already invoiced or an extra discount.
   Write the minus sign in the quantity and keep the unit price positive: the
   taxes of the line are lowered too. The total of the invoice must stay zero
   or positive, see the next question.

.. help-question:: What if the negative lines make the total negative?

   An invoice with a negative total is a credit note in disguise: the money
   goes to the customer, not from the customer.

   .. help-version:: 10

      Odoo 10.0 does not stop you, but do not validate it: the invoice would
      show the amount as due from the customer and **Register Payment** would
      propose to collect it, while the journal entry records the opposite.
      Correct the lines, or delete the draft and press **Refund Invoice** on
      the original invoice.

   .. help-version:: 11-12

      Odoo refuses to validate it: *You cannot validate an invoice with a
      negative total amount. You should create a credit note instead.*
      Correct the lines, or delete the draft and press **Add Credit Note** on
      the original invoice; a credit note with no original invoice is created
      in **Invoicing ‣ Customers ‣ Credit Notes**.

   .. help-version:: >=13

      Odoo refuses to confirm it: *You cannot validate an invoice with a
      negative total amount. You should create a credit note instead. Use the
      action menu to transform it into a credit note or refund.* Correct the
      lines, or turn the draft into a credit note with
      :version:`<=14|**Action ‣ Switch into refund/credit note**;<=16|**Action
      ‣ Switch into invoice/credit note**;*|**Switch into invoice/credit
      note** in the menu under the gear icon`: Odoo changes the sign of the
      quantities, so the credit note has a positive total. A credit note of a
      posted invoice is created with
      :version:`<18|**Add Credit Note**;*|**Credit Note**` on the invoice.

.. help-version:: 10

   .. help-include:: account_invoice_faq_einvoice.rst

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-10-02 07:23 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
