=================================================
|icon| Context help/Aiuto contestuale 10.0.1.0.15
=================================================

**Context help button**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/10.0/web_context_help/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| Adds a |sos| button to the control panel of every view: it opens the help of the
current view in a separate window, so the Odoo tab stays usable.

The help pages are on two levels:

* **Standard level**: the pages supplied by the help modules (e.g.
  help_account_invoice, help_sale_order), which show the help of the standard
  Odoo modules. They have a priority of 64 or more (96 by default), so they are
  the last fallback, always available
* **Customized level**: the pages built for the custom modules, or the copies
  of the standard pages changed to fit the company. They have a priority lower
  than 64 (32 by default), and 1 is the highest: a customized page is shown in
  place of the standard page of the same view. Editors write them in *Help ‣
  Help Editor ‣ Help Pages*, or in the ``help/`` directory of the custom module

* Administrators can edit a help page from the Odoo interface, with the editor
  of the page form: in the database a page is HTML, so no RST is needed. The
  edited version is kept when the module is upgraded, and a warning appears
  when the RST source changes afterwards, so the edit can be checked against
  the new source
* The source of a help page is an RST file, written by the developer in the
  ``help/`` directory of the module (one file per language); the server turns
  it into the HTML page of the database, when it starts and when the source
  changes
* Images are added to the RST source (``image`` directive, file in the
  ``static/`` of a module), videos by the editors in the HTML page; the guided
  tours need the *Context help tours* module (``web_context_help_tour``)
* The help window follows the navigation (*Follow Odoo*), highlights the fields
  named by the page and can start a guided tour
* Questions are answered by a full-text search over the help sections; every
  question is logged for the administrator
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

Le pagine di aiuto sono su due livelli:

* **Livello standard**: le pagine fornite dai moduli di aiuto (ad es.
  help_account_invoice, help_sale_order), che mostrano l'aiuto dei moduli
  standard di Odoo. Hanno una priorità di 64 o più (96 per default), quindi sono
  l'ultima alternativa, sempre disponibile
* **Livello personalizzato**: le pagine costruite per i moduli custom, o le
  copie delle pagine standard modificate per adattarle all'azienda. Hanno una
  priorità minore di 64 (32 per default), dove 1 è la più alta: una pagina
  personalizzata è mostrata al posto della pagina standard della stessa vista.
  Gli editor le scrivono in *Aiuto ‣ Editor dell'aiuto ‣ Pagine di aiuto*, o
  nella cartella ``help/`` del modulo custom

* Gli amministratori possono modificare una pagina di aiuto dall'interfaccia
  di Odoo, con l'editor della scheda della pagina: nel database una pagina è
  HTML, quindi non serve RST. La versione modificata è mantenuta quando il
  modulo è aggiornato, e un avviso compare quando in seguito cambia la
  sorgente RST, così la modifica può essere verificata rispetto alla nuova
  sorgente
* La sorgente di una pagina di aiuto è un file RST, scritto dallo sviluppatore
  nella cartella ``help/`` del modulo (un file per lingua); il server lo
  trasforma nella pagina HTML del database, all'avvio e quando la sorgente
  cambia
* Le immagini si aggiungono alla sorgente RST (direttiva ``image``, file nella
  ``static/`` di un modulo), i video dagli editor nella pagina HTML; i tour
  guidati richiedono il modulo *Context help tours*
  (``web_context_help_tour``)
* La finestra di aiuto segue la navigazione (*Segui Odoo*), evidenzia i campi
  citati dalla pagina e può avviare un tour guidato
* Le domande hanno risposta da una ricerca testuale nelle sezioni di aiuto;
  ogni domanda è registrata per l'amministratore
* Una pagina può essere scelta in base a un campo del record aperto, anche
  many2one: con il ``:when:`` della sua sorgente RST o con regole impostate
  dall'amministratore, ad es. un aiuto diverso per ogni tipo di ordine di vendita
* Le viste senza pagina ricevono una pagina automatica costruita dall'aiuto dei campi
* Il menu **Aiuto** apre la pagina iniziale dell'aiuto; il suo pulsante
  **Sommario** elenca le pagine di ogni modulo di aiuto installato (ad es.
  help_account_invoice, help_sale_order)

.. |sos| unicode:: U+1F6DF


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/10.0/web_context_help/static/description/


Configuration | Configurazione
------------------------------

No configuration is needed. Pages are rebuilt at server start when a help source
changes; a help editor can force it with **Rebuild all pages** in *Help > Help
Editor > Help Pages*.

Help level of the users
~~~~~~~~~~~~~~~~~~~~~~~

Every internal user reads the help. The help level of a user is set in the user
form (*Settings > Users*, field **Context Help** in the *Application* section):

* empty: no edit, the help is only read;
* **No help**: the help is not shown to the user: no |sos| button in the
  views, no **Help** menu, and the help pages are refused;
* **User**: edits the help pages of priority lower than 64 and their rules.
  Editing a page of priority 64 or more, e.g. a page of a module (96), creates a
  copy of it with the default priority (32), and the copy is edited: being of
  higher priority, it is shown in place of the original;
* **System**: edits all the help pages.

The levels **User** and **System** need no administrator rights: they get the
*Help Editor* section in the left bar of the **Help** menu (pages, rules,
questions asked) and the [`Edit`] button of the help window.

The field sets the level of the administrators too: they start as **System**
(when the module is installed, or already had it before this version), and can
be lowered to **User**, to no edit or to **No help**. A user made administrator
later gets no help level by default.

Videos
~~~~~~

The videos inserted in the help pages are read from the directory of the system
parameter ``web_help_video_path`` (default ``~/Video``, the home of the user
running Odoo), subdirectories included; change it in *Settings > Technical >
System Parameters*.



Usage | Utilizzo
----------------

The **Help** menu, at the top of the menu tree, opens the help home page in
the help window. The **Summary** button in the header lists, grouped by module,
the pages of every installed help module; **Ready** goes back to the home page.
Users allowed to change the help pages also see **Edit**, which opens the page
in the backend: the home page itself can be adapted like any other page.
In the page form, the **Insert video** button lists the videos of the video
directory: the chosen one is inserted, as a player started by a click, at the
end of the page or after the paragraph holding the text written in *After the
text*. In developer mode the **</>** button of the editor shows the HTML code
of the page, where a video can be moved or removed.

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

The *Example* and *FAQ* sections of a page and the fields help of its model
are shown on their own pages, opened by the [`Example`], [`FAQ`] and [`Fields`]
buttons in the help window header; the |sos| button goes back to the page
(on the Example, FAQ and Fields pages it is labelled [`Topic`]). The questions built by
``help-question`` ``:auto:`` are left to the **Fields** page.

Moving from page to page of the help window, the [`Topic`] button goes back to
the help page of the view open in Odoo; it is hidden when that page (or its
Example / FAQ / Fields page) is the one shown.

Writing help for a module: put RST files in ``help/common/`` or in the
directory of a group of Odoo versions (``help/v10``, ``help/v11_14``,
``help/v15``, ``help/v16_20``); a group file overrides the common one with the
same name. Italian twins are named ``page.it_IT.rst``.

Standard layout: every page has these sections, in this order, with their
label and title; some apply only to the form or only to the list view (a
kanban view follows the list rules):

* *Contents*: table of contents, built by the help window, not written in RST;
  it lists the sections left on the page, footer excepted; the sections of a
  page with several parts (titles of first level) are grouped by part
* ``description`` *Description*: summary of the view / model; its first
  paragraph is always "Click on button ``[`Ready`]`` for help about how to use
  this help; click on button ``[`FAQ`]`` for the most common solved questions."
* ``new_record`` *How to insert a new record*: in the form, steps to insert a
  record; in list / kanban, a brief text about the [`New`] button ([`Create`]
  up to Odoo 15)
* ``search`` *Suggestions for search*: list / kanban only, how to find, filter
  and group
* ``update_record`` *How to update a record*: in the form, steps to update a
  record; in list / kanban, a brief text: click on a line (list) or on a card
  (kanban) to open its form
* ``cancel`` *How to cancel or delete record* when the model has a
  ``state`` field, else *How to archive or delete record*: form and list,
  steps to cancel (or archive) a record, restore it and delete it, with the
  conditions that forbid each step
* ``configure`` *How to set up*: settings and configuration
* ``report`` *Report and export file*: prints, pdf attachment, export
* ``example`` *Example*: useful examples, on their own page opened by the
  [`Example`] button
* ``faq`` *FAQ*: ``help-question`` blocks, on their own page opened by the
  [`FAQ`] button; the first paragraph, before the first question, is always
  "Click on button ``[`Topic`]`` to return to the specific help page."
* ``footer`` *Footer*: date and time of page creation and copyright notice,
  not in the table of contents

A section that does not apply keeps one line saying so.

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
a page: field of the page model (selection, boolean or many2one), *is* or *is not*, and the values (selection: their keys comma separated, e.g.
``draft, sent``, listed in *Allowed values*), the checkbox (boolean) or the
record (many2one). A page with rules is shown when one of them is met, and the
``:when:`` of its source too.

The rules apply to the **Clear cut** pages only: a clear cut page is shown only
when one of its rules is met. Every page has a **Priority**, 1 being the
highest. The clear cut pages are checked first, in priority order: the first
one with a rule met is shown. With no rule met, the general page (not clear
cut, its rules ignored) with the highest priority is shown. The pages of the
administrator get 32 by default, the pages built from the modules 96: these are
the last fallback, always available. The priority of a module page is set by
the ``:priority:`` option of its ``help-page``, 96 when missing.

A clear cut page, or a page of priority 64 or less, shows the [`Loose help`]
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

    Press :version:`16|**Create and View Invoice**;17|**Create Draft Invoice**;>=18|**Create Draft**`.

Conditions: ``16``, ``16-18``, ``>=17``, ``>17``, ``<=16``, ``<17``, or a star
(the star: any version), several joined by comma (``10,16``). The role shows the text of
the first matching condition, inline markup allowed, roles not allowed; write
``\ `` before the role when it is glued to the previous word.
Roles ``:field:`` and ``:tour:`` highlight a field or run a tour in the Odoo tab.

A button label written between ``[`` and ``]`` with backquotes,
``[`Save`]``, is shown as a button, the label inside a frame. Inside
``:version:`` the backquotes are escaped:
``:version:`<16|[\`Create\`];>=16|[\`New\`]```. It cannot be nested in
Italic and bold are written with one or two stars around the words
(*italic*, **bold**); in a code block the stars stay as written.
The help pages write every button this way; menu paths (``**Sales ‣
Orders**``), tabs, menu items after ‣ and titles stay in bold.

Text that makes sense only with another module goes in ``help-if``: it is
shown only when the module is installed, or the model exists. The pages are
rebuilt when a module or model named by a condition is installed or removed,
in whatever order the modules are installed.

::

    .. help-if:: module = sale

       Invoicing from sale order
       -------------------------

       RST shown only when sale is installed (sections allowed)

    .. help-if:: model = sale.order and module != purchase

       RST shown when sale.order exists and purchase is not installed

Conditions: ``module`` or ``model``, ``=`` (any of the names joined by comma
is installed / exists) or ``!=`` (none of them), several joined by ``and``.

Images and videos
~~~~~~~~~~~~~~~~~

**Images** are written in the RST source of the page with the ``image``
directive. The file is in the ``static/`` directory of a module, e.g.
``static/description/`` of the module, and the path is the URL of the
file, which starts with the technical name of the module::

    .. image:: /web_context_help/static/description/devel_mode.png
       :alt: Activate developer mode
       :width: 100%

Put a description in ``:alt:``, and ``:width: 100%`` to fit the image to the
help window. The image is part of the source, so every language of the page
shows it. An image can also be added to the page in the Odoo page editor, as
in any other HTML field.

**Videos** are not written in RST: a help editor inserts them in the HTML page
from the Odoo interface. The video files are not in the module but in a
directory of the server, set by the ``web_help_video_path`` system parameter
(see *Configuration*), so the same files must be copied to every server where
the page is shown. In the page form press the **Insert video** button: the
list shows the videos of the video directory, and the chosen one is inserted
at the end of the page or after the paragraph holding the text written in
*After the text*. The player starts at a click, and the page keeps the video
when the module is upgraded, like any other edit of the page.

**Guided tours** are written in the RST source of the page too (see below) but
need another module: they are shown only when *Context help tours*
(``web_context_help_tour``) is installed.

Guided tours
~~~~~~~~~~~~

``help-tour`` writes a guided tour in the page, where it is needed, e.g. in
*How to insert a new record*. With the *Context help tours* module
(``web_context_help_tour``) installed, the help window shows a button: pressed,
it plays the steps in the Odoo tab, one at a time, dimming the screen around
the element of the step, with the **Previous**, **Next** and **Stop**
buttons. Without that module the tour is not shown. The steps are written in
the page, so the Italian twin has its own text and ``help-version`` /
``help-if`` work inside the tour too.

::

    .. help-tour:: res_partner_new
       :label: Show me how to create a contact

       .. help-step:: new
          :click:

          Press **New** to open an empty contact form.

       .. help-step:: field:name
          :position: right

          Type the name: it is the only required field.

``:label:`` is the text of the button, *Show me how* when missing.
Targets of ``help-step``: ``field:<field name>`` (the field and its label;
the column in a list), ``button:<button name>``, ``tab:<notebook page
name>``, ``menu:<menu xmlid>``, ``css:<selector>``, or ``new``, ``save``,
``discard``, ``search``, ``filters``, ``actions`` (gear menu),
``breadcrumb``, ``statusbar``. ``:click:``: **Next** presses the target for
the user, e.g. **New**; ``:position:`` places the popover (``auto``,
``top``, ``bottom``, ``left``, ``right``). A step whose target is not on
screen waits for it: the user opens the screen, or does what the previous
step asks. The targets are those of the Odoo version: put the tour in a
``help-version`` block of the versions it was checked on.

.. |sos| unicode:: U+1F6DF



Getting started | Primi passi
=============================

|Try Me|


Prerequisites | Prerequisiti
----------------------------

* python 2.7+ (best 2.7.5+)
* postgresql 9.2+ (best 9.5)

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
| $HOME/10.0 |
+----------------------------------------------------------------------------+

::

    # Odoo repository installation; OCB repository must be installed
    deploy_odoo clone -r web_help -b 10.0 -G zero -p $HOME/10.0
    # Upgrade virtual environment
    vem amend $HOME/10.0/venv_odoo



Upgrade | Aggiornamento
-----------------------

::

    deploy_odoo update -r web_help -b 10.0 -G zero -p $HOME/10.0
    vem amend $HOME/10.0/venv_odoo
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

10.0.1.0.15 (2026-11-22)
~~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Documentation: how to add images (image directive, file in the static directory of a module) and videos (page editor), and the guided tours that need the web_context_help_tour module
* [IMP] Module category changed from Hidden/Tools to Tutorial, as the apps of odoo.com
* [IMP] Description: the help pages are on two levels, standard (supplied by the help modules, priority 64 or more) and customized (priority lower than 64)
* [QUA] Test coverage 91% (1486: 135+1351) [0 TestPoints] - quality rating 51 (target 100)
* [NEW] Help level *No help* (user form, field Context Help): the help is hidden to the user, with no Help button, no Help menu and no help pages (the User and System levels keep the help)
* [FIX] Code cleanup for flake8 (unused loop variables, loop variable bound in a lambda)
* [IMP] Documentation: buttons written as [`Label`] and the |sos| button, as the help pages

10.0.1.0.14 (2026-11-22)
~~~~~~~~~~~~~~~~~~~~~~~~

* [QUA] Test coverage 91% (1446: 133+1313) [0 TestPoints] - quality rating 51 (target 100)
* [IMP] Help window: text column limited to 860px; on windows 1200px wide or more the Contents box hangs in the right margin, always in view while scrolling (before it was above the text)

10.0.1.0.13 (2026-11-15)
~~~~~~~~~~~~~~~~~~~~~~~~

* [NEW] Guided tours: help-tour / help-step directives write the steps in the page, shown as a button by web_context_help_tour; the help window sends the steps to the Odoo tab and its find box skips them
* [IMP] Tour button: while its tour plays it reads *Return to record view* and brings the Odoo tab back; the original label returns when the tour ends
* [IMP] Standard layout: new section cancel, *How to cancel or delete record* (model with state) or *How to archive or delete record*, after How to update a record
* [IMP] Standard layout: list and kanban pages have the sections How to insert a new record (brief: button New / Create) and How to update a record (brief: click on a line or a card)
* [NEW] Button frames: [`Save`] in the RST shows the label as a button, inside a frame, in the help window and in the page editor
* [QUA] Test coverage 91% (1446: 133+1313) [0 TestPoints] - quality rating 51 (target 100)
* [IMP] Help home and help editor pages: buttons written [`Label`], shown inside a frame; the mandatory Ready / FAQ / Topic sentences use it too

10.0.1.0.12 (2026-11-08)
~~~~~~~~~~~~~~~~~~~~~~~~

* [FIX] Odoo tab loaded in the help window (expired session, login): the help pages no more replace the Odoo views, e.g. the Invoicing dashboard
* [FIX] Help pages with automatic FAQ (help-question :auto:) not parsed on Python 2 ("ascii codec can't decode") when a field string or help holds non-ascii bytes
* [IMP] Help on help: how to move inside the help, the header buttons, the FAQ, the find box; FAQ of the main page
* [IMP] Help pages: the Help pages page starts with the hint to the Ready and FAQ buttons; every FAQ page starts with the hint to the Topic button; the rules are in USAGE
* [IMP] Help edit authorization in 3 levels, field Context Help of the user form: empty (no edit), User (new: edits the pages of priority lower than 64; editing a page of priority 64 or more edits a copy of it with the default priority) and System (edits all the pages, the former Help Editor group); the administrators are no more System by default: the field sets their level too, the existing ones keep System

10.0.1.0.11 (2026-11-01)
~~~~~~~~~~~~~~~~~~~~~~~~

* [QUA] Test coverage 91% (1318: 119+1199) [0 TestPoints] - quality rating 51 (target 100)
* [IMP] Help sources: new ``help-if`` directive: content shown only when a module is installed or a model exists (``module = sale``, ``model != sale.order``); the pages are rebuilt when a module or model named by a condition is installed or removed

10.0.1.0.10 (2026-10-31)
~~~~~~~~~~~~~~~~~~~~~~~~

* [QUA] Test coverage 91% (1259: 116+1143) [0 TestPoints] - quality rating 51 (target 100)
* [IMP] Help pages: standard layout: Contents, Description, How to insert a new record (form only), Suggestions for search (list and kanban only), How to update a record (form only), How to set up, Report and export file; Example and FAQ on their own pages, footer last
* [IMP] Help window: the page starts with its table of contents (Indice in Italian), built from its sections, footer excepted
* [IMP] Help window: new **Example** button (Esempio in Italian): the Example section is shown on its own page, like the FAQ
* [IMP] Help window: Font Awesome icons on the header buttons: Topic (anchor), Ready (life saver), FAQ (question), Loose help (globe), Example (eye), Fields (map), Summary (table), Edit (edit)
* [IMP] Help window: on the Example, FAQ and Fields pages the button back to the page is labelled **Topic** (Argomento in Italian), and the Loose help button is not shown
* [QUA] HTML escape from markupsafe only: no more import of the deprecated cgi module
* [IMP] Help window: new **Topic** button (Argomento in Italian), back to the help page of the current Odoo view after moving to other pages; hidden when that page, or its FAQ / Fields page, is shown

10.0.1.0.9 (2026-10-30)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] List pages no longer get the "Searching with the wildcard" text at the end of their How to search section: the wildcard search is explained once, in the "Ready help" part of the help home page
* [FIX] Documentation: the Usage section is shown again in the module page (index.html)
* [IMP] Help window: the Home button is renamed Ready (Pronto in Italian)
* [QUA] Test coverage 90% (1241: 120+1121) [0 TestPoints] - quality rating 51 (target 100)
* [IMP] Help home page: new part "Ready help", before "Help on help", with the chapters "Activate developer mode" (with picture), "Finding, filtering and grouping a list" (search bar picture, searching, searching several words, wildcard search, filters, groups, favorites, breadcrumbs, view switcher and pager) and "Import and Export data" (export, import, updating records by External ID)

10.0.1.0.8 (2026-10-30)
~~~~~~~~~~~~~~~~~~~~~~~

* [QUA] Test coverage 90% (1241: 120+1121) [0 TestPoints] - quality rating 51 (target 100)
* [IMP] Help home page: new chapter "Activate developer mode", with picture, before "Changing this page"

10.0.1.0.7 (2026-10-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Migrated from 18.0 to 10.0: Python 2.7, Odoo 10 ORM, list views as tree and attrs, assets and QWeb templates of the Odoo 10 web client
* [IMP] Odoo 10 adapter of the control panel: the [?] button opens the help of the view shown, the help window follows the views and the records (pager, save), highlights the fields and runs the tours
* [IMP] Odoo 10: the Insert video button of the page form inserts a video of the video directory at the end of the page or after a paragraph, in place of the editor plugin of 18.0
* [IMP] Odoo 10: the selection values of a help rule are written as their keys, comma separated, checked against the allowed values shown in the rule form
* [IMP] Odoo 10: help page of the Help pages form in help/v10
* [IMP] Odoo 10: the Help Editor menus are in the left bar of the Help menu, Odoo 10 having no apps menu; the Help menu still opens the help window
* [FIX] Videos streamed with HTTP range support without the 18.0 Stream class
* [FIX] Page keys quoted in the URLs: a duplicated page (key ending with " (copy)") opens
* [QUA] Test coverage 90% (1241: 120+1121) [0 TestPoints] - quality rating 51 (target 100)
* [FIX] RST engine on Python 2: byte strings accepted, icons out of the basic plane (e.g. U+1F6DF) rendered on narrow builds, global search text copied without the docutils 0.16 system messages

10.0.0
~~~~~~

* [IMP] help-page :when: condition on many2one fields too, the record named by xmlid or id, e.g. type_id = sale_order_type.normal_sale_type
* [IMP] Help rules (Settings ‣ Technical ‣ Context Help ‣ Help Rules, or the Rules tab of a page): the administrator chooses which page is shown by a selection, boolean or many2one field of the record, no RST source needed; several rules of a page are alternatives; in the rule form field, operator and value are shown together
* [IMP] Help lookup by page Priority (1 the highest) and Clear cut flag: the clear cut pages come first, the first one with a rule met is shown; otherwise the general page (not clear cut, its rules ignored) with the highest priority: pages of the administrator (default 32) before the pages of the modules (96), the last fallback; same priority, the page meeting more :when: conditions wins
* [IMP] Help pages created by the administrator are kept by the rebuild of the pages and their sections are built from their content
* [IMP] Help Editor group: writes the help pages, their rules and reads the questions asked, with no administrator rights, from the new Help Editor app; the administrators are help editors too
* [IMP] help-page :priority: option, the priority of a module page (96 when missing)
* [IMP] Help window: Loose help button on a clear cut page or a page of priority 64 or less: opens the general page of priority 64 or more with the highest priority, for the same record (usually the page of the module)
* [FIX] Odoo 18 form views: the help sees the fields of the open record (the form view did not share its record with the control panel), so the :when: conditions and the rules work on the record; the help window follows the record when it is saved or the pager moves to another one
* [FIX] Help pages: Duplicate no longer fails on the duplicate key: the copy key ends with " (copy)" (" (copy 2)" and so on for further copies); the copy has no source file, so it is a page of the administrator kept by the rebuild

10.0.0
~~~~~~

* [IMP] Help pages: Help video button in the floating toolbar of the editor (and /Help video command): inserts a video of the directory set by the system parameter web_help_video_path (default ~/Video), played on click; Backspace or Delete next to a video removes it
* [UPD] Help pages: HTML code view (</>) shown only in developer mode, as in standard Odoo; the custom field widget is removed
* [FIX] Help pages: the Sections of a page edited by the administrator (editor or HTML code view) are rebuilt from its content, so the added headings and text are listed and found by the search; a reset to source rebuilds them too

10.0.0
~~~~~~

* [IMP] Help menu at the top of the menu tree: opens the help home page, editable by the administrator; HTML code view (</>) on the content of the help pages, also without developer mode and as wide as the page
* [IMP] Help window: Summary button, page listing the help pages of every installed help module, each title followed by its view type (list) or (form); Home and Edit buttons
* [FIX] Help window: a malformed lang in the URL (e.g. ?lang=it_IT?debug=1) no longer falls back to the English page



Credits | Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


Authors | Autori
----------------

* `Zeroincombenze srls <https://www.zeroincombenze.it>`__



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

Last Update / Ultimo aggiornamento: 2026-11-22

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-black.png
    :target: https://odoo-community.org/page/development-status
    :alt: 
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
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
