.. _configure:

Configure
---------

* Payment terms are in **Invoicing ‣ Configuration ‣**
  :version:`<13|**Management**;*|**Invoicing**` **‣ Payment Terms**, for the
  users with the accountant rights.
* On the partner, :version:`10|**Accounting**;*|**Sales & Purchase**` tab:
  the *Payment Terms* of the customer (proposed on sale orders and customer
  invoices) and those of the vendor (proposed on purchase orders and vendor
  bills).
* In a multi-company database the :field:`company <company_id>` limits the
  terms to one company; empty means every company.

.. help-version:: >=16

   * :version:`16|*Display terms on invoice*;*|*Show installment dates*`
     prints the due dates with their amounts on the invoice.
   * The early payment discount: :version:`16|*Discount %* and *Discount Days*
     on the line;*|*Early Discount* with its percentage and days`, and the
     *Cash Discount Tax Reduction* in **Invoicing ‣ Configuration ‣
     Settings**.

**OCA module account_payment_term_extension**

The OCA module ``account_payment_term_extension`` (repository
:version:`<13|account-invoicing;*|account-payment`) adds to the lines:

* :field:`Payment day(s) <payment_days>`: the days of the month when the
  partner pays, e.g. ``31`` (end of month) or ``10,20``: the due date moves
  to the first of these days on or after the computed date.
* the number of weeks\ :version:`<16|, and the number of months`\
  :version:`>=17|: delay types in weeks and months, enabled by *Payment
  terms Delay types* in **Invoicing ‣ Configuration ‣ Settings**`.
* :field:`Amount Rounding <amount_round>` of the instalments\
  :version:`>=13|, and the *Percent (Untaxed amount)* type`.

and to the terms *Sequential lines* (each line starts from the due date of
the previous one) and the *Holidays* with their postponed date.

.. help-version:: 12-15

   With the module, the field *On the … of the month* of the line is
   :version:`12|ignored by the computation;*|hidden`: use *Payment day(s)*.
