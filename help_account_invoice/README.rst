=================================================
|icon| Help for invoices/Aiuto fatture 10.0.1.0.4
=================================================

**Context help pages for customer invoices and vendor bills**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/10.0/help_account_invoice/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| Context help pages for the invoice list and form, shown by web_context_help:
customer invoices, vendor bills and their credit notes.

The model depends on the Odoo version: before 13.0 the pages follow
``account.invoice``, from 13.0 ``account.move``, where an invoice is a journal
entry with an invoice type.

Every page follows the standard layout of web_context_help:

* **Contents**: the sections of the page, built by the help window
* **Description**: what invoices are, their statuses and the main fields
* **How to insert a new record** (form): step-by-step guide to create, validate
  and send an invoice or a vendor bill
* **Invoicing from sale order** (form, only when the Sales app is installed):
  invoicing policy, invoice status, regular invoices and down payments,
  several orders at once
* **Suggestions for search** (list): menus, search, filters and groupings
* **How to update a record** (form): changing an invoice, registering payments,
  credit notes, cancelling and deleting
* **How to set up**: the Invoicing settings, journals, payment terms and taxes
* **Report and export file**: the invoice PDF, sending, the invoice analysis
  and the export of the invoices to a file
* **Example** button: common cases, e.g. partial payments or correcting a
  posted invoice
* **FAQ** button and **Footer**

A page for the Accounting Dashboard (journal kanban) explains the cards of
the journals, their buttons and figures, and the **More** menu.

Pages are in English and Italian, with the menus, buttons and statuses of the
running Odoo version.


|it| Pagine di aiuto contestuale per la lista e la maschera delle fatture, mostrate
da web_context_help: fatture clienti, fatture fornitori e le loro note di
credito.

Il modello dipende dalla versione di Odoo: prima della 13.0 le pagine seguono
``account.invoice``, dalla 13.0 ``account.move``, dove una fattura è una
registrazione contabile di tipo fattura.

Ogni pagina segue la struttura standard di web_context_help:

* **Indice**: le sezioni della pagina, costruito dalla finestra di aiuto
* **Descrizione**: cosa sono le fatture, i loro stati e i campi principali
* **Come inserire un nuovo record** (maschera): guida passo passo per creare,
  validare e inviare una fattura o una fattura fornitore
* **Fatturazione da ordine di vendita** (maschera, solo con l'app Vendite
  installata): politica di fatturazione, stato fattura, fatture normali e
  anticipi, più ordini insieme
* **Suggerimenti per la ricerca** (lista): menu, ricerca, filtri e
  raggruppamenti
* **Come modificare un record** (maschera): modificare una fattura, registrare
  i pagamenti, note di credito, annullamento ed eliminazione
* **Come configurare**: le impostazioni di Fatturazione, registri, termini di
  pagamento e imposte
* **Stampe ed esportazione**: il PDF della fattura, l'invio, l'analisi fatture
  e l'esportazione delle fatture in un file
* Pulsante **Esempio**: casi comuni, ad es. pagamenti parziali o correzione di
  una fattura registrata
* Pulsante **FAQ** e **Piè di pagina**

Una pagina per la Bacheca della contabilità (kanban dei registri) spiega le
schede dei registri, i loro pulsanti e importi, e il menu **Altro**.

Le pagine sono in inglese e in italiano, con i menu, i pulsanti e gli stati
della versione di Odoo in uso.


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/10.0/help_account_invoice/static/description/


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

10.0.1.0.4 (2026-11-01)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Invoice form: new section Invoicing from sale order (Fatturazione da ordine di vendita), shown only when the sale module is installed
* [NEW] Accounting Dashboard (journal kanban) help page: cards of sale, purchase, bank, cash and miscellaneous journals, the More menu, search, set up and FAQ

10.0.1.0.3 (2026-10-31)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Help pages in the standard layout: sections renamed How to insert a new record, How to update a record, Suggestions for search, How to set up, Report and export file (Italian titles too); the Report section explains how to export the records to a file

10.0.1.0.2 (2026-10-29)
~~~~~~~~~~~~~~~~~~~~~~~

* [IMP] Migrated from 18.0 to 10.0 (requires web_context_help 10.0.1.0.7)

10.0.0
~~~~~~

* [IMP] Help pages declared with :priority: 96, the priority of the module pages: the last fallback after the pages of the administrator (requires web_context_help 18.0.1.0.6)

10.0.0
~~~~~~

* [NEW] Help pages for invoice list and form, English and Italian, Odoo 10 to 18 (account.invoice before 13.0, account.move since 13.0, journal entries excluded)



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

Last Update / Ultimo aggiornamento: 2026-11-01

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
