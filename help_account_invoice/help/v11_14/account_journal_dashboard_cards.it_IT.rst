**Registri vendite e acquisti**

* **Nuova fattura** apre una nuova fattura cliente (vendite) o fattura
  fornitore (acquisti) in questo registro.
* **Importa fatture** (acquisti) apre *Importa fatture fornitore*:
  aggiungere i file delle fatture (ad es. il PDF ricevuto per email) e
  premere **Importa**; ogni file diventa una fattura fornitore in bozza con
  il file allegato, da completare.
* *N fatture da validare*: quanti documenti sono ancora in bozza, e il loro
  totale; fare clic per elencarli (filtro *Bozza*).
* *N fatture non pagate* (vendite) o *N fatture da pagare* (acquisti): quanti
  documenti validati non sono ancora pagati, e l'importo ancora dovuto; fare
  clic per elencarli (filtro *Aperta*). Le note di credito sono sottratte dai
  totali.

.. help-if:: module = hr_expense

   * *N spese da elaborare* (acquisti): le note spese approvate o registrate
     di questo registro, e il loro totale; fare clic per elencarle.

* Il grafico a barre mostra l'importo ancora dovuto dei documenti validati,
  per settimana della loro scadenza: *Precedenti*, la settimana scorsa,
  *Questa sett.*, le due settimane successive e *Future*.

**Registri banca e cassa**

* **Configura** (banca) compare finché i feed bancari del registro non sono
  impostati: apre *Creazione di un conto corrente bancario*, vedere *Domande
  frequenti*.

.. help-if:: module != account_bank_statement_import

   * Il collegamento **Crea** di *Crea estratti conto* (banca) apre un nuovo
     estratto conto bancario, per registrare a mano i movimenti del conto.

.. help-if:: module = account_bank_statement_import

   * *Crea oppure Importa estratti conto* (banca): **Crea** apre un nuovo
     estratto conto bancario, per registrare a mano i movimenti del conto;
     **Importa** carica il file dell'estratto conto scaricato dalla banca.

* **Nuove operazioni** (cassa) apre un nuovo estratto conto di cassa.
* **Riconcilia N movimenti** compare quando righe degli estratti conto aperti
  sono ancora da abbinare a fatture, pagamenti o conti: apre la
  riconciliazione. **Nuove operazioni** diventa allora un collegamento sotto
  di esso.
* *Saldo nel libro mastro*: il saldo delle registrazioni confermate sui conti
  dare e avere predefiniti del registro, fino a oggi. *Ultimo estratto
  conto*: il saldo finale dell'ultimo estratto conto, mostrato solo quando è
  diverso dal *Saldo nel libro mastro*.

.. help-if:: module = account_check_printing

   * *N Assegni da stampare* (banca): gli assegni in attesa di stampa; fare
     clic per elencarli.

* Il grafico a linee mostra il saldo degli estratti conto negli ultimi 30
  giorni.

**Registri varie**

* **Registrazioni contabili** elenca le registrazioni del registro. La scheda
  non mostra importi: usare il menu **⋮**.

**Il menu ⋮**

**⋮**, in alto a destra di una scheda, apre il suo menu, in colonne.

* Registri vendite e acquisti:

  * *Visualizza*: **Fatture**, **Note di credito**, **Abbinamento
    pagamenti** (le fatture e i pagamenti dei clienti o dei fornitori ancora
    da abbinare).
  * *Nuovo*: **Fattura**, **Nota di credito** (vendite) o **Nota di credito
    fattura** (acquisti).
  * *Rendicontazione*: **Analisi fatture** (solo *Responsabile
    fatturazione*).

* Registri banca e cassa:

  * *Visualizza*: **Estratti conto**, **Operazioni** (le righe degli estratti
    conto del registro), **Pagamenti cliente**, **Pagamenti fornitore** e
    **Trasferimenti interni** (i pagamenti del registro di quel tipo).
  * *Nuovo*: **Estratto conto**, **Pagamento cliente**, **Pagamento
    fornitore** e **Trasferimento interno**: questi tre aprono un nuovo
    pagamento di quel tipo in questo registro.

    .. help-if:: module = account_bank_statement_import

       Su un registro banca anche **Importa estratto conto**.

  * *Riconciliazione*: **Modelli di riconciliazione** (solo *Responsabile
    fatturazione*), le contropartite predefinite proposte dalla
    riconciliazione, ad es. le spese bancarie.

* Registri varie:

  * *Visualizza*: **Registrazioni contabili**, e **Registrazioni da
    controllare**, solo le registrazioni *Non confermato* del registro.
  * *Nuovo*: **Registrazione contabile**.
  * *Operazioni*: **Conferma tutte le registrazioni**; in questa versione non
    funziona, vedere *Domande frequenti* per confermare le registrazioni in
    bozza.

In modalità sviluppatore *Visualizza* elenca anche i **Movimenti contabili**
del registro. In fondo, solo per il diritto di accesso *Responsabile
fatturazione*, i colori della scheda, la stella **Aggiungi a preferiti** /
**Rimuovi dai preferiti** (vedere *Suggerimenti per la ricerca*) e
**Impostazioni**, che apre la maschera del registro.
