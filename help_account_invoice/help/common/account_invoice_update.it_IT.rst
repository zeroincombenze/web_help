.. _update_record:

Modifica record
---------------

.. help-version:: <13

   #. Aprire la fattura dalla lista e premere **Modifica**. Una fattura in
      *Bozza* si modifica liberamente; premere **Salva** alla fine.
   #. Una fattura validata (*Aperta*) non si può modificare. Per correggerla
      premere **Annullare fattura**, poi
      :version:`10|**Riportare in bozza**;*|**Reimposta a bozza**`,
      modificarla e premere di nuovo :version:`10|**Validare**;*|**Valida**`:
      mantiene il suo numero. L'annullamento richiede l'opzione
      :version:`10|*Consenti cancellazione registrazioni*;*|*Consentire
      annullamento registrazioni*` del registro, vedere *Configurazione*.
   #. Per registrare un pagamento premere
      :version:`10|**Registrare pagamento**;*|**Registra pagamento**`:
      controllare il registro di pagamento (banca o cassa), l'importo, la data
      e la causale, poi premere :version:`10|**Validare**;*|**Valida**`. Un
      importo minore lascia aperto il resto
      (:version:`10|*Lasciare aperto*;11|*Tenere aperto*;*|*Lasciare aperta*`)
      o lo storna (:version:`10|*Marca la fattura come pagata
      interamente*;11|*Indicazione fattura saldata*;*|*Segnare fattura come
      pagata*`).
   #. Un pagamento già ricevuto, ad es. dall'estratto conto bancario, è
      mostrato sotto i totali come *credito in sospeso*: premere **Aggiungi**
      accanto ad esso.
   #. Per rimborsare il cliente premere :version:`10|**Nota di
      credito**;*|**Aggiungi nota di credito**`, scrivere il motivo e la data,
      scegliere il metodo e premere :version:`10|**Crea nota di
      credito**;*|**Aggiungi nota di credito**`:

      * :version:`10|*Creare nota di credito in bozza*;11|*Creazione di bozza di
        nota di credito*;*|*Crea nota di credito in bozza*`: una bozza da
        modificare, ad es. per un rimborso parziale;
      * :version:`10|*Annullare: creare nota di credito e
        riconciliare*;11|*Annullamento: creare nota di credito e
        riconciliare*;*|*Annulla: crea nota di credito e riconcilia*`: l'intera
        fattura è annullata;
      * *Modifica*: come l'annullamento, più una nuova fattura in bozza da
        correggere.

   #. Una fattura in bozza che non ha mai ricevuto un numero si elimina da
      **Azione ‣ Elimina**; una fattura validata si annulla o si rimborsa, non
      si elimina mai.

.. help-version:: >=13

   #. Aprire la fattura dalla lista. :version:`<17|Premere **Modifica**: una
      fattura in *Bozza* si modifica liberamente, poi premere
      **Salva**.;*|Una fattura in *Bozza* si modifica liberamente e si salva
      automaticamente.`
   #. Una fattura :version:`13|*Confermato*;*|*Confermata*` non si può
      modificare: premere **Reimposta a bozza**, modificarla e premere di
      nuovo **Conferma**; mantiene il suo numero. Il pulsante manca in un
      periodo chiuso e sui registri protetti: emettere invece una nota di
      credito.
   #. Per registrare un pagamento premere **Registra pagamento**: controllare
      il registro, il metodo di pagamento, l'importo, la data e la causale,
      poi premere **Crea pagamento**. Un importo minore lascia da pagare il
      resto (:version:`13|*Lasciare aperta*;*|*Tieni aperta*`) o lo storna
      (:version:`13|*Impostare fattura come pagata*;*|*Segna come totalmente
      pagata*`).
   #. Un pagamento già ricevuto, ad es. dall'estratto conto bancario, è
      mostrato sotto i totali come *credito in sospeso*: premere **Aggiungi**
      accanto ad esso.
   #. Per rimborsare il cliente premere :version:`<18|**Aggiungi nota di
      credito**;*|**Nota di credito**`, scrivere il motivo e controllare la
      data di storno e il registro.

      .. help-version:: <17

         Scegliere il metodo e premere **Storna**:

         * *Rimborso parziale*: una nota di credito in bozza da modificare e
           confermare;
         * *Rimborso completo*: la nota di credito è confermata e abbinata alla
           fattura, che risulta pagata;
         * *Rimborso completo e nuova fattura in bozza*: come *Rimborso
           completo*, più una nuova fattura in bozza da correggere.

      .. help-version:: >=17

         Premere **Storna** per una nota di credito in bozza da modificare e
         confermare, o **Storna e crea fattura** per annullare l'intera
         fattura con una nota di credito confermata e aprire una nuova fattura
         in bozza da correggere.

   #. Per scartare una fattura in bozza premere
      :version:`<15|**Annulla registrazione**;*|**Annulla**`; si può anche
      eliminare :version:`<17|da **Azione ‣ Elimina**;*|dall'icona
      dell'ingranaggio ‣ **Elimina**` quando il suo numero è l'ultimo della
      sequenza.

   .. help-version:: >=15

      Una fattura segnata *Da controllare*, ad es. creata da un'email o da un
      PDF scansionato, mostra **Impostare come Controllato**: premerlo dopo
      aver verificato la fattura.

   .. help-version:: >=17

      Una fattura elettronica già inviata all'amministrazione fiscale mostra
      **Richiesta di annullamento**: l'annullamento è chiesto tramite il
      servizio di fatturazione elettronica.
