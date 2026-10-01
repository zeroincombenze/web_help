.. _usage:

Utilizzo
--------

#. Aprire **Vendite ‣ Vendite ‣ Preventivi** e premere **Crea**.
#. Scegliere il :field:`cliente <partner_id>`. Odoo compila dal cliente il
   :field:`listino prezzi <pricelist_id>` e i
   :field:`termini di pagamento <payment_term_id>` e, con l'impostazione
   *Indirizzi cliente*, l':field:`indirizzo di fatturazione <partner_invoice_id>`
   e l':field:`indirizzo di consegna <partner_shipping_id>`; modificarli se
   necessario.
#. Impostare la :field:`data di scadenza <validity_date>` del preventivo.
#. Nella scheda **Righe ordine** premere **Aggiungi un elemento**, scegliere il
   prodotto e indicare la quantità; prezzo, imposte e sconto sono proposti dal
   listino.
#. Completare la scheda **Altre informazioni** (addetto vendite, riferimento
   cliente, posizione fiscale, …) e scrivere i
   :field:`termini e condizioni <note>`.
#. Premere **Invia via e-mail** per inviare il preventivo, lo stato diventa
   *Preventivo inviato*; **Stampa** produce il PDF.
#. Premere **Conferma vendita** quando il cliente accetta: il preventivo
   diventa un *Ordine di vendita* e, se Magazzino è installato, viene creata la
   consegna.
#. Premere **Crea fattura** e scegliere cosa fatturare: *Righe fatturabili*,
   *Righe fatturabili (dedotti gli acconti)* o un acconto (percentuale o
   importo fisso), poi **Crea e visualizza fatture**.
#. **Annulla** annulla l'ordine e **Imposta come preventivo** lo riporta in
   bozza; **Blocca** chiude un ordine confermato a ulteriori modifiche.
