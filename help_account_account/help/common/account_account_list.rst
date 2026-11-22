.. help-page:: account_account_list
   :title: Chart of Accounts
   :model: account.account
   :view: account.view_account_list
   :view-type: list
   :priority: 96

Chart of Accounts
=================

.. _description:

Description
-----------

Click on button [`Ready`] for help about how to use this help; click on
button [`FAQ`] for the most common solved questions.

The chart of accounts: the list of the ledger accounts where the journal items
are posted. Each row shows the :field:`code <code>`, the :field:`account name
<name>`, the :field:`type <account_type>` and the *Allow Reconciliation*
switch; the other columns (group, default taxes, tags, allowed journals, *Non
Trade*) are shown with the toggle at the right of the header. The rows are
sorted by code. The lines can be changed in place, without opening the form.

.. _new_record:

How to insert a new record
--------------------------

Press [`New`] at the top left: an empty line opens at the top of the list,
where you type the code, the name and the type of the account. See the help
of the form for the meaning of the fields and for the other ones.

.. help-include:: account_account_list_search.rst

.. _update_record:

How to update a record
----------------------

Click on a line of the list to change it in place; to see all its fields
press the arrow button at the end of the line (*Open in form view*) and
follow the help of the form.

.. help-include:: account_account_cancel.rst

.. help-include:: account_account_configure.rst

.. help-include:: account_account_report.rst

.. help-include:: account_account_example.rst

.. _faq:

FAQ
---

Click on button [`Topic`] to return to the specific help page.

.. help-question:: Why don't I see some accounts?

   The list opens with the filter *Active Account*, which hides the
   deprecated accounts. Remove the filter to see them all. In a multi-company
   database you see the accounts of the company you are working in: change it
   with the company switcher in the top bar.

.. help-question:: Why don't I see the Chart of Accounts menu?

   The menu **Invoicing ‣ Configuration** is shown to the users with the
   *Accounting / Administrator* access right; the chart of accounts is empty
   until a *Fiscal Localization* package is chosen, see *How to set up*.

.. help-question:: How do I show the default taxes or the tags of the accounts?

   Use the toggle at the right of the column titles and tick *Default Taxes*,
   *Tags*, *Allowed Journals*, *Group* or *Non Trade*.

.. _footer:

Footer
------

Page created on 2026-11-22 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
