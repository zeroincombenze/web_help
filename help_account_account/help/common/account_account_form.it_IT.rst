.. help-page:: account_account_form
   :title: Conto
   :model: account.account
   :view: account.view_account_form
   :view-type: form
   :priority: 96

Conto
=====

.. _description:

Descrizione
-----------

Fare clic sul pulsante [`Pronto`] per sapere come usare questo aiuto; fare
clic sul pulsante [`FAQ`] per le domande più comuni già risolte.

Un conto è un conto di contabilità generale del piano dei conti: ogni riga di
una fattura, di un pagamento o di una scrittura contabile è registrata su un
conto, e i report (stato patrimoniale, conto economico, report delle imposte)
sommano i conti.

* Il :field:`codice <code>`, con il :field:`nome conto <name>`, identifica il
  conto; il codice accetta solo lettere, cifre e punti.
* La :field:`tipologia <account_type>` dice cos'è il conto (credito, banca e
  cassa, ricavi, costi ...) e decide come lo usano i report e la chiusura
  dell'esercizio.
* Le :field:`Imposte predefinite <tax_ids>` sono proposte sulle registrazioni
  del conto; le :field:`Etichette <tag_ids>` raggruppano i conti per report
  personalizzati.
* I :field:`Registri autorizzati <allowed_journal_ids>` limitano i registri
  dove il conto si può usare; vuoto significa tutti i registri.
* :field:`Non attivo <deprecated>` toglie il conto dalle scelte e vieta nuove
  registrazioni.
* Il pulsante **Saldo** in alto a destra apre le righe delle scritture del
  conto; il pulsante **Imposte** elenca le imposte che registrano su di esso.

.. help-include:: account_account_new.rst

.. help-include:: account_account_update.rst

.. help-include:: account_account_cancel.rst

.. help-include:: account_account_configure.rst

.. help-include:: account_account_report.rst

.. help-include:: account_account_example.rst

.. _faq:

Domande frequenti
-----------------

Fare clic sul pulsante [`Argomento`] per tornare alla pagina di aiuto specifica.

.. help-question:: Perché non riesco a salvare il codice del conto?

   Il codice può contenere solo lettere, cifre e punti, e deve essere unico
   nell'azienda (e nelle sue aziende madre e filiali): scegliere un altro
   codice. Con più aziende il codice deve essere impostato per ognuna.

.. help-question:: Perché non riesco a togliere Consentire riconciliazione?

   Un conto di credito o di debito deve essere riconciliabile. Per gli altri
   conti l'interruttore non si può togliere finché ci sono riconciliazioni
   parziali in sospeso sulle sue righe. I conti di banca e cassa, carta di
   credito, fuori bilancio, patrimonio netto, ricavi e costi non sono mai
   riconciliabili.

.. help-question:: Perché non riesco a cambiare la tipologia del conto?

   Un conto usato come conto predefinito di un registro di banca, o di un
   registro di vendita o di acquisto, non può diventare *Credito* o *Debito*.
   Solo un conto per azienda può avere tipologia *Utili di esercizio*.

.. help-question:: Perché non riesco a rendere non attivo o eliminare il conto?

   Vedere *Come archiviare o eliminare un record*: un conto con righe di
   scritture, un conto della mappatura di una posizione fiscale o della
   ripartizione di un'imposta non si può eliminare, e un conto della
   ripartizione di un'imposta non si può rendere non attivo.

.. help-question:: Perché non posso creare un conto da un campo di un registro o di una registrazione?

   I conti si creano solo dal menu Piano dei conti.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-22 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
