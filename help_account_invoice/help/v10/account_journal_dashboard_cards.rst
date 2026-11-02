**Sale and purchase journals**

* **New Invoice** (sales) or **New Bill** (purchases) opens a new customer
  invoice or vendor bill in this journal.
* *Invoices to validate* (sales) or *Draft bills* (purchases): how many
  documents are still in draft, and their total; click to list them.
* *Awaiting payments* (sales) or *Payments to do* (purchases): how many
  validated documents are not paid yet, and their total; click to list them.
  Refunds are subtracted from the totals.
* The bar chart shows the amount still due of the validated documents, by
  week of their accounting date: *Past*, the previous week, *This Week*, the
  next two weeks and *Future*.

**Bank and cash journals**

* **New Statement** (bank) or **New Transactions** (cash) creates a statement
  to record the movements of the account.

  .. help-if:: module = account_bank_statement_import

     **Import Statement** loads the statement file downloaded from the bank.
     A new bank journal shows both buttons; once you use one of them, the
     journal remembers it in its *Bank Feeds* (*Record Manually* or *File
     Import*) and the card shows only that one.

* **Reconcile N Items** appears when statement lines are still to be matched
  with invoices, payments or accounts: it opens the reconciliation. The
  statement buttons then become links below it.
* *Balance in GL*: the balance of the account of the journal in the accounts,
  up to today. *Latest Statement*: the ending balance of the last statement,
  shown only when it differs from *Balance in GL*.

  .. help-if:: module = account_check_printing

     *Checks to print*: the checks waiting to be printed; click to list them.

* The line chart shows the balance of the statements over the last 30 days.

**Miscellaneous journals**

The card shows no figures: use the **More** menu.

**The More menu**

**More ▾**, at the top right of a card, opens its menu, in columns.

* Sale and purchase journals:

  * *View*: **Invoices** or **Bills**, **Refunds**, **Payments Matching**
    (the invoices and payments of the partners still to be matched).
  * *New*: **Invoice** or **Bill**, **Refund** or **Bill Refund**.
  * *Reports*: **Invoices Analysis** or **Bills Analysis** (*Adviser*
    only).

* Bank and cash journals:

  * *View*: **Bank Statements** or **Cash Statements**, **Search Operations**
    (the statement lines of the journal).
  * *New*: **Transaction** (a new statement), **Send Money**, **Receive
    Money** and **Internal Transfer**: these three open the payments of the
    journal of that kind, where **Create** records a new one.

    .. help-if:: module = account_bank_statement_import

       On a bank journal also **Import Statement**.

  * *Reconciliation*: **Reconcile** (*Nothing to Reconcile* when every line
    is matched) and **Reconciliation Models** (*Adviser* only), the
    predefined counterparts proposed by the reconciliation, e.g. the bank
    fees.

* Miscellaneous journals:

  * *View*: **Journal Entries** and **Entries to Review**; both list the
    entries of the journal.
  * *New*: **Journal Entry**.
  * *Operations*: **Post All Entries**; see *FAQ* to post the draft entries.

In developer mode *View* also lists the **Journal Items** of the journal.
At the bottom, for the *Adviser* access right only, **☆ Favorite** adds or
removes the journal from the favorites (see *Suggestions for search*) and
**Settings** opens the journal form.
