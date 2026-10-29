.. _update_record:

Modifica record
---------------

#. Aprire l'ordine da **Acquisti ‣ Acquisto ‣ Richieste di preventivo** o
   **Acquisti ‣ Acquisto ‣ Ordini di acquisto**, premere **Modifica**, cambiare
   i campi e premere **Salva** (**Annulla** scarta le modifiche). Ogni cambio
   di stato è registrato nel chatter.
#. **RFQ** o **RFQ Inviata**: tutti i campi sono modificabili. Modificare una
   RdP inviata non la reinvia: premere **Rispedisci RdP per Email**.
#. **Da Approvare**: un responsabile acquisti preme **Approva Ordine** per
   confermarlo.
#. **Ordine di Acquisto**: fornitore, data ordine, valuta e prodotto delle
   righe diventano di sola lettura. Si possono ancora cambiare quantità e
   prezzi e aggiungere righe: Magazzino aggiorna il ricevimento. Le righe non
   si possono eliminare: impostare la quantità a 0. **Invia PO per email**
   invia al fornitore l'ordine confermato.
#. **Prodotti in entrata** (o il pulsante **Spedizione**) apre il ricevimento:
   indicare le quantità ricevute e premere **Valida**. Un ricevimento parziale
   crea un ordine arretrato per la merce mancante.
#. Pulsante **Fatture fornitori**: crea la fattura del fornitore dall'ordine,
   oppure apre quelle esistenti. Una fattura si può creare anche da **Acquisti
   ‣ Controllo ‣ Fatture fornitori** scegliendo l'ordine nel campo **Aggiungi
   ordini d'acquisto**. Le quantità proposte dipendono dalla politica *Controllo
   Fatture di Acquisto* del prodotto; lo :field:`stato fatturazione
   <invoice_status>` viene poi ricalcolato.
#. **Blocca** (o l'impostazione *Modifica Ordini di Acquisto* impostata a *Gli
   ordini di acquisto confermati non sono modificabili*) porta lo stato a
   *Bloccato*: le righe non sono più modificabili, ma la merce si può ancora
   ricevere e fatturare. Un responsabile acquisti può premere **Sblocca**.
#. **Annulla** annulla l'ordine e i suoi ricevimenti; è rifiutato se parte
   della merce è stata ricevuta o una fattura fornitore è validata. **Imposta
   come Bozza** riporta un ordine annullato a RdP.
#. Per eliminare un ordine selezionarlo nell'elenco e usare **Azione ‣
   Elimina**: si possono eliminare solo gli ordini annullati.
