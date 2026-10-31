.. _update_record:

Come modificare un record
-------------------------

#. Aprire l'ordine da **Vendite ‣ Ordini ‣ Preventivi** o **Vendite ‣ Ordini ‣
   Ordini**, premere **Modifica**, cambiare i campi e premere **Salva**
   (:version:`11|**Annulla**;*|**Abbandona**` scarta le modifiche). Ogni cambio
   di stato è registrato nel chatter.
#. **Preventivo** o **Preventivo inviato**: ogni campo si può cambiare.
   Cambiare il :field:`listino prezzi <pricelist_id>` non ricalcola le righe
   già inserite: :version:`<=13|scegliere di nuovo il loro prodotto;*|premere
   **Aggiorna prezzi**`. Modificare un preventivo inviato non lo rinvia:
   inviarlo di nuovo.
#. **Ordine di vendita**: cliente, indirizzi, listino e data di scadenza
   diventano di sola lettura. Si possono ancora cambiare le quantità e
   aggiungere righe: il magazzino aggiorna la consegna e lo :field:`stato
   fatturazione <invoice_status>` è ricalcolato. Il prodotto di una riga non si
   può cambiare una volta fatturato o inviato al magazzino. Le righe non si
   possono eliminare: mettere la quantità a 0.
#. **Crea fattura** fattura quanto dovuto: :version:`<=12|scegliere *Righe
   fatturabili*, *Righe fatturabili (con anticipo dedotto)* o un anticipo
   (percentuale o valore fisso), poi **Crea fatture** o **Crea e visualizza
   fatture**;*|scegliere *Fattura normale* (con la deduzione degli anticipi
   quando ce ne sono) o un anticipo (percentuale o importo fisso), poi **Crea
   fattura** o **Crea e visualizza fattura**`.
#. **Blocca** (o l'impostazione :version:`11|*Blocca Ordini confermati*;12|*Blocca
   vendite confermate*;*|*Blocco vendite confermate*`) porta lo stato a
   *Bloccato*: l'ordine non si può più modificare, ma si può ancora
   consegnare e fatturare. **Sblocca** lo rende di nuovo modificabile.
#. Per cambiare molto un ordine confermato: premere **Annulla**, poi **Imposta
   a preventivo**, modificarlo e premere di nuovo
   :version:`11|**Conferma ordine**;*|**Conferma**`.
#. Per eliminare un preventivo selezionarlo nell'elenco e usare **Azione ‣
   Elimina**: si possono eliminare solo i preventivi non ancora inviati e gli
   ordini annullati.
