.. help-page:: home
   :title: Help

Ready help
==========

.. _developer_mode:

Activate developer mode
-----------------------

In some menus, you are prompted to "Activate developer mode." This mode
reveals certain menus and functions that are otherwise hidden.

.. image:: /web_context_help/static/description/devel_mode.png
   :alt: Activate developer mode
   :width: 100%

.. _list_search:

Finding, filtering and grouping a list
--------------------------------------

Every list has a search bar at the top right, to find, filter and group its
records.

.. help-version:: >=17

   .. image:: /web_context_help/static/description/search_bar.png
      :alt: Search bar
      :width: 100%

.. _search_bar:

Searching
~~~~~~~~~

Type a value in the search box: a drop-down proposes the fields where to look
for it, e.g. *Search Customer for: Rossi*. Choose one with the arrow keys and
Enter, or with a click; the small arrow next to a field lists the matching
records, to pick exactly one of them. The plain search uses the *contains*
operator, so upper and lower case do not matter.

Every search becomes a box (a *facet*) inside the search bar: remove it with
its **×** or with Backspace. Searches on the same field are joined by *or*,
searches on different fields by *and*.

.. _several_words:

Searching several words
~~~~~~~~~~~~~~~~~~~~~~~

Sometimes the text to find has two or more words. Suppose you are looking for
*Mario Rossi*, without knowing whether he was registered as *Mario Rossi* or
as *Rossi Mario*, and that the contacts are:

#. Dr. Rossi Mario
#. Mario De Rossi
#. Rossi Forniture
#. Rossi e Bianchi
#. Mario Bianchi

Searching ``Rossi`` finds the contacts 1 to 4, *Rossi Forniture* and *Rossi e
Bianchi* included. Adding a second search ``Mario`` does not narrow the list:
it shows all five contacts.

This is how Odoo joins several searches: searches on the same field are
joined by *or* (the box in the search bar shows *Rossi or Mario*), searches on
different fields by *and*. ``Rossi`` and ``Mario`` are searched in the same
field, so Odoo shows the contacts with *Rossi* or with *Mario*.

There are two ways to narrow the search.

**1. A custom filter with "and".** The most precise way, but it takes some
typing:

.. help-version:: >=17

   in **Filters ‣ Add Custom Filter** write a rule *Name contains Rossi* and a
   second rule *Name contains Mario*, choose *Match all of the following
   rules* and press **Add**.

.. help-version:: <17

   the conditions of a single custom filter are joined by *or*, so apply two
   custom filters: **Filters ‣ Add Custom Filter**, condition *Name contains
   Rossi*, **Apply**; then again **Add Custom Filter**, condition *Name
   contains Mario*, **Apply**. Two custom filters are joined by *and*.

The result is the contacts 1 and 2.

**2. The wildcard.** Quicker to type, it takes advantage of the *or* between
searches on the same field: search ``Rossi%Mario`` and then ``Mario%Rossi``.
The ``%`` (percent) stands for any text, see *Searching with the wildcard*:
the first search finds the names with *Rossi* before *Mario* (contact 1), the
second the names with *Mario* before *Rossi* (contact 2). Note that
``Mario%Rossi`` finds both *Mario Rossi* (not in the list) and *Mario De
Rossi*.

The ``_`` (underscore) stands for exactly one character: ``Ross_`` finds
*Rossi*, *Rosso* and *Rossa*. For the same reason a ``%`` or ``_`` typed in a
search is never taken as a plain character.

.. help-include:: search_wildcard.rst

Filters, groups and favorites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. help-version:: >=17

   The toggle **▾** at the right of the search box opens three columns:
   **Filters**, **Group By** and **Favorites**.

.. help-version:: <17

   The **Filters**, **Group By** and **Favorites** buttons under the search box
   open their menus.

* **Filters**: ready-made selections of the records. Filters of the same group
  (between two separator lines) are joined by *or*, filters of different groups
  by *and*. **Add Custom Filter** builds a condition with a field, an operator
  and a value\ :version:`>=17|, joined by *any* or *all* of the rules, and can
  include the archived records`. Archived records are hidden: the *Archived*
  filter, when present, shows them.
* **Group By**: groups the rows by a field, e.g. by customer; choosing a
  second grouping divides every group again. Click a group heading to open or
  close it: it shows the number of records and the totals of the number
  columns. :version:`<=10|**Add custom group**;*|**Add Custom Group**` groups
  by any field.
* **Favorites**: **Save current search** keeps the search, filters and
  groups under a name; :version:`<=10|*Use by default*;*|*Default filter*`
  applies it every time the menu opens and
  :version:`<=10|*Share with all users*;*|*Shared*` makes it visible to
  everyone.

.. _navigation:

Moving around
~~~~~~~~~~~~~

* **Breadcrumbs**, at the top left: the path of the views opened, e.g.
  *Sales Orders / S00042*. Click a step to go back to it; better than the Back
  button of the browser, which may lose the search.
* **View switcher**, at the top right: shows the same records as kanban
  cards, list or, where available, calendar, pivot and graph, keeping the
  search.
* **Pager**, next to the view switcher: *1-80 / 97* means records 1 to 80
  of 97. The arrows go to the next or previous page; click the numbers to
  change them, e.g. *1-200* to see more rows. In a form the pager shows the
  position of the record, and the arrows open the next or previous record of
  the list.

.. help-version:: >=13

   Some lists have a side panel on the left (e.g. the categories of the
   **Apps**): a click on an item filters the list.

.. _import_export:

Import and Export data
----------------------

Every list can be saved to a spreadsheet file and filled from one: to take
the data elsewhere, to load many records at once or to change many records
together.

.. _export:

Export
~~~~~~

#. Open the list, search and filter the records you need and tick them. The
   box in the header ticks all the records of the page\ :version:`<=12|, and
   with it all the records found are exported;*|, then **Select all** ticks
   all the records found`.
#. Press :version:`<=16|**Action ‣ Export**;*|**⚙ Actions ‣ Export**`.
   :version:`>=17|With no record ticked, **⚙ ‣ Export All** (the gear next to
   the view title) exports all the records found.`
#. Choose the fields: search them in *Available fields* and add them to
   *Fields to export*, then drag them to change their order. A field list used
   often can be saved and picked again:
   :version:`<=12|**Save fields list**;*|**Template ‣ New template**`.
#. Tick :version:`<=12|*Import-Compatible Export*;*|*I want to update data
   (import-compatible export)*` when the file will be imported back: only the
   fields that can be imported are offered, and the record identifier
   (*External ID*) is exported too.
#. Choose the format, :version:`<=10|*CSV* or *Excel*;*|*XLSX* or *CSV*`, and
   press **Export**: the browser downloads the file.

.. _import:

Import
~~~~~~

#. Open the list where the records go and press
   :version:`<=12|the **Import** button next to **Create**;13-16|**Favorites ‣
   Import records**;*|**⚙ ‣ Import records** (the gear next to the view
   title)`.
#. Press :version:`<=10|**Load File**;*|**Upload Data File**` and choose the
   file, :version:`<=10|CSV or Excel;*|XLSX, XLS, ODS or CSV`. For a CSV file
   check the encoding, the separator and the text delimiter
   (:version:`<=10|options;*|**Formatting**`): Odoo expects commas and double
   quotes.
#. Odoo matches every column of the file with a field by its title: check the
   matches and choose the field of the columns not recognised; a column with no
   field is not imported. The fields of the related records are shown by
   *Show fields of relation fields (advanced)*.
#. Press :version:`<=10|**Validate**;*|**Test**`: Odoo checks the whole file
   without saving anything and lists the errors with their lines. Correct the
   file and load it again.
#. Press **Import**.

⚠ **Caution!** An import cannot be undone. To find the records just imported,
group or filter the list by *Created on*.

Good to know:

* **Changing many records**: export them as import-compatible, change the
  columns in the spreadsheet, keep the *External ID* column (``id``) and
  import the file back. The rows with an ID update their record, the rows with
  no ID create new records: an import without IDs repeated twice creates every
  record twice.
* **Related records** (customer, country, product, …) are found by their name,
  or by their identifier in a column titled e.g. ``Country/External ID``. Import
  the related records first.
* **Dates** are read without doubts in the form ``YYYY-MM-DD`` (e.g.
  ``2026-03-01``); in an Excel file use real date cells.
* **Large files** may stop for a time-out: split them into smaller files.

Help on help
============

.. _description:

Welcome
-------

This is the help of your Odoo. Press **Summary** in the header to see every
help page available: the list grows with each help module installed (e.g.
invoices, sale orders, payment terms).

.. _usage:

Help of the current view
------------------------

Press the |sos| button in the control panel of any view: the help window opens
the page explaining that view. The Odoo tab stays usable and, with
*Follow Odoo* checked, the help window follows you from view to view.
When a view has no page, an automatic page lists the help of its fields.

.. |sos| unicode:: U+1F6DF

.. _navigate:

Moving inside the help
----------------------

A long page starts with its **Contents**: click a title to jump to that
section. Inside the text:

* a link to another page or section opens it in the help window; the Back
  button of the browser returns to the previous page;
* a field name shown as a link (e.g. on the **Fields** page) highlights that
  field in the Odoo tab, so you can see where it is in the form.

.. _buttons:

The buttons in the header
-------------------------

The header shows only the buttons that make sense for the page you are
reading:

* **Follow Odoo**: checked, the help window changes page every time you open
  another view in Odoo; unchecked, it stays on the page you are reading, e.g.
  to keep it open while you work elsewhere.
* **Topic**: on a page, it appears when the Odoo view has a page other than
  the one you are reading (e.g. after opening the **Summary**, or with *Follow
  Odoo* unchecked): it brings you back to the help of the current view. On the
  **FAQ**, **Example** and **Fields** pages it brings you back to the page they
  belong to.
* **Ready**: opens this page, the general help, from any page.
* **Loose help**: shown on the pages written for a special case, e.g. one type
  of order: it opens the general help of the same record.
* **Example**: opens a worked example of the page, on a page of its own.
* **FAQ**: opens the frequently asked questions of the page, see below.
* **Fields**: lists every field of the form with its explanation; click a
  field name to highlight it in Odoo.
* **Summary**: lists all the help pages, grouped by module; click a title to
  open it.
* **Edit**: help editors only, see *Changing this page*.

.. _faq_button:

Frequently asked questions (FAQ)
--------------------------------

The questions about a page are kept apart, so the page stays short: the
**FAQ** button appears only when the page has questions. Press it to open
them on a page of their own: every question is a box with the question in bold
and its answer underneath. Scroll the list, or type a word of your doubt in the
find box (e.g. *rebuild*) to go straight to the question that answers it. Press
**Topic** to go back to the page.

This page has its FAQ too: try the **FAQ** button.

.. _search:

Finding text inside help
------------------------

The box in the header finds text in the page, like the browser Ctrl+F (which
moves to this box). Case and accents are ignored; text in quotes is searched
as an exact phrase. With more words, the places where they are near each other
are shown first; when there is none, the counter shows *any word* and every
word is found on its own.

The counter shows the current match and the total, e.g. *2/5*. Press Enter or
▼ for the next match, Shift+Enter or ▲ for the previous one, Esc to clear the
search. The search looks only in the page you are reading: to search the
questions, open the **FAQ** first.

.. _configure:

Changing this page
------------------

The help editors see the **Edit** button in the header: it opens the page in
*Help > Help Editor > Help Pages*, where its content can be adapted to your
company, this page included. An edited page keeps your version when the
module is upgraded. A help editor of level **User** edits a copy of the pages
of priority 64 or more, e.g. this page: **Edit** creates the copy, with the
default priority, and opens it.

.. _faq:

Questions
---------

Click on button **Topic** to return to the specific help page.

.. help-question:: Pressing the help button, no window opens. Why?

   The browser has blocked the pop-up window: allow pop-ups for the Odoo
   site (the icon at the right of the address bar) and press the button again.

.. help-question:: The help window shows a page that is not about my view. Why?

   *Follow Odoo* is unchecked, or you have opened another page from the help.
   Press **Topic** to go back to the help of the current view, or check
   *Follow Odoo*.

.. help-question:: Why don't I see the FAQ button?

   The page you are reading has no questions. The **FAQ**, **Example**,
   **Fields** and **Loose help** buttons appear only on the pages that have
   them.

.. help-question:: The page lists only the fields of the form. Why?

   Nobody has written a page for this view yet: the help shows an automatic
   page with the explanation of its fields.

.. _footer:

Footer
------

Page created on 2026-10-14 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
