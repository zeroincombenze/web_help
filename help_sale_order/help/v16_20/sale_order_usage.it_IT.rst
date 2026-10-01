.. _usage:

Utilizzo
--------

#. Aprire **Vendite ‣ Ordini ‣ Preventivi** e premere **Nuovo**.
#. Scegliere il :field:`cliente <partner_id>`. Odoo compila dal cliente l'
   :field:`indirizzo di fatturazione <partner_invoice_id>`, l'
   :field:`indirizzo di consegna <partner_shipping_id>`, il
   :field:`listino prezzi <pricelist_id>` e i
   :field:`termini di pagamento <payment_term_id>`; modificarli se necessario.
#. Impostare la :field:`data di scadenza <validity_date>`: dopo di essa il
   cliente non può più accettare il preventivo online.
#. Nella scheda **Righe ordine** premere **Aggiungi un prodotto**, scegliere il
   prodotto e indicare la quantità; prezzo, imposte e sconto sono proposti dal
   listino. Su Odoo 18 **Catalogo** aggiunge più prodotti in una volta.
   **Aggiungi una sezione** e **Aggiungi una nota** organizzano le righe;
   trascinare la maniglia a sinistra per riordinarle.
#. Completare la scheda **Altre informazioni** (addetto vendite, riferimento
   cliente, data di consegna, …) e scrivere i
   :field:`termini e condizioni <note>`.
#. Premere **Invia via e-mail** per inviare il preventivo: lo stato diventa
   *Preventivo inviato*. **Anteprima** lo mostra come lo vede il cliente nel
   portale.
#. Premere **Conferma** quando il cliente accetta: il preventivo diventa un
   *Ordine di vendita* e, se Magazzino è installato, viene creata la consegna.
#. Premere **Crea fattura** e scegliere *Fattura regolare* o un acconto
   (percentuale o importo fisso), poi **Crea e visualizza fattura**.
#. **Annulla** annulla l'ordine; **Blocca** impedisce ulteriori modifiche a un
   ordine confermato.
