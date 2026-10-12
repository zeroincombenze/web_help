.. _wildcard:

Searching with the wildcard
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes a more specific or more difficult search is needed. Suppose, for
example, you are looking for the orders of the customers of *Settimo
Torinese*.

.. help-version:: >=17

   Use **Filters ‣ Add Custom Filter**, choose the field *Customer ‣ City* and
   the operator *contains*.

.. help-version:: <17

   The custom filter of the orders cannot reach the customer fields: search in
   the :version:`<12|**Sales ‣ Sales ‣ Customers**;*|**Sales ‣ Orders ‣
   Customers**` list with **Filters ‣ Add Custom Filter**, field *City* and
   operator *contains*.

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
