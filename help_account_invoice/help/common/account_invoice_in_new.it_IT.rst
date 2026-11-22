.. _new_record:

Come inserire un nuovo record
-----------------------------

.. help-version:: <13

   #. Aprire :version:`10|**Fatturazione ‣ Acquisti ‣ Fatture fornitori**;11|**Fatturazione
      ‣ Acquisti ‣ Fatture fornitore**;*|**Fatturazione ‣ Fornitori ‣
      Fatture**` e premere [`Crea`].
   #. Scegliere il :field:`fornitore <partner_id>` (obbligatorio): Odoo compila
      i :field:`termini di pagamento <payment_term_id>` e la :field:`posizione
      fiscale <fiscal_position_id>` dal fornitore; cambiarli se serve.
   #. Scrivere il :field:`riferimento fornitore <reference>`, il numero scritto
      dal fornitore sulla sua fattura, e la :field:`data fattura
      <date_invoice>`, o lasciarla vuota per usare la data di validazione.
      Senza termini di pagamento, scrivere la :field:`data di scadenza
      <date_due>`.
   #. Nella scheda **Fattura** premere :version:`10|[\`Aggiungi voce\`];11|[\`Aggiungi un
      elemento\`];*|[\`Aggiungi riga\`]`, scegliere il prodotto e indicare la
      quantità: descrizione, conto, prezzo e imposte di acquisto sono proposti
      e si possono cambiare. Una riga senza prodotto richiede una descrizione e
      un conto.
   #. Controllare i totali sotto le righe rispetto alla fattura cartacea e
      scrivere le :field:`informazioni aggiuntive <comment>`, se ce ne sono.
   #. Completare la scheda **Altre informazioni**: :field:`registro
      <journal_id>` e, se serve, la :field:`data contabile <date>`. Il
      :field:`documento di origine <origin>` è scritto dal documento che genera
      la fattura, ad es. l'ordine di acquisto, e compare solo se compilato.
   #. Premere [`Salva`].
   #. Premere [`Valida`]: Odoo assegna il
      :field:`numero <number>`, scrive la registrazione contabile e lo stato
      diventa *Aperta*. :version:`10|Odoo 10.0 non blocca una fattura con
      totale negativo, ma non bisogna validarla: creare invece una nota di
      credito.;*|Odoo rifiuta di validare una fattura con totale negativo:
      creare invece una nota di credito.`
   #. Per pagarla, vedere *Altre azioni*.

.. help-version:: >=13

   #. Aprire **Fatturazione ‣ Fornitori ‣**
      :version:`14-15,17|**Fatture fornitore**;*|**Fatture**` e premere
      :version:`<17|[\`Crea\`];*|[\`Nuovo\`]`\ :version:`>=17|, o premere
      [\`Carica\`] per creare la fattura dal PDF inviato dal fornitore`.

      .. help-if:: module = purchase

         Le fatture si creano anche dagli ordini di acquisto, vedere *Fattura
         da ordine fornitore*.

   #. Scegliere il :field:`fornitore <partner_id>` (obbligatorio): Odoo compila
      i :field:`termini di pagamento <invoice_payment_term_id>` e la
      :field:`posizione fiscale <fiscal_position_id>` dal fornitore; cambiarli
      se serve.
   #. Scrivere il :field:`riferimento fattura <ref>`, il numero scritto dal
      fornitore sulla sua fattura, e la :field:`data fattura <invoice_date>`
      (obbligatoria). Senza termini di pagamento, scrivere la :field:`data di
      scadenza <invoice_date_due>`. La :field:`data contabile <date>`
      registra la fattura in un altro periodo.

      .. help-version:: 13

         Il :field:`riferimento di pagamento <invoice_payment_ref>` è il
         riferimento da scrivere sul pagamento; il :field:`conto bancario
         <invoice_partner_bank_id>` è il conto del fornitore su cui si paga.

      .. help-version:: >=14

         Il :field:`riferimento di pagamento <payment_reference>` è il
         riferimento da scrivere sul pagamento; la :field:`banca del
         destinatario <partner_bank_id>` è il conto del fornitore su cui si
         paga.

   #. Nella scheda **Righe fattura** premere [`Aggiungi riga`], scegliere il
      prodotto e indicare la quantità: descrizione, conto, prezzo e imposte di
      acquisto sono proposti e si possono cambiare. [`Aggiungi sezione`] e
      [`Aggiungi nota`] organizzano le righe.
      :version:`>=18|**Catalogo** aggiunge più prodotti in una volta.`
   #. Controllare i totali sotto le righe rispetto alla fattura cartacea e
      scrivere i :field:`termini e condizioni <narration>`, se ce ne sono.
   #. Completare la scheda **Altre informazioni**: :field:`posizione fiscale
      <fiscal_position_id>` e, se serve, gli altri campi della scheda.
   #. :version:`<17|Premere [\`Salva\`].;*|Il record si salva automaticamente
      quando si esce, o subito con l'icona della nuvola accanto al percorso.`
   #. Premere [`Conferma`]: Odoo assegna il :field:`numero <name>` dalla
      sequenza del registro e lo stato diventa
      :version:`13|*Confermato*;*|*Confermata*`. Odoo rifiuta di confermare una
      fattura con totale negativo: creare invece una nota di credito.
   #. Per pagarla, vedere *Altre azioni*.
