.. help-version:: <13

   .. help-page:: account_invoice_in_form
      :title: Fattura fornitore
      :model: account.invoice
      :view: account.invoice_supplier_form
      :view-type: form
      :priority: 96

.. help-version:: 13

   .. help-page:: account_invoice_in_form
      :title: Fattura fornitore
      :model: account.move
      :view: account.view_move_form
      :view-type: form
      :when: type = in_invoice, in_refund, in_receipt
      :priority: 96

.. help-version:: >=14

   .. help-page:: account_invoice_in_form
      :title: Fattura fornitore
      :model: account.move
      :view: account.view_move_form
      :view-type: form
      :when: move_type = in_invoice, in_refund, in_receipt
      :priority: 96

Fattura fornitore
=================

.. _description:

Descrizione
-----------

Fare clic sul pulsante [`Pronto`] per sapere come usare questo aiuto; fare
clic sul pulsante [`FAQ`] per le domande più comuni già risolte.

.. help-version:: <13

   Una fattura fornitore registra quanto un :field:`fornitore <partner_id>`
   chiede di pagare per beni o servizi. Le sue rettifiche sono le **note di
   credito** del fornitore. Prodotti, quantità, prezzi e imposte sono elencati
   nella scheda **Fattura**.

   La barra dello :field:`stato <state>` in alto mostra a che punto è la
   fattura:

   * *Bozza*: la fattura si modifica liberamente; non ha numero e non ha
     effetto sui conti.
   * *Aperta*: validata. Odoo ha assegnato il :field:`numero <number>` e ha
     scritto la registrazione contabile; la fattura attende il pagamento.
   * *Pagata*: i pagamenti coprono l'intero importo.
   * *Annullata*: la fattura non conta più.

   .. help-version:: 12

      Tra *Aperta* e *Pagata* la fattura è *In pagamento*: pagata, in attesa
      che il pagamento sia abbinato all'estratto conto bancario.

.. help-version:: >=13

   Una fattura fornitore registra quanto un :field:`fornitore <partner_id>`
   chiede di pagare per beni o servizi. Le sue rettifiche sono le **note di
   credito** del fornitore. Prodotti, quantità, prezzi e imposte sono elencati
   nella scheda **Righe fattura**, i dare e avere che ne derivano nella scheda
   **Movimenti contabili**.

   Una fattura fornitore è una registrazione contabile di tipo fattura: la
   stessa maschera mostra anche le fatture clienti e le registrazioni contabili
   semplici, che hanno un loro aiuto.

   La barra dello :field:`stato <state>` in alto mostra lo stato contabile:

   * *Bozza*: la fattura si modifica liberamente e non ha effetto sui conti.
   * :version:`13|*Confermato*;*|*Confermata*`: Odoo ha assegnato il
     :field:`numero <name>` e la fattura conta nei conti.
   * *Annullata*: la fattura non conta più.

   .. help-version:: 13

      Una fascia mostra lo :field:`stato del pagamento
      <invoice_payment_state>`: *Non pagato*, *In pagamento* o *Pagata*.

   .. help-version:: >=14

      Una fascia mostra lo :field:`stato del pagamento <payment_state>`: *Non
      pagata*, *Parzialmente pagata*, *In pagamento* (pagata, in attesa
      dell'estratto conto bancario), *Pagata* o *Stornata* (annullata da una
      nota di credito).

.. help-include:: account_invoice_in_fields.rst

.. help-include:: account_invoice_in_new.rst

.. help-include:: account_invoice_in_purchase.rst

.. help-include:: account_invoice_in_update.rst

.. help-include:: account_invoice_in_cancel.rst

.. help-include:: account_invoice_in_form_actions.rst

.. help-include:: account_invoice_in_configure.rst

.. help-include:: account_invoice_in_report.rst

.. help-include:: account_invoice_in_example.rst

.. _faq:

Domande frequenti
-----------------

Fare clic sul pulsante [`Argomento`] per tornare alla pagina di aiuto specifica.

.. help-question:: Perché non riesco a modificare la fattura?

   .. help-version:: <13

      Una fattura validata è bloccata. Annullarla (il registro deve consentire
      l'annullamento delle registrazioni, vedere *Come configurare*) e premere
      [`Imposta a bozza`]. Se è pagata, togliere prima il pagamento.

   .. help-version:: >=13

      Una fattura confermata è bloccata: premere [`Reimposta a bozza`],
      modificarla e confermarla di nuovo. Se il pulsante manca, la fattura è
      in un periodo chiuso o il suo registro protegge le registrazioni;
      registrare invece una nota di credito.

.. help-question:: Perché non riesco a eliminare la fattura?

   .. help-version:: <13

      Si possono eliminare solo le fatture in bozza o annullate che non hanno
      mai ricevuto un numero. Una fattura validata mantiene il suo numero:
      annullarla, o registrare una nota di credito.

   .. help-version:: >=13

      Si possono eliminare solo le fatture in bozza, e solo se il loro numero è
      l'ultimo della sequenza, così da non lasciare buchi. Reimpostarla a bozza
      e annullarla, o registrare una nota di credito.

.. help-question:: Come pago solo una parte della fattura?

   Premere [`Registra pagamento`] e ridurre l'importo. Scegliere
   :version:`10|*Lasciare aperto*;11|*Tenere aperto*;12-13|*Lasciare
   aperta*;*|*Tieni aperta*` per pagare il resto più tardi, o
   :version:`10|*Marca la fattura come pagata interamente*;11|*Indicazione
   fattura saldata*;12|*Segnare fattura come pagata*;13|*Impostare fattura come
   pagata*;*|*Segna come totalmente pagata*` per stornare la differenza su un
   conto, ad es. per uno sconto del fornitore.

.. help-question:: Come annullo una fattura pagata?

   Togliere prima il pagamento: nei pagamenti sotto i totali fare clic
   sull'icona ⓘ del pagamento e premere [`Annulla riconciliazione`]. Poi
   annullare la fattura, o registrare una nota di credito.

.. help-question:: Perché la fattura attende ancora un pagamento già effettuato?

   Il pagamento è stato registrato senza la fattura, ad es. dall'estratto conto
   bancario: la fattura lo mostra sotto i totali come *debito in sospeso*.
   Premere [`Aggiungi`] accanto al pagamento per usarlo.

   .. help-version:: >=12

      *In pagamento* significa che il pagamento è registrato ma non ancora
      abbinato all'estratto conto bancario: la fattura diventa *Pagata* dopo la
      riconciliazione.

.. help-question:: Il totale della fattura è diverso da quello cartaceo: cosa faccio?

   Controllare le quantità, i prezzi unitari e le imposte di ogni riga, e
   l'arrotondamento (*Come configurare*): il totale della fattura deve essere
   uguale a quello scritto dal fornitore.

.. help-question:: Cosa succede se il totale della fattura è negativo?

   Una fattura con totale negativo è una nota di credito mascherata: il denaro
   arriva dal fornitore, non va al fornitore.

   .. help-version:: 10

      Odoo 10.0 non lo impedisce, ma non bisogna validarla: la fattura
      mostrerebbe l'importo come dovuto al fornitore, mentre la registrazione
      contabile riporta il contrario. Correggere le righe, oppure eliminare la
      bozza e chiedere la nota di credito al fornitore con [`Richiesta nota di
      credito`] sulla fattura originale.

   .. help-version:: 11-12

      Odoo rifiuta di validarla: *Impossibile validare una fattura con un
      importo totale negativo. Creare invece una nota di credito.* Correggere
      le righe, oppure eliminare la bozza e premere
      :version:`11|[\`Richiesta di nota di credito\`];*|[\`Richiedi nota di
      credito\`]` sulla fattura originale.

   .. help-version:: >=13

      Odoo rifiuta di confermarla: *Impossibile validare una fattura con un
      importo totale negativo. Creare invece una nota di credito. Usare il menu
      azioni per trasformarla in una nota di credito o un rimborso.* Correggere
      le righe, oppure trasformare la bozza in nota di credito con
      :version:`<=14|**Azione ‣ Cambia in rimborso/nota di credito**;<=16|**Azione
      ‣ Trasforma in fattura/nota di credito**;*|**Trasforma in fattura/nota di
      credito** nel menu sotto l'icona dell'ingranaggio`: Odoo cambia il segno
      delle quantità, così la nota di credito ha un totale positivo.

.. help-version:: 10

   .. help-include:: account_invoice_in_faq_einvoice.rst

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-22 10:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
