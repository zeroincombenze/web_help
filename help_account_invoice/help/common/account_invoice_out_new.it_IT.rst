.. _new_record:

Come inserire un nuovo record
-----------------------------

.. help-version:: <13

   #. Aprire :version:`10|**Fatturazione ‣ Vendite ‣ Fatture cliente**;11|**Fatturazione
      ‣ Vendite ‣ Fatture cliente**;*|**Fatturazione ‣ Clienti ‣ Fatture**` e
      premere [`Crea`]. Le fatture si creano anche dagli ordini di vendita
      ([`Crea fattura`]).
   #. Scegliere il :field:`cliente <partner_id>` (obbligatorio): Odoo compila i
      :field:`termini di pagamento <payment_term_id>` e la :field:`posizione
      fiscale <fiscal_position_id>` dal cliente; cambiarli se serve.
   #. Scrivere la :field:`data fattura <date_invoice>`, o lasciarla vuota per
      usare la data di validazione. Senza termini di pagamento, scrivere la
      :field:`data di scadenza <date_due>`.
   #. Nella scheda **Righe fattura** premere :version:`10|[\`Aggiungi voce\`];11|[\`Aggiungi un
      elemento\`];*|[\`Aggiungi riga\`]`, scegliere il prodotto e indicare la
      quantità: descrizione, conto, prezzo e imposte sono proposti e si possono
      cambiare. Una riga senza prodotto richiede una descrizione e un conto.
   #. Controllare i totali sotto le righe e scrivere le :field:`informazioni
      aggiuntive <comment>` da stampare sulla fattura, se ce ne sono.
   #. Completare la scheda **Altre informazioni**: :field:`addetto vendite
      <user_id>`, :field:`registro <journal_id>`, :field:`documento di origine
      <origin>`.
   #. Premere [`Salva`].
      :version:`10|**PRO FORMA** (impostazione *Consentire fatture pro-forma*)
      segna la bozza come pro-forma da inviare al cliente.`
   #. Premere [`Valida`]: Odoo assegna il
      :field:`numero <number>`, scrive la registrazione contabile e lo stato
      diventa *Aperta*. :version:`10|Odoo 10.0 non blocca una fattura con
      totale negativo, ma non bisogna validarla: creare invece una nota di
      credito.;*|Odoo rifiuta di validare una fattura con totale negativo:
      creare invece una nota di credito.`
   #. Premere :version:`10|[\`Invia per Email\`];11|[\`Inviare per e-mail\`];*|[\`Invia
      e stampa\`]` per inviare al cliente la fattura con il suo PDF.

.. help-version:: >=13

   #. Aprire **Fatturazione ‣ Clienti ‣ Fatture** e premere
      :version:`<17|[\`Crea\`];*|[\`Nuovo\`]`. Le fatture si creano anche dagli
      ordini di vendita ([`Crea fattura`]).
   #. Scegliere il :field:`cliente <partner_id>` (obbligatorio): Odoo compila i
      :field:`termini di pagamento <invoice_payment_term_id>` e la
      :field:`posizione fiscale <fiscal_position_id>` dal cliente; cambiarli se
      serve.
   #. Scrivere la :field:`data fattura <invoice_date>`, o lasciarla vuota per
      usare la data di conferma. Senza termini di pagamento, scrivere la
      :field:`data di scadenza <invoice_date_due>`.
   #. Nella scheda **Righe fattura** premere [`Aggiungi riga`], scegliere il
      prodotto e indicare la quantità: descrizione, conto, prezzo e imposte
      sono proposti e si possono cambiare. [`Aggiungi sezione`] e [`Aggiungi
      nota`] organizzano le righe.
      :version:`>=18|**Catalogo** aggiunge più prodotti in una volta.`
   #. Controllare i totali sotto le righe e scrivere i :field:`termini e
      condizioni <narration>`, se ce ne sono.
   #. Completare la scheda **Altre informazioni**: :field:`riferimento cliente
      <ref>`, :field:`addetto vendite <invoice_user_id>`, :field:`posizione
      fiscale <fiscal_position_id>`, :field:`Incoterm <invoice_incoterm_id>`.
   #. :version:`<17|Premere [\`Salva\`].;*|Il record si salva automaticamente
      quando si esce, o subito con l'icona della nuvola accanto al percorso.`
   #. Premere [`Conferma`]: Odoo assegna il :field:`numero <name>` dalla
      sequenza del registro e lo stato diventa
      :version:`13|*Confermato*;*|*Confermata*`. Odoo rifiuta di confermare una
      fattura con totale negativo: creare invece una nota di credito.
   #. Premere :version:`<18|[\`Invia e stampa\`];*|[\`Invia\`]` per inviare al
      cliente la fattura con il suo PDF.
