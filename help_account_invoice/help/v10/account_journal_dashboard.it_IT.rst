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

.. help-if:: module != account_accountant

   La bacheca aperta da **Fatturazione ‣ Bacheca**.

.. help-if:: module = account_accountant

   La bacheca aperta da **Contabilità ‣ Bacheca**.

Mostra una scheda per ogni registro dell'azienda corrente; la vedono solo gli
utenti con il diritto di accesso *Contabile* o *Consulente*. Ogni scheda
mostra il :field:`nome del registro <name>`, che apre i documenti del
registro, e il :field:`tipo <type>`: *Vendita*, *Acquisto*, *Cassa*, *Banca*
o *Varie*. Qui non si possono creare schede: i registri si impostano nella
configurazione, vedere *Come configurare*.

.. help-include:: account_journal_dashboard_cards.rst

.. help-include:: account_journal_dashboard_search.rst

.. help-include:: account_journal_dashboard_configure.rst

.. _report:

Stampe ed esportazione
----------------------

* La bacheca non stampa nulla e non esporta: aprire i documenti da una scheda
  (**Altro ‣ Visualizzare**) e stamparli o esportarli dalla loro lista.
* **Altro ‣ Rendiconti ‣ Analisi fatture** su una scheda vendite, **Analisi
  delle fatture** su una scheda acquisti (solo *Consulente*), apre l'analisi
  delle fatture come pivot o grafico.
* I grafici delle schede servono solo a vedere l'andamento: passare il mouse
  su una barra o su un punto per leggerne l'importo.

.. help-include:: account_journal_dashboard_example.rst

.. _faq:

Domande frequenti
-----------------

Fare clic sul pulsante **Argomento** per tornare alla pagina di aiuto specifica.

.. help-question:: Perché non vedo il menu Bacheca?

   Il menu è solo per i diritti di accesso *Contabile* e *Consulente*; con
   *Fatturazione* le fatture si raggiungono dai menu *Vendite* e *Acquisti*.
   L'amministratore imposta il diritto di accesso di ogni utente in
   **Configurazione ‣ Utenti ‣ Utenti**, campo *Contabilità e finanza*.

.. help-question:: Perché un registro non compare nella bacheca?

   La bacheca si apre con il filtro *Preferiti*, che mostra solo i registri
   segnati con la stella ★. Togliere il filtro dalla barra di ricerca per
   vederli tutti. La bacheca mostra solo i registri dell'azienda corrente:
   cambiare azienda nella barra in alto per vedere gli altri.

.. help-question:: Perché la bacheca è vuota?

   Non è ancora installato un piano dei conti, quindi non ci sono registri:
   la bacheca vuota mostra un collegamento per scegliere il piano dei conti
   del proprio paese.

.. help-question:: Perché Saldo su libro mastro e Ultimo Rendiconto sono diversi?

   *Saldo su libro mastro* è il saldo del conto bancario in contabilità,
   *Ultimo Rendiconto* il saldo finale dell'ultimo estratto conto. Sono
   diversi finché alcune righe dell'estratto conto sono da riconciliare
   (**Riconciliazione**), o quando sul conto bancario sono state scritte
   registrazioni fuori dagli estratti conto.

.. help-question:: Perché non vedo Preferito e Impostazioni sulla scheda?

   Sono in fondo al menu **Altro**, solo per il diritto di accesso
   *Consulente*.

.. help-question:: Come si confermano tutte le registrazioni in bozza di un registro?

   Aprire **Altro ‣ Visualizzare ‣ Registrazioni contabili** sulla scheda,
   scegliere il filtro *Non generata*, selezionare le registrazioni con le
   caselle di spunta e usare **Azione ‣ Genera registrazioni contabili**.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-01 16:38 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
