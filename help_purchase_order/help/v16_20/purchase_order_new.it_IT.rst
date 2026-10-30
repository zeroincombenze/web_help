.. _new_record:

Nuovo record
------------

#. Aprire **Acquisti ‣ Ordini ‣ Richieste di preventivo** e premere **Nuovo**.
   Le RdP sono create anche automaticamente dalle regole di riordino e dal
   percorso *Acquista* dei prodotti.
#. Scegliere il :field:`fornitore <partner_id>` (obbligatorio): digitare alcune
   lettere del nome, la partita IVA o l'e-mail, oppure scegliere *Crea e
   modifica…* per un nuovo fornitore. Odoo compila dal fornitore i
   :field:`termini di pagamento <payment_term_id>`, la :field:`posizione
   fiscale <fiscal_position_id>` e la valuta; modificarli se necessario.
#. Digitare il :field:`riferimento fornitore <partner_ref>` se il fornitore ha
   già inviato un'offerta.
#. Controllare la :field:`scadenza per ordine <date_order>` e l':field:`arrivo
   previsto <date_planned>`.
#. Nella scheda **Prodotti** premere **Aggiungi prodotto**, scegliere il
   prodotto e indicare la quantità; il prezzo unitario arriva dal listino
   fornitore del prodotto e si può cambiare. :version:`>=17|**Catalogo**
   aggiunge più prodotti in una volta.` **Aggiungi sezione** e **Aggiungi
   nota** organizzano le righe; trascinare la maniglia a sinistra per
   riordinarle.
#. Scrivere i :field:`termini e condizioni <notes>` sotto le righe.
#. Completare la scheda **Altre informazioni**: :field:`acquirente <user_id>`,
   :field:`documento di origine <origin>`, :field:`termini di pagamento
   <payment_term_id>`, :field:`posizione fiscale <fiscal_position_id>`.
#. Il record si salva automaticamente quando si esce; premere l'icona della
   nuvola accanto al percorso per salvare subito. Odoo assegna il
   :field:`riferimento <name>` (es. *P00042*).
#. Premere **Invia con e-mail** per inviare la RdP al fornitore con il suo PDF:
   lo stato diventa *RdP inviata*. **Stampa RdP** produce il PDF.
#. Premere **Conferma ordine** quando l'offerta del fornitore è accettata: la
   RdP diventa un *Ordine di acquisto*, il fornitore viene aggiunto al listino
   fornitore dei prodotti non ancora acquistati da lui e, se Magazzino è
   installato, viene creata la ricezione. Con l'impostazione *Approvazione
   ordine di acquisto* un ordine sopra l'importo minimo passa invece a *Da
   approvare*, a meno di essere un responsabile acquisti.
