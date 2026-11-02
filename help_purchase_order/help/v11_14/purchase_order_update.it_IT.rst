.. _update_record:

Come modificare un record
-------------------------

#. Aprire l'ordine dal suo elenco (**Richieste di preventivo** o **Ordini di
   acquisto**), premere **Modifica**, cambiare i campi e premere **Salva**
   (:version:`11|**Annulla**;*|**Abbandona**` scarta le modifiche). Ogni cambio
   di stato è registrato nel chatter.
#. **RdP** o **RdP inviata**: ogni campo si può cambiare. Modificare una RdP
   inviata non la rinvia: premere :version:`11|**Rispedisci RDP per
   email**;*|**Reinvia con e-mail**`.
#. **Da approvare**: un responsabile acquisti preme :version:`12|**Approva Ordine**;*|**Approva ordine**` per
   confermarlo.
#. **Ordine di acquisto**: fornitore, data ordine, valuta e il prodotto delle
   righe diventano di sola lettura. Si possono ancora cambiare quantità e
   prezzi e aggiungere righe: il magazzino aggiorna il ricevimento. Le righe
   non si possono eliminare: mettere la quantità a 0.
   :version:`11|**Invia PO per email**;12|**Invia OA con e-mail**;*|**Invia
   OdA con e-mail**` invia l'ordine confermato al fornitore.
#. :version:`12|**Ricevi Prodotti** (o il pulsante del ricevimento)
   apre;<=14|**Ricevi prodotti** (o il pulsante del ricevimento) apre;*|Il pulsante **Ricezione** apre` il ricevimento: indicare le
   quantità ricevute e premere **Valida**. Un ricevimento parziale crea un
   ordine residuo per la merce mancante.
#. :version:`11|Il pulsante **Fatture fornitore** crea la fattura fornitore
   dall'ordine, o apre quelle esistenti;*|**Crea fattura** crea la fattura
   fornitore dall'ordine, e il pulsante **Fatture fornitore** apre quelle
   esistenti`. In una nuova fattura fornitore, il campo
   :version:`<=12|**Aggiungi Ordine d'Acquisto**;*|**Autocompletamento**`
   carica le righe di un ordine. Le quantità proposte dipendono dalla
   *Politica di controllo* del prodotto; lo :field:`stato fatturazione
   <invoice_status>` è poi ricalcolato.
#. **Blocca** (o l'impostazione :version:`<=13|*Blocca Ordini
   confermati*;*|*Blocco ordini confermati*`) porta lo stato a *Bloccato*: le
   righe non si possono più cambiare, ma la merce si può ancora ricevere e
   fatturare. Un responsabile acquisti può premere **Sblocca**.
#. **Annulla** annulla l'ordine e i suoi ricevimenti; è rifiutato quando una
   parte della merce è ricevuta o una fattura fornitore non è annullata.
   **Imposta a bozza** riporta un ordine annullato a RdP.
#. Per eliminare un ordine selezionarlo nell'elenco e usare **Azione ‣
   Elimina**: si possono eliminare solo gli ordini annullati.
