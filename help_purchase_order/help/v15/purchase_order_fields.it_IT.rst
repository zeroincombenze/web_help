.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

* :field:`Riferimento fornitore <partner_ref>`: il numero del preventivo o
  dell'ordine di vendita del fornitore, usato per abbinare la fattura
  fornitore.
* :field:`Data ordine <date_order>`: la data della RdP, poi della conferma.
* :field:`Documento di origine <origin>`: il documento che ha generato
  l'ordine, ad es. una regola di riordino o un ordine di vendita.
* :field:`Data pianificata <date_planned>` (:version:`<=12|*Data
  pianificata*;*|*Data ricezione*`): quando è attesa la merce; ogni riga ha la
  sua data, calcolata dai tempi di consegna del fornitore.
* :field:`Consegna a <picking_type_id>`: l'operazione di ricevimento del
  magazzino (con più ubicazioni); con la spedizione diretta,
  l':field:`indirizzo di consegna diretta <dest_address_id>` del cliente.
* :field:`Termine di resa <incoterm_id>`: le condizioni commerciali
  internazionali (Incoterm) della consegna.
* :field:`Termini di pagamento <payment_term_id>`: proposti sulla fattura
  fornitore.
* :field:`Posizione fiscale <fiscal_position_id>`: converte imposte e conti, ad
  es. per i fornitori esteri.
* :field:`Stato fatturazione <invoice_status>`: *Nulla da fatturare*, *In
  attesa di fatture* o *Fatture ricevute*.
