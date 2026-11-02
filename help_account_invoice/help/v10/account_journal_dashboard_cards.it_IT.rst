**Registri vendite e acquisti**

* **Nuova fattura** apre una nuova fattura cliente (vendite) o fattura
  fornitore (acquisti) in questo registro.
* *Fatture da validare* (vendite) o *Fatture in bozza* (acquisti): quanti
  documenti sono ancora in bozza, e il loro totale; fare clic per elencarli.
* *Pagamenti in attesa* (vendite) o *Pagamenti da effettuare* (acquisti):
  quanti documenti validati non sono ancora pagati, e il loro totale; fare
  clic per elencarli. Le note di credito sono sottratte dai totali.
* Il grafico a barre mostra l'importo ancora dovuto dei documenti validati,
  per settimana della loro data contabile: *Precedente/i*, la settimana
  scorsa, *Questa settimana*, le due settimane successive e *Future*.

**Registri banca e cassa**

* **Nuovo estratto conto** (banca) o **Nuove operazioni** (cassa) crea un
  estratto conto per registrare i movimenti del conto.

  .. help-if:: module = account_bank_statement_import

     **Importa estratto conto** carica il file dell'estratto conto scaricato
     dalla banca. Un nuovo registro banca mostra entrambi i pulsanti; dopo
     averne usato uno, il registro lo ricorda nelle sue *Spese bancarie*
     (*Registra manualmente* o *File Import*) e la scheda mostra solo
     quello.

* **Riconciliazione N Elementi** compare quando ci sono righe dell'estratto
  conto ancora da abbinare a fatture, pagamenti o conti: apre la
  riconciliazione. I pulsanti dell'estratto conto diventano allora
  collegamenti sotto di esso.
* *Saldo su libro mastro*: il saldo del conto del registro in contabilità,
  fino a oggi. *Ultimo Rendiconto*: il saldo finale dell'ultimo estratto
  conto, mostrato solo quando è diverso dal *Saldo su libro mastro*.

  .. help-if:: module = account_check_printing

     *Assegni da stampare*: gli assegni in attesa di stampa; fare clic per
     elencarli.

* Il grafico a linee mostra il saldo degli estratti conto negli ultimi 30
  giorni.

**Registri varie**

La scheda non mostra importi: usare il menu **Altro**.

**Il menu Altro**

**Altro ▾**, in alto a destra di una scheda, apre il suo menu, in colonne.

* Registri vendite e acquisti:

  * *Visualizzare*: **Fatture**, **Note credito**, **Riconciliazione
    pagamenti** (le fatture e i pagamenti dei partner ancora da abbinare).
  * *Nuovo*: **Fattura**, **Nota credito** (vendite) o **Nota di credito**
    (acquisti).
  * *Rendiconti*: **Analisi fatture** (vendite) o **Analisi delle fatture**
    (acquisti), solo *Consulente*.

* Registri banca e cassa:

  * *Visualizzare*: **Estratti conto bancari** o **Rendiconto di cassa**,
    **Ricerca movimenti** (le righe degli estratti conto del registro).
  * *Nuovo*: **Transazione** (un nuovo estratto conto), **Invio contanti**,
    **Ricezione contanti** e **Trasferimento interno**: questi tre aprono i
    pagamenti del registro di quel tipo, dove **Crea** ne registra uno nuovo.

    .. help-if:: module = account_bank_statement_import

       Su un registro banca anche **Importa estratto conto**.

  * *Riconciliazione*: **Riconciliazione** (*Nulla da riconciliare* quando
    ogni riga è abbinata) e **Modelli di riconciliazione** (solo
    *Consulente*), le contropartite predefinite proposte dalla
    riconciliazione, ad es. le spese bancarie.

* Registri varie:

  * *Visualizzare*: **Registrazioni contabili** e **Registrazioni da
    controllare**; entrambi elencano le registrazioni del registro.
  * *Nuovo*: **Registrazione contabile**.
  * *Operazioni*: **Genera tutte le registrazioni**; vedere *Domande
    frequenti* per confermare le registrazioni in bozza.

In modalità sviluppatore *Visualizzare* elenca anche le **Righe contabili**
del registro. In fondo, solo per il diritto di accesso *Consulente*, **☆
Preferito** aggiunge o toglie il registro dai preferiti (vedere
*Suggerimenti per la ricerca*) e **Impostazioni** apre la maschera del
registro.
