.. _new_record:

Come inserire un nuovo record
-----------------------------

#. Aprire **Vendite ‣ Ordini ‣ Preventivi** e premere **Crea**.
#. Scegliere il :field:`cliente <partner_id>` (obbligatorio): scrivere qualche
   lettera del nome, o scegliere *Crea e modifica...* per aggiungere un nuovo
   cliente. Odoo compila il :field:`listino prezzi <pricelist_id>` e i
   :field:`termini di pagamento <payment_term_id>` dal cliente e, con
   l'impostazione *Indirizzi cliente*, l':field:`indirizzo di fatturazione
   <partner_invoice_id>` e l':field:`indirizzo di consegna
   <partner_shipping_id>`; cambiarli se serve.
#. Impostare la :field:`data di scadenza <validity_date>` del
   preventivo\ :version:`>=12|, proposta dall'impostazione *Validità
   predefinita del preventivo*`.
#. Nella scheda **Righe ordine** premere :version:`11|**Aggiungi
   voce**;*|**Aggiungi prodotto**`, scegliere il prodotto e impostare la
   quantità; prezzo, imposte e sconto sono proposti dal listino e si possono
   cambiare. :version:`>=12|**Aggiungi sezione** e **Aggiungi nota**
   organizzano le righe.`
#. Scrivere i :field:`termini e condizioni <note>` sotto le righe.
#. Completare la scheda **Altre informazioni** (addetto vendite, team di
   vendita, riferimento cliente, posizione fiscale, …).
#. Premere **Salva**: Odoo assegna il :field:`numero <name>` (es. *SO042*).
#. Premere :version:`11|**Invia per Email**;*|**Invia con e-mail**` per
   inviare il preventivo, il suo stato diventa *Preventivo inviato*;
   :version:`<=12|**Stampa** produce il PDF;*|il menu **Stampa** produce il
   PDF`.
#. Premere :version:`11|**Conferma ordine**;*|**Conferma**` quando il cliente
   accetta: il preventivo diventa un *Ordine di vendita*, e la consegna è
   creata se il Magazzino è installato.
