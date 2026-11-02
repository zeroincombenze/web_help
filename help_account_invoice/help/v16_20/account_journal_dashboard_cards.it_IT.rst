**Registri vendite e acquisti**

* **Nuovo** crea una nuova fattura cliente (vendite) o fattura fornitore
  (acquisti) in questo registro. Su una scheda acquisti **Carica** carica il
  PDF di una fattura e ne crea una fattura in bozza; **Nuovo** è accanto.
* *N Da convalidare*: i documenti ancora in bozza, e il loro totale.
* *N Non pagato* (vendite) o *N Da pagare* (acquisti): i documenti confermati
  non ancora pagati del tutto, e l'importo ancora dovuto. Le note di credito
  sono sottratte.
* *N In ritardo*: la parte di essi con la scadenza passata.
* *N Da controllare*: i documenti confermati non ancora segnati come
  controllati.
* Fare clic su un importo per elencarne i documenti.
* Il grafico a barre mostra l'importo ancora dovuto dei documenti confermati,
  per settimana della loro scadenza: *Scadute* (più vecchie), la settimana
  precedente, *Questa settimana*, le due settimane successive e *Non scadute*
  (più avanti).

**Registri banca, cassa e carta di credito**

* **Transazioni** apre le transazioni del conto. Su un registro banca non
  ancora impostato (senza numero di conto e senza flusso bancario scelto)
  **Configurazione banca** imposta il conto bancario.

  .. help-if:: module = account_accountant

     **N da riconciliare** compare quando ci sono transazioni ancora da
     abbinare a fatture, pagamenti o conti: apre la riconciliazione bancaria.

* *Saldo*: il saldo delle transazioni del conto. *Ultimo estratto conto*: il
  saldo finale dell'ultimo estratto conto, mostrato solo quando è diverso dal
  *Saldo*.
* *Pagamenti*: i pagamenti confermati del registro non ancora abbinati a una
  transazione bancaria, e il loro totale; fare clic per elencarli.
* *Operazioni varie*: registrazioni scritte direttamente sul conto bancario
  dopo l'ultimo estratto conto; vedere *Domande frequenti*.

  .. help-if:: module = account_accountant

     *N da controllare*: le transazioni non ancora segnate come controllate.

  .. help-if:: module = account_check_printing

     *N assegni da stampare*: gli assegni in attesa di stampa; fare clic per
     elencarli.

* Il grafico a linee mostra il saldo del conto negli ultimi 30 giorni.

**Registri varie**

* **Nuovo** crea una registrazione contabile in questo registro.
* Le prossime attività del registro, ad es. le dichiarazioni IVA da
  presentare, e *N Da controllare*: le registrazioni confermate non ancora
  segnate come controllate.

Su ogni scheda *Sequenze irregolari* o *Registrazioni prive di hash*, in
arancione, avvisano sulla numerazione o sull'inalterabilità del registro;
vedere *Domande frequenti*.

**Il menu ⋮**

**⋮**, in alto a destra di una scheda quando il mouse è sopra, apre il suo
menu, in colonne.

* Registri vendite e acquisti:

  * *Visualizza*: **Fatture**, **Note di credito** (vendite) o **Rimborso**
    (acquisti), **Movimenti contabili**.

    .. help-if:: module = account_accountant

       Anche **Abbinamento pagamenti**: le fatture e i pagamenti dei partner
       ancora da abbinare.

  * *Nuovo*: **Fattura**, **Nota di credito** (vendite) o **Rimborso**
    (acquisti); su una scheda vendite anche **Carica fatture**, che crea le
    fatture da file.
  * *Rendicontazione*: **Analisi fatture**.

* Registri banca, cassa e carta di credito:

  * *Visualizza*: **Estratti conto** (banca e carta di credito) o **Registri
    di cassa** (cassa), **Pagamenti** (tutti i pagamenti del registro).

    .. help-if:: module = account_accountant

       Anche **Transazioni**: le transazioni bancarie come lista.

  * *Nuovo*: **Pagamento cliente** e **Pagamento fornitore**.

    .. help-if:: module = account_bank_statement_import

       Su un registro banca anche **Importa file**, che carica il file
       dell'estratto conto scaricato dalla banca.

* Registri varie:

  * *Visualizza*: **Registrazioni contabili**, **Registrazioni da
    controllare** (le registrazioni in bozza) e, in modalità sviluppatore,
    **Movimenti contabili**.
  * *Nuovo*: **Registrazione contabile**.
  * *Operations*: **Conferma tutte le registrazioni**; vedere *Domande
    frequenti*.

In fondo al menu i colori della scheda e, solo per il diritto di accesso
*Amministratore*, **☆** aggiunge o toglie il registro dai preferiti (vedere
*Suggerimenti per la ricerca*) e **Configurazione** apre la maschera del
registro.
