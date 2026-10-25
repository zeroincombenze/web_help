================================================
|icon| Context help/Aiuto contestuale 18.0.1.0.6
================================================

**Context help button, pages written in RST by each module**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/18.0/web_context_help/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| Adds a |sos| button to the control panel of every view: it opens the help of the
current view in a separate window, so the Odoo tab stays usable.

* Help pages are written in RST by each module, in its ``help/`` directory
* The help window follows the navigation (*Follow Odoo*), highlights the fields
  named by the page and can start a guided tour
* Questions are answered by a full-text search over the help sections; every
  question is logged for the administrator
* Administrators can edit a page; the edited version survives the upgrades and
  a warning appears when the original source changes
* A page can be chosen by a field of the open record, many2one included: by
  the ``:when:`` of its RST source or by rules set by the administrator, e.g. a
  different sale order help for each order type
* Views without a page get an automatic page built from the fields help
* The **Help** menu opens the help home page; its **Summary** button lists the
  pages of every installed help module (e.g. help_account_invoice,
  help_sale_order)

.. |sos| unicode:: U+1F6DF


|it| Aggiunge un pulsante |sos| al pannello di controllo di ogni vista: apre l'aiuto
della vista corrente in una finestra separata, così la scheda di Odoo resta
utilizzabile.

* Le pagine di aiuto sono scritte in RST da ogni modulo, nella cartella ``help/``
* La finestra di aiuto segue la navigazione (*Segui Odoo*), evidenzia i campi
  citati dalla pagina e può avviare un tour guidato
* Le domande hanno risposta da una ricerca testuale nelle sezioni di aiuto;
  ogni domanda è registrata per l'amministratore
* Gli amministratori possono modificare una pagina; la versione modificata
  sopravvive agli aggiornamenti e un avviso compare quando cambia la sorgente
* Una pagina può essere scelta in base a un campo del record aperto, anche
  many2one: con il ``:when:`` della sua sorgente RST o con regole impostate
  dall'amministratore, ad es. un aiuto diverso per ogni tipo di ordine di vendita
* Le viste senza pagina ricevono una pagina automatica costruita dall'aiuto dei campi
* Il menu **Aiuto** apre la pagina iniziale dell'aiuto; il suo pulsante
  **Sommario** elenca le pagine di ogni modulo di aiuto installato (ad es.
  help_account_invoice, help_sale_order)

.. |sos| unicode:: U+1F6DF


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/18.0/web_context_help/static/description/


Configuration | Configurazione
------------------------------

No configuration is needed. Pages are rebuilt at server start when a help
source changes; a help editor can force it with **Rebuild all pages** in
*Help Editor > Help Pages*.

Every internal user reads the help. The help pages and their rules are written
by the users of the group **Help Editor** (*Settings > Users*, section
*Context Help*), with no administrator rights: they get the *Help Editor* app
(pages, rules, questions asked) and the **Edit** button of the help window.
The administrators are help editors too.

The videos inserted in the help pages are read from the directory of the system
parameter ``web_help_video_path`` (default ``~/Video``, the home of the user
running Odoo), subdirectories included; change it in *Settings > Technical >
System Parameters*.



Usage | Utilizzo
----------------

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
*Help Editor ‣ Help Rules* or from the **Rules** tab of
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



Getting started | Primi passi
=============================

|Try Me|


Prerequisites | Prerequisiti
----------------------------

::

    cd $HOME
    # Follow statements activate deployment, installation and upgrade tools
    cd $HOME
    [[ ! -d ./tools ]] && git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -pUT
    source $HOME/devel/activate_tools



Installation | Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instructions are just an  | Istruzioni di esempio valide solo per    |
| example; use on Linux CentOS 7+ | distribuzioni Linux CentOS 7+,           |
| Ubuntu 14+ and Debian 8+        | Ubuntu 14+ e Debian 8+                   |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://zeroincombenze-tools.readthedocs.io/>`__ |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| $HOME/18.0 |
+----------------------------------------------------------------------------+

::

    # Odoo repository installation; OCB repository must be installed
    deploy_odoo clone -r web_help -b 18.0 -G zero -p $HOME/18.0
    # Upgrade virtual environment
    vem amend $HOME/18.0/venv_odoo



Upgrade | Aggiornamento
-----------------------

::

    deploy_odoo update -r web_help -b 18.0 -G zero -p $HOME/18.0
    vem amend $HOME/18.0/venv_odoo
    # Adjust following statements as per your system
    sudo systemctl restart odoo



Support | Supporto
------------------

|Zeroincombenze| This module is supported by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



Get involved | Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/web_help/issues>`_.

In case of trouble, please check there if your issue has already been reported.



Proposals for enhancement
-------------------------

|en| If you have a proposal to change this module, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare questo modulo, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.



ChangeLog History | Cronologia modifiche
----------------------------------------

18.0.1.0.6 (2026-10-22)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] help-page :when: condition on many2one fields too, the record named by xmlid or id, e.g. type_id = sale_order_type.normal_sale_type
* [IMP] Help rules (Settings ‣ Technical ‣ Context Help ‣ Help Rules, or the Rules tab of a page): the administrator chooses which page is shown by a selection, boolean or many2one field of the record, no RST source needed; several rules of a page are alternatives; in the rule form field, operator and value are shown together
* [IMP] Help lookup by page Priority (1 the highest) and Clear cut flag: the clear cut pages come first, the first one with a rule met is shown; otherwise the general page (not clear cut, its rules ignored) with the highest priority: pages of the administrator (default 32) before the pages of the modules (96), the last fallback; same priority, the page meeting more :when: conditions wins
* [IMP] Help pages created by the administrator are kept by the rebuild of the pages and their sections are built from their content
* [IMP] Help Editor group: writes the help pages, their rules and reads the questions asked, with no administrator rights, from the new Help Editor app; the administrators are help editors too
* [IMP] help-page :priority: option, the priority of a module page (96 when missing)
* [IMP] Help window: Loose help button on a clear cut page or a page of priority 64 or less: opens the general page of priority 64 or more with the highest priority, for the same record (usually the page of the module)
* [FIX] Odoo 18 form views: the help sees the fields of the open record (the form view did not share its record with the control panel), so the :when: conditions and the rules work on the record; the help window follows the record when it is saved or the pager moves to another one
* [FIX] Help pages: Duplicate no longer fails on the duplicate key: the copy key ends with " (copy)" (" (copy 2)" and so on for further copies); the copy has no source file, so it is a page of the administrator kept by the rebuild

18.0.1.0.5 (2026-10-14)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages: Help video button in the floating toolbar of the editor (and /Help video command): inserts a video of the directory set by the system parameter web_help_video_path (default ~/Video), played on click; Backspace or Delete next to a video removes it
* [UPD] Help pages: HTML code view (</>) shown only in developer mode, as in standard Odoo; the custom field widget is removed
* [FIX] Help pages: the Sections of a page edited by the administrator (editor or HTML code view) are rebuilt from its content, so the added headings and text are listed and found by the search; a reset to source rebuilds them too

18.0.1.0.4 (2026-10-14)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help menu at the top of the menu tree: opens the help home page, editable by the administrator; HTML code view (</>) on the content of the help pages, also without developer mode and as wide as the page
* [IMP] Help window: Summary button, page listing the help pages of every installed help module, each title followed by its view type (list) or (form); Home and Edit buttons
* [FIX] Help window: a malformed lang in the URL (e.g. ?lang=it_IT?debug=1) no longer falls back to the English page

18.0.1.0.3 (2026-10-02)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help window: find in page box, like the browser Ctrl+F, with previous / next buttons; several words found when near each other, phrase in quotes
* [IMP] Help window: FAQ and fields help on their own pages, opened by the FAQ and Fields buttons
* [IMP] Every list page gets the global wildcard search text at the end of its How to search section
* [IMP] help-page :when: condition on the open record or the menu context, e.g. move_type != entry
* [FIX] RST: a :field: role wrapped on two lines was printed as text; a :version: role with a stray ";" now fails on every version instead of cutting the text

18.0.1.0.2 (2026-10-01)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Version specific help: help-version directive and :version: role, pages built for the running Odoo version

18.0.1.0.1 (2026-09-27)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Field labels highlighted too, dialogs keep the help of the main view

18.0.1.0.0 (2026-09-27)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Migrated from 16.0: list views, invisible expressions, Odoo 18 control panel adapter

18.0.0
~~~~~~

* [NEW] Context help button, help pages built from the RST sources of each module



Credits | Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* Zeroincombenze srls <False>
* `SHS-AV s.r.l. <https://www.zeroincombenze.it>`__



Contributors | Partecipanti
---------------------------

* `Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>`__



Maintainer | Manutenzione
-------------------------

* `Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>`__



----------------

|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://www.zeroincombenze.it/>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://www.zeroincombenze.it/>`__ è progettata per le esigenze del mercato italiano.


|
|

This module is part of web_help project.

Last Update / Ultimo aggiornamento: 2026-10-25

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-black.png
    :target: https://odoo-community.org/page/development-status
    :alt: 
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-18.svg
    :target: https://erp18.zeroincombenze.it
    :alt: Try Me
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/Desktoptelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md
