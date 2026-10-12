.. _example:

Esempi
------

**Prezzo sbagliato su una fattura già inviata**

.. help-version:: <13

   Se il cliente non ha ancora pagato e il registro consente l'annullamento
   delle registrazioni, premere **Annullare fattura**,
   :version:`10|**Riportare in bozza**;*|**Reimposta a bozza**`, correggere il
   prezzo e premere :version:`10|**Validare**;*|**Valida**`: la fattura
   mantiene il suo numero. Altrimenti premere :version:`10|**Nota di
   credito**;*|**Aggiungi nota di credito**`, scegliere il metodo *Modifica* e
   correggere la nuova fattura in bozza.

.. help-version:: >=13

   Se il periodo è aperto, premere **Reimposta a bozza**, correggere il prezzo
   e premere **Conferma**: la fattura mantiene il suo numero. Quando la fattura
   deve restare com'è stata inviata (ad es. una fattura elettronica già
   consegnata), premere :version:`<18|**Aggiungi nota di credito**;*|**Nota di
   credito**` e scegliere :version:`<17|*Rimborso completo e nuova fattura in
   bozza*;*|**Storna e crea fattura**`, poi correggere la nuova bozza.

**Pagamento in due rate**

Creare i termini di pagamento *50% subito, saldo a 30 giorni* in
**Fatturazione ‣ Configurazione ‣**
:version:`<12|**Gestione**;12|**Amministrazione**;*|**Fatturazione**` **‣
Termini di pagamento** e sceglierli sulla fattura: la registrazione contabile
ha due scadenze. Quando arriva la prima metà, registrarla lasciando aperto il
resto: la fattura resta :version:`<13|*Aperta*;13|*Non pagato*;*|*Parzialmente
pagata*` finché il saldo non è pagato.

**Rimborso parziale di un prodotto reso**

Premere :version:`10|**Nota di credito**;<18|**Aggiungi nota di
credito**;*|**Nota di credito**`, scrivere il motivo (ad es. *Merce
danneggiata*) e creare una nota di credito in bozza; tenere solo la riga
restituita con la sua quantità e :version:`<13|validarla;*|confermarla`. Il
cliente deve la differenza, oppure si rimborsa l'importo della nota di
credito.
