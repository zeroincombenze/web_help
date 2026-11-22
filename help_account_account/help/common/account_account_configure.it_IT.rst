.. _configure:

Come configurare
----------------

* Il piano dei conti è in **Fatturazione ‣ Configurazione ‣ Contabilità ‣
  Piano dei conti**, per gli utenti con i diritti di contabilità.
* **Caricare il piano dei conti**: aprire **Fatturazione ‣ Configurazione ‣
  Impostazioni** (amministratori), blocco *Localizzazione fiscale*, scegliere
  il *Pacchetto* del proprio paese, ad es. *Italia*, e salvare. Odoo carica i
  conti, le imposte, le posizioni fiscali e i registri del paese. Con
  registrazioni contabili già registrate il pacchetto non si può cambiare. Il
  blocco è mostrato solo sull'azienda principale.
* **Codice**: lettere, cifre e punti, unico nell'azienda. Le prime cifre
  indicano il gruppo (il campo *Gruppo* è calcolato dall'inizio del codice e si
  può mostrare nell'elenco). Usare codici della stessa lunghezza per lo stesso
  livello.
* **Tipologia**: scegliere quella adatta: *Credito*, *Banca e cassa*,
  *Attività correnti*, *Attività non correnti*, *Risconti attivi*,
  *Immobilizzazioni*, *Debito*, *Carta di credito*, *Passività correnti*,
  *Passività non correnti*, *Patrimonio netto*, *Utili di esercizio*,
  *Ricavi*, *Altri ricavi*, *Costi*, *Ammortamento*, *Costo del venduto*,
  *Fuori bilancio*. La tipologia è usata dai report del paese e dalla chiusura
  dell'esercizio: i conti di ricavi e costi sono azzerati ogni anno, gli altri
  riportano il saldo.
* I conti **Credito e Debito** sono quelli di clienti e fornitori, impostati
  sul partner (scheda **Fatturazione**, gruppo *Registrazioni contabili*,
  *Conto di credito* e *Conto di debito*). L'interruttore *Non commerciale*,
  mostrato per questi conti, indica che non sono per crediti o debiti
  commerciali (ad es. il conto Tesoro IVA). Solo un conto per azienda può
  essere *Utili di esercizio*.
* **Consentire riconciliazione**: attivo per i conti le cui righe si
  abbinano (clienti, fornitori, pagamenti in sospeso, conti transitori); non
  può essere attivo per le tipologie *Banca e cassa*, *Carta di credito* e
  *Fuori bilancio*, ed è sempre attivo per *Credito* e *Debito*; i conti di
  ricavi, costi e patrimonio netto non sono mai riconciliabili.
* **Imposte predefinite**: imposte proposte sulle righe delle scritture del
  conto, ad es. l'IVA sui conti di ricavo; non per i conti fuori bilancio.
* **Etichette**: etichette con applicabilità *Conti*, per raggruppare i conti
  in report personalizzati; i report legali del paese richiedono quelle
  caricate dal suo pacchetto.
* **Registri autorizzati**: i registri che possono usare il conto. Se una
  riga di scrittura del conto è già in un altro registro, il limite è
  rifiutato.
* **Valuta del conto** (con più valute): non si può impostare una valuta su un
  conto che ha righe di scritture in un'altra valuta estera.
* **Aziende**: un conto può essere condiviso da più aziende dello stesso
  albero (non per *Banca e cassa*); il codice di ogni azienda è nella scheda
  **Mappatura**.

.. help-if:: module = l10n_it

   **Piano dei conti italiano (l10n_it)**

   Il pacchetto *Italia*, in *Localizzazione fiscale*, carica un piano dei
   conti con codici di quattro cifre disposti come lo stato patrimoniale
   italiano: ad es. *1101 Costi di impianto*, *1501 Crediti verso i clienti*,
   *2501 Debiti v/fornitori*, *3101* per i ricavi e *4101* per i costi. I conti
   1501 e 2501 sono i conti di credito e di debito, con *Consentire
   riconciliazione* attivo; i conti 2605 e 2607 (Tesoro IVA ed Erario c/IVA
   Split Payment) sono di debito *Non commerciale*. Quasi ogni conto ha
   un'etichetta dello stato patrimoniale o del conto economico italiano, ad
   es. *Immobilizzazioni*, *Attivo circolante*, *Debiti*, *Capitale proprio*;
   le etichette sono usate dai report italiani, non toglierle. I nomi sono
   tradotti in italiano quando la lingua dell'utente è *Italiano*. Aggiungere i
   propri conti accanto a un conto simile: se si lascia vuota la tipologia, la
   tipologia e le etichette sono copiate dal conto con il codice subito
   precedente.
