.. help-if:: module = l10n_it_edi

   .. help-question:: Perché Odoo smette di ricevere le fatture elettroniche e le notifiche?

      L'azione pianificata *IT EDI: Ricezione fatture dall'SdI* è
      disattivata o in errore. In modalità sviluppatore aprire **Impostazioni
      ‣ Tecnico ‣ Automazione ‣ Azioni pianificate** e riattivarla. Se si
      ripete, contattare l'assistenza.

   .. help-question:: Perché una fattura fornitore importata ha righe senza imposta ("Imposta non trovata")?

      Nessuna imposta di acquisto ha l'aliquota e la natura dell'XML (ad es.
      0% *N6.3*, *N6.7*, *N7*): Odoo scrive *Imposta non trovata per la riga*
      nel chatter della fattura. Creare l'imposta di acquisto con
      quell'aliquota ed *Esenzione*, poi impostarla sulle righe, oppure
      eliminare la fattura e importarla di nuovo.

   .. help-question:: Perché la fattura fornitore viene assegnata al fornitore sbagliato, o a uno nuovo?

      Odoo cerca il fornitore per partita IVA e codice fiscale; se nessuno
      corrisponde crea un nuovo contatto e scrive *Impossibile recuperare un
      partner* nel chatter. Correggere partita IVA e codice fiscale del
      contatto giusto, archiviare quello sbagliato, poi eliminare la fattura
      e importarla di nuovo.

   .. help-question:: Perché le fatture fornitori sono duplicate, o perché una fattura elettronica non viene importata di nuovo?

      Odoo salta una fattura elettronica ricevuta dallo SdI quando un file
      con lo stesso nome è già stato importato. Una copia inserita a mano non
      viene riconosciuta: eliminarla e tenere la fattura importata.

   .. help-question:: Come importo una fattura elettronica ricevuta via PEC o in uno ZIP?

      In **Fatturazione ‣ Fornitori ‣ Fatture** premere [`Carica`] e
      scegliere il file *IT...xml* (o *.xml.p7m*) della fattura, non il file
      dei metadati *_MT_*.

      .. help-if:: module = l10n_it_edi_extension

         Per un file ZIP usare **Fatturazione ‣ Fornitori ‣ File importazione
         e-fattura**, vedere *Stampe ed esportazione*.

   .. help-question:: Come elimino una fattura fornitore importata da XML per importarla di nuovo?

      Riportare la fattura in bozza ed eliminarla; poi caricare di nuovo
      l'XML.

   .. help-question:: Perché l'XML del fornitore non si importa (EORI usato come codice destinatario, dati mancanti)?

      Il fornitore ha compilato male l'XML: chiedere al fornitore un XML
      corretto; in alternativa l'assistenza può correggere il file XML prima
      dell'importazione.

.. help-if:: module = rectify_negative_refund

   .. help-question:: Come correggo una fattura o nota di credito negativa (ad es. una nota di credito estera diventata TD17 negativa)?

      Il documento è stato registrato con il tipo sbagliato: una fattura
      negativa invece di una nota di credito, o viceversa. Aprirlo e premere
      [`Rettificare`] in alto: diventa del tipo corretto, con importi
      positivi.
