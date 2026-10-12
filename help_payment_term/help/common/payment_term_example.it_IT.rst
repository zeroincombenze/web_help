.. _example:

Esempi
------

**30 giorni fine mese**

L'importo scade alla fine del mese in cui cade il 30° giorno dopo la data
fattura:

* fattura del 15 gennaio → 14 febbraio → scadenza **28 febbraio**;
* fattura del 31 gennaio → 2 marzo → scadenza **31 marzo**.

Creare il termine come in *Nuovo record*, chiamarlo *30 giorni fine mese*,
poi impostare la riga come segue.

.. help-version:: <12

   Le opzioni della riga non sanno aggiungere 30 giorni e poi andare a fine
   mese. La più vicina è :version:`10|*Ultimo giorno del prossimo
   mese*;*|*Ultimo giorno del mese seguente*`: la fine del mese successivo a
   quello della fattura. Dà la stessa scadenza tranne che per le fatture di
   fine mese, quando il 30° giorno cade due mesi dopo: la fattura del 31
   gennaio scade il 28 febbraio invece del 31 marzo.

   Non usare *Giorno/i dopo fine mese della fattura (DF FM)* con 30 giorni:
   significa fine mese della fattura + 30 giorni, quindi la fattura del 15
   gennaio scade il 2 marzo.

   **Con il modulo OCA account_payment_term_extension** la scadenza è esatta.
   Nella maschera della riga:

   #. :field:`Tipo <value>`: *Saldo*.
   #. Opzione :version:`10|*Giorno/i dopo la data fattura (DF)*;*|*Giorno/i
      dopo la data fattura*`, :field:`Numero di giorni <days>`: 30.
   #. :field:`Giorno/i di pagamento <payment_days>`: ``31``.

   Odoo aggiunge 30 giorni alla data fattura, poi si sposta al successivo
   giorno di pagamento: 31 è l'ultimo giorno di qualunque mese (30 aprile, 28
   febbraio).

.. help-version:: 12-15

   Nella maschera della riga:

   #. :field:`Tipo termine <value>`: *Saldo*.
   #. Scadenza :field:`30 <days>` *giorni dopo la data della fattura*.
   #. :field:`Giorno del mese <day_of_the_month>`: 31, l'ultimo giorno di
      qualunque mese (30 aprile, 28 febbraio).

   Non usare *giorni dopo la fine del mese della fattura* con 30: significa
   fine mese della fattura + 30 giorni, quindi la fattura del 15 gennaio
   scade il 2 marzo.

   **Con il modulo OCA account_payment_term_extension** il campo *giorno del
   mese* è :version:`12|ignorato dal calcolo;*|nascosto`, e la fine mese è
   data dai giorni di pagamento:

   #. Scadenza 30 *giorni dopo la data della fattura*.
   #. :field:`Giorno/i di pagamento <payment_days>`: ``31``.

   Odoo aggiunge 30 giorni alla data fattura, poi si sposta al successivo
   giorno di pagamento: il risultato è lo stesso del *giorno del mese* 31
   nativo. Se si disinstalla il modulo, scrivere prima il 31 nel *giorno del
   mese*.

.. help-version:: 16

   Nella tabella **Condizioni**, sulla riga *Saldo*:

   #. :field:`Mesi <months>`: 0, :field:`Giorni <days>`: 30.
   #. :field:`Fine del mese <end_month>`: acceso.
   #. :field:`Giorni successivi alla fine del mese <days_after>`: 0.

   Odoo aggiunge 30 giorni alla data fattura, poi va all'ultimo giorno di
   quel mese. Non scrivere il 30 in *Giorni successivi alla fine del mese*
   con 0 giorni: significa fine mese della fattura + 30 giorni, quindi la
   fattura del 15 gennaio scade il 2 marzo.

   **Con il modulo OCA account_payment_term_extension** il termine del
   modulo, *Giorni* 30 con :field:`Giorno/i di pagamento <payment_days>`
   ``31`` e *Fine del mese* spento, dà la stessa scadenza: continua a
   funzionare, ma la *Fine del mese* nativa è più chiara. Usare uno dei due,
   non entrambi.

.. help-version:: 17

   I tipi di ritardo non sanno aggiungere 30 giorni e poi andare a fine mese.
   Il più vicino è 100% :field:`Dopo <nb_days>` 0 *Giorni che seguono la fine
   del prossimo mese*: la fine del mese successivo a quello della fattura. Dà
   la stessa scadenza tranne che per le fatture di fine mese, quando il 30°
   giorno cade due mesi dopo: la fattura del 31 gennaio scade il 28 febbraio
   invece del 31 marzo.

   Non usare 30 *Giorni dopo la fine del mese*: significa fine mese della
   fattura + 30 giorni, quindi la fattura del 15 gennaio scade il 2 marzo.

   **Con il modulo OCA account_payment_term_extension** la scadenza è esatta:

   #. 100% :field:`Dopo <nb_days>` 30 *Giorni che seguono la data di
      fatturazione*.
   #. :field:`Giorno/i di pagamento <payment_days>`: ``31``.

   Odoo aggiunge 30 giorni alla data fattura, poi si sposta al successivo
   giorno di pagamento: 31 è l'ultimo giorno di qualunque mese (30 aprile, 28
   febbraio).

.. help-version:: >=18

   Nella tabella **Termini di scadenza**:

   #. 100% :field:`Dopo <nb_days>` 30, tipo di ritardo *Giorni fine mese il*.
   #. Nella casella dopo il tipo di ritardo (:field:`giorni nel prossimo mese
      <days_next_month>`, 10 di default) scrivere 0: 0 significa la fine del
      mese.

   Odoo aggiunge 30 giorni alla data fattura, poi va all'ultimo giorno di
   quel mese. Verificarlo nell'**Anteprima** con 15 gennaio e 31 gennaio. Non
   usare 30 *Giorni dopo la fine del mese*: significa fine mese della
   fattura + 30 giorni, quindi la fattura del 15 gennaio scade il 2 marzo.

   **Con il modulo OCA account_payment_term_extension** il termine del
   modulo, 30 *Giorni che seguono la data di fatturazione* con
   :field:`Giorno/i di pagamento <payment_days>` ``31``, dà la stessa
   scadenza: i termini caricati così, ad es. in un database migrato,
   continuano a funzionare. Per i nuovi termini usare il nativo *Giorni fine
   mese il*, che non richiede moduli ed è mostrato nell'**Anteprima**. Usare
   uno dei due, non entrambi.

**30 giorni fine mese + 5 giorni**

L'importo scade 5 giorni dopo il *30 giorni fine mese*, cioè il 5 del mese
successivo:

* fattura del 15 gennaio → 28 febbraio → scadenza **5 marzo**;
* fattura del 31 gennaio → 31 marzo → scadenza **5 aprile**.

Creare il termine *30 giorni fine mese + 5* e impostare la riga come segue.

.. help-version:: <12

   Le opzioni della riga non sanno calcolare questo termine. **Con il modulo
   OCA account_payment_term_extension**:

   #. Opzione :version:`10|*Giorno/i dopo la data fattura (DF)*;*|*Giorno/i
      dopo la data fattura*`, :field:`Numero di giorni <days>`: 35 (30 + 5).
   #. :field:`Giorno/i di pagamento <payment_days>`: ``5``.

   Odoo aggiunge 35 giorni alla data fattura, poi si sposta al successivo
   giorno 5 di un mese: è sempre il 5 dopo la fine del mese del 30° giorno
   (15 gennaio + 35 giorni = 19 febbraio → 5 marzo).

.. help-version:: 12-15

   #. Scadenza 35 (30 + 5) *giorni dopo la data della fattura*.
   #. :field:`Giorno del mese <day_of_the_month>`: 5.

   Odoo aggiunge 35 giorni alla data fattura, poi si sposta al successivo
   giorno 5 di un mese: è sempre il 5 dopo la fine del mese del 30° giorno
   (15 gennaio + 35 giorni = 19 febbraio → 5 marzo).

   **Con il modulo OCA account_payment_term_extension** scrivere ``5`` in
   :field:`Giorno/i di pagamento <payment_days>` invece del *giorno del
   mese*, con gli stessi 35 giorni.

.. help-version:: 16

   Sulla riga *Saldo*: :field:`Giorni <days>` 30, :field:`Fine del mese
   <end_month>` acceso, :field:`Giorni successivi alla fine del mese
   <days_after>` 5.

   **Con il modulo OCA account_payment_term_extension** lo stesso risultato
   si ottiene con *Giorni* 35, :field:`Giorno/i di pagamento <payment_days>`
   ``5`` e *Fine del mese* spento.

.. help-version:: 17

   Il tipo di ritardo più vicino è 100% :field:`Dopo <nb_days>` 5 *Giorni che
   seguono la fine del prossimo mese*, con la stessa eccezione delle fatture
   di fine mese (31 gennaio → 5 marzo invece del 5 aprile).

   **Con il modulo OCA account_payment_term_extension** la scadenza è esatta:
   100% *Dopo* 35 (30 + 5) *Giorni che seguono la data di fatturazione* e
   :field:`Giorno/i di pagamento <payment_days>` ``5``. Odoo aggiunge 35
   giorni, poi si sposta al successivo giorno 5 di un mese (15 gennaio + 35
   giorni = 19 febbraio → 5 marzo).

.. help-version:: >=18

   100% :field:`Dopo <nb_days>` 30, tipo di ritardo *Giorni fine mese il*, e
   5 nella casella dopo: Odoo aggiunge 30 giorni alla data fattura, poi va al
   5 del mese successivo (15 gennaio → 14 febbraio → 5 marzo).

   **Con il modulo OCA account_payment_term_extension** il vecchio termine, 35
   *Giorni che seguono la data di fatturazione* con :field:`Giorno/i di
   pagamento <payment_days>` ``5``, dà la stessa scadenza.
