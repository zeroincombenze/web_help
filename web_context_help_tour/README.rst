================================================================
|icon| Context help tours/Tour dell'aiuto contestuale 12.0.1.0.0
================================================================

**Guided tours of the context help pages, played in the Odoo tab**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/12.0/web_context_help_tour/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| Guided tours for the context help pages of web_context_help.

A help page writes its mini tours where they are needed, e.g. a tour to
create a record in *How to insert a new record* and a tour to change it in
*How to update a record*. The help window shows each tour as a button;
pressed, the tour plays in the Odoo tab:

* the screen is dimmed around the element of the step (field and its label,
  button, tab, menu) and a pulsing ring shows it;
* a popover explains the step, with **Previous**, **Next** (**Finish** on the
  last step) and **Stop**; **Esc** stops the tour too;
* the dimmed screen still takes the clicks: the user does the work, the tour
  shows where; a step can also press its button for the user, e.g. **New**;
* a step whose element is not on screen waits for it, e.g. until the form
  opens.

The steps are written in RST in the help pages (``help-tour`` and
``help-step`` directives), so every tour has its English and Italian text and
follows the Odoo version, like the rest of the help. Without this module the
tours are not shown.


|it| Tour guidati per le pagine di aiuto contestuale di web_context_help.

Una pagina di aiuto scrive i suoi mini tour dove servono, ad es. un tour per
creare un record in *Come inserire un nuovo record* e un tour per modificarlo
in *Come modificare un record*. La finestra di aiuto mostra ogni tour come un
pulsante; premuto, il tour si svolge nella scheda di Odoo:

* lo schermo è oscurato intorno all'elemento del passo (campo e sua
  etichetta, pulsante, scheda, menu) e un anello pulsante lo indica;
* un fumetto spiega il passo, con **Indietro**, **Avanti** (**Fine**
  all'ultimo passo) e **Interrompi**; anche **Esc** interrompe il tour;
* lo schermo oscurato riceve comunque i clic: l'utente fa il lavoro, il tour
  mostra dove; un passo può anche premere il suo pulsante per l'utente, ad es.
  **Nuovo**;
* un passo il cui elemento non è sullo schermo lo attende, ad es. finché la
  maschera si apre.

I passi sono scritti in RST nelle pagine di aiuto (direttive ``help-tour`` e
``help-step``), quindi ogni tour ha il suo testo inglese e italiano e segue la
versione di Odoo, come il resto dell'aiuto. Senza questo modulo i tour non
sono mostrati.


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/12.0/web_context_help_tour/static/description/


Usage | Utilizzo
----------------

Open the help window with the |sos| button and press the tour button of a
chapter, e.g. **Show me how to create a contact** in the contact help. The
Odoo tab comes to the front and the tour starts:

* read the step and do it, or press **Next** to go on;
* **Previous** goes back one step;
* **Stop**, the **×** of the popover or **Esc** end the tour.

While the tour plays, its button in the help window reads **Return to record
view**: it brings the Odoo tab back. When the tour ends, the button shows its
label again.

A step whose element is not on screen shows *Waiting for this step*: open the
screen it refers to, or do what the previous step asks; the tour goes on by
itself. **Next** skips the step.

To write a tour see *Guided tours* in the usage of web_context_help: the
``help-tour`` directive, its ``help-step`` steps and their targets.

.. |sos| unicode:: U+1F6DF



Getting started | Primi passi
=============================

|Try Me|


Prerequisites | Prerequisiti
----------------------------

* python 3.7
* postgresql 9.6+ (best 10.0+)

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
| $HOME/12.0 |
+----------------------------------------------------------------------------+

::

    # Odoo repository installation; OCB repository must be installed
    deploy_odoo clone -r web_help -b 12.0 -G zero -p $HOME/12.0
    # Upgrade virtual environment
    vem amend $HOME/12.0/venv_odoo



Upgrade | Aggiornamento
-----------------------

::

    deploy_odoo update -r web_help -b 12.0 -G zero -p $HOME/12.0
    vem amend $HOME/12.0/venv_odoo
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

12.0.1.0.0 (2026-11-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [NEW] Tour player of the help-tour tours: dimmed screen around the target, ring, popover with Previous / Next / Stop, waiting for a missing target
* [NEW] The help window is told when the tour ends (Finish, Stop, Esc), so the tour button gets back its label
* [IMP] A press on the tour popover (mouse or Enter on Next) does not close an Odoo dropdown opened by the tour, e.g. the Filters menu; new test of the contact search tour



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
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-12.svg
    :target: https://erp12.zeroincombenze.it
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
