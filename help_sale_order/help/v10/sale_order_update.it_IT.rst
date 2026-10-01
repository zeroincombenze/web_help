.. _update_record:

Modifica record
---------------

#. Aprire l'ordine da **Vendite ‣ Vendite ‣ Preventivi** o **Vendite ‣ Vendite
   ‣ Ordini di Vendita**, premere **Modifica**, cambiare i campi e premere
   **Salva** (**Annulla** scarta le modifiche). Ogni cambio di stato è
   registrato nel chatter.
#. **Preventivo** o **Preventivo Inviato**: tutti i campi sono modificabili.
   Cambiare il :field:`listino prezzi <pricelist_id>` non ricalcola le righe
   già inserite: scegliere di nuovo il loro prodotto. Premere **(aggiornare)**
   accanto al totale per ricalcolare imposte e totali. Modificare un preventivo
   inviato non lo reinvia: premere di nuovo **Invia per Email**.
#. **Ordine di vendita**: cliente, indirizzi, listino e data di scadenza
   diventano di sola lettura. Si possono ancora cambiare le quantità e
   aggiungere righe: Magazzino aggiorna la consegna e lo :field:`stato
   fatturazione <invoice_status>` viene ricalcolato. Il prodotto di una riga
   non si può più cambiare dopo la fatturazione o l'invio al magazzino. Le
   righe non si possono eliminare: impostare la quantità a 0.
#. **Crea fattura** fattura quanto dovuto: scegliere *Righe fatturabili*,
   *Righe fatturabili (con anticipo dedotto)* o un acconto (percentuale o
   importo fisso), poi **Crea fatture** o **Crea e mostra fattura**.
#. **Blocca** (o l'impostazione *Modifiche agli Ordini di vendita* impostata a
   *Non permettere mai la modifica di un ordine di vendita confermato*) porta
   lo stato a *Bloccato*: prodotti, quantità, prezzi e imposte non sono più
   modificabili, ma l'ordine si può ancora consegnare e fatturare. Un ordine
   bloccato non si può sbloccare.
#. Per modifiche importanti a un ordine confermato: premere **Annulla**, poi
   **Converti in preventivo**, modificarlo e premere di nuovo **Conferma
   Ordine**.
#. Per eliminare un preventivo selezionarlo nell'elenco e usare **Azione ‣
   Elimina**: si possono eliminare solo i preventivi non ancora inviati e gli
   ordini annullati.
