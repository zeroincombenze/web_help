.. _update_record:

Come modificare un record
-------------------------

.. help-version:: <13

   #. Aprire la fattura dalla lista e premere [`Modifica`]. Una fattura in
      *Bozza* si modifica liberamente; premere [`Salva`] alla fine.
   #. Una fattura validata (*Aperta*) non si può modificare. Per correggerla
      annullarla (vedere *Come annullare o eliminare un record*), premere
      [`Imposta a bozza`], modificarla e premere di nuovo
      [`Valida`]: mantiene il suo numero.
   #. Per pagarla, vedere *Altre azioni*.
   #. Per chiedere una nota di credito al fornitore premere
      :version:`10|[\`Richiesta nota di credito\`];11|[\`Richiesta di nota di
      credito\`];*|[\`Richiedi nota di credito\`]`, scrivere il motivo e la
      data, scegliere il metodo e premere :version:`10|[\`Crea nota di
      credito\`];*|[\`Aggiungi nota di credito\`]`:

      * :version:`10|*Creare nota di credito in bozza*;11|*Creazione di bozza di
        nota di credito*;*|*Crea nota di credito in bozza*`: una bozza da
        modificare e da abbinare alla nota di credito ricevuta dal fornitore,
        ad es. per un rimborso parziale;
      * :version:`10-11|*Annullamento: creare nota di credito e
        riconciliare*;*|*Annulla: crea nota di credito e riconcilia*`: l'intera
        fattura è annullata;
      * :version:`10|*Modify: create refund, reconcile and create a new draft
        invoice*;*|*Modifica*`: come l'annullamento, più una nuova fattura in bozza da
        correggere.

.. help-version:: >=13

   #. Aprire la fattura dalla lista. :version:`<17|Premere [\`Modifica\`]: una
      fattura in *Bozza* si modifica liberamente, poi premere
      [\`Salva\`].;*|Una fattura in *Bozza* si modifica liberamente e si salva
      automaticamente.`
   #. Una fattura :version:`13|*Confermato*;*|*Confermata*` non si può
      modificare: premere [`Reimposta a bozza`], modificarla e premere di
      nuovo [`Conferma`]; mantiene il suo numero. Il pulsante manca in un
      periodo chiuso e sui registri protetti: registrare invece una nota di
      credito.
   #. Per pagarla, vedere *Altre azioni*.
   #. Per registrare una nota di credito ricevuta dal fornitore premere
      :version:`<17|[\`Aggiungi nota di credito\`];*|[\`Nota di credito\`]`
      sulla fattura confermata, scrivere il motivo e controllare la data di
      storno e il registro.

      .. help-version:: <17

         Scegliere il metodo e premere [`Storna`]:

         * *Rimborso parziale*: una nota di credito in bozza da modificare e
           confermare;
         * *Rimborso completo*: la nota di credito è confermata e abbinata alla
           fattura, che risulta pagata;
         * *Rimborso completo e nuova fattura in bozza*: come *Rimborso
           completo*, più una nuova fattura in bozza da correggere.

      .. help-version:: >=17

         Premere [`Storna`] per una nota di credito in bozza da modificare e
         confermare, o [`Storna e crea fattura`] per annullare l'intera
         fattura con una nota di credito confermata e aprire una nuova fattura
         in bozza da correggere.

   .. help-version:: >=15

      Una fattura segnata *Da controllare*, ad es. creata da un'email o da un
      PDF scansionato, mostra [`Impostare come Controllato`]: premerlo dopo
      aver verificato la fattura.
