.. _new_record:

Nuovo record
------------

#. Aprire **Vendite ‣ Ordini ‣ Preventivi** e premere **Nuovo**. Un preventivo
   si può creare anche da un'opportunità CRM con **Nuovo preventivo**.
#. Scegliere il :field:`cliente <partner_id>` (obbligatorio): digitare alcune
   lettere del nome, oppure scegliere *Crea e modifica…* per un nuovo cliente.
   Odoo compila dal cliente l':field:`indirizzo di fatturazione
   <partner_invoice_id>`, l':field:`indirizzo di consegna
   <partner_shipping_id>` (visibili con l'impostazione *Indirizzi cliente*), il
   :field:`listino prezzi <pricelist_id>` e i :field:`termini di pagamento
   <payment_term_id>`; modificarli se necessario. Termini di pagamento vuoti
   significano *Pagamento immediato*.
#. Se serve, scegliere un :field:`modello di preventivo
   <sale_order_template_id>`: compila righe, prodotti opzionali, condizioni e
   validità.
#. Controllare la :field:`data di scadenza <validity_date>`, proposta
   dall'impostazione *Validità predefinita del preventivo*: dopo di essa il
   cliente non può più accettare il preventivo online.
#. Nella scheda **Righe ordine** premere **Aggiungi prodotto**, scegliere il
   prodotto e indicare la quantità; prezzo, imposte e sconto sono proposti dal
   listino e si possono cambiare. :version:`>=17|**Catalogo** aggiunge più
   prodotti in una volta.` **Aggiungi sezione** e **Aggiungi nota** organizzano
   le righe; trascinare la maniglia a sinistra per riordinarle. **Sconto**
   (impostazione *Sconti*) applica uno sconto globale a tutte le righe.
#. Scrivere i :field:`termini e condizioni <note>` sotto le righe, se non
   arrivano dalle impostazioni o dal modello.
#. Completare la scheda **Altre informazioni**: :field:`addetto vendite
   <user_id>`, :field:`team di vendita <team_id>`, :field:`riferimento cliente
   <client_order_ref>`, :field:`etichette <tag_ids>`, :field:`firma online
   <require_signature>` e :field:`pagamento online <require_payment>`,
   :field:`data di consegna <commitment_date>`, :field:`posizione fiscale
   <fiscal_position_id>`. In **Prodotti opzionali** elencare i prodotti che il
   cliente può aggiungere dal portale.
#. Il record si salva automaticamente quando si esce; premere l'icona della
   nuvola accanto al percorso per salvare subito. Odoo assegna il
   :field:`numero <name>` (es. *S00042*).
#. Premere **Invia con e-mail** per inviare il preventivo con il suo PDF: lo
   stato diventa *Preventivo inviato*. **Anteprima** lo mostra come lo vede il
   cliente nel portale.
#. Premere **Conferma** quando il cliente accetta (oppure lasciare che firmi o
   paghi online): il preventivo diventa un *Ordine di vendita* e, se Magazzino
   è installato, viene creata la consegna. Odoo non conferma se una riga è
   senza prodotto.
