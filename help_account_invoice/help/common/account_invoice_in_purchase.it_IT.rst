.. help-if:: module = purchase

   .. _purchase_order:

   Fattura da ordine fornitore
   ---------------------------

   Con l'app Acquisti le fatture fornitore si creano di solito dagli ordini
   di acquisto confermati: Odoo copia il fornitore, i termini di pagamento, la
   posizione fiscale e le righe, e tiene traccia di quanto è già fatturato.

   Cosa si può fatturare dipende dal campo :version:`10|*Controllo Fatture di
   Acquisto*;11|*Politica Controllo*;*|*Politica di controllo*` di ogni
   prodotto, impostato sul prodotto\ :version:`>=11|, nella scheda
   **Acquisto**`:

   * :version:`10|*Quantitativi ordinati*;*|*Su quantità ordinate*`: tutta la
     quantità ordinata, appena l'ordine è confermato;
   * :version:`10|*Quantitativi ricevuti*;*|*Su quantità ricevute*`: solo la
     quantità già ricevuta, ad esempio dopo la convalida della ricezione.

   .. help-version:: 10

      Lo :field:`Stato Fatturazione <invoice_status>` di un ordine mostra cosa
      resta: :version:`10-11|*Niente da Fatturare*;*|*Nulla da fatturare*`,
      :version:`10-11|*Attesa fattura*;12-13|*In attesa di
      fatture*;*|*In attesa di fatturazione*` e
      :version:`10|*Fatture Ricevute*;11-12|*Nessuna fattura da
      ricevere*;*|*Completamente fatturato*`.

   .. help-version:: >=11

      Lo :field:`Stato fatturazione <invoice_status>` di un ordine mostra cosa
      resta: :version:`10-11|*Niente da Fatturare*;*|*Nulla da fatturare*`,
      :version:`10-11|*Attesa fattura*;12-13|*In attesa di
      fatture*;*|*In attesa di fatturazione*` e
      :version:`10|*Fatture Ricevute*;11-12|*Nessuna fattura da
      ricevere*;*|*Completamente fatturato*`.

   #. Aprire :version:`10|**Acquisti ‣ Acquisto ‣ Ordini di
      acquisto**;<13|**Acquisti ‣ Acquisti ‣ Ordini di
      acquisto**;*|**Acquisti ‣ Ordini ‣ Ordini di acquisto**` e aprire
      l'ordine (una richiesta di offerta diventa ordine con :version:`10|[\`Conferma
      Ordine\`];*|[\`Conferma ordine\`]`).
   #. Se la politica di controllo dei prodotti è :version:`10|*Quantitativi ricevuti*;*|*Su quantità ricevute*`,
      ricevere prima la merce con :version:`10|[\`Prodotti in
      entrata\`];11-13|[\`Ricevi Prodotti\`];14-15|[\`Ricevi
      prodotti\`];*|[\`Ricezione prodotti\`]`\
      :version:`>=14|, o con il pulsante **Ricezione**`, e convalidare la
      ricezione: prima non si può fatturare nulla.
   #. :version:`10|Premere il pulsante **Fatture fornitori** dell'ordine e
      poi [\`Crea\`]: la nuova fattura ha le righe dell'ordine, con le quantità
      non ancora fatturate.;11|Premere il pulsante **Fatture fornitore** dell'ordine e
      creare lì una nuova fattura: l'ordine è già scelto nel campo *Aggiungi
      Ordine d'Acquisto* e le sue righe sono aggiunte.;12-13|Premere [\`Creare
      fattura\`] sull'ordine (anche il pulsante **Fatture fornitore** apre le
      sue fatture): la nuova fattura si apre in bozza, con le quantità ancora
      da fatturare.;*|Premere [\`Crea fattura\`] sull'ordine (anche il
      pulsante **Fatture fornitore** apre le sue fatture): la nuova fattura si
      apre in bozza, con le quantità ancora da fatturare.`
   #. Scrivere il riferimento del fornitore sulla fattura
      (:version:`<13|*Riferimento fornitore*;13|*Riferimento*;*|*Rif.
      fattura/ricevuta*`) e la data fattura.
   #. Controllare quantità, prezzi e imposte rispetto all'ordine: cambiare la
      quantità di una riga per fatturarne solo una parte.
   #. Premere :version:`<13|[\`Valida\`];*|[\`Conferma\`]`: la fattura è
      confermata e lo :version:`10|*Stato Fatturazione*;*|*Stato fatturazione*` dell'ordine si
      aggiorna.

   *Alternativa*: creare la fattura a mano, come descritto in *Come inserire
   un nuovo record*, scegliere il fornitore e poi l'ordine nel campo
   :version:`10|*Aggiungi ordini d'acquisto*;11|*Aggiungi Ordine
   d'Acquisto*;*|*Autocompletamento*` della fattura (compare su una fattura in
   bozza, per gli utenti dell'app Acquisti): le righe dell'ordine sono caricate
   nella fattura. :version:`10|Il campo propone solo gli ordini di quel
   fornitore con *Stato Fatturazione* *Attesa fattura*.;>=13|Lo stesso campo può anche copiare le righe di
   una vecchia fattura del fornitore.`

   *Fatturazione parziale*: si fattura solo una parte dell'ordine (cambiando
   la quantità delle righe, o ricevendo la merce in più passaggi con la
   politica :version:`10|*Quantitativi ricevuti*;*|*Su quantità ricevute*`): l'ordine resta in attesa di fatturazione.
   Quando si deve fatturare il resto, premere :version:`10|[\`Crea\`] in
   **Fatturazione ‣ Acquisti ‣ Fatture fornitori** e scegliere l'ordine nel
   campo *Aggiungi ordini d'acquisto* (il pulsante **Fatture fornitori** di un
   ordine con una sola fattura apre quella fattura);11|di nuovo il pulsante
   **Fatture fornitore**;12-13|di nuovo [\`Creare fattura\`];*|di nuovo [\`Crea
   fattura\`]`: sono proposte solo le quantità non ancora fatturate.

   La fattura è collegata all'ordine: il pulsante :version:`10|**Fatture fornitori**;*|**Fatture fornitore**`
   dell'ordine apre le sue fatture. :version:`>=18|Sulla fattura, il pulsante
   **Acquisti** apre gli ordini e **Corrispondenza acquisto** abbina le righe
   della fattura a quelle dell'ordine, e sull'ordine **Corrispondenza
   fattura** fa lo stesso.`
