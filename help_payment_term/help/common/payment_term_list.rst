.. help-page:: payment_term_list
   :title: Payment Terms
   :model: account.payment.term
   :view: account.view_payment_term_tree
   :view-type: list
   :priority: 96

Payment Terms
=============

.. _description:

Description
-----------

The list of the payment terms: each one computes the due dates of the
invoices that use it. Each row shows the :field:`name <name>` and, in a
multi-company database, the :field:`company <company_id>`. The terms are
listed :version:`<11|by name;*|in the order of the selection lists`. Click a
row to open the terms and see their lines.

.. help-include:: payment_term_list_search.rst

.. help-include:: payment_term_configure.rst

.. help-include:: payment_term_report.rst

.. help-include:: payment_term_list_example.rst

.. _faq:

FAQ
---

.. help-question:: Why don't I see some payment terms?

   Archived terms are hidden: :version:`<13|search them with a custom filter
   *Active* is not set;*|use the *Archived* filter to see them`, open them
   and :version:`<17|use **Action ‣ Unarchive**;*|use the gear icon ‣
   **Unarchive**` to use them again. In a multi-company database you see only
   the terms of your companies, and those without company.

.. help-question:: How do I change the order of the terms in the selection lists?

   .. help-version:: <11

      The terms are sorted by name: rename them, e.g. with a number in front.

   .. help-version:: >=11

      Drag the rows by the handle at the left: the terms are proposed in that
      order.

.. help-question:: Which payment terms does Odoo already provide?

   The module ``account`` installs the most common ones:
   :version:`<12|*Immediate Payment*, *15 Days* and *30 Net Days*;12-13|*Immediate
   Payment*, *15 Days*, *30 Net Days*, *45 Days* and *2 Months*;14-15|*Immediate
   Payment*, *15 Days*, *21 Days*, *30 Days*, *45 Days*, *2 Months*, *End of
   Following Month* and *30% Now, Balance 60 Days*;16|*Immediate Payment*, *15
   Days*, *21 Days*, *30 Days*, *45 Days*, *2 Months*, *End of Following
   Month*, *30 days End of Month on the 10th*, *30% Now, Balance 60 Days* and
   *2/7 Net 30*;*|*Immediate Payment*, *15 Days*, *21 Days*, *30 Days*, *45
   Days*, *End of Following Month*, *10 Days after End of Next Month*, *30%
   Now, Balance 60 Days* and *2/7 Net 30*`. Change or archive the ones you do
   not use.

.. _footer:

Footer
------

Page created on 2026-10-12 06:38 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
