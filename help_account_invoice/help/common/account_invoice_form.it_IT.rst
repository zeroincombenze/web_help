.. help-version:: <13

   .. help-page:: account_invoice_form
      :title: Fattura
      :model: account.invoice
      :view: account.invoice_form, account.invoice_supplier_form
      :view-type: form
      :priority: 96

.. help-version:: 13

   .. help-page:: account_invoice_form
      :title: Fattura
      :model: account.move
      :view: account.view_move_form
      :view-type: form
      :when: type != entry
      :priority: 96

.. help-version:: >=14

   .. help-page:: account_invoice_form
      :title: Fattura
      :model: account.move
      :view: account.view_move_form
      :view-type: form
      :when: move_type != entry
      :priority: 96

Fattura
=======

.. _description:

Descrizione
-----------

.. help-version:: <13

   Una fattura chiede al :field:`cliente <partner_id>` il pagamento di beni o
   servizi; una **fattura fornitore** registra quanto un fornitore chiede di
   pagare. Le loro rettifiche sono le **note di credito**. Prodotti, quantità,
   prezzi e imposte sono elencati nella scheda **Righe fattura**.

   La barra dello :field:`stato <state>` in alto mostra a che punto è la
   fattura:

   * *Bozza*: la fattura si modifica liberamente; non ha numero e non ha
     effetto sui conti.
   * *Aperta*: validata. Odoo ha assegnato il :field:`numero <number>` e ha
     scritto la registrazione contabile; la fattura attende il pagamento.
   * *Pagata*: i pagamenti coprono l'intero importo.
   * *Annullata*: la fattura non conta più.

   .. help-version:: 10

      Con l'impostazione *Consentire fatture pro-forma* una bozza può diventare
      *Pro-forma*: una bozza inviata al cliente prima della validazione.

   .. help-version:: 12

      Tra *Aperta* e *Pagata* la fattura è *In pagamento*: pagata, in attesa
      che il pagamento sia abbinato all'estratto conto bancario.

.. help-version:: >=13

   Una fattura chiede al :field:`cliente <partner_id>` il pagamento di beni o
   servizi; una **fattura fornitore** registra quanto un fornitore chiede di
   pagare. Le loro rettifiche sono le **note di credito**. Prodotti, quantità,
   prezzi e imposte sono elencati nella scheda **Righe fattura**, i dare e
   avere che ne derivano nella scheda **Movimenti contabili**.

   Una fattura è una registrazione contabile di tipo fattura: la stessa
   maschera mostra anche le registrazioni contabili semplici, che non hanno
   partner, righe fattura né pagamenti.

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

.. help-include:: account_invoice_fields.rst

.. help-include:: account_invoice_new.rst

.. help-include:: account_invoice_update.rst

.. help-include:: account_invoice_configure.rst

.. help-include:: account_invoice_report.rst

.. help-include:: account_invoice_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non riesco a modificare la fattura?

   .. help-version:: <13

      Una fattura validata è bloccata. Annullarla con **Annullare fattura** e
      premere :version:`10|**Riportare in bozza**;*|**Reimposta a bozza**`: il
      registro deve consentire l'annullamento delle registrazioni, vedere
      *Configurazione*. Se è pagata, togliere prima il pagamento.

   .. help-version:: >=13

      Una fattura confermata è bloccata: premere **Reimposta a bozza**,
      modificarla e confermarla di nuovo. Se il pulsante manca, la fattura è
      in un periodo chiuso o il suo registro protegge le registrazioni;
      emettere invece una nota di credito.

.. help-question:: Perché non riesco a eliminare la fattura?

   .. help-version:: <13

      Si possono eliminare solo le fatture in bozza o annullate che non hanno
      mai ricevuto un numero. Una fattura validata mantiene il suo numero:
      annullarla, o emettere una nota di credito.

   .. help-version:: >=13

      Si possono eliminare solo le fatture in bozza, e solo se il loro numero è
      l'ultimo della sequenza, così da non lasciare buchi. Reimpostarla a bozza
      e annullarla, o emettere una nota di credito.

.. help-question:: Come registro un pagamento parziale?

   Premere :version:`10|**Registrare pagamento**;*|**Registra pagamento**` e
   ridurre l'importo. Scegliere
   :version:`10|*Lasciare aperto*;11|*Tenere aperto*;12-13|*Lasciare
   aperta*;*|*Tieni aperta*` per attendere il resto, o
   :version:`10|*Marca la fattura come pagata interamente*;11|*Indicazione
   fattura saldata*;12|*Segnare fattura come pagata*;13|*Impostare fattura come
   pagata*;*|*Segna come totalmente pagata*` per stornare la differenza su un
   conto, ad es. per le spese bancarie.

.. help-question:: Come annullo una fattura pagata?

   Togliere prima il pagamento: nei pagamenti sotto i totali fare clic
   sull'icona ⓘ del pagamento e premere **Annulla riconciliazione**. Poi
   annullare la fattura, o emettere una nota di credito.

.. help-question:: Perché la fattura attende ancora un pagamento già registrato?

   Il pagamento è stato registrato senza la fattura, ad es. dall'estratto conto
   bancario: la fattura lo mostra sotto i totali come *credito in sospeso*.
   Premere **Aggiungi** accanto al pagamento per usarlo.

   .. help-version:: >=12

      *In pagamento* significa che il pagamento è registrato ma non ancora
      abbinato all'estratto conto bancario: la fattura diventa *Pagata* dopo la
      riconciliazione.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-02 07:23 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
