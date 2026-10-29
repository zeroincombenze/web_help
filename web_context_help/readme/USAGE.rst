The **Help** menu, at the top of the menu tree, opens the help home page in
the help window. The **Summary** button in the header lists, grouped by module,
the pages of every installed help module; **Home** goes back to the home page.
Users allowed to change the help pages also see **Edit**, which opens the page
in the backend: the home page itself can be adapted like any other page.
In the editor, the film button of the floating toolbar (or the */Help video*
command) lists the videos of the video directory: the chosen one is inserted
after the current paragraph, as a player started by a click. To remove a
video, press Backspace in the line after it or Delete in the line before it. In developer mode
the **</>** button shows the HTML code of the page.

Press the |sos| button in the control panel. Pages are looked up by view xmlid,
then by model and view type, then by model; otherwise an automatic page lists
the fields help.

The box in the help window header finds text in the page, like the browser
Ctrl+F (which focuses it). Case and accents are ignored, line breaks and bold or
linked words too. With several words, words of 1-2 letters are ignored and only the places where all of them are
within 12 words in the same paragraph are shown; when there is no such place,
every occurrence of every word is shown and the counter says *any word*. Text
in quotes (``"draft invoice"``) is searched as an exact phrase.
**Enter** / ▼ and **Shift+Enter** / ▲ go to the next / previous match,
**Esc** clears the search.

The *FAQ* section of a page and the fields help of its model are shown on
their own pages, opened by the **FAQ** and **Fields** buttons in the help
window header; the **Help** button goes back to the page. The questions built by
``help-question`` ``:auto:`` are left to the **Fields** page.

Writing help for a module: put RST files in ``help/common/`` or in the
directory of a group of Odoo versions (``help/v10``, ``help/v11_14``,
``help/v15``, ``help/v16_20``); a group file overrides the common one with the
same name. Italian twins are named ``page.it_IT.rst``.

Every page has these sections, in this order, with their label:
``description`` (summary of the view / model),
``new_record`` (form only: steps to insert a record),
``update_record`` (form only: steps to update a record),
``search`` (list only: how to search and group by),
``configure`` (how to configure the model),
``report`` (how to show the report or the pdf attachment),
``example`` (useful examples),
``faq`` (frequently asked questions, ``help-question`` blocks),
``footer`` (date and time of page creation and copyright notice).
A section that does not apply keeps one line saying so.
Every list page gets the *Searching with the wildcard* text of
web_context_help (``help/common/search_wildcard.rst``) at the end of its
``search`` section: do not write it in the module; a page section labelled
``wildcard`` is replaced by it.

::

    .. help-page:: partner
       :title: Partners
       :model: res.partner
       :view: base.view_partner_form
       :view-type: form
       :when: is_company = True
       :priority: 96

    .. help-include:: common_part.rst

    .. help-inherit:: other_module.partner
       :section: usage
       :position: after

       RST added after the section labelled "usage"

    .. help-question:: How do I add a tag?

       Use the :field:`Tags <category_id>` field.

    .. help-question::
       :auto:

``:when:`` shows the page only when the open record (its selection, boolean
and many2one fields) or the menu (its ``default_<field>`` context keys) match:
conditions ``field = value``, ``field != value``, several values joined by
comma, several conditions joined by ``and``. When the value is unknown the page
is not used, e.g. ``move_type != entry`` keeps the invoice help away from the
journal entries, which share the invoice form. A many2one value is the xmlid
or the id of the record, e.g. ``type_id = sale_order_type.normal_sale_type``;
``False`` means empty. Among the pages of the same priority that can be shown,
the one meeting more conditions wins: a page with ``:when:`` beats the page
without it.

Rules
~~~~~

Without writing RST, a help editor chooses which page is shown from
*Help ‣ Help Editor ‣ Help Rules* or from the **Rules** tab of
a page: field of the page model (selection, boolean or many2one), *is* or *is
not*, and the values (selection), the checkbox (boolean) or the record
(many2one). A page with rules is shown when one of them is met, and the
``:when:`` of its source too.

The rules apply to the **Clear cut** pages only: a clear cut page is shown only
when one of its rules is met. Every page has a **Priority**, 1 being the
highest. The clear cut pages are checked first, in priority order: the first
one with a rule met is shown. With no rule met, the general page (not clear
cut, its rules ignored) with the highest priority is shown. The pages of the
administrator get 32 by default, the pages built from the modules 96: these are
the last fallback, always available. The priority of a module page is set by
the ``:priority:`` option of its ``help-page``, 96 when missing.

A clear cut page, or a page of priority 64 or less, shows the **Loose help**
button in the help window: it opens the general page of priority 64 or more
with the highest priority, for the same record, usually the page of the
module.

Example: sale orders with a different help for each OCA *sale_order_type*.
Create a page per type (*Help Pages ‣ New*: key, title, model ``sale.order``,
view type ``form``, content), check *Clear cut* and add to it the rule
*Type is <the type>*.
Orders of the other types keep the standard sale order help. A page created
this way, or by **Duplicate** of the standard page (key followed by " (copy)"),
has no source: it is kept by the rebuild of the pages.

``:position:`` is one of ``before``, ``after``, ``replace``, ``remove``.
``:auto:`` builds the questions from the fields help of the page model.

A page shows only the text of the running Odoo version: put version specific
blocks in ``help-version`` and version specific words in the ``:version:``
role; the version directories remain for whole files that differ.

::

    .. help-version:: >=17

       RST shown on Odoo 17 and later (sections allowed)

    Press :version:`16|**Create and View Invoice**;17|**Create Draft Invoice**;*|**Create Draft**`.

Conditions: ``16``, ``16-18``, ``>=17``, ``>17``, ``<=16``, ``<17``, ``*``
(any version), several joined by comma (``10,16``). The role shows the text of
the first matching condition, inline markup allowed, roles not allowed; write
``\ `` before the role when it is glued to the previous word.
Roles ``:field:`` and ``:tour:`` highlight a field or run a tour in the Odoo tab.

.. |sos| unicode:: U+1F6DF
