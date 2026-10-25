.. help-page:: payment_term_form
   :title: Payment Terms
   :model: account.payment.term
   :view: account.view_payment_term_form
   :view-type: form
   :priority: 96

Payment Terms
=============

.. _description:

Description
-----------

Payment terms tell when a customer must pay an invoice, or when you must pay a
vendor bill: Odoo computes the :version:`<13|due date;*|due dates` of the
invoice from the invoice date and the lines of the terms. Payment terms are
chosen on the partner and proposed on the sale orders, the purchase orders and
the invoices.

Every term has a :field:`name <name>`, shown in the selection lists (e.g.
*30 Days*), a :field:`description on the invoice <note>`, printed on the PDF,
and one or more :field:`lines <line_ids>`: each line is an instalment, with
its amount and its due date. A line computes the due date from the invoice
date: it adds days (or months) and can move the date to the end of the month
or to a fixed day of the month.

.. help-include:: payment_term_lines.rst

.. help-include:: payment_term_new.rst

.. help-include:: payment_term_update.rst

.. help-include:: payment_term_configure.rst

.. help-include:: payment_term_report.rst

.. help-include:: payment_term_example.rst

.. _faq:

FAQ
---

.. help-question:: Why can't I save the payment terms?

   .. help-version:: <17

      The terms need exactly one line of type *Balance*,
      :version:`<16|and it must be the last line;*|for the rest of the
      amount`. Percentages must be between 0 and 100.

   .. help-version:: >=17

      The *Percent* lines must add up to 100%: e.g. 30% and 70%, or a single
      100% line. A *Fixed* line is added to them.

.. help-question:: I changed the payment terms: why do my invoices keep the old due date?

   The due dates are computed when the invoice is
   :version:`<13|validated;*|created or the terms are chosen`, and saved on
   the invoice. Invoices already :version:`<13|validated;*|posted` keep their
   due dates; the new terms apply to the new invoices, or to a draft invoice
   when you choose the terms again.

.. help-question:: Why can't I delete the payment terms?

   Payment terms used by invoices cannot be deleted: archive them, so that
   they are no longer proposed but the old invoices keep them.

.. help-question:: What does day 31 mean in a month with 30 days?

   A day beyond the end of the month means the last day of the month: 31 is
   the 30th of April and the 28th (or 29th) of February. Use 31 to say *end of
   month*.

.. help-question:: Why is "end of month + 30 days" not "30 days end of month"?

   *End of month + 30 days* counts the days from the end of the invoice month:
   an invoice of 15 January is due on 2 March. *30 days end of month* counts
   30 days from the invoice date and then moves to the end of that month: the
   same invoice is due on 28 February. See *Example*.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-10-12 06:38 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
