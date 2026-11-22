.. _configure:

How to set up
-------------

* The chart of accounts is in **Invoicing ‣ Configuration ‣ Accounting ‣
  Chart of Accounts**, for the users with the accountant rights.
* **Load the chart of accounts**: open **Invoicing ‣ Configuration ‣
  Settings** (administrators), block *Fiscal Localization*, choose the
  *Package* of your country, e.g. *Italy*, and save. Odoo loads the accounts,
  the taxes, the fiscal positions and the journals of the country. With
  accounting entries already posted the package cannot be changed.
  The block is shown on the main company only.
* **Code**: letters, digits and dots, unique in the company. The first digits
  tell the group (the *Group* field is computed from the beginning of the code
  and can be shown in the list). Use codes of the same length for the same level.
* **Type**: choose the one that fits: *Receivable*, *Bank and Cash*, *Current
  Assets*, *Non-current Assets*, *Prepayments*, *Fixed Assets*, *Payable*,
  *Credit Card*, *Current Liabilities*, *Non-current Liabilities*, *Equity*,
  *Current Year Earnings*, *Income*, *Other Income*, *Expenses*,
  *Depreciation*, *Cost of Revenue*, *Off-Balance Sheet*. The type is used by
  the country reports and by the closing of the fiscal year: accounts of
  income and expenses are reset to zero each year, the others bring the
  balance forward.
* **Receivable and Payable** accounts are the ones of the customers and the
  vendors, set on the partner (tab **Invoicing**, group *Accounting Entries*,
  *Account Receivable* and *Account Payable*). The switch *Non Trade*, shown for them, tells they are
  not for trade receivables or payables (e.g. the VAT treasury account).
  Only one account per company can be *Current Year Earnings*.
* **Allow Reconciliation**: on for the accounts whose journal items are
  matched (customers, vendors, outstanding payments, transit accounts); it
  cannot be on for the types *Bank and Cash*, *Credit Card* and *Off-Balance
  Sheet*, and is always on for *Receivable* and *Payable*; income, expense
  and equity accounts are never reconcilable.
* **Default Taxes**: taxes proposed on the journal items of the account,
  e.g. VAT on the income accounts; not for the off-balance accounts.
* **Tags**: tags of applicability *Accounts*, to group accounts in custom
  reports; the legal reports of the country need the ones loaded by its
  package.
* **Allowed Journals**: the journals that can use the account. If a journal
  item of the account is already in another journal, the limit is refused.
* **Account Currency** (with several currencies): a currency cannot be set on
  an account that has journal items in another foreign currency.
* **Companies**: an account can be shared by several companies of the same
  tree (not for *Bank and Cash*); the code of every company is in the
  **Mapping** tab.

.. help-if:: module = l10n_it

   **Italian chart of accounts (l10n_it)**

   The package *Italy*, in *Fiscal Localization*, loads a chart of accounts of
   four-digit codes arranged as the Italian balance sheet: e.g. *1101 Planting
   costs* (*Costi di impianto*), *1501 Customer receivables* (*Crediti verso i
   clienti*), *2501 Accounts payable* (*Debiti v/fornitori*), *3101* for the
   income and *4101* for the expenses. The accounts 1501 and 2501 are the
   receivable and the payable accounts, with *Allow Reconciliation* on; the
   accounts 2605 and 2607 (VAT treasury and VAT split payment) are payable
   *Non Trade*. Almost every account has a tag of the Italian balance sheet, e.g. *Fixed
   assets*, *Current assets*, *Debts*, *Shareholders' Equity*; the tags are
   used by the Italian reports, do not remove them. The names are translated
   in Italian when the language of the user is *Italian*.
   Add your own accounts with the same code length, next to a similar
   account: if you leave the type empty, the type and the tags are copied from
   the account with the code just before.
