.. _new_record:

Nuovo record
------------

#. Aprire **Vendite ‣ Vendite ‣ Preventivi** e premere **Crea**.
#. Scegliere il :field:`cliente <partner_id>` (obbligatorio): digitare alcune
   lettere del nome, oppure scegliere *Crea e Modifica...* per un nuovo
   cliente. Odoo compila dal cliente il :field:`listino prezzi <pricelist_id>`
   e i :field:`termini di pagamento <payment_term_id>` e, con l'impostazione
   *Indirizzi*, l':field:`indirizzo di fatturazione <partner_invoice_id>` e
   l':field:`indirizzo di consegna <partner_shipping_id>`; modificarli se
   necessario.
#. Impostare la :field:`data di scadenza <validity_date>` del preventivo.
#. Nella scheda **Righe Ordine** premere **Aggiungi voce**, scegliere il
   prodotto e indicare la quantità; prezzo, imposte e sconto sono proposti dal
   listino e si possono cambiare.
#. Scrivere i :field:`termini e condizioni <note>` sotto le righe.
#. Completare la scheda **Altre informazioni** (addetto vendite, team di
   vendita, riferimento cliente, posizione fiscale, …).
#. Premere **Salva**: Odoo assegna il :field:`numero <name>` (es. *SO042*).
#. Premere **Invia per Email** per inviare il preventivo, lo stato diventa
   *Preventivo Inviato*; **Stampa** produce il PDF.
#. Premere **Conferma Ordine** quando il cliente accetta: il preventivo diventa
   un *Ordine di vendita* e, se Magazzino è installato, viene creata la
   consegna.
