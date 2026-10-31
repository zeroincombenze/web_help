.. _new_record:

Come inserire un nuovo record
-----------------------------

#. Aprire :version:`11|**Acquisti ‣ Acquisto**;12|**Acquisti ‣
   Acquisti**;*|**Acquisti ‣ Ordini**` **‣ Richieste di preventivo** e premere
   **Crea**.
#. Scegliere il :field:`fornitore <partner_id>` (obbligatorio): scrivere
   qualche lettera del nome, o scegliere *Crea e modifica...* per aggiungere un
   nuovo fornitore. Odoo compila i :field:`termini di pagamento
   <payment_term_id>`, la :field:`posizione fiscale <fiscal_position_id>` e la
   valuta dal fornitore.
#. Scrivere il :field:`riferimento fornitore <partner_ref>` se il fornitore ha
   già inviato un preventivo.
#. Nella scheda **Prodotti** premere :version:`11|**Aggiungi
   voce**;*|**Aggiungi prodotto**`, scegliere il prodotto e impostare la
   quantità; descrizione, data pianificata, prezzo unitario e imposte sono
   proposti dall'elenco fornitori del prodotto e si possono cambiare.
#. Scrivere i :field:`termini e condizioni <notes>` sotto le righe.
#. Completare la scheda :version:`11|**Consegne & Fatture**;*|**Altre
   informazioni**`: :field:`data pianificata <date_planned>`, :field:`termine
   di resa <incoterm_id>`, termini di pagamento.
#. Premere **Salva**: Odoo assegna il :field:`riferimento <name>` (es.
   *PO00042*).
#. Premere :version:`11|**Invia RDP per email**;*|**Invia con e-mail**` per
   inviare la richiesta al fornitore, lo stato diventa *RdP inviata*;
   :version:`<=12|**Stampa RDP**;*|**Stampa RdP**` produce il PDF.
#. Premere **Conferma ordine** quando il fornitore è d'accordo: la RdP diventa
   un *Ordine di acquisto*, il fornitore è aggiunto ai fornitori dei prodotti
   e, se il Magazzino è installato, è creato il ricevimento. Con
   l'approvazione degli ordini lo stato diventa invece *Da approvare*.
