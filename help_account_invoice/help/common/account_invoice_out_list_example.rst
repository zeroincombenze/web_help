.. _example:

Example
-------

**Overdue invoices of a customer**

Choose the *Overdue* filter, type the customer name in the search bar and
select the partner search: the total still due is at the bottom of the
column.

**Searching with the wildcard**

The ``%`` (percent) character in a search value means *any text*. Searching
the partner ``Rossi%Milano`` finds *Rossi S.r.l. - Milano* and *Rossi Mario
Milano*, but not *Rossi S.p.A. - Roma*. Searching the number ``%/2026/%``
finds the invoices numbered in 2026, in any journal.

**Invoiced amount of each month**

:version:`<13|Choose the *Open* and *Paid* filters;*|Choose the *Posted*
filter`, then **Group By ‣ Invoice Date ‣ Month**: each group shows its
subtotal. Save the search with **Favorites ‣ Save current search** to
reuse it.

**Print several invoices**

Select the invoices with the check boxes, then
:version:`<18|**Print ‣ Invoices**;*|**Print ‣ Invoice PDF**`: one PDF holds
all of them.
