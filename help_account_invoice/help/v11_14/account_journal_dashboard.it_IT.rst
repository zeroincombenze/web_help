.. help-version:: 12

   .. help-page:: account_journal_dashboard
      :title: Panoramica contabilità
      :model: account.journal
      :view: account.account_journal_dashboard_kanban_view
      :view-type: kanban
      :priority: 96

Panoramica contabilità
======================

.. _description:

Descrizione
-----------

La bacheca aperta da **Fatturazione ‣ Panoramica**. Il menu è visibile solo
agli utenti con *Mostrare funzionalità contabili complete* (vedere *Domande
frequenti*). Mostra una scheda per ogni registro dell'azienda corrente. Ogni
scheda mostra il :field:`nome del registro <name>`, che apre i documenti del
registro, e la :field:`tipologia <type>`: *Vendita*, *Acquisto*, *Cassa*,
*Banca* o *Varie*. Qui non si possono creare schede: i registri si impostano
nella configurazione, vedere *Come configurare*.

Gli amministratori vedono anche, sopra le schede, il pannello dei
suggerimenti di configurazione con i passaggi *Dati aziendali*, *Conto
bancario*, *Anno fiscale* e *Piano dei conti*; la ✕ in alto a destra lo
nasconde per sempre, dopo la conferma con **Rimuovi**.

.. help-include:: account_journal_dashboard_cards.rst

.. help-include:: account_journal_dashboard_search.rst

.. help-include:: account_journal_dashboard_configure.rst

.. _report:

Stampe ed esportazione
----------------------

* La bacheca non stampa nulla e non esporta: aprire i documenti da una scheda
  (**⋮ ‣ Visualizza**) e stamparli o esportarli dalla loro lista.
* **⋮ ‣ Rendicontazione ‣ Analisi fatture**, su una scheda vendite o
  acquisti (solo *Responsabile fatturazione*), apre l'analisi delle fatture
  come grafico o pivot.
* I grafici delle schede servono solo a vedere l'andamento: passare il mouse
  su una barra o su un punto per leggerne l'importo.

.. help-include:: account_journal_dashboard_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non vedo il menu Panoramica?

   Il menu è visibile solo agli utenti con *Mostrare funzionalità contabili
   complete*; senza, le fatture si raggiungono dai menu *Clienti* e
   *Fornitori*. L'amministratore attiva la modalità sviluppatore (**Attiva la
   modalità sviluppatore** in *Impostazioni*), apre l'utente in
   **Impostazioni ‣ Utenti e aziende ‣ Utenti** e spunta *Mostrare
   funzionalità contabili complete* nella sezione *Impostazioni tecniche*.

.. help-question:: Perché un registro non compare nella bacheca?

   La bacheca si apre con il filtro *Preferiti*, che mostra solo i registri
   segnati con la stella ★. Togliere il filtro dalla barra di ricerca per
   vederli tutti. La bacheca mostra solo i registri dell'azienda corrente:
   cambiare azienda nella barra in alto per vedere gli altri. Un registro
   archiviato compare solo con il filtro *Archiviato*.

.. help-question:: Perché la bacheca è vuota?

   Non è ancora installato un piano dei conti, quindi non ci sono registri:
   la bacheca vuota mostra il collegamento **Esplora nazioni disponibili.**
   per scegliere il piano dei conti del proprio paese.

.. help-question:: Perché Saldo nel libro mastro e Ultimo estratto conto sono diversi?

   *Saldo nel libro mastro* è il saldo delle registrazioni confermate sui
   conti del registro, *Ultimo estratto conto* il saldo finale dell'ultimo
   estratto conto. Sono diversi finché alcune righe dell'estratto conto sono
   da riconciliare (**Riconcilia N movimenti**), o quando sul conto bancario
   sono state scritte registrazioni fuori dagli estratti conto.

.. help-question:: Perché la scheda banca mostra sempre Configura?

   **Configura** compare finché i :field:`Feed bancari
   <bank_statements_source>` del registro sono *Non ancora definiti*.
   Senza un modulo che importa i file degli estratti conto *Non ancora
   definiti* è l'unica scelta, quindi il pulsante resta; apre *Creazione di
   un conto corrente bancario*, l'impostazione del conto bancario.

   .. help-if:: module = account_bank_statement_import

      Quando è installato un formato di file degli estratti conto (ad es. OFX
      o CAMT), *Feed bancari* offre anche *Importa(…)* seguito dai formati:
      sceglierlo, o importare un file di estratto conto con **Importa**, e il
      pulsante scompare.

.. help-question:: Perché non vedo la stella, i colori e Impostazioni sulla scheda?

   Sono in fondo al menu **⋮**, solo per il diritto di accesso *Responsabile
   fatturazione*.

.. help-question:: Come si confermano tutte le registrazioni in bozza di un registro?

   Non usare **⋮ ‣ Operazioni ‣ Conferma tutte le registrazioni**: in questa
   versione non passa le registrazioni del registro alla conferma, che finisce
   con un errore o conferma una registrazione in bozza estranea. Aprire
   invece **⋮ ‣ Visualizza ‣ Registrazioni da controllare** sulla scheda (le
   registrazioni *Non confermato* del registro), selezionare le
   registrazioni con le caselle di spunta e usare **Azione ‣ Conferma
   registrazioni contabili**, poi confermare con **Conferma registrazioni
   contabili**.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-01 16:55 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
