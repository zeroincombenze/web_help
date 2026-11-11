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

.. help-if:: module != accountant

   The dashboard opened by **Invoicing ‣ Dashboard**.

.. help-if:: module = accountant

   The dashboard opened by **Accounting ‣ Dashboard**.

It shows a card for each journal of the selected companies. Each card shows
the :field:`journal name <name>`, which opens the documents of the journal,
and, when several companies are selected, the company of the journal. Its
:field:`type <type>` (*Sales*, *Purchase*, *Bank*, *Cash*, *Credit Card* or
*Miscellaneous*) decides the buttons, the figures and the chart of the card.
Cards cannot be created here: the journals are set up in the configuration,
see *How to set up*.

A journal with no documents yet shows a short hint, e.g. *Connect your bank.
Match invoices automatically.*, and its chart is drawn grey with *Sample
data*. You can also drop files on a card: invoices or bills on a sales or
purchase card, statement files on a bank card, attachments on a
miscellaneous card.

.. help-include:: account_journal_dashboard_cards.rst

.. help-include:: account_journal_dashboard_search.rst

.. help-include:: account_journal_dashboard_configure.rst

.. _report:

Report and export file
----------------------

* The dashboard prints nothing and has no export: open the documents from a
  card (**⋮ ‣ View**) and print or export them from their list.
* **⋮ ‣ Reporting ‣ Invoices Analysis** on a sales card, **Bills Analysis** on
  a purchase card, opens the analysis of the invoices as pivot or graph.
* The charts of the cards are for display only: move the mouse over a bar or a
  point to read its amount.

.. help-include:: account_journal_dashboard_example.rst

.. _faq:

FAQ
---

Click on button **Topic** to return to the specific help page.

.. help-question:: Why don't I see the Dashboard menu?

   .. help-if:: module != account_accountant

      With the Invoicing app only, the menu is shown only to users with the
      technical right *Show Full Accounting Features*: the administrator sets
      it in developer mode in **Settings ‣ Users & Companies ‣ Users**, tab
      *Access Rights*. Without it the invoices are reached from the
      *Customers* and *Vendors* menus.

   .. help-if:: module = account_accountant

      The menu needs the *Invoicing & Banks* or *Administrator* access right:
      the administrator sets it in **Settings ‣ Users & Companies ‣ Users**,
      field *Invoicing*. With *Invoicing* the invoices are reached from the
      *Customers* and *Vendors* menus.

.. help-question:: Why is a journal missing from the dashboard?

   The dashboard opens with the *Favorites* filter, which shows only the
   journals marked with the ★ star. Remove the filter from the search bar to
   see all of them. The dashboard shows only the journals of the selected
   companies: tick the other companies in the company switcher of the top bar.
   An archived journal appears only with the *Archived* filter.

.. help-question:: Why is the dashboard empty?

   No chart of accounts is installed yet, so there are no journals: the empty
   dashboard shows a link to browse the charts of accounts of the available
   countries.

.. help-question:: Why are Balance and Last Statement different?

   *Balance* is the balance of the bank transactions of the journal, *Last
   Statement* the ending balance of the last statement. They differ while
   some transactions are not yet in a statement, e.g. the ones imported or
   written after the last statement.

.. help-question:: What do Misc. Operations, Unhashed entries and Irregular Sequences mean?

   *Misc. Operations* are entries written directly on the bank account, not
   coming from a bank transaction nor from a payment, after the last
   statement; usually they are mistakes to check. *Irregular Sequences*
   warns that some numbers of the journal are missing or out of order since
   the last lock date, because of draft, cancelled or deleted documents.
   *Unhashed entries* warns that, on a journal with the inalterability hash,
   some posted entries are not secured yet. Click the warning to list the
   entries concerned.

.. help-question:: Why don't I see the star and Configuration in the ⋮ menu?

   They are at the bottom of the **⋮** menu, for the *Administrator* access
   right only.

.. help-question:: How do I post all the draft entries of a journal?

   On a miscellaneous card use **⋮ ‣ Operations ‣ Post All Entries**: the
   *Confirm Entries* window posts every draft entry of the journal. On the
   other cards open the documents from **⋮ ‣ View**, choose the *Draft*
   filter, select the documents and use **Actions ‣ Confirm Entries**.

.. _footer:

Footer
------

Page created on 2026-11-01 21:09 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
