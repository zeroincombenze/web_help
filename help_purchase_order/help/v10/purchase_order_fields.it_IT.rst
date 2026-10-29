.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

* :field:`Riferimento fornitore <partner_ref>`: il numero del preventivo o
  dell'ordine di vendita del fornitore, usato per abbinare la fattura.
* :field:`Data ordine <date_order>`: la data della RdP, poi della conferma.
* :field:`Documento di origine <origin>`: il documento che ha generato
  l'ordine, ad es. una regola di riapprovvigionamento o un ordine di vendita.
* :field:`Data pianificata <date_planned>`: quando è attesa la merce; ogni riga
  ha la sua data, calcolata dal tempo di consegna del fornitore.
* :field:`Consegna <picking_type_id>`: l'operazione di ricevimento del
  magazzino (con più ubicazioni); con il dropshipping, l':field:`indirizzo
  dropshipping <dest_address_id>` del cliente.
* :field:`Incoterm <incoterm_id>`: i termini commerciali internazionali della
  consegna.
* :field:`Termini di pagamento <payment_term_id>`: proposti sulla fattura del
  fornitore.
* :field:`Posizione fiscale <fiscal_position_id>`: converte imposte e conti, ad
  es. per i fornitori esteri.
* :field:`Stato fatturazione <invoice_status>`: *Niente da Fatturare*, *Attesa
  fattura* o *Fatture Ricevute*.
