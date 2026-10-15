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

    .. help-include:: common_part.rst

    .. help-inherit:: other_module.partner
       :section: usage
       :position: after

       RST added after the section labelled "usage"

    .. help-question:: How do I add a tag?

       Use the :field:`Tags <category_id>` field.

    .. help-question::
       :auto:

``:when:`` shows the page only when the open record (its selection and boolean
fields) or the menu (its ``default_<field>`` context keys) match: conditions
``field = value``, ``field != value``, several values joined by comma, several
conditions joined by ``and``. When the value is unknown the page is not used,
e.g. ``move_type != entry`` keeps the invoice help away from the journal
entries, which share the invoice form.

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
