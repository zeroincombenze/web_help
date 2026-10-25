.. help-version:: <13

   .. help-page:: account_invoice_list
      :title: Invoices
      :model: account.invoice
      :view: account.invoice_tree, account.invoice_tree_with_onboarding, account.invoice_supplier_tree
      :view-type: list
      :priority: 96

.. help-version:: 13

   .. help-page:: account_invoice_list
      :title: Invoices
      :model: account.move
      :view: account.view_invoice_tree, account.view_out_invoice_tree, account.view_in_invoice_tree
      :view-type: list
      :when: type != entry
      :priority: 96

.. help-version:: >=14

   .. help-page:: account_invoice_list
      :title: Invoices
      :model: account.move
      :view: account.view_invoice_tree, account.view_out_invoice_tree, account.view_in_invoice_tree
      :view-type: list
      :when: move_type != entry
      :priority: 96

Invoices
========

.. _description:

Description
-----------

.. help-version:: <13

   The list of customer invoices, or of vendor bills, depending on the menu.
   Each row shows the :field:`number <number>`, the :field:`partner
   <partner_id>`, the :field:`invoice date <date_invoice>`, the :field:`due
   date <date_due>`, the total, the amount still due and the :field:`status
   <state>`. Click a row to open the invoice.

.. help-version:: >=13

   The list of customer invoices, credit notes, vendor bills or refunds,
   depending on the menu. Each row shows the :field:`number <name>`, the
   :field:`partner <partner_id>`, the :field:`invoice date <invoice_date>`,
   the :field:`due date <invoice_date_due>`, the total, the amount still due
   and the :field:`status <state>`\ :version:`>=14|, with the payment status`.
   Click a row to open the invoice.

.. help-include:: account_invoice_list_search.rst

.. help-include:: account_invoice_configure.rst

.. help-include:: account_invoice_report.rst

.. help-include:: account_invoice_list_example.rst

.. _faq:

FAQ
---

.. help-question:: Why don't I see the credit notes?

   .. help-version:: 10

      Refunds are in the same list as the invoices: use the *Refunds* filter,
      or *Invoices* to hide them.

   .. help-version:: 11

      They have their own menu: **Invoicing ‣ Sales ‣ Customer Credit Notes**,
      and **Invoicing ‣ Purchases ‣ Vendor Credit Notes** for the vendors.

   .. help-version:: >=12

      They have their own menu: **Invoicing ‣ Customers ‣ Credit Notes**, and
      **Invoicing ‣ Vendors ‣** :version:`<14|**Refund**;*|**Refunds**` for the
      vendors.

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

.. _footer:

Footer
------

Page created on 2026-10-02 07:23 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
