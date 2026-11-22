.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

.. help-version:: <13

   * :field:`Fornitore <partner_id>`: propone i termini di pagamento, la
     posizione fiscale e il :field:`conto debiti <account_id>`.
   * :field:`Riferimento fornitore <reference>`: il numero scritto dal
     fornitore sulla fattura.
   * :field:`Data fattura <date_invoice>`: vuota indica la data di
     validazione. La :field:`data contabile <date>` registra la fattura in un
     altro periodo.
   * :field:`Termini di pagamento <payment_term_id>` o :field:`data di
     scadenza <date_due>`: con i termini di pagamento le scadenze sono
     calcolate, altrimenti scrivere la data di scadenza.
   * :field:`Registro <journal_id>`: il registro acquisti, che dà la sequenza
     dei numeri.
   * :field:`Documento di origine <origin>`: il documento che ha generato la
     fattura, ad es. l'ordine di acquisto.
   * :field:`Posizione fiscale <fiscal_position_id>`: converte imposte e
     conti, ad es. per i fornitori esteri.
   * :field:`Valuta <currency_id>` (impostazione :version:`<12|*Multi-valute*;*|*Multi valuta*`).
   * :field:`Informazioni aggiuntive <comment>`: testo libero.

.. help-version:: >=13

   * :field:`Fornitore <partner_id>`: propone i termini di pagamento e la
     posizione fiscale.
   * :field:`Riferimento fattura <ref>`: il numero scritto dal fornitore sulla
     fattura.
   * :field:`Data fattura <invoice_date>`: la data scritta dal fornitore,
     obbligatoria. La :field:`data contabile <date>` registra la fattura in un
     altro periodo.
   * :field:`Termini di pagamento <invoice_payment_term_id>` o :field:`data di
     scadenza <invoice_date_due>`: con i termini di pagamento le scadenze sono
     calcolate, altrimenti scrivere la data di scadenza.
   * :field:`Registro <journal_id>` e :field:`valuta <currency_id>`: visibili
     quando ci sono più registri acquisti, o più valute.
   * :field:`Documento di origine <invoice_origin>`: il documento che ha
     generato la fattura, ad es. l'ordine di acquisto.
   * :field:`Posizione fiscale <fiscal_position_id>`: converte imposte e
     conti, ad es. per i fornitori esteri.
   * :field:`Metodo di arrotondamento di cassa <invoice_cash_rounding_id>`
     (impostazione *Arrotondamento di cassa*): arrotonda il totale, ad es. a
     0,05.
   * :field:`Termini e condizioni <narration>`: testo libero.

   .. help-version:: 13

      Il :field:`riferimento di pagamento <invoice_payment_ref>` è il
      riferimento da scrivere sul pagamento al fornitore; il :field:`conto
      bancario <invoice_partner_bank_id>` è il conto del fornitore su cui si
      paga.

   .. help-version:: >=14

      Il :field:`riferimento di pagamento <payment_reference>` è il
      riferimento da scrivere sul pagamento al fornitore; la :field:`banca del
      destinatario <partner_bank_id>` è il conto del fornitore su cui si paga.
