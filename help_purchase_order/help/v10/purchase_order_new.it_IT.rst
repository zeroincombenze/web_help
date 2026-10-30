.. _new_record:

Nuovo record
------------

#. Aprire **Acquisti ‣ Acquisto ‣ Richieste di preventivo** e premere **Crea**.
#. Scegliere il :field:`fornitore <partner_id>` (obbligatorio): digitare alcune
   lettere del nome, oppure scegliere *Crea e Modifica...* per un nuovo
   fornitore. Odoo compila dal fornitore i :field:`termini di pagamento
   <payment_term_id>`, la :field:`posizione fiscale <fiscal_position_id>` e la
   valuta.
#. Digitare il :field:`riferimento fornitore <partner_ref>` se il fornitore ha
   già inviato un preventivo.
#. Nella scheda **Prodotti** premere **Aggiungi voce**, scegliere il prodotto e
   indicare la quantità; descrizione, data pianificata, prezzo unitario e
   imposte sono proposti dall'elenco fornitori del prodotto e si possono
   cambiare.
#. Scrivere i :field:`termini e condizioni <notes>` sotto le righe.
#. Completare la scheda **Consegne & Fatture**: :field:`data pianificata
   <date_planned>` (il pulsante calendario la copia su tutte le righe),
   :field:`incoterm <incoterm_id>`, termini di pagamento.
#. Premere **Salva**: Odoo assegna il :field:`riferimento <name>` (es.
   *PO00042*).
#. Premere **Invia RdP per Email** per inviare la richiesta al fornitore, lo
   stato diventa *RFQ Inviata*; **Stampa RdP** produce il PDF.
#. Premere **Conferma Ordine** quando il fornitore accetta: la RdP diventa un
   *Ordine di Acquisto*, il fornitore viene aggiunto ai fornitori dei prodotti
   e, se Magazzino è installato, viene creato il ricevimento. Con 2 livelli di
   approvazione lo stato diventa invece *Da Approvare*.
