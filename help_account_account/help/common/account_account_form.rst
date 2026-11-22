.. help-page:: account_account_form
   :title: Account
   :model: account.account
   :view: account.view_account_form
   :view-type: form
   :priority: 96

Account
=======

.. _description:

Description
-----------

Click on button [`Ready`] for help about how to use this help; click on
button [`FAQ`] for the most common solved questions.

An account is a ledger account of the chart of accounts: every journal item
of an invoice, a payment or a journal entry is posted on an account, and the
reports (balance sheet, profit and loss, tax report) add up the accounts.

* The :field:`code <code>`, with the :field:`account name <name>`, identifies
  the account; the code accepts letters, digits and dots only.
* The :field:`type <account_type>` tells what the account is (receivable,
  bank and cash, income, expense ...) and decides how the reports and the
  closing of the fiscal year use it.
* :field:`Default Taxes <tax_ids>` are proposed on the entries posted on the
  account; :field:`Tags <tag_ids>` group the accounts for custom reports.
* :field:`Allowed Journals <allowed_journal_ids>` limit the journals where
  the account can be used; empty means all the journals.
* :field:`Deprecated <deprecated>` hides the account from the choices and
  forbids new entries.
* The button **Balance** at the top right opens the journal items of the
  account; the button **Taxes** lists the taxes that post on it.

.. help-include:: account_account_new.rst

.. help-include:: account_account_update.rst

.. help-include:: account_account_cancel.rst

.. help-include:: account_account_configure.rst

.. help-include:: account_account_report.rst

.. help-include:: account_account_example.rst

.. _faq:

FAQ
---

Click on button [`Topic`] to return to the specific help page.

.. help-question:: Why can't I save the account code?

   The code may contain only letters, digits and dots, and it must be unique
   in the company (and in its parent and branch companies): choose another
   code. With several companies the code must be set for each of them.

.. help-question:: Why can't I turn off Allow Reconciliation?

   A receivable or payable account must be reconcilable. For the other
   accounts, the switch cannot be turned off while partial reconciliations are
   pending on its journal items. Bank and cash, credit card, off-balance,
   equity, income and expense accounts are never reconcilable.

.. help-question:: Why can't I change the type of the account?

   An account used as default account of a bank journal, or of a sales or
   purchase journal, cannot become *Receivable* or *Payable*. Only one account
   per company can be of type *Current Year Earnings*.

.. help-question:: Why can't I deprecate or delete the account?

   See *How to archive or delete record*: an account with journal items, an
   account of a fiscal position mapping or of a tax distribution cannot be
   deleted, and one of a tax distribution cannot be deprecated.

.. help-question:: Why can't I create an account from a field of a journal or a move?

   Accounts are created only from the Chart of Accounts menu.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-11-22 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
