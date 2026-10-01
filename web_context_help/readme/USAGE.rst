Press the |sos| button in the control panel. Pages are looked up by view xmlid,
then by model and view type, then by model; otherwise an automatic page lists
the fields help.

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

::

    .. help-page:: partner
       :title: Partners
       :model: res.partner
       :view: base.view_partner_form
       :view-type: form

    .. help-include:: common_part.rst

    .. help-inherit:: other_module.partner
       :section: usage
       :position: after

       RST added after the section labelled "usage"

    .. help-question:: How do I add a tag?

       Use the :field:`Tags <category_id>` field.

    .. help-question::
       :auto:

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
