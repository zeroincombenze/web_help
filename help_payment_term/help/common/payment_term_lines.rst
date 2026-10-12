.. _lines:

Lines
~~~~~

.. help-version:: <16

   The lines are listed in the **Terms** table; click a line, or
   :version:`<12|**Add an item**;*|**Add a line**`, to open its form:

   * :field:`Type <value>`: *Balance* (the rest of the amount), *Percent* (a
     percentage of the total) or *Fixed Amount*. One line, the last one, must
     be *Balance*: the terms *30 Days* have a single *Balance* line.
   * :field:`Number of days <days>` and :field:`option <option>`: how the due
     date is computed.

   .. help-version:: <12

      The options are *Day(s) after the invoice date*, *Day(s) after the end of
      the invoice month (Net EOM)*, *Last day of following month* and *Last
      day of current month*; with the last two the number of days is ignored.

   .. help-version:: 12-15

      The options are :version:`12|*day(s) after the invoice date*, *day(s)
      after the end of the invoice month*;*|*days after the invoice date*,
      *days after the end of the invoice month*`, *of the following month* and
      *of the current month*: with the last two the number is the day of the
      month (e.g. the 10th of the following month). With *after the invoice
      date*, :field:`On the … of the month <day_of_the_month>` moves the due
      date to that day of the month (31 means the last day).

.. help-version:: 16

   The lines are edited directly in the **Terms** table:

   * :field:`Due Type <value>`: *Balance* (the rest of the amount), *Percent*
     or *Fixed Amount*, with its :field:`value <value_amount>`. Exactly one
     line must be *Balance*.
   * :field:`Months <months>` and :field:`Days <days>` are added to the
     invoice date.
   * :field:`End of month <end_month>` then moves the date to the last day of
     that month, and :field:`Days after End of month <days_after>` adds some
     days after it.
   * :field:`Discount % <discount_percentage>` and :field:`Discount Days
     <discount_days>`: the early payment discount.

   The *Example* under the table shows the due dates of an amount on a date:
   change the date to check the terms.

.. help-version:: >=17

   The lines are edited directly in the **Due Terms** table:

   * :field:`Due <value_amount>` with *Percent* or *Fixed*: the amount of the
     instalment. The percentages must add up to 100%.
   * :field:`After <nb_days>` and the :field:`delay type <delay_type>`: the
     number of days and where they start: *Days after invoice date*, *Days
     after end of month* (the end of the invoice month) or *Days after end of
     next month*.

   .. help-version:: >=18

      *Days end of month on the* adds the days to the invoice date, then goes
      to the :field:`day of the next month <days_next_month>` written in the
      small box after it; 0 means the end of the month.

   The **Preview** shows the due dates of an amount on a date: change the date
   to check the terms. :field:`Show installment dates <display_on_invoice>`
   prints the due dates and amounts on the invoice; *Early Discount* grants a
   discount for early payment.
