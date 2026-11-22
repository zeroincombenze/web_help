.. _update_record:

Come modificare un record
-------------------------

.. help-version:: <13

   #. Aprire la fattura dalla lista e premere [`Modifica`]. Una fattura in
      *Bozza* si modifica liberamente; premere [`Salva`] alla fine.
   #. Una fattura validata (*Aperta*) non si può modificare. Per correggerla
      premere :version:`<12|[\`Annulla fattura\`];*|[\`Annulla\`]`, poi
      :version:`10|[\`Riportare in bozza\`];*|[\`Reimposta a bozza\`]`,
      modificarla e premere di nuovo :version:`10|[\`Validare\`];*|[\`Valida\`]`:
      mantiene il suo numero. L'annullamento richiede l'opzione
      :version:`10|*Consenti cancellazione registrazioni*;*|*Consentire
      annullamento registrazioni*` del registro, vedere *Come configurare*.
   #. Per registrare un pagamento, vedere *Altre azioni*.
   #. Per rimborsare il cliente premere :version:`10|[\`Nota di
      credito\`];*|[\`Aggiungi nota di credito\`]`, scrivere il motivo e la data,
      scegliere il metodo e premere :version:`10|[\`Crea nota di
      credito\`];*|[\`Aggiungi nota di credito\`]`:

      * :version:`10|*Creare nota di credito in bozza*;11|*Creazione di bozza di
        nota di credito*;*|*Crea nota di credito in bozza*`: una bozza da
        modificare, ad es. per un rimborso parziale;
      * :version:`10|*Annullare: creare nota di credito e
        riconciliare*;11|*Annullamento: creare nota di credito e
        riconciliare*;*|*Annulla: crea nota di credito e riconcilia*`: l'intera
        fattura è annullata;
      * :version:`12|*Modifica: crea nota di credito, riconcilia e genera nuova
        fattura in bozza*;*|*Modifica*`: come l'annullamento, più una nuova
        fattura in bozza da correggere.

.. help-version:: >=13

   #. Aprire la fattura dalla lista. :version:`<17|Premere [\`Modifica\`]: una
      fattura in *Bozza* si modifica liberamente, poi premere
      [\`Salva\`].;*|Una fattura in *Bozza* si modifica liberamente e si salva
      automaticamente.`
   #. Una fattura :version:`13|*Confermato*;*|*Confermata*` non si può
      modificare: premere [`Reimposta a bozza`], modificarla e premere di
      nuovo [`Conferma`]; mantiene il suo numero. Il pulsante manca in un
      periodo chiuso e sui registri protetti: emettere invece una nota di
      credito.
   #. Per registrare un pagamento, vedere *Altre azioni*.
   #. Per rimborsare il cliente premere :version:`<18|[\`Aggiungi nota di
      credito\`];*|[\`Nota di credito\`]`, scrivere il motivo e controllare la
      data di storno e il registro.

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
