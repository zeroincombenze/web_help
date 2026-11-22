==================================================================
|icon| Help for chart of accounts/Aiuto piano dei conti 18.0.1.0.0
==================================================================

**Context help pages for the chart of accounts**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/18.0/help_account_account/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| Context help pages for the chart of accounts list and form
(``account.account``), shown by web_context_help.

The chart of accounts is the list of the ledger accounts where every journal
item is posted. The pages explain how to set it up:

* the *Fiscal Localization* package that loads the chart of the country, e.g.
  the Italian one of ``l10n_it`` (four-digit codes, receivable and payable
  accounts, tags of the balance sheet)
* the account *Code* and *Type* and what the type decides
* *Allow Reconciliation* for receivable, payable and other accounts
* the *Default Taxes*, the *Tags* and the *Allowed Journals* of an account

Every page follows the standard layout of web_context_help:

* **Contents**: the sections of the page, built by the help window
* **Description**: what the chart of accounts is and what each field means
* **How to insert a new record**: step-by-step guide to add an account
* **Suggestions for search** (list): menu, search, filters and groupings
* **How to update a record**: changing an account
* **How to archive or delete record**: deprecating, restoring and deleting
  accounts, with the conditions that forbid each step
* **How to set up**: chart of accounts, account types, codes, reconciliation,
  taxes and tags, Italian chart of accounts
* **Report and export file**: where accounts are used in the reports and how
  to export or import the chart
* **Example** button and **FAQ** button, **Footer**

Pages are in English and Italian, with the fields and options of Odoo 18.


|it| Pagine di aiuto contestuale per la lista e la maschera del piano dei conti
(``account.account``), mostrate da web_context_help.

Il piano dei conti è l'elenco dei conti di contabilità generale su cui si
registrano le righe delle scritture. Le pagine spiegano come configurarlo:

* il pacchetto di *Localizzazione fiscale* che carica il piano dei conti del
  paese, ad esempio quello italiano di ``l10n_it`` (codici di quattro cifre,
  conti di credito e debito, etichette dello stato patrimoniale)
* il *Codice* e la *Tipologia* del conto e cosa decide la tipologia
* *Consentire riconciliazione* per i conti di credito, debito e gli altri
* le *Imposte predefinite*, le *Etichette* e i *Registri autorizzati* di un
  conto

Ogni pagina segue la struttura standard di web_context_help:

* **Indice**: le sezioni della pagina, costruito dalla finestra di aiuto
* **Descrizione**: cos'è il piano dei conti e cosa significa ogni campo
* **Come inserire un nuovo record**: guida passo passo per aggiungere un conto
* **Suggerimenti per la ricerca** (lista): menu, ricerca, filtri e
  raggruppamenti
* **Come modificare un record**: modificare un conto
* **Come archiviare o eliminare un record**: rendere non attivo, ripristinare
  ed eliminare i conti, con le condizioni che impediscono ogni passo
* **Come configurare**: piano dei conti, tipologie, codici, riconciliazione,
  imposte ed etichette, piano dei conti italiano
* **Stampe ed esportazione**: dove si usano i conti nei report e come
  esportare o importare il piano dei conti
* Pulsante **Esempio** e pulsante **FAQ**, **Piè di pagina**

Le pagine sono in inglese e in italiano, con i campi e le opzioni di Odoo 18.


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/18.0/help_account_account/static/description/


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

18.0.1.0.0 (2026-11-22)
~~~~~~~~~~~~~~~~~~~~~~~

* [NEW] Help pages for the chart of accounts list and form (``account.account``), English and Italian, Odoo 18: account types, codes, reconciliation, default taxes, tags and allowed journals, with the Italian chart of accounts of ``l10n_it``



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
