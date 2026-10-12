.. _example:

Example
-------

**30 days end of month**

The amount is due at the end of the month in which the 30th day after the
invoice date falls:

* invoice of 15 January → 14 February → due on **28 February**;
* invoice of 31 January → 2 March → due on **31 March**.

Create the terms as in *New record*, name them *30 Days End of Month*, then
set the line as follows.

.. help-version:: <12

   The options of the line cannot add 30 days and then go to the end of the
   month. The nearest one is *Last day of following month*: the end of the
   month after the invoice month. It gives the same due date except for the
   invoices at the end of a month, when the 30th day falls two months later:
   the invoice of 31 January is due on 28 February instead of 31 March.

   Do not use *Day(s) after the end of the invoice month (Net EOM)* with 30
   days: it means end of the invoice month + 30 days, so the invoice of 15
   January is due on 2 March.

   **With the OCA module account_payment_term_extension** the due date is
   exact. In the line form:

   #. :field:`Type <value>`: *Balance*.
   #. Option *Day(s) after the invoice date*, :field:`Number of days <days>`:
      30.
   #. :field:`Payment day(s) <payment_days>`: ``31``.

   Odoo adds 30 days to the invoice date, then moves to the next payment day:
   31 is the last day of any month (30 April, 28 February).

.. help-version:: 12-15

   In the line form:

   #. :field:`Term Type <value>`: *Balance*.
   #. Due :field:`30 <days>` :version:`12|*day(s) after the invoice
      date*;*|*days after the invoice date*`.
   #. :field:`On the 31 of the month <day_of_the_month>`: 31 is the last day of
      any month (30 April, 28 February).

   Do not use :version:`12|*day(s) after the end of the invoice
   month*;*|*days after the end of the invoice month*` with 30: it means end
   of the invoice month + 30 days, so the invoice of 15 January is due on
   2 March.

   **With the OCA module account_payment_term_extension** the field *On the …
   of the month* is :version:`12|ignored by the computation;*|hidden`, and
   the end of month is given by the payment days:

   #. Due 30 :version:`12|*day(s) after the invoice date*;*|*days after the
      invoice date*`.
   #. :field:`Payment day(s) <payment_days>`: ``31``.

   Odoo adds 30 days to the invoice date, then moves to the next payment day:
   the result is the same as the native *On the 31 of the month*. If the
   module is uninstalled, write the 31 in *On the … of the month* first.

.. help-version:: 16

   In the **Terms** table, on the *Balance* line:

   #. :field:`Months <months>`: 0, :field:`Days <days>`: 30.
   #. :field:`End of month <end_month>`: on.
   #. :field:`Days after End of month <days_after>`: 0.

   Odoo adds 30 days to the invoice date, then goes to the last day of that
   month. Do not write the 30 in *Days after End of month* with 0 days: that
   means end of the invoice month + 30 days, so the invoice of 15 January is
   due on 2 March.

   **With the OCA module account_payment_term_extension** the terms of the
   module, *Days* 30 with :field:`Payment day(s) <payment_days>` ``31`` and
   *End of month* off, give the same due date: they keep working, but the
   native *End of month* is clearer. Use one of the two, not both.

.. help-version:: 17

   The delay types cannot add 30 days and then go to the end of the month.
   The nearest one is 100% :field:`After <nb_days>` 0 *Days after end of next
   month*: the end of the month after the invoice month. It gives the same
   due date except for the invoices at the end of a month, when the 30th day
   falls two months later: the invoice of 31 January is due on 28 February
   instead of 31 March.

   Do not use 30 *Days after end of month*: it means end of the invoice
   month + 30 days, so the invoice of 15 January is due on 2 March.

   **With the OCA module account_payment_term_extension** the due date is
   exact:

   #. 100% :field:`After <nb_days>` 30 *Days after invoice date*.
   #. :field:`Payment day(s) <payment_days>`: ``31``.

   Odoo adds 30 days to the invoice date, then moves to the next payment day:
   31 is the last day of any month (30 April, 28 February).

.. help-version:: >=18

   In the **Due Terms** table:

   #. 100% :field:`After <nb_days>` 30, delay type *Days end of month on the*.
   #. In the small box after the delay type (:field:`days on the next month
      <days_next_month>`, 10 by default) write 0: 0 means the end of the
      month.

   Odoo adds 30 days to the invoice date, then goes to the last day of that
   month. Check it in the **Preview** with 15 January and 31 January. Do not
   use 30 *Days after end of month*: it means end of the invoice month + 30
   days, so the invoice of 15 January is due on 2 March.

   **With the OCA module account_payment_term_extension** the terms of the
   module, 30 *Days after invoice date* with :field:`Payment day(s)
   <payment_days>` ``31``, give the same due date: terms loaded that way, e.g.
   in a migrated database, keep working. For new terms use the native *Days
   end of month on the*, which needs no module and is shown in the
   **Preview**. Use one of the two, not both.

**30 days end of month + 5 days**

The amount is due 5 days after the *30 days end of month*, i.e. on the 5th of
the following month:

* invoice of 15 January → 28 February → due on **5 March**;
* invoice of 31 January → 31 March → due on **5 April**.

Create the terms *30 Days End of Month + 5* and set the line as follows.

.. help-version:: <12

   The options of the line cannot compute these terms. **With the OCA module
   account_payment_term_extension**:

   #. Option *Day(s) after the invoice date*, :field:`Number of days <days>`:
      35 (30 + 5).
   #. :field:`Payment day(s) <payment_days>`: ``5``.

   Odoo adds 35 days to the invoice date, then moves to the next 5th of a
   month: it is always the 5th after the end of the month of the 30th day
   (15 January + 35 days = 19 February → 5 March).

.. help-version:: 12-15

   #. Due 35 (30 + 5) :version:`12|*day(s) after the invoice date*;*|*days
      after the invoice date*`.
   #. :field:`On the 5 of the month <day_of_the_month>`.

   Odoo adds 35 days to the invoice date, then moves to the next 5th of a
   month: it is always the 5th after the end of the month of the 30th day
   (15 January + 35 days = 19 February → 5 March).

   **With the OCA module account_payment_term_extension** write ``5`` in
   :field:`Payment day(s) <payment_days>` instead of *On the … of the month*,
   with the same 35 days.

.. help-version:: 16

   On the *Balance* line: :field:`Days <days>` 30, :field:`End of month
   <end_month>` on, :field:`Days after End of month <days_after>` 5.

   **With the OCA module account_payment_term_extension** the same result is
   given by *Days* 35 with :field:`Payment day(s) <payment_days>` ``5`` and
   *End of month* off.

.. help-version:: 17

   The nearest delay type is 100% :field:`After <nb_days>` 5 *Days after end
   of next month*, with the same exception of the invoices at the end of a
   month (31 January → 5 March instead of 5 April).

   **With the OCA module account_payment_term_extension** the due date is
   exact: 100% *After* 35 (30 + 5) *Days after invoice date* and
   :field:`Payment day(s) <payment_days>` ``5``. Odoo adds 35 days, then moves
   to the next 5th of a month (15 January + 35 days = 19 February → 5 March).

.. help-version:: >=18

   100% :field:`After <nb_days>` 30, delay type *Days end of month on the*,
   and 5 in the box after it: Odoo adds 30 days to the invoice date, then goes
   to the 5th of the next month (15 January → 14 February → 5 March).

   **With the OCA module account_payment_term_extension** the old terms, 35
   *Days after invoice date* with :field:`Payment day(s) <payment_days>`
   ``5``, give the same due date.
