.. help-version:: <13

   .. help-page:: account_invoice_in_list
      :title: Vendor bills
      :model: account.invoice
      :view: account.invoice_supplier_tree
      :view-type: list
      :priority: 96

.. help-version:: 13

   .. help-page:: account_invoice_in_list
      :title: Vendor bills
      :model: account.move
      :view: account.view_invoice_tree, account.view_in_invoice_tree
      :view-type: list
      :when: type = in_invoice, in_refund, in_receipt
      :priority: 96

.. help-version:: >=14

   .. help-page:: account_invoice_in_list
      :title: Vendor bills
      :model: account.move
      :view: account.view_invoice_tree, account.view_in_invoice_tree, account.view_in_invoice_bill_tree, account.view_in_invoice_refund_tree, account.view_in_invoice_receipt_tree
      :view-type: list
      :when: move_type = in_invoice, in_refund, in_receipt
      :priority: 96

Vendor bills
============

.. _description:

Description
-----------

Click on button [`Ready`] for help about how to use this help; click on
button [`FAQ`] for the most common solved questions.

.. help-version:: <13

   The list of the vendor bills and of their :version:`10|refunds;*|credit
   notes`, depending on the menu: what the vendors ask you to pay. Each row
   shows the :field:`vendor <partner_id>`, the :field:`bill date
   <date_invoice>`, the :field:`number <number>`, the :field:`vendor reference
   <reference>`, the :field:`due date <date_due>`, the total, the amount still
   to pay and the :field:`status <state>`. Click a row to open the bill.

.. help-version:: >=13

   The list of the vendor bills and of their refunds, depending on the menu:
   what the vendors ask you to pay. Each row shows the :field:`number <name>`,
   the :field:`vendor <partner_id>`, the :field:`bill date <invoice_date>`,
   the :field:`due date <invoice_date_due>`, the total, the amount still due
   and the :field:`status <state>`\ :version:`>=14|, with the payment status`.
   Click a row to open the bill.

.. _new_record:

How to insert a new record
--------------------------

Press :version:`<16|[\`Create\`];*|[\`New\`]` at the top left: an empty form
opens, see its help for the fields to fill in.
:version:`>=17|[\`Upload\`] creates a bill from the PDF sent by the vendor.`

.. help-include:: account_invoice_in_list_search.rst

.. _update_record:

How to update a record
----------------------

Click on a line of the list to open its form, then follow the help of the
form to change it.

.. help-include:: account_invoice_in_cancel.rst

.. help-include:: account_invoice_in_list_actions.rst

.. help-include:: account_invoice_in_configure.rst

.. help-include:: account_invoice_in_report.rst

.. help-include:: account_invoice_in_list_example.rst

.. _faq:

FAQ
---

Click on button [`Topic`] to return to the specific help page.

.. help-question:: Why don't I see the vendor credit notes?

   .. help-version:: 10

      Refunds are in the same list as the bills: use the *Refunds* filter, or
      *Invoices* to hide them.

   .. help-version:: >=11

      They have their own menu:
      :version:`11|**Invoicing ‣ Purchases ‣ Vendor Credit
      Notes**;12-13|**Invoicing ‣ Vendors ‣ Refund**;*|**Invoicing ‣ Vendors ‣
      Refunds**`.

.. help-question:: How do I see the bills still to be paid?

   Use the :version:`10|*Not Paid*;11-12|*Open*;13-14|*Not Paid*;15-17|*Unpaid*;*|*To pay*`
   filter; *Overdue* shows only those whose due date is passed.

.. help-question:: Why do I see journal entries here?

   .. help-version:: <13

      The list shows only invoices and bills; the journal entries are in the
      accounting menus, visible to the accountants.

   .. help-version:: >=13

      A bill is a journal entry with a bill type: the vendor menus show only
      the bill types, while the journal entries list of the accountants shows
      every entry, bills included, and has no bill help.

.. help-if:: module = purchase

   .. help-question:: Where do the bills of a purchase order appear?

      In this list too: a bill created from a purchase order is a normal
      vendor bill, linked to the order. See the form help for how to create
      it.

.. help-version:: 10

   .. help-include:: account_invoice_in_faq_einvoice.rst

.. _footer:

Footer
------

Page created on 2026-11-22 10:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
