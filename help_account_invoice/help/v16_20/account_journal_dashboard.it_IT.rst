.. help-page:: account_journal_dashboard
   :title: Bacheca della contabilità
   :model: account.journal
   :view: account.account_journal_dashboard_kanban_view
   :view-type: kanban
   :priority: 96

Bacheca della contabilità
=========================

.. _description:

Descrizione
-----------

Fare clic sul pulsante **Pronto** per sapere come usare questo aiuto; fare
clic sul pulsante **FAQ** per le domande più comuni già risolte.

.. help-if:: module != accountant

   La bacheca aperta da **Fatturazione ‣ Bacheca**.

.. help-if:: module = accountant

   La bacheca aperta da **Contabilità ‣ Bacheca**.

Mostra una scheda per ogni registro delle aziende selezionate. Ogni scheda
mostra il :field:`nome del registro <name>`, che apre i documenti del
registro, e, quando sono selezionate più aziende, l'azienda del registro. La
sua :field:`tipologia <type>` (*Vendita*, *Acquisto*, *Banca*, *Cassa*,
*Carta di credito* o *Varie*) decide i pulsanti, gli importi e il grafico
della scheda. Qui non si possono creare schede: i registri si impostano nella
configurazione, vedere *Come configurare*.

Un registro ancora senza documenti mostra un breve suggerimento, ad es.
*Collega la tua banca. Abbina le fatture automaticamente.*, e il suo grafico
è disegnato in grigio con *Dati campione*. Si possono anche trascinare file
su una scheda: fatture su una scheda vendite o acquisti, file degli estratti
conto su una scheda banca, allegati su una scheda varie.

.. help-include:: account_journal_dashboard_cards.rst

.. help-include:: account_journal_dashboard_search.rst

.. help-include:: account_journal_dashboard_configure.rst

.. _report:

Stampe ed esportazione
----------------------

* La bacheca non stampa nulla e non esporta: aprire i documenti da una scheda
  (**⋮ ‣ Visualizza**) e stamparli o esportarli dalla loro lista.
* **⋮ ‣ Rendicontazione ‣ Analisi fatture**, su una scheda vendite o
  acquisti, apre l'analisi delle fatture come pivot o grafico.
* I grafici delle schede servono solo a vedere l'andamento: passare il mouse
  su una barra o su un punto per leggerne l'importo.

.. help-include:: account_journal_dashboard_example.rst

.. _faq:

Domande frequenti
-----------------

Fare clic sul pulsante **Argomento** per tornare alla pagina di aiuto specifica.

.. help-question:: Perché non vedo il menu Bacheca?

   .. help-if:: module != account_accountant

      Con la sola app Fatturazione il menu compare solo agli utenti con il
      diritto tecnico *Mostrare funzionalità contabili complete*:
      l'amministratore lo imposta in modalità sviluppatore in
      **Impostazioni ‣ Utenti e aziende ‣ Utenti**, scheda *Diritti di
      accesso*. Senza di esso le fatture si raggiungono dai menu *Clienti* e
      *Fornitori*.

   .. help-if:: module = account_accountant

      Il menu richiede il diritto di accesso *Fatturazione e banche* o
      *Amministratore*: l'amministratore lo imposta in **Impostazioni ‣
      Utenti e aziende ‣ Utenti**, campo *Fatturazione*. Con *Fatturazione*
      le fatture si raggiungono dai menu *Clienti* e *Fornitori*.

.. help-question:: Perché un registro non compare nella bacheca?

   La bacheca si apre con il filtro *Preferiti*, che mostra solo i registri
   segnati con la stella ★. Togliere il filtro dalla barra di ricerca per
   vederli tutti. La bacheca mostra solo i registri delle aziende
   selezionate: spuntare le altre aziende nel selettore delle aziende della
   barra in alto. Un registro archiviato compare solo con il filtro *In
   archivio*.

.. help-question:: Perché la bacheca è vuota?

   Non è ancora installato un piano dei conti, quindi non ci sono registri:
   la bacheca vuota mostra un collegamento per esplorare i piani dei conti
   delle nazioni disponibili.

.. help-question:: Perché Saldo e Ultimo estratto conto sono diversi?

   *Saldo* è il saldo delle transazioni del registro, *Ultimo estratto conto*
   il saldo finale dell'ultimo estratto conto. Sono diversi finché alcune
   transazioni non sono ancora in un estratto conto, ad es. quelle importate
   o scritte dopo l'ultimo estratto conto.

.. help-question:: Cosa significano Operazioni varie, Registrazioni prive di hash e Sequenze irregolari?

   *Operazioni varie* sono registrazioni scritte direttamente sul conto
   bancario, che non vengono da una transazione bancaria né da un pagamento,
   dopo l'ultimo estratto conto; di solito sono errori da controllare.
   *Sequenze irregolari* avvisa che alcuni numeri del registro mancano o sono
   fuori ordine dall'ultima data di blocco, per documenti in bozza,
   annullati o eliminati. *Registrazioni prive di hash* avvisa che, su un
   registro con l'hash di inalterabilità, alcune registrazioni confermate non
   sono ancora protette. Fare clic sull'avviso per elencare le registrazioni
   interessate.

.. help-question:: Perché non vedo la stella e Configurazione nel menu ⋮?

   Sono in fondo al menu **⋮**, solo per il diritto di accesso
   *Amministratore*.

.. help-question:: Come si confermano tutte le registrazioni in bozza di un registro?

   Su una scheda varie usare **⋮ ‣ Operations ‣ Conferma tutte le
   registrazioni**: la finestra *Conferma registrazioni* conferma ogni
   registrazione in bozza del registro. Sulle altre schede aprire i documenti
   da **⋮ ‣ Visualizza**, scegliere il filtro *Bozza*, selezionare i
   documenti e usare **Azioni ‣ Conferma registrazioni**.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-01 21:09 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
