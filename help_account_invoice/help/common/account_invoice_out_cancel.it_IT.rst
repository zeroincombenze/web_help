.. _cancel:

Come annullare o eliminare un record
------------------------------------

.. help-version:: <13

   #. Per annullare una fattura serve il modulo *Cancel Journal Entries*, che
      aggiunge il pulsante :version:`<12|[\`Annulla fattura\`];*|[\`Annulla\`]`.

      .. help-if:: module != account_cancel

         L'amministratore lo installa dal menu
         :version:`<12|**Apps**;*|**Applicazioni**`.

         .. help-version:: 10

            Senza il modulo, [`Annulla fattura`] compare solo in modalità
            sviluppatore.

   #. :version:`10|[\`Annulla fattura\`] compare sulle fatture *Bozza*,
      *Pro-forma* e *Aperta*.;11|[\`Annulla fattura\`] compare sulle fatture
      *Bozza* e *Aperta*.;*|[\`Annulla\`] compare sulle fatture *Bozza*,
      *Aperta*, *In pagamento* e *Pagata*.` Una fattura validata si può
      annullare solo se è attiva l'opzione :version:`10|*Consenti
      cancellazione registrazioni*;*|*Consentire annullamento registrazioni*`
      del suo sezionale (modalità sviluppatore). :version:`<12|Una fattura
      pagata anche solo in parte non si può annullare: annullare prima la
      riconciliazione dei pagamenti.;*|I pagamenti della fattura vengono
      scollegati e restano aperti.` La registrazione contabile viene
      eliminata e la fattura diventa :version:`11|*Annullata*;*|*Annullato*`,
      mantenendo il suo numero.
   #. [`Reimposta a bozza`] riporta una fattura annullata a *Bozza*:
      modificarla e validarla di nuovo, con lo stesso numero.
   #. Si può eliminare solo una fattura in bozza o annullata che non ha mai
      ricevuto un numero, da **Azione ‣ Elimina** nella maschera, oppure
      selezionandola nell'elenco e usando **Azione ‣ Elimina**. Una fattura
      validata si annulla o si storna con una nota di credito, non si elimina
      mai.
   #. Le fatture non si possono archiviare.

.. help-version:: >=13

   #. :version:`<15|[\`Annulla registrazione\`];*|[\`Annulla\`]` compare sulle
      fatture in *Bozza*: la fattura diventa :version:`13|*Annullato*;*|*Annullata*`
      e conserva le sue righe, ma non conta più nei conti né negli importi
      dovuti.
   #. Una fattura :version:`13|*Confermato*;*|*Confermata*` si annulla in due
      passi: premere [`Reimposta a bozza`] (i suoi pagamenti vengono
      scollegati e restano aperti), poi :version:`<15|[\`Annulla
      registrazione\`];*|[\`Annulla\`]`. [`Reimposta a bozza`] è rifiutato in un
      periodo bloccato e manca nei sezionali con registrazioni protette da
      hash (inalterabilità): emettere invece una nota di credito, vedere
      *Come modificare un record*.

      .. help-version:: >=17

         Una fattura elettronica già inviata all'autorità fiscale mostra
         invece [`Richiesta di annullamento`]: l'annullamento è chiesto
         tramite il servizio di fatturazione elettronica.

   #. [`Reimposta a bozza`] riporta anche una fattura annullata a *Bozza*,
      per modificarla e confermarla di nuovo.
   #. Si possono eliminare solo le fatture in bozza o annullate: nella
      maschera usare :version:`<17|**Azione ‣ Elimina**;*|l'icona
      dell'ingranaggio ‣ **Elimina**`, nell'elenco selezionarle e usare
      :version:`<17|**Azione ‣ Elimina**;*|**Azioni ‣ Elimina**`.

      .. help-version:: <15

         Una fattura confermata almeno una volta non si può più eliminare:
         annullarla.

      .. help-version:: >=15

         Una fattura che ha ricevuto un numero si può eliminare solo se il
         suo numero è l'ultimo della sequenza del sezionale, per non lasciare
         buchi; le altre si annullano.

      .. help-version:: >=16

         Un utente con il permesso :version:`<18|*Responsabile
         fatturazione*;*|*Amministratore* della contabilità` può eliminarla
         comunque, dopo un avviso.

      .. help-version:: >=18

         Con l'opzione :version:`18|*Traccia di audit*;*|*Traccia di audit
         restrittiva*` delle impostazioni di contabilità, una fattura
         confermata almeno una volta non si può mai eliminare: annullarla.

   #. Le fatture non si possono archiviare.
