================================================
|icon| Help for company/Aiuto aziende 18.0.1.0.0
================================================

**Context help pages for companies, with Italian e-invoicing setup**

.. |icon| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/18.0/help_company/static/description/icon.png


.. contents::



Overview | Panoramica
=====================

|en| Context help pages for the company list and form (``res.company``), shown by
web_context_help.

Every page follows the standard layout of web_context_help: description, new
record, update record or search, set up, report, example, FAQ and footer.

The *How to set up* section of the form explains how to activate the Italian
electronic invoicing (FatturaPA through the SdI): which modules to install,
Odoo ones (``l10n_it``, ``l10n_it_edi`` and its add-ons) and OCA ones
(``l10n_it_edi_extension``, ``l10n_it_edi_pec``, …), what each one does, and
the company and settings data to fill in.

When ``l10n_it_edi`` is installed, the page shows an important warning: the
*Regime fiscale* (Tax System) of the company must be set, otherwise the
e-invoices are not created.

Pages are in English and Italian.


|it| Pagine di aiuto contestuale per l'elenco e la maschera delle aziende
(``res.company``), mostrate da web_context_help.

Ogni pagina segue la struttura standard di web_context_help: descrizione,
nuovo record, modifica record o ricerca, configurazione, stampe, esempio,
domande frequenti e piè di pagina.

La sezione *Come configurare* della maschera spiega come attivare la fattura
elettronica italiana (FatturaPA tramite lo SdI): quali moduli installare, di
Odoo (``l10n_it``, ``l10n_it_edi`` e i suoi moduli aggiuntivi) e OCA
(``l10n_it_edi_extension``, ``l10n_it_edi_pec``, …), a cosa serve ciascuno e
i dati da compilare nell'azienda e nelle impostazioni.

Quando ``l10n_it_edi`` è installato, la pagina mostra un avviso importante: il
*Regime fiscale* dell'azienda deve essere impostato, altrimenti le fatture
elettroniche non vengono create.

Le pagine sono in inglese e in italiano.


|thumbnail|

.. |thumbnail| image:: https://raw.githubusercontent.com/zeroincombenze/web_help/18.0/help_company/static/description/


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

18.0.1.0.0 (2026-11-07)
~~~~~~~~~~~~~~~~~~~~~~~

* [NEW] Help pages for company list and form, English and Italian: how to insert, update and set up a company, with the activation of the Italian e-invoicing (modules to install and their purpose) and a warning to set the Regime fiscale when l10n_it_edi is installed



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

Last Update / Ultimo aggiornamento: 2026-11-07

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
