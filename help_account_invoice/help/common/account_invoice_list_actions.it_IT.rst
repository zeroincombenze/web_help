.. _actions:

Altre azioni
------------

Selezionare le fatture con le caselle di spunta della lista per agire su
tutte insieme; ogni azione è disponibile anche sulla singola fattura, dalla
sua scheda.

Confermare le fatture
~~~~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   Selezionare le fatture in bozza, poi
   :version:`10|**Azione ‣ Conferma la fattura in bozza**;11|**Azione ‣
   Conferma delle fatture in bozza**;*|**Azione ‣ Conferma fatture in
   bozza**` e premere :version:`10|**Conferma le fatture**;*|**Conferma
   fatture**`: ogni fattura riceve il suo numero e la sua registrazione
   contabile, e non può più essere modificata. Si possono confermare solo le
   fatture in bozza; nella scheda il pulsante è **Valida**.

.. help-version:: >=13

   Selezionare le fatture in bozza, poi :version:`<=16|**Azione ‣ Conferma
   registrazioni**;*|**Azioni ‣ Conferma registrazioni**` e premere
   :version:`<18|**Conferma registrazioni contabili**;*|**Conferma**`: ogni
   fattura riceve il suo numero e la sua registrazione contabile, e non può
   più essere modificata; per correggerla, rimetterla in bozza. Nella scheda
   il pulsante è **Conferma**.

Registrare un pagamento
~~~~~~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   Selezionare le fatture aperte dello stesso tipo (clienti o fornitori), poi
   :version:`10|**Azione ‣ Registra pagamenti**;11|**Azione ‣ Registrazione
   pagamento**;*|**Azione ‣ Registra pagamento**`: scegliere il registro del
   pagamento (banca o cassa), la data del pagamento e premere **Valida**. Le
   fatture passano allo stato *Pagata*. Nella scheda il pulsante è
   :version:`10|**Registra pagamenti**;11|**Registrazione
   pagamento**;*|**Registra pagamento**`, e permette anche di pagare un
   importo parziale.

.. help-version:: 13

   Selezionare le fatture confermate, poi **Azione ‣ Registra pagamento**:
   scegliere il registro del pagamento (banca o cassa), la data del pagamento
   e premere **Crea pagamento**. Le fatture passano allo stato *Pagata*.
   Nella scheda il pulsante è **Registra pagamento**, e permette anche di
   pagare un importo parziale.

.. help-version:: >=14

   Selezionare le fatture confermate: sopra la lista compare il pulsante
   **Registra pagamento**\ :version:`<17| (solo per gli utenti con il
   permesso *Mostrare funzionalità contabili complete*)`. Scegliere il
   registro del pagamento (banca o cassa), la data e l'importo, poi premere
   **Crea pagamento**\ :version:`>=17| (**Crea pagamenti** quando sono più
   di uno)`. Con più fatture dello stesso partner, *Raggruppa pagamenti* crea
   un solo pagamento per tutte. Le fatture passano allo stato *Pagata*, o *In
   pagamento* finché il pagamento non è riconciliato con l'estratto conto.
   Nella scheda il pulsante è **Registra pagamento**.

Come creare una nota di debito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   Una nota di debito chiede al cliente un importo aggiuntivo su una fattura
   già emessa (ad es. un aumento di prezzo o un addebito dimenticato). Questa
   versione non ha una funzione apposita: creare una nuova fattura per
   l'importo aggiuntivo, e scrivere il numero della fattura originale nel
   suo riferimento.

.. help-version:: >=13

   Una nota di debito chiede al cliente un importo aggiuntivo su una fattura
   già emessa (ad es. un aumento di prezzo o un addebito dimenticato), o
   registra l'importo aggiuntivo chiesto da un fornitore.

   .. help-if:: module != account_debit_note

      La funzione richiede il modulo *Note di debito*: l'amministratore lo
      installa dal menu **Applicazioni**.

   .. help-if:: module = account_debit_note

      Selezionare le fatture confermate, poi :version:`<=16|**Azione ‣ Crea
      nota di debito**;*|**Azioni ‣ Crea nota di debito**` (nella scheda,
      :version:`<17|il pulsante **Aggiungi nota di debito**;*|**Nota di
      debito** nel menu sotto l'icona dell'ingranaggio`). Compilare la
      *Causale*, la *Data nota di debito*, il *Registro* e, per partire da
      una copia delle righe della fattura, *Copia righe*; poi premere **Crea
      nota di debito**. Viene creata una fattura in bozza, collegata a quella
      originale: correggerne righe e importi, poi confermarla. La fattura
      originale mostra il pulsante *Note di debito*.

   .. help-version:: >=18

      .. help-if:: module = l10n_it_edi_ndd_account_dn

         La fattura elettronica di una nota di debito è inviata con il tipo
         documento *TD05*.
