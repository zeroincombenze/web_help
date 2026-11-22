.. help-if:: module = l10n_it_einvoice_in

   .. help-question:: Perché non riesco a validare una fattura fornitore importata da XML: "totale e IVA diversi dalla e-fattura"?

      I totali della fattura non coincidono con l'XML: sconti in testata e
      sulle righe, bolli scontati, reverse charge su alcune righe,
      arrotondamenti del fornitore. Se la fattura in Odoo è corretta:
      **Modifica**, scheda **Incongruenze e-fattura**, spuntare
      :field:`Forzare validazione e-fattura <e_invoice_force_validation>`,
      **Salva** e **Valida**.

   .. help-question:: Perché una fattura fornitore differisce di 1 centesimo, e non si importa o non si valida?

      L'XML del fornitore contiene arrotondamenti, e mancano i conti di
      arrotondamento (spesso dopo un aggiornamento). In **Contabilità ‣
      Configurazione ‣ Impostazioni**, sezione **Fattura elettronica**,
      impostare *Conto arrotondamento attivo*, *Conto arrotondamento passivo*
      e *Arrotondamento Imposta*; poi aggiungere alla fattura una riga di
      arrotondamento, oppure importare di nuovo l'XML.

   .. help-question:: Perché ricevo "Nessun codice IVA con aliquota X e natura Y" importando l'XML?

      Nessuna imposta di acquisto ha quell'aliquota e natura (ad es. 0%
      *N6.3*, *N6.7*, *N7*), oppure più imposte la hanno e la prima è quella
      sbagliata. Creare l'imposta di acquisto con aliquota, natura e, per il
      reverse charge, il suo tipo di reverse charge; con più imposte cambiare
      la sequenza per mettere prima quella giusta. Controllare anche
      l'imposta di acquisto predefinita nelle impostazioni.

   .. help-question:: Perché ricevo "codice REA duplicato", o perché l'azienda ha perso il codice REA?

      Un'autofattura all'azienda stessa (TD17, TD20...) torna dallo SdI con
      l'azienda come fornitore: l'importazione assegna il REA a un altro
      contatto e lo toglie all'azienda. Riscrivere il REA in **Contabilità ‣
      Configurazione ‣ Impostazioni**, sezione **Fattura elettronica**, e
      toglierlo dal fornitore duplicato. Non importare l'autofattura di
      ritorno: collegarla a quella originale. Il software aggiornato (2024)
      corregge il problema.

   .. help-question:: Perché le fatture fornitori non si importano dopo che la partita IVA aziendale è diventata EU...?

      Importando un'autofattura è stato aggiunto il prefisso *EU* alla
      partita IVA dell'azienda. Correggere la partita IVA (*IT...*)
      dell'azienda, poi importare o collegare di nuovo le fatture.

   .. help-question:: Perché la fattura fornitore viene assegnata al fornitore sbagliato?

      Il fornitore è un indirizzo sotto un altro contatto, ha un nome simile,
      oppure la sua partita IVA è errata. Correggere partita IVA e codice
      fiscale del contatto giusto, staccarlo dal padre sbagliato, poi
      eliminare la fattura e importarla di nuovo.

   .. help-question:: Perché le fatture fornitori sono duplicate, o ricevo "file già importato"?

      Lo stesso file non può essere importato due volte. La fattura è stata
      inserita a mano e poi scaricata dallo SdI, oppure il canale ha inviato
      la stessa fattura firmata (*.xml.p7m*) e non firmata (*.xml*):
      eliminare la copia inserita a mano. Dal 2025 il software riconosce che
      *.xml* e *.xml.p7m* sono la stessa fattura.

   .. help-question:: Come importo una fattura elettronica ricevuta via PEC o in uno ZIP?

      In **Contabilità ‣ Acquisti ‣ Fattura fornitore elettronica ‣ File
      e-fatture in ingresso** caricare il file *IT...xml* (o *.xml.p7m*)
      della fattura, non il file dei metadati *_MT_*.

      .. help-if:: module = l10n_it_einvoice_import_zip

         Per un file ZIP usare **Contabilità ‣ Acquisti ‣ Fattura fornitore
         elettronica ‣ Import eInvoice from ZIP**.

   .. help-question:: Come elimino una fattura fornitore importata da XML per importarla di nuovo?

      Annullare la fattura, riportarla in bozza ed eliminarla; poi creare di
      nuovo la fattura dal suo file e-fattura in ingresso.

   .. help-question:: Perché l'XML del fornitore non si importa (EORI usato come codice destinatario, dati mancanti)?

      Il fornitore ha compilato male l'XML: chiedere al fornitore un XML
      corretto; in alternativa l'assistenza può correggere il file XML prima
      dell'importazione.

.. help-if:: module = rectify_negative_refund

   .. help-question:: Come correggo una fattura o nota di credito negativa (ad es. una nota di credito estera diventata TD17 negativa)?

      Il documento è stato registrato con il tipo sbagliato: una fattura
      negativa invece di una nota di credito, o viceversa. Aprirlo e premere
      **Rettificare** in alto: diventa del tipo corretto, con importi
      positivi.
