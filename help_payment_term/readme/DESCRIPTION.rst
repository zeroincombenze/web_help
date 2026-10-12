Context help pages for the payment terms list and form
(``account.payment.term``), shown by web_context_help.

Payment terms compute the due dates of the invoices. The pages explain how to
load the most common terms:

* **30 days**: due 30 days after the invoice date
* **30 days end of month**: due at the end of the month, 30 days after the
  invoice date; with the native rules of the running Odoo version or with the
  *Payment day(s)* of the OCA module ``account_payment_term_extension``
* **30 days end of month + 5 days**: due on the 5th of the following month

Every page follows the help rule of web_context_help:

* **Description**: what payment terms are and how the lines work
* **New record** (form): step-by-step guide to load the *30 days* terms
* **Update record** (form): changing, archiving and deleting payment terms
* **How to search** (list): menu, search, filters and groupings
* **Configure**: where payment terms are used and the OCA module
* **Report**: the due dates printed on the invoice
* **Example**: *30 days end of month* and *30 days end of month + 5 days*
* **FAQ** and **Footer**

Pages are in English and Italian, with the fields and options of the running
Odoo version.
