.. _update_record:

Modifica record
---------------

#. Aprire l'ordine da **Vendite ‣ Ordini ‣ Preventivi** o **Vendite ‣ Ordini ‣
   Ordini** e modificare i campi; il record si salva quando si esce, oppure
   premere l'icona della nuvola. Ogni cambio di stato è registrato nel chatter.
#. **Preventivo** o **Preventivo inviato**: tutti i campi sono modificabili.
   Dopo aver cambiato il :field:`listino prezzi <pricelist_id>` premere
   **Aggiorna prezzi** per ricalcolare i prezzi delle righe; dopo aver cambiato
   la :field:`posizione fiscale <fiscal_position_id>` premere **Aggiorna
   tasse**. Modificare un preventivo inviato non lo reinvia: premere di nuovo
   **Invia con e-mail**.
#. **Ordine di vendita**: cliente, listino, data di scadenza e modello
   diventano di sola lettura. Si possono ancora aumentare o ridurre le quantità
   e aggiungere righe: Magazzino aggiorna la consegna e lo :field:`stato
   fatturazione <invoice_status>` viene ricalcolato. Il prodotto di una riga si
   può cambiare solo finché non è consegnato o fatturato. Le righe non si
   possono eliminare: impostare la quantità a 0. La quantità **Consegnati** di
   servizi e prodotti manuali si digita sulla riga.
#. **Crea fattura** fattura quanto dovuto: scegliere *Fattura normale* o un
   acconto (percentuale o importo fisso), poi :version:`16|**Crea e visualizza
   fattura**;17|**Crea bozza fattura**;*|**Crea bozza**`. Il pulsante
   intelligente **Fatture** le apre.
#. Ordine **bloccato** (impostazione *Blocco vendite confermate*, o **Blocca**
   premuto da un amministratore vendite): righe e data di consegna non sono
   modificabili, ma l'ordine si può ancora consegnare e fatturare. Un
   amministratore vendite preme **Sblocca** per modificarlo di nuovo.
   :version:`16|Lo stato diventa *Bloccato*.;*|Compare un lucchetto e lo stato
   resta *Ordine di vendita*.`
#. Per modifiche importanti a un ordine confermato: sbloccarlo se serve,
   premere **Annulla** (una procedura guidata propone di avvisare il cliente
   via e-mail; le fatture in bozza sono annullate), poi **Imposta a
   preventivo**, modificarlo e **Conferma** di nuovo.
#. Per eliminare un preventivo selezionarlo nell'elenco e usare **Azioni ‣
   Elimina**: si possono eliminare solo i preventivi non ancora inviati e gli
   ordini annullati.
