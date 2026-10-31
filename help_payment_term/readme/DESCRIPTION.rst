Context help pages for the payment terms list and form
(``account.payment.term``), shown by web_context_help.

Payment terms compute the due dates of the invoices. The pages explain how to
load the most common terms:

* **30 days**: due 30 days after the invoice date
* **30 days end of month**: due at the end of the month, 30 days after the
  invoice date; with the native rules of the running Odoo version or with the
  *Payment day(s)* of the OCA module ``account_payment_term_extension``
* **30 days end of month + 5 days**: due on the 5th of the following month

Every page follows the standard layout of web_context_help:

* **Contents**: the sections of the page, built by the help window
* **Description**: what payment terms are and how the lines work
* **How to insert a new record** (form): step-by-step guide to load the
  *30 days* terms
* **Suggestions for search** (list): menu, search, filters and groupings
* **How to update a record** (form): changing, archiving and deleting payment
  terms
* **How to set up**: where payment terms are used and the OCA module
* **Report and export file**: the due dates printed on the invoice and the
  export of the payment terms to a file
* **Example** button: *30 days end of month* and *30 days end of month + 5
  days*
* **FAQ** button and **Footer**

Pages are in English and Italian, with the fields and options of the running
Odoo version.
