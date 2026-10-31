.. _report:

Report and export file
----------------------

Payment terms have no printable report of their own; they are printed on the
documents that use them:

* The invoice PDF shows the :field:`description on the invoice <note>` and
  the due date\ :version:`16|, and with *Display terms on invoice* every
  instalment with its amount;>=17|, and with *Show installment dates* every
  instalment with its amount`.
* The sale order and the purchase order show the chosen terms.
* The invoice list shows the *Due Date* of every invoice; the *Overdue*
  filter shows the late ones.
* To get a file of the payment terms, select them in the list view, then
  :version:`<=16|**Action ‣ Export**;*|**Actions ‣ Export**`: choose the
  fields and the format (xlsx or csv). See *Import and Export data* in the
  **Ready** page of the help.
