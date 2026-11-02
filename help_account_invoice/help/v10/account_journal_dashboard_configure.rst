.. _configure:

How to set up
-------------

.. help-if:: module != account_accountant

   * **Invoicing ‣ Configuration ‣ Accounting ‣ Journals** (*Adviser* only):
     every journal is a card of the dashboard.

.. help-if:: module = account_accountant

   * **Accounting ‣ Configuration ‣ Accounting ‣ Journals** (*Adviser*
     only): every journal is a card of the dashboard.

* In the journal form: the :field:`Journal Name <name>` and the
  :field:`Type <type>` shown on the card; in the *Journal Entries* tab the
  :field:`Short Code <code>` and the default debit and credit accounts,
  whose balance is the *Balance in GL* of a bank or cash card.
* A bank journal has the *Bank Account* tab: the account number, the bank and
  the :field:`Bank Feeds <bank_statements_source>`, which chooses the
  statement buttons of the card.
* **More ‣ Settings** on a card opens the same form; **More ‣ Favorite** adds
  the journal to the *Favorites* filter or removes it. In developer mode the
  same choice is the :field:`Show journal on dashboard <show_on_dashboard>`
  check box, in the *Advanced Settings* tab.
* The access right of each user is in **Settings ‣ Users ‣ Users**, field
  *Accounting & Finance*: the dashboard is for *Accountant* and *Adviser*.
