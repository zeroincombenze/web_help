.. _example:

Esempi
------

**Prezzo sbagliato su una fattura già confermata**

.. help-version:: <13

   Se il fornitore non è ancora stato pagato e il registro consente
   l'annullamento delle registrazioni, annullare la fattura (vedere *Come
   annullare o eliminare un record*), premere [`Imposta a bozza`], correggere
   il prezzo e premere [`Valida`]: la fattura
   mantiene il suo numero. Altrimenti premere :version:`10|[\`Richiesta nota di
   credito\`];11|[\`Richiesta di nota di credito\`];*|[\`Richiedi nota di
   credito\`]`, scegliere il metodo *Modifica* e correggere la nuova fattura in
   bozza.

.. help-version:: >=13

   Se il periodo è aperto, premere [`Reimposta a bozza`], correggere il prezzo
   e premere [`Conferma`]: la fattura mantiene il suo numero. Quando la
   fattura deve restare com'è stata ricevuta, premere
   :version:`<17|[\`Aggiungi nota di credito\`];*|[\`Nota di credito\`]` e
   scegliere :version:`<17|*Rimborso completo e nuova fattura in
   bozza*;*|[\`Storna e crea fattura\`]`, poi correggere la nuova bozza.

**Pagamento in due rate**

Creare i termini di pagamento *50% subito, saldo a 30 giorni* in
**Fatturazione ‣ Configurazione ‣**
:version:`10|**Management**;11|**Gestione**;12|**Amministrazione**;*|**Fatturazione**` **‣
Termini di pagamento** e sceglierli sulla fattura: la registrazione contabile
ha due scadenze. Quando si paga la prima metà, registrarla lasciando aperto il
resto: la fattura resta :version:`<13|*Aperta*;13|*Non pagato*;*|*Parzialmente
pagata*` finché il saldo non è pagato.

**Nota di credito parziale per un prodotto reso**

Premere :version:`10|[\`Richiesta nota di credito\`];11|[\`Richiesta di nota di
credito\`];12|[\`Richiedi nota di credito\`];<17|[\`Aggiungi nota di
credito\`];*|[\`Nota di credito\`]`, scrivere il motivo (ad es. *Merce
danneggiata*) e creare una nota di credito in bozza; tenere solo la riga
restituita con la sua quantità e :version:`<13|validarla;*|confermarla`. Il
fornitore deve la differenza, oppure si paga la fattura al netto della nota di
credito.
