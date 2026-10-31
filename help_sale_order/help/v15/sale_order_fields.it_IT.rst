.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

.. help-version:: 11

   * :field:`Modello di preventivo <template_id>`: compila righe, prodotti
     opzionali e condizioni da un modello (impostazione *Modelli di
     preventivi*).

.. help-version:: >=12

   * :field:`Modello di preventivo <sale_order_template_id>`: compila righe,
     prodotti opzionali e condizioni da un modello (impostazione *Modelli
     preventivo*).

* :field:`Listino prezzi <pricelist_id>`: prezzi e sconti automatici per il
  cliente (impostazione dei listini).
* :field:`Termini di pagamento <payment_term_id>`: scadenze delle fatture.
* **Sconto %** sulle righe dell'ordine (impostazione *Sconti*).
* :field:`Addetto vendite <user_id>` e :field:`team di vendita <team_id>`: chi
  segue l'ordine, usati nei rendiconti.
* :field:`Riferimento cliente <client_order_ref>`: il numero d'ordine del
  cliente, stampato sui documenti.
* :field:`Posizione fiscale <fiscal_position_id>`: converte imposte e conti, ad
  es. per i clienti esteri.
* :field:`Documento di origine <origin>`: il documento che ha generato
  l'ordine.
* :field:`Stato fatturazione <invoice_status>`: se resta qualcosa da
  fatturare.
