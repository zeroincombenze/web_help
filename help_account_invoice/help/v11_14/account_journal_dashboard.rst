.. help-version:: 12

   .. help-page:: account_journal_dashboard
      :title: Accounting Overview
      :model: account.journal
      :view: account.account_journal_dashboard_kanban_view
      :view-type: kanban
      :priority: 96

Accounting Overview
===================

.. _description:

Description
-----------

The dashboard opened by **Invoicing ‣ Overview**. The menu is shown only to
the users with *Show Full Accounting Features* (see *FAQ*). It shows a card
for each journal of your current company. Each card shows the
:field:`journal name <name>`, which opens the documents of the journal, and
the :field:`type <type>`: *Sale*, *Purchase*, *Cash*, *Bank* or
*Miscellaneous*. Cards cannot be created here: the journals are set up in the
configuration, see *How to set up*.

Administrators also see, above the cards, the configuration tips panel with
the steps *Company Data*, *Bank Account*, *Fiscal Year* and *Chart of
Accounts*; the ✕ at its top right hides it for good, after confirming with
**Remove**.

.. help-include:: account_journal_dashboard_cards.rst

.. help-include:: account_journal_dashboard_search.rst

.. help-include:: account_journal_dashboard_configure.rst

.. _report:

Report and export file
----------------------

* The dashboard prints nothing and has no export: open the documents from a
  card (**⋮ ‣ View**) and print or export them from their list.
* **⋮ ‣ Reporting ‣ Invoices Analysis** on a sales card, **Bills Analysis**
  on a purchase card (*Billing Manager* only), opens the analysis of the
  invoices as graph or pivot.
* The charts of the cards are for display only: move the mouse over a bar or a
  point to read its amount.

.. help-include:: account_journal_dashboard_example.rst

.. _faq:

FAQ
---

.. help-question:: Why don't I see the Overview menu?

   The menu is shown only to the users with *Show Full Accounting Features*;
   without it the invoices are reached from the *Customers* and *Vendors*
   menus. The administrator activates the developer mode (**Activate the
   developer mode** in *Settings*), opens the user in **Settings ‣ Users &
   Companies ‣ Users** and ticks *Show Full Accounting Features* in the
   *Technical Settings* section.

.. help-question:: Why is a journal missing from the dashboard?

   The dashboard opens with the *Favorites* filter, which shows only the
   journals marked with the ★ star. Remove the filter from the search bar to
   see all of them. The dashboard shows only the journals of your current
   company: change company in the top bar to see the others. An archived
   journal is shown only by the *Archived* filter.

.. help-question:: Why is the dashboard empty?

   No chart of accounts is installed yet, so there are no journals: the empty
   dashboard shows the link **Browse available countries.** to choose the
   chart of accounts of your country.

.. help-question:: Why are Balance in General Ledger and Latest Statement different?

   *Balance in General Ledger* is the balance of the posted entries on the
   accounts of the journal, *Latest Statement* the ending balance of the last
   statement. They differ while some statement lines are still to be
   reconciled (**Reconcile N Items**), or when entries were written on the
   bank account outside the statements.

.. help-question:: Why does the bank card always show Configure?

   **Configure** is shown while the :field:`Bank Feeds
   <bank_statements_source>` of the journal is *Undefined Yet*.

   Without a module that imports the statement files *Undefined Yet* is the
   only choice, so the button stays; it opens *Create a Bank Account*, the
   set up of the bank account.

   .. help-if:: module = account_bank_statement_import

      When a statement file format is installed (e.g. OFX or CAMT), *Bank
      Feeds* also offers *Import(…)* followed by the formats: choose it, or
      import a statement file with **Import**, and the button disappears.

.. help-question:: Why don't I see the star, the colors and Settings on the card?

   They are at the bottom of the **⋮** menu, for the *Billing Manager*
   access right only.

.. help-question:: How do I post all the draft entries of a journal?

   Do not use **⋮ ‣ Operations ‣ Post All Entries**: in this version it does
   not pass the entries of the journal to the confirmation, which ends with
   an error or posts an unrelated draft entry. Instead open **⋮ ‣ View ‣
   Entries to Review** on the card (the *Unposted* entries of the journal),
   select the entries with the check boxes and use **Action ‣ Post Journal
   Entries**, then confirm with **Post Journal Entries**.

.. _footer:

Footer
------

Page created on 2026-11-01 16:55 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
