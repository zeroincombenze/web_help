.. help-version:: <13

   .. help-page:: account_invoice_out_list
      :title: Customer invoices
      :model: account.invoice
      :view: account.invoice_tree, account.invoice_tree_with_onboarding
      :view-type: list
      :priority: 96

.. help-version:: 13

   .. help-page:: account_invoice_out_list
      :title: Customer invoices
      :model: account.move
      :view: account.view_invoice_tree, account.view_out_invoice_tree, account.view_out_credit_note_tree
      :view-type: list
      :when: type = out_invoice, out_refund, out_receipt
      :priority: 96

.. help-version:: >=14

   .. help-page:: account_invoice_out_list
      :title: Customer invoices
      :model: account.move
      :view: account.view_invoice_tree, account.view_out_invoice_tree, account.view_out_credit_note_tree
      :view-type: list
      :when: move_type = out_invoice, out_refund, out_receipt
      :priority: 96

Customer invoices
=================

.. _description:

Description
-----------

Click on button [`Ready`] for help about how to use this help; click on
button [`FAQ`] for the most common solved questions.

.. help-version:: <13

   The list of the customer invoices and of their credit notes, depending on
   the menu. Each row shows the :field:`number <number>`, the :field:`customer
   <partner_id>`, the :field:`invoice date <date_invoice>`, the :field:`due
   date <date_due>`, the total, the amount still due and the :field:`status
   <state>`. Click a row to open the invoice.

.. help-version:: >=13

   The list of the customer invoices and credit notes, depending on the menu.
   Each row shows the :field:`number <name>`, the :field:`customer
   <partner_id>`, the :field:`invoice date <invoice_date>`,
   the :field:`due date <invoice_date_due>`, the total, the amount still due
   and the :field:`status <state>`\ :version:`>=14|, with the payment status`.
   Click a row to open the invoice.

.. _new_record:

How to insert a new record
--------------------------

Press :version:`<16|[\`Create\`];*|[\`New\`]` at the top left: an empty form
opens, see its help for the fields to fill in.

.. help-include:: account_invoice_out_list_search.rst

.. _update_record:

How to update a record
----------------------

Click on a line of the list to open its form, then follow the help of the
form to change it.

.. help-include:: account_invoice_out_cancel.rst

.. help-include:: account_invoice_out_list_actions.rst

.. help-include:: account_invoice_out_configure.rst

.. help-include:: account_invoice_out_report.rst

.. help-include:: account_invoice_out_list_example.rst

.. _faq:

FAQ
---

Click on button [`Topic`] to return to the specific help page.

.. help-question:: Why don't I see the credit notes?

   .. help-version:: 10

      Refunds are in the same list as the invoices: use the *Refunds* filter,
      or *Invoices* to hide them.

   .. help-version:: 11

      They have their own menu: **Invoicing ‣ Sales ‣ Customer Credit Notes**.

   .. help-version:: >=12

      They have their own menu: **Invoicing ‣ Customers ‣ Credit Notes**.

.. help-question:: How do I see the invoices still to be paid?

   Use the :version:`10|*Not Paid*;11-12|*Open*;13-14|*Not Paid*;15-17|*Unpaid*;*|*To pay*`
   filter; *Overdue* shows only those whose due date is passed.

.. help-question:: Why do I see journal entries here?

   .. help-version:: <13

      The list shows only invoices; the journal entries are in the accounting
      menus, visible to the accountants.

   .. help-version:: >=13

      An invoice is a journal entry with an invoice type: the invoice menus
      show only the invoice types, while the journal entries list of the
      accountants shows every entry, invoices included, and has no invoice
      help.

.. help-version:: 18

   .. help-include:: account_invoice_out_faq_einvoice.rst

.. _footer:

Footer
------

Page created on 2026-11-20 10:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
