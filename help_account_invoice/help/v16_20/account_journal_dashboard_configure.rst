.. _configure:

How to set up
-------------

.. help-if:: module != accountant

   * **Invoicing ‣ Configuration ‣ Accounting ‣ Journals** (*Administrator*
     only): every journal is a card of the dashboard.

.. help-if:: module = accountant

   * **Accounting ‣ Configuration ‣ Accounting ‣ Journals** (*Administrator*
     only): every journal is a card of the dashboard.

* In the journal form: the :field:`Journal Name <name>` and the
  :field:`Type <type>` shown on the card; in the *Journal Entries* tab the
  default account, whose balance a bank or cash card follows, and the
  :field:`Short Code <code>`.
* A bank journal has, in the same tab, the *Account Number*, the bank and the
  :field:`Bank Feeds <bank_statements_source>`, how the transactions arrive.
  While the account number is empty and the bank feed is not chosen yet, the
  card shows **Bank Setup**.
* The *Incoming Payments* and *Outgoing Payments* tabs of a bank or cash
  journal list the payment methods, used by **Customer Payment** and
  **Vendor Payment**.
* **⋮ ‣ Configuration** on a card opens the same form; **⋮ ‣ ☆** adds the
  journal to the *Favorites* filter or removes it; the colour chosen in the
  **⋮** menu marks the card.
* The access right of each user is in **Settings ‣ Users & Companies ‣
  Users**, field *Invoicing*.
