**Sales and purchase journals**

* **New** creates a new customer invoice (sales) or vendor bill (purchase) in
  this journal. On a purchase card **Upload** loads the PDF of a bill and
  creates a draft bill from it; **New** is next to it.
* *N To Validate*: the documents still in draft, and their total.
* *N Unpaid* (sales) or *N To Pay* (purchase): the posted documents not fully
  paid yet, and the amount still due. Credit notes are subtracted.
* *N Late*: the part of them whose due date is passed.
* *N To Check*: the posted documents not yet marked as checked.
* Click a figure to list its documents.
* The bar chart shows the amount still due of the posted documents, by week
  of their due date: *Due* (older), the previous week, *This Week*, the next
  two weeks and *Not Due* (later).

**Bank, cash and credit card journals**

* **Transactions** opens the transactions of the account. On a bank journal
  not set up yet (no account number, no bank feed chosen) **Bank Setup** sets
  up the bank account.

  .. help-if:: module = account_accountant

     **N to reconcile** appears when transactions are still to be matched
     with invoices, payments or accounts: it opens the bank reconciliation.

* *Balance*: the balance of the transactions of the account. *Last
  Statement*: the ending balance of the last statement, shown only when it
  differs from *Balance*.
* *Payments*: the posted payments of the journal not yet matched with a bank
  transaction, and their total; click to list them.
* *Misc. Operations*: entries written directly on the bank account after the
  last statement; see *FAQ*.

  .. help-if:: module = account_accountant

     *N to check*: the transactions not yet marked as checked.

  .. help-if:: module = account_check_printing

     *N Checks to print*: the checks waiting to be printed; click to list
     them.

* The line chart shows the balance of the account over the last 30 days.

**Miscellaneous journals**

* **New** creates a journal entry in this journal.
* The next activities of the journal, e.g. the tax returns to file, and *N To
  Check*: the posted entries not yet marked as checked.

On every card *Irregular Sequences* or *Unhashed entries*, in orange, warn
about the numbering or the inalterability of the journal; see *FAQ*.

**The ⋮ menu**

**⋮**, at the top right of a card when the mouse is on it, opens its menu, in
columns.

* Sales and purchase journals:

  * *View*: **Invoices** or **Bills**, **Credit Notes** or **Refund**,
    **Journal Items**.

    .. help-if:: module = account_accountant

       Also **Payments Matching**: the invoices and payments of the partners
       still to be matched.

  * *New*: **Invoice** or **Bill**, **Credit Note** or **Refund**; on a
    sales card also **Upload Invoices**, which creates invoices from files.
  * *Reporting*: **Invoices Analysis** or **Bills Analysis**.

* Bank, cash and credit card journals:

  * *View*: **Statements** (bank and credit card) or **Cash Registers**
    (cash), **Payments** (all the payments of the journal).

    .. help-if:: module = account_accountant

       Also **Transactions**: the bank transactions as a list.

  * *New*: **Customer Payment** and **Vendor Payment**.

    .. help-if:: module = account_bank_statement_import

       On a bank journal also **Import File**, which loads the statement
       file downloaded from the bank.

* Miscellaneous journals:

  * *View*: **Journal Entries**, **Entries to Review** (the draft entries)
    and, in developer mode, **Journal Items**.
  * *New*: **Journal Entry**.
  * *Operations*: **Post All Entries**; see *FAQ*.

At the bottom of the menu the colours of the card and, for the
*Administrator* access right only, **☆** adds or removes the journal from the
favorites (see *Suggestions for search*) and **Configuration** opens the
journal form.
