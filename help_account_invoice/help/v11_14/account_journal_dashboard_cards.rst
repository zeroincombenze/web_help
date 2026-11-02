**Sale and purchase journals**

* **New Invoice** (sales) or **New Bill** (purchases) opens a new customer
  invoice or vendor bill in this journal.
* **Import Bills** (purchases) opens *Import Vendor Bills*: add the files of
  the bills (e.g. the PDF received by email) and press **Import**; each file
  becomes a draft vendor bill with the file attached, to be completed.
* *N Invoices to Validate* (sales) or *N Bills to Validate* (purchases): how
  many documents are still in draft, and their total; click to list them
  (*Draft* filter).
* *N Unpaid Invoices* (sales) or *N Bills to Pay* (purchases): how many
  validated documents are not paid yet, and the amount still due; click to
  list them (*Open* filter). Credit notes are subtracted from the totals.

.. help-if:: module = hr_expense

   * *N Expenses to Process* (purchases): the approved or posted expense
     reports of this journal, and their total; click to list them.

* The bar chart shows the amount still due of the validated documents, by
  week of their due date: *Past*, the previous week, *This Week*, the next
  two weeks and *Future*.

**Bank and cash journals**

* **Configure** (bank) is shown while the bank feeds of the journal are not
  set: it opens *Create a Bank Account*, see *FAQ*.

.. help-if:: module != account_bank_statement_import

   * The **Create** link of *Create Statements* (bank) opens a new bank
     statement, to record the movements of the account by hand.

.. help-if:: module = account_bank_statement_import

   * *Create or Import Statements* (bank): **Create** opens a new bank
     statement, to record the movements of the account by hand; **Import**
     loads the statement file downloaded from the bank.

* **New Transactions** (cash) opens a new cash statement.
* **Reconcile N Items** appears when lines of the open statements are still
  to be matched with invoices, payments or accounts: it opens the
  reconciliation. **New Transactions** then becomes a link below it.
* *Balance in General Ledger*: the balance of the posted entries on the
  default debit and credit accounts of the journal, up to today. *Latest
  Statement*: the ending balance of the last statement, shown only when it
  differs from *Balance in General Ledger*.

.. help-if:: module = account_check_printing

   * *N Checks to print* (bank): the checks waiting to be printed; click to
     list them.

* The line chart shows the balance of the statements over the last 30 days.

**Miscellaneous journals**

* **Journal Entries** lists the entries of the journal. The card shows no
  figures: use the **⋮** menu.

**The ⋮ menu**

**⋮**, at the top right of a card, opens its menu, in columns.

* Sale and purchase journals:

  * *View*: **Invoices** or **Bills**, **Credit Notes**, **Payments
    Matching** (the invoices and payments of the customers or vendors still
    to be matched).
  * *New*: **Invoice** or **Bill**, **Credit Note** or **Credit Note Bill**.
  * *Reporting*: **Invoices Analysis** or **Bills Analysis** (*Billing
    Manager* only).

* Bank and cash journals:

  * *View*: **Statements**, **Operations** (the statement lines of the
    journal), **Customer Payments**, **Vendor Payments** and **Internal
    Transfers** (the payments of the journal of that kind).
  * *New*: **Statement**, **Customer Payment**, **Vendor Payment** and
    **Internal Transfer**: these three open a new payment of that kind in
    this journal.

    .. help-if:: module = account_bank_statement_import

       On a bank journal also **Import Statement**.

  * *Reconciliation*: **Reconciliation Models** (*Billing Manager* only),
    the predefined counterparts proposed by the reconciliation, e.g. the bank
    fees.

* Miscellaneous journals:

  * *View*: **Journal Entries**, and **Entries to Review**, only the
    *Unposted* entries of the journal.
  * *New*: **Journal Entry**.
  * *Operations*: **Post All Entries**; it does not work in this version, see
    *FAQ* to post the draft entries.

In developer mode *View* also lists the **Journal Items** of the journal.
At the bottom, for the *Billing Manager* access right only, the colors of
the card, the star **Add to Favorites** / **Remove from Favorites** (see
*Suggestions for search*) and **Settings**, which opens the journal form.
