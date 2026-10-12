.. _new_record:

Nuovo record
------------

I passi caricano il termine *30 giorni*: l'intero importo scade 30 giorni dopo
la data fattura (fattura del 15 gennaio, scadenza 14 febbraio).

#. Aprire **Fatturazione ‣ Configurazione ‣**
   :version:`<12|**Gestione**;12|**Amministrazione**;*|**Fatturazione**`
   **‣ Termini di pagamento** e premere :version:`<17|**Crea**;*|**Nuovo**`.
#. Scrivere il :field:`nome <name>`, ad es. *30 giorni*: è il testo mostrato
   quando si sceglie il termine su un partner o una fattura.
#. Scrivere la :field:`descrizione in fattura <note>`, ad es. *Pagamento a 30
   giorni data fattura*: è stampata sul PDF della fattura.

.. help-version:: <16

   4. La tabella **Condizioni** contiene già una riga *Saldo* a 0 giorni:
      cliccarla per aprirne la maschera.
   #. Lasciare :field:`Tipo <value>` su *Saldo*, scrivere 30 in
      :field:`Numero di giorni <days>` e scegliere l'opzione
      :version:`10|*Giorno/i dopo la data fattura (DF)*;11|*Giorno/i dopo la
      data fattura*;*|*giorni dopo la data della fattura*`.

      .. help-version:: 12-15

         Lasciare il :field:`giorno del mese <day_of_the_month>` a 0.

   #. Premere **Salva e chiudi** per chiudere la riga, poi **Salva** il
      termine.

.. help-version:: 16

   4. La tabella **Condizioni** contiene già una riga *Saldo* a 0 giorni:
      cliccarla e scrivere 30 in :field:`Giorni <days>`. Lasciare
      :field:`Mesi <months>` a 0 e :field:`Fine del mese <end_month>` spento.
   #. Controllare l'*Esempio* sotto la tabella: con data fattura 15 gennaio,
      la scadenza è il 14 febbraio.
   #. Premere **Salva**.

.. help-version:: >=17

   4. La tabella **Termini di scadenza** contiene già una riga *100 %
      Percentuale Dopo 0 Giorni che seguono la data di fatturazione*:
      cliccare :field:`Dopo <nb_days>` e scrivere 30; lasciare *Giorni che
      seguono la data di fatturazione*.
   #. Controllare l'**Anteprima**: con data fattura 15 gennaio, l'importo
      scade il 14 febbraio.
   #. Il record si salva automaticamente quando lo si lascia, o subito con
      l'icona della nuvola accanto al percorso.

Scegliere il nuovo termine sui partner (scheda **Vendite e acquisti**) o
direttamente sulla fattura. I termini con più rate (ad es. 30% subito, 70% a
60 giorni) hanno una riga per rata:
:version:`<17|l'ultima riga è il *Saldo*;*|le percentuali sommano 100%`.
