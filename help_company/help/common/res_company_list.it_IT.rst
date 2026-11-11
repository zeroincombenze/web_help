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

Fare clic sul pulsante **Pronto** per sapere come usare questo aiuto; fare
clic sul pulsante **FAQ** per le domande più comuni già risolte.

L'elenco delle aziende gestite nel database. Ogni riga mostra il
:field:`nome dell'azienda <name>`, il suo :field:`partner <partner_id>` (il
contatto che contiene indirizzo e partita IVA dell'azienda) e le sue
:field:`filiali <child_ids>`. L'ordine delle righe, cambiato trascinando la
maniglia a sinistra, è l'ordine con cui le aziende sono proposte. Fare clic
su una riga per aprire l'azienda.

.. _search:

Suggerimenti per la ricerca
---------------------------

* **Impostazioni ‣ Utenti e aziende ‣ Aziende** elenca le aziende; il menu
  è visibile agli amministratori.
* Scrivere nella barra di ricerca per cercare le aziende per nome.
* **Filtri ‣ In archivio** mostra le aziende non più usate.
* **Raggruppa per ‣ Aggiungi gruppo personalizzato** raggruppa le aziende,
  ad es. per azienda principale, per vedere le filiali sotto la loro azienda.

.. help-include:: res_company_configure.rst

.. help-include:: res_company_report.rst

.. _example:

Esempio
-------

**Una seconda azienda nello stesso database.** Premere **Nuovo**, scrivere
nome, indirizzo e partita IVA e uscire dalla maschera. Poi aprire
**Impostazioni ‣ Utenti e aziende ‣ Utenti**, aprire ogni utente che deve
lavorare per la nuova azienda e aggiungerla alle *Aziende consentite*. Gli
utenti passano da un'azienda all'altra con il selettore delle aziende nella
barra in alto.

.. _faq:

Domande frequenti
-----------------

Fare clic sul pulsante **Argomento** per tornare alla pagina di aiuto specifica.

.. help-question:: Perché non vedo il menu Aziende?

   Il menu è visibile solo agli amministratori (diritti *Impostazioni*).

.. help-question:: Perché non vedo un'azienda nel selettore delle aziende?

   Il selettore mostra le *Aziende consentite* del proprio utente: chiedere a
   un amministratore di aggiungere l'azienda al proprio utente.

.. help-question:: Come si elimina un'azienda?

   Un'azienda usata da documenti non si può eliminare: archiviarla invece,
   aprendola e premendo l'icona dell'ingranaggio ‣ **Archivia**. Un'azienda
   che è ancora l'azienda predefinita di un utente attivo non si può
   archiviare: cambiare prima l'azienda predefinita dell'utente.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-07 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
