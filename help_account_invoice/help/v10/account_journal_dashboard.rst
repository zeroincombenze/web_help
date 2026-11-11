.. help-page:: account_journal_dashboard
   :title: Accounting Dashboard
   :model: account.journal
   :view: account.account_journal_dashboard_kanban_view
   :view-type: kanban
   :priority: 96

Accounting Dashboard
====================

.. _description:

Description
-----------

Click on button **Ready** for help about how to use this help; click on
button **FAQ** for the most common solved questions.

.. help-if:: module != account_accountant

   The dashboard opened by **Invoicing ‣ Dashboard**.

.. help-if:: module = account_accountant

   The dashboard opened by **Accounting ‣ Dashboard**.

It shows a card for each journal of your current company; only the users
with the *Accountant* or *Adviser* access right see it. Each card shows the
:field:`journal name <name>`, which opens the documents of the journal, and
the :field:`type <type>`: *Sale*, *Purchase*, *Cash*, *Bank* or
*Miscellaneous*. Cards cannot be created here: the journals are set up in the
configuration, see *How to set up*.

.. help-include:: account_journal_dashboard_cards.rst

.. help-include:: account_journal_dashboard_search.rst

.. help-include:: account_journal_dashboard_configure.rst

.. _report:

Report and export file
----------------------

* The dashboard prints nothing and has no export: open the documents from a
  card (**More ‣ View**) and print or export them from their list.
* **More ‣ Reports ‣ Invoices Analysis** on a sales card, **Bills Analysis**
  on a purchase card (*Adviser* only), opens the analysis of the invoices as
  pivot or graph.
* The charts of the cards are for display only: move the mouse over a bar or a
  point to read its amount.

.. help-include:: account_journal_dashboard_example.rst

.. _faq:

FAQ
---

Click on button **Topic** to return to the specific help page.

.. help-question:: Why don't I see the Dashboard menu?

   The menu is for the *Accountant* and *Adviser* access rights only; with
   *Billing* the invoices are reached from the *Sales* and *Purchases* menus.
   The administrator sets the access right of each user in **Settings ‣ Users
   ‣ Users**, field *Accounting & Finance*.

.. help-question:: Why is a journal missing from the dashboard?

   The dashboard opens with the *Favorites* filter, which shows only the
   journals marked with the ★ star. Remove the filter from the search bar to
   see all of them. The dashboard shows only the journals of your current
   company: change company in the top bar to see the others.

.. help-question:: Why is the dashboard empty?

   No chart of accounts is installed yet, so there are no journals: the empty
   dashboard shows a link to choose the chart of accounts of your country.

.. help-question:: Why are Balance in GL and Latest Statement different?

   *Balance in GL* is the balance of the bank account in the accounts,
   *Latest Statement* the ending balance of the last statement. They differ
   while some statement lines are still to be reconciled (**Reconcile**), or
   when entries were written on the bank account outside the statements.

.. help-question:: Why don't I see Favorite and Settings on the card?

   They are at the bottom of the **More** menu, for the *Adviser* access right
   only.

.. help-question:: How do I post all the draft entries of a journal?

   Open **More ‣ View ‣ Journal Entries** on the card, choose the *Unposted*
   filter, select the entries with the check boxes and use **Action ‣ Post
   Journal Entries**.

.. _footer:

Footer
------

Page created on 2026-11-01 16:38 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
