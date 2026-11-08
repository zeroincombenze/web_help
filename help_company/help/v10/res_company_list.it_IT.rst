.. help-page:: res_company_list
   :title: Aziende
   :model: res.company
   :view: base.view_company_tree
   :view-type: list
   :priority: 96

Aziende
=======

.. _description:

Descrizione
-----------

L'elenco delle aziende gestite nel database. Ogni riga mostra il :field:`nome
dell'azienda <name>` e il suo :field:`partner <partner_id>` (il contatto che
contiene indirizzo e partita IVA dell'azienda). L'ordine delle righe,
cambiato trascinando la maniglia a sinistra, è l'ordine in cui le aziende
sono proposte. Fare clic su una riga per aprire l'azienda.

.. _search:

Suggerimenti per la ricerca
---------------------------

* **Configurazione ‣ Utenti ‣ Aziende** elenca le aziende; il menu è
  visibile agli amministratori.
* Scrivere nella barra di ricerca per cercare le aziende per nome.
* **Raggruppa per ‣ Crea raggruppamento personalizzato** raggruppa le
  aziende, ad es. per *Azienda Principale*, per vedere le aziende di un
  gruppo sotto la loro azienda principale.

.. help-include:: res_company_configure.rst

.. help-include:: res_company_report.rst

.. _example:

Esempio
-------

**Una seconda azienda nello stesso database.** In **Configurazione ‣
Impostazioni Generali** spuntare *Gestione multi aziendale* e premere
**Salva**. Poi premere **Crea** in questo elenco, scrivere nome, indirizzo e
partita IVA e premere **Salva**. Aprire **Configurazione ‣ Utenti ‣ Utenti**,
aprire ogni utente che deve lavorare per la nuova azienda, premere
**Modifica** e aggiungerla alle *Aziende consentite* della scheda **Diritti di
accesso**. Gli utenti passano da un'azienda all'altra con il selettore delle
aziende nella barra in alto.

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non vedo il menu Aziende?

   Il menu **Configurazione** è mostrato solo agli amministratori.

.. help-question:: Perché non vedo un'azienda nel selettore delle aziende?

   Il selettore mostra le *Aziende consentite* del proprio utente, e compare
   solo quando sono più di una: chiedere a un amministratore di aggiungere
   l'azienda al proprio utente.

.. help-question:: Come si elimina un'azienda?

   In questa versione un'azienda non si può archiviare. Si può eliminare
   (selezionarla nell'elenco, poi **Azione ‣ Elimina**) solo finché nessun
   documento, utente o altro record la usa; un'azienda già usata va
   mantenuta.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-07 18:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
