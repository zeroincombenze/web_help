.. _lines:

Righe
~~~~~

.. help-version:: <16

   Le righe sono nella tabella **Condizioni**; cliccare una riga, o
   :version:`<12|**Aggiungi un elemento**;*|**Aggiungi riga**`, per aprirne la
   maschera:

   * :field:`Tipo <value>`: *Saldo* (il resto dell'importo), *Percentuale*
     (una percentuale del totale) o *Importo fisso*. Una riga, l'ultima, deve
     essere *Saldo*: il termine *30 giorni* ha una sola riga *Saldo*.
   * :field:`Numero di giorni <days>` e :field:`opzione <option>`: come si
     calcola la scadenza.

   .. help-version:: <12

      Le opzioni sono :version:`10|*Giorno/i dopo la data fattura (DF)*,
      *Giorno/i dopo fine mese della fattura (DF FM)*, *Ultimo giorno del
      prossimo mese*;*|*Giorno/i dopo la data fattura*, *Giorno/i dopo la fine
      del mese di fatturazione (DF FM)*, *Ultimo giorno del mese seguente*` e
      *Ultimo giorno del mese corrente*; con le ultime due il numero di giorni
      è ignorato.

   .. help-version:: 12-15

      Le opzioni sono *giorni dopo la data della fattura*, *giorni dopo la fine
      del mese della fattura*, *del mese prossimo* e *del mese in corso*: con
      le ultime due il numero è il giorno del mese (ad es. il 10 del mese
      prossimo). Con *dopo la data della fattura*, il :field:`giorno del mese
      <day_of_the_month>` sposta la scadenza a quel giorno del mese (31
      significa l'ultimo giorno).

.. help-version:: 16

   Le righe si modificano direttamente nella tabella **Condizioni**:

   * :field:`Tipo di scadenza <value>`: *Saldo* (il resto dell'importo),
     *Percentuale* o *Importo fisso*, con il suo :field:`valore
     <value_amount>`. Esattamente una riga deve essere *Saldo*.
   * :field:`Mesi <months>` e :field:`Giorni <days>` si aggiungono alla data
     fattura.
   * :field:`Fine del mese <end_month>` sposta poi la data all'ultimo giorno
     di quel mese, e :field:`Giorni successivi alla fine del mese
     <days_after>` aggiunge alcuni giorni dopo.
   * :field:`Sconto % <discount_percentage>` e :field:`Giorni sconto
     <discount_days>`: lo sconto per pagamento anticipato.

   L'*Esempio* sotto la tabella mostra le scadenze di un importo a una data:
   cambiare la data per verificare il termine.

.. help-version:: >=17

   Le righe si modificano direttamente nella tabella **Termini di scadenza**:

   * :field:`l'importo <value_amount>` con *Percentuale* o *Fisso*: l'importo
     della rata. Le percentuali devono sommare 100%.
   * :field:`Dopo <nb_days>` e il :field:`tipo di ritardo <delay_type>`: il
     numero di giorni e da dove partono: *Giorni che seguono la data di
     fatturazione*, *Giorni dopo la fine del mese* (la fine del mese della
     fattura) o *Giorni che seguono la fine del prossimo mese*.

   .. help-version:: >=18

      *Giorni fine mese il* aggiunge i giorni alla data fattura, poi va al
      :field:`giorno del mese successivo <days_next_month>` scritto nella
      casella dopo; 0 significa la fine del mese.

   L'**Anteprima** mostra le scadenze di un importo a una data: cambiare la
   data per verificare il termine. :field:`Mostra date versamento
   <display_on_invoice>` stampa scadenze e importi sulla fattura; *Sconto
   anticipato* concede uno sconto per pagamento anticipato.
