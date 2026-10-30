.. _update_record:

Modifica record
---------------

#. Aprire l'ordine da **Acquisti ‣ Ordini ‣ Richieste di preventivo** o
   **Acquisti ‣ Ordini ‣ Ordini di acquisto** e modificare i campi; il record
   si salva quando si esce, oppure premere l'icona della nuvola. Ogni cambio di
   stato è registrato nel chatter.
#. **RdP** o **RdP inviata**: tutti i campi sono modificabili. Modificare una
   RdP inviata non la reinvia: premere **Reinvia con e-mail**.
#. **Da approvare**: un responsabile acquisti preme **Approva ordine** per
   confermarlo, oppure **Annulla** per rifiutarlo.
#. **Ordine di acquisto**: fornitore e valuta diventano di sola lettura. Si
   possono ancora cambiare quantità e prezzi e aggiungere righe: Magazzino
   aggiorna la ricezione e lo :field:`stato fatturazione <invoice_status>`
   viene ricalcolato. Le righe non si possono eliminare: impostare la quantità
   a 0. **Invia OdA con e-mail** invia l'ordine confermato al fornitore. La
   quantità **Ricevuta** dei servizi si digita sulla riga.
#. Con Magazzino installato, **Ricezione prodotti** (o il pulsante intelligente
   **Ricezione**) apre la ricezione da validare quando arriva la merce.
#. **Crea fattura** crea la fattura fornitore in bozza di quanto dovuto,
   secondo il *Controllo fatture* di ogni prodotto (quantità ordinate o
   ricevute); il pulsante intelligente **Fatture fornitore** apre le fatture.
#. **Blocca** (o l'impostazione *Blocco ordini confermati*) porta lo stato a
   *Bloccato*: le righe non sono più modificabili, ma l'ordine si può ancora
   ricevere e fatturare. Un responsabile acquisti preme **Sblocca** per
   modificarlo di nuovo.
#. Per cambiare il fornitore o gran parte dell'ordine: premere **Annulla** (le
   fatture vanno annullate prima), poi **Imposta a bozza**, modificarlo e
   premere di nuovo **Conferma ordine**.
#. Per eliminare un ordine selezionarlo nell'elenco e usare **Azioni ‣
   Elimina**: si possono eliminare solo gli ordini annullati.
