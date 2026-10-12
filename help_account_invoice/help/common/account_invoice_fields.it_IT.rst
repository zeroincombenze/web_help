.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

.. help-version:: <13

   * :field:`Cliente <partner_id>` (:field:`Fornitore <partner_id>` su una
     fattura fornitore): propone i termini di pagamento, la posizione fiscale
     e il :field:`conto crediti / debiti <account_id>`.
   * :field:`Data fattura <date_invoice>`: vuota indica la data di
     validazione. La :field:`data contabile <date>` (solo fatture fornitore)
     registra la fattura in un altro periodo.
   * :field:`Termini di pagamento <payment_term_id>` o :field:`data di
     scadenza <date_due>`: con i termini di pagamento le scadenze sono
     calcolate, altrimenti scrivere la data di scadenza.
   * :field:`Registro <journal_id>`: il registro vendite o acquisti, che dà la
     sequenza dei numeri.
   * :field:`Addetto vendite <user_id>`: chi segue la fattura, usato nelle
     analisi.
   * :field:`Documento di origine <origin>`: il documento che ha generato la
     fattura, ad es. l'ordine di vendita.
   * :field:`Riferimento fornitore <reference>` (fatture fornitore): il numero
     scritto dal fornitore sulla fattura.
   * :field:`Posizione fiscale <fiscal_position_id>`: converte imposte e
     conti, ad es. per i partner esteri.
   * :field:`Valuta <currency_id>` (impostazione *Multi-valute*).
   * :field:`Informazioni aggiuntive <comment>`: testo libero stampato sulla
     fattura.

   .. help-version:: >=11

      Il :field:`metodo di arrotondamento di cassa <cash_rounding_id>`
      (impostazione *Arrotondamento di cassa*) arrotonda il totale, ad es. a
      0,05.

   .. help-version:: 12

      Il :field:`riferimento di pagamento <reference>` (fatture clienti) è il
      riferimento che il cliente scrive sul pagamento; il :field:`conto
      bancario <partner_bank_id>` è il conto su cui il cliente paga;
      l':field:`Incoterm <incoterm_id>` è il termine di resa internazionale.

.. help-version:: >=13

   * :field:`Cliente <partner_id>` (:field:`Fornitore <partner_id>` su una
     fattura fornitore): propone i termini di pagamento e la posizione
     fiscale.
   * :field:`Data fattura <invoice_date>`: vuota indica la data di conferma;
     obbligatoria sulle fatture fornitore (la data scritta dal fornitore). La
     :field:`data contabile <date>` registra il documento in un altro periodo.
   * :field:`Termini di pagamento <invoice_payment_term_id>` o :field:`data di
     scadenza <invoice_date_due>`: con i termini di pagamento le scadenze sono
     calcolate, altrimenti scrivere la data di scadenza.
   * :field:`Registro <journal_id>` e :field:`valuta <currency_id>`: visibili
     quando ci sono più registri vendite o acquisti, o più valute.
   * :field:`Riferimento cliente / Riferimento fattura <ref>`: il riferimento
     dell'ordine del cliente, o il numero scritto dal fornitore sulla fattura.
   * :field:`Addetto vendite <invoice_user_id>`: chi segue la fattura.
   * :field:`Documento di origine <invoice_origin>`: il documento che ha
     generato la fattura, ad es. l'ordine di vendita.
   * :field:`Posizione fiscale <fiscal_position_id>`: converte imposte e
     conti, ad es. per i partner esteri.
   * :field:`Incoterm <invoice_incoterm_id>`: il termine di resa
     internazionale.
   * :field:`Metodo di arrotondamento di cassa <invoice_cash_rounding_id>`
     (impostazione *Arrotondamento di cassa*): arrotonda il totale, ad es. a
     0,05.
   * :field:`Termini e condizioni <narration>`: testo libero stampato sotto le
     righe.

   .. help-version:: 13

      Il :field:`riferimento di pagamento <invoice_payment_ref>` è il
      riferimento che il cliente scrive sul pagamento; il :field:`conto
      bancario <invoice_partner_bank_id>` è il conto su cui il cliente paga, o
      su cui si paga il fornitore.

   .. help-version:: >=14

      Il :field:`riferimento di pagamento <payment_reference>` è il
      riferimento che il cliente scrive sul pagamento; la :field:`banca del
      destinatario <partner_bank_id>` è il conto su cui il cliente paga, o su
      cui si paga il fornitore.

   .. help-version:: >=16

      L':field:`indirizzo di consegna <partner_shipping_id>` (impostazione
      *Indirizzi cliente*) è l'indirizzo dove sono consegnati i beni.

   .. help-version:: >=17

      La :field:`data di consegna <delivery_date>` è la data in cui i beni sono
      stati consegnati, stampata sulla fattura quando la legge lo richiede.
