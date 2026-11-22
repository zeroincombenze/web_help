.. _example:

Example
-------

**Overdue bills of a vendor**

Choose the *Overdue* filter, type the vendor name in the search bar and
select the partner search: the total still due is at the bottom of the
column.

**Searching with the wildcard**

The ``%`` (percent) character in a search value means *any text*. Searching
the partner ``Rossi%Milano`` finds *Rossi S.r.l. - Milano* and *Rossi Mario
Milano*, but not *Rossi S.p.A. - Roma*. Searching the number ``%/2026/%``
finds the bills numbered in 2026, in any journal.

**Bills to pay this month**

Choose the :version:`10|*Not Paid*;11-12|*Open*;13-14|*Not Paid*;15-17|*Unpaid*;*|*To
pay*` filter, then **Group By ‣ Due Date ‣ Month**: each group shows its
subtotal, i.e. what you have to pay in that month. Save the search with
**Favorites ‣ Save current search** to reuse it.
