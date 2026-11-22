.. help-version:: 18

   .. help-if:: module = l10n_it_edi

      .. _new_from_xml:

      Come creare una fattura da XML
      ------------------------------

      Una fattura elettronica del fornitore (FatturaPA, file *.xml* o
      *.xml.p7m*) si carica invece di digitare la fattura: Odoo legge il file e
      crea una fattura fornitore in bozza con i dati del fornitore.

      #. Aprire **Fatturazione ‣ Fornitori ‣ Fatture** e premere [`Carica`] (o
         trascinare il file sulla lista), oppure premere [`Carica`] sulla
         scheda del registro acquisti nella Bacheca della contabilità. Scegliere
         il file ricevuto dal fornitore, quello *IT...xml* (o *.xml.p7m*), non
         il file dei metadati *_MT_*. Più file creano più fatture.
      #. La fattura è creata nel registro acquisti della scheda, o nel primo
         registro acquisti dell'azienda quando il pulsante è quello della
         lista. Un file apre la sua fattura, più file aprono la lista dei
         documenti generati.
      #. Controllare la fattura in bozza, come descritto sotto, poi premere
         [`Conferma`].

      Odoo crea le fatture anche da solo quando riceve le fatture elettroniche
      dal SdI (azione pianificata *IT EDI: Receive invoices from the SdI*):
      si trovano nella stessa lista, in bozza.

      Cosa compila Odoo:

      * il :field:`fornitore <partner_id>`: cercato per Codice Fiscale, poi per
        partita IVA, nome, telefono ed email; se non lo trova crea un nuovo
        contatto e il chatter dice *Could not retrieve a partner corresponding
        to ...*;
      * il :field:`riferimento fattura <ref>` (il numero del documento), la
        :field:`data fattura <invoice_date>`, la valuta se non è quella
        dell'azienda, l'imposta di bollo, le causali come :field:`termini e
        condizioni <narration>` e i riferimenti degli ordini come
        :field:`documento di origine <invoice_origin>`;
      * le righe del documento, con le imposte trovate per aliquota e natura
        (una riga senza imposta è registrata nel chatter come *Tax not found
        for line ...*);
      * la :field:`data di scadenza <invoice_date_due>` (la più lontana delle
        scadenze di pagamento del file, senza termini di pagamento), il
        riferimento di pagamento e il conto bancario (IBAN) del fornitore;
      * il tipo del documento: fatture, note di credito (*TD04*) e gli altri
        tipi noti a Odoo diventano il tipo di fattura giusto; un tipo
        sconosciuto diventa una fattura fornitore;
      * ordini, contratti, DDT e gli allegati dell'XML sono scritti nel
        chatter; il file XML resta allegato alla fattura, nella scheda
        **Fatturazione Elettronica**.

      .. help-if:: module = l10n_it_edi_withholding

         La ritenuta d'acconto del documento è importata come imposta di
         ritenuta sulle righe: controllare gli importi.

      .. help-if:: module = l10n_it_edi_extension

         Con *Italy - E-invoicing - Base Feature* un file ZIP con più fatture
         elettroniche si carica da **Fatturazione ‣ Fornitori ‣ File
         importazione e-fattura** (vedere *Stampe ed esportazione*). Inoltre:

         * il dettaglio delle righe dipende dal *Livello dettaglio
           importazione e-fatture* (**Fatturazione ‣ Configurazione ‣
           Impostazioni**, o l'impostazione del fornitore): *Minimo* crea la
           fattura senza righe, *Aliquota fiscale* una riga per ogni aliquota,
           *Massimo* (predefinito) ogni riga del file;
         * i dati del fornitore (provincia, EORI, albi...) aggiornano il
           contatto, salvo che sia impostato *Non aggiornare il contatto dai
           dati della fattura elettronica*;
         * un messaggio blu in cima alla fattura avvisa quando imponibile,
           imposta o totale del file sono diversi da quelli della fattura; la
           scheda **Dettagli e-fattura** mostra gli importi del file e
           *Fattura elettronica importata* con la sua [`Anteprima`].

      Prima di premere [`Conferma`] controllare:

      * il fornitore (un contatto nuovo? quello giusto?), il riferimento e la
        data della fattura;
      * i totali rispetto al documento e le imposte delle righe, in particolare
        quelle con aliquota zero;
      * la data di scadenza e il conto bancario;
      * l'avviso *Avviso: il documento può essere un duplicato di ...* in cima
        alla fattura: stesso fornitore, riferimento, data e totale. Odoo
        rifiuta anche un file il cui nome è già stato ricevuto dal SdI, e
        l'importazione dello ZIP si ferma con *E-invoice already exists*; il
        pulsante [`Carica`] non controlla il nome del file.

      Errori comuni: se la partita IVA e il Codice Fiscale dell'azienda non
      sono nella sezione acquirente del file, non è importato nulla e il
      chatter dice *Your company's VAT number and Fiscal Code haven't been
      found in the buyer and/or seller sections inside the document*: il file
      è di un'altra azienda. Un file che non è una FatturaPA resta allegato a
      una fattura in bozza vuota. Per gli altri casi (imposta non trovata,
      fornitore sbagliato, duplicati, il file che non si importa) vedere le
      **Domande frequenti**.
