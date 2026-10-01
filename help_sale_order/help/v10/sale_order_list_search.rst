.. _search:

How to search
-------------

* **Sales ‣ Sales ‣ Quotations** lists the quotations, **Sales ‣ Sales ‣ Sales
  Orders** the confirmed orders, **Sales ‣ Invoicing ‣ Sales to Invoice** the
  orders waiting for an invoice.
* Type in the search bar and choose what to search: *Sales Order* (number or
  customer reference), *Customer*, *Salesperson* or *Sales Team*.
* **Filters**: *My Orders* shows your documents only; *Quotations*, *Quotations
  Sent*, *Sales*, *To Invoice* and *Upselling* narrow the list; *Add Custom
  Filter* builds any condition.
* **Group By**: *Salesperson*, *Customer* or *Order Month*, with subtotals;
  :field:`invoice status <invoice_status>` (*Nothing to Invoice*, *To Invoice*,
  *Fully Invoiced*, *Upselling Opportunity*) can be used in a custom filter.
* **Favorites ‣ Save current search** keeps filters and groups for later.

.. _wildcard:

Searching with the wildcard
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes a more specific or more difficult search is needed. Suppose, for
example, you are looking for the orders of the customers of *Settimo
Torinese*.
The custom filter of the orders cannot reach the customer fields: search in
the **Sales ‣ Sales ‣ Customers** list with **Filters ‣ Add Custom Filter**,
field *City* and operator *contains*.

* With the field *City*, the operator *contains* and the value ``Settimo``
  you also get records of other towns, e.g. *Settimo Milanese*.
* With the value ``Settimo Torinese`` the search is precise, even too precise:
  the customers whose city is written *Settimo T.se* are not found.

The solution is the ``%`` (percent) character, called wildcard, which means
*any value*. The value ``Settimo T%se`` finds both *Settimo Torinese* and
*Settimo T.se*, but not *Settimo Milanese*.
A search with *contains* ignores upper and lower case.

A more complex example is the search for towns named after saints, e.g.
*Santa Maria Capua Vetere*. This town may be written:

* Santa Maria di Capua Vetere
* Santa Maria Capua Vetere
* Santa Maria di C.V.
* Santa Maria CV
* S\. Maria di Capua Vetere
* S\. Maria di CV

Moreover many towns are named Santa Maria, e.g. *Santa Maria a Vico*, *Santa
Maria della Versa* and *Santa Maria Maggiore*, just to name a few. The trick
of a good search is to look for the parts that are surely in the name you are
looking for. In the example the parts are:

#. initial ``S``, for *S.* or *Santa*
#. ``Maria``, in full, without abbreviations
#. ``C``, for *Capua* or its abbreviation
#. ``V``, for *Vetere* or its abbreviation

The filter value becomes ``S%Maria%C%V``, which reads: contains, in this
order, "S", "Maria", "C" and "V". *Santa Maria Maggiore* is not included
because "C" and "V" are missing; *Santa Maria della Versa* is not included
because, although it contains "V", "C" is missing.
