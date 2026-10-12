.. _new_record:

New record
----------

The steps load the terms *30 Days*: the whole amount is due 30 days after the
invoice date (invoice of 15 January, due on 14 February).

#. Open **Invoicing ‣ Configuration ‣**
   :version:`<13|**Management**;*|**Invoicing**` **‣ Payment Terms** and
   press :version:`<17|**Create**;*|**New**`.
#. Write the :field:`name <name>`, e.g. *30 Days*: it is the text shown when
   the terms are chosen on a partner or an invoice.
#. Write the :field:`description on the invoice <note>`, e.g. *Payment terms:
   30 days from the invoice date*: it is printed on the invoice PDF.

.. help-version:: <16

   4. The table **Terms** already holds one line *Balance* with 0 days: click
      it to open its form.
   #. Leave :field:`Type <value>` on *Balance*, write 30 in
      :field:`Number of days <days>` and choose the option
      :version:`<12|*Day(s) after the invoice date*;12|*day(s) after the
      invoice date*;*|*days after the invoice date*`.

      .. help-version:: 12-15

         Leave :field:`On the … of the month <day_of_the_month>` on 0.

   #. Press **Save & Close** to close the line, then **Save** the payment
      terms.

.. help-version:: 16

   4. The table **Terms** already holds one line *Balance* with 0 days: click
      it and write 30 in :field:`Days <days>`. Leave :field:`Months <months>`
      on 0 and :field:`End of month <end_month>` off.
   #. Check the *Example* under the table: with an invoice date of 15
      January, the due date is 14 February.
   #. Press **Save**.

.. help-version:: >=17

   4. The table **Due Terms** already holds one line *100 % Percent After 0
      Days after invoice date*: click :field:`After <nb_days>` and write 30;
      leave *Days after invoice date*.
   #. Check the **Preview**: with an invoice date of 15 January, the amount is
      due on 14 February.
   #. The record is saved automatically when you leave it, or at once with
      the cloud icon next to the breadcrumb.

Choose the new terms on the partners (**Sales & Purchase** tab) or directly
on the invoice. Terms with more instalments (e.g. 30% now, 70% at 60 days)
have one line per instalment:
:version:`<17|the last line is the *Balance*;*|their percentages add up to 100%`.
