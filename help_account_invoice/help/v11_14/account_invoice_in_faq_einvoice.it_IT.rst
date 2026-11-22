.. help-if:: module = l10n_it_fatturapa_in

   .. help-question:: Perché non riesco a validare una fattura fornitore importata da XML: i totali differiscono dalla e-fattura?

      I totali della fattura non coincidono con l'XML: sconti in testata e
      sulle righe, bolli scontati, reverse charge su alcune righe,
      arrotondamenti del fornitore. Se la fattura in Odoo è corretta:
      **Modifica**, scheda **Incongruenze e-fattura**, spuntare
      :field:`Forza validazione e-fattura <e_invoice_force_validation>`,
      **Salva** e **Valida**.

   .. help-question:: Perché una fattura fornitore differisce di 1 centesimo, e non si importa o non si valida?

      L'XML del fornitore contiene arrotondamenti, e mancano i conti di
      arrotondamento. In **Fatturazione ‣ Configurazione ‣ Impostazioni**,
      sezione **Fatture elettroniche**, impostare *Conto arrotondamenti
      attivi*, *Conto arrotondamenti passivi* e *Imposta arrotondamento*; poi
      importare di nuovo l'XML.

   .. help-question:: Perché ricevo "Nessuna imposta con aliquota X e natura Y" importando l'XML?

      Nessuna imposta di acquisto ha quell'aliquota e natura (ad es. 0%
      *N6.3*, *N6.7*, *N7*), oppure più imposte la hanno e viene scelta
      quella sbagliata. Creare l'imposta di acquisto con aliquota e *Natura
      esenzione*; con più imposte cambiare la sequenza per mettere prima
      quella giusta.

   .. help-question:: Perché la fattura fornitore viene assegnata al fornitore sbagliato?

      Il fornitore è un indirizzo sotto un altro contatto, ha un nome simile,
      oppure la sua partita IVA è errata. Correggere partita IVA e codice
      fiscale del contatto giusto, staccarlo dal padre sbagliato, poi
      eliminare la fattura e importarla di nuovo.

   .. help-question:: Perché le fatture fornitori sono duplicate, o ricevo "Il nome del file della e-fattura deve essere unico"?

      Lo stesso file non può essere importato due volte. Se la fattura è
      stata inserita a mano e poi scaricata dallo SdI, eliminare la copia
      inserita a mano.

   .. help-question:: Come importo una fattura elettronica ricevuta via PEC o in uno ZIP?

      In **Fatturazione ‣ Fornitori ‣ Fattura elettronica ‣ File e-fatture in
      ingresso** caricare il file *IT...xml* (o *.xml.p7m*) della fattura,
      non il file dei metadati *_MT_*.

      .. help-if:: module = l10n_it_einvoice_import_zip

         Per un file ZIP usare **Fatturazione ‣ Fornitori ‣ Fattura
         elettronica ‣ Import eInvoice from ZIP**.

   .. help-question:: Come elimino una fattura fornitore importata da XML per importarla di nuovo?

      Annullare la fattura, riportarla in bozza ed eliminarla; poi creare di
      nuovo la fattura dal suo file e-fattura in ingresso.

   .. help-question:: Perché l'XML del fornitore non si importa (EORI usato come codice destinatario, dati mancanti)?

      Il fornitore ha compilato male l'XML: chiedere al fornitore un XML
      corretto; in alternativa l'assistenza può correggere il file XML prima
      dell'importazione.
