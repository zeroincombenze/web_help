.. help-if:: module = l10n_it_einvoice_base

   .. help-question:: Fattura elettronica a cliente estero: perché l'XML si ferma su CAP o provincia?

      I controlli italiani su CAP e provincia vengono saltati solo se il
      cliente ha il :field:`Codice destinatario <codice_destinatario>`
      *XXXXXXX* (sette X maiuscole): *0000000* o *xxxxxxx* minuscolo non
      funzionano. Nella scheda cliente, scheda **Fattura elettronica**,
      impostare *XXXXXXX*, poi creare di nuovo l'XML.

   .. help-question:: Perché il CAP di un cliente italiano viene rifiutato?

      Il CAP deve avere esattamente 5 cifre, senza spazi prima o dopo.
      Correggerlo nell'indirizzo del cliente e creare di nuovo la fattura
      elettronica.

   .. help-question:: Perché la partita IVA di un cliente estero viene rifiutata?

      La partita IVA deve iniziare con il codice ISO del paese (*ES*, *DE*,
      *CH*...) senza spazi, ad es. *ESB02876001*. Controllare che il prefisso
      sia quello del paese (ad es. *CH*, non *IT*, per un cliente svizzero);
      per la Francia scrivere *FR* e le 11 cifre che seguono. Una partita IVA
      UE deve essere valida sul VIES. Per la Svizzera aggiungere *MWST* o
      *TVA* dopo uno spazio.

   .. help-question:: Cliente extra UE senza partita IVA (Giappone, Regno Unito...): come lo fatturo?

      Non scrivere una partita IVA fittizia (ad es. *OO99999999999*): lasciare
      vuota la partita IVA e impostare il Codice destinatario *XXXXXXX*, Odoo
      compila da solo l'XML. Un cliente estero con partita IVA italiana
      richiede un indirizzo italiano, oppure una partita IVA estera, oppure
      nessuna partita IVA.

   .. help-question:: Come fatturo a un privato estero?

      Non scrivere un codice fiscale estero numerico: lo SdI lo rifiuta. Per
      un privato estero con codice fiscale italiano impostare il Codice
      destinatario *XXXXXXX* e il codice fiscale italiano corretto.

   .. help-question:: Perché la fattura a una Pubblica Amministrazione viene rifiutata, o inviata come fattura a privati?

      Il cliente è impostato come privato (Codice destinatario di 7
      caratteri) invece che come PA. Nella scheda cliente spuntare *Pubblica
      amministrazione* e scrivere il *Codice ufficio* (IPA) di 6 caratteri.
      Eliminare la fattura elettronica rifiutata e crearla di nuovo.

      .. help-if:: module = universal_connector

         Se il cliente arriva da VG7 correggerlo anche su VG7, altrimenti la
         prossima sincronizzazione riscrive i vecchi dati.

   .. help-question:: Perché ricevo l'errore "non soggetto a fattura elettronica"?

      Il cliente non ha spuntato *Soggetto a fattura elettronica*, oppure è
      un duplicato creato senza i dati della fattura elettronica. Spuntarlo e
      controllare il Codice destinatario o la *PEC destinatario*.

      .. help-if:: module = universal_connector

         Se il cliente arriva da VG7 correggerlo anche su VG7, altrimenti il
         prossimo ordine toglie di nuovo la spunta.

   .. help-question:: Perché la fattura elettronica viene rifiutata per il Codice destinatario?

      Il Codice destinatario deve avere 7 lettere o cifre (ad es. *G4A/1U8*
      non è valido), altrimenti l'esportazione si ferma con *Il codice
      destinatario del nominativo ... deve essere lungo 7 caratteri*. Senza
      codice e senza PEC
      lo SdI non può recapitare la fattura: scrivere un codice valido, oppure
      *0000000* e la PEC. Senza alcun dato usare *0000000*: la fattura resta
      nel cassetto fiscale del cliente.

   .. help-question:: Perché la fattura elettronica con quantità negative viene rifiutata?

      Lo SdI non accetta quantità negative. Nelle righe di storno o di
      acconto scrivere una quantità positiva e un prezzo unitario negativo;
      controllare che anche la riga di acconto abbia l'imposta.

   .. help-question:: Perché non riesco a inviare la fattura elettronica se la ragione sociale è lunga?

      Lo SdI accetta al massimo 80 caratteri per la ragione sociale:
      accorciarla nella scheda cliente e creare di nuovo l'XML.

   .. help-question:: Perché le note lunghe della fattura elettronica vengono rifiutate?

      Ogni riga delle note (*Causale*) può contenere al massimo 200
      caratteri: dividere il testo su più righe.

   .. help-question:: Perché il termine di pagamento viene rifiutato, o non stampato, nella fattura elettronica?

      La descrizione del termine può superare 60 caratteri (il limite dello
      SdI) o contenere solo uno spazio. In **Contabilità ‣ Configurazione ‣
      Termini di pagamento** accorciare la descrizione, impostare il metodo di
      pagamento e i dati della fattura elettronica (*MPxx*) su ogni riga, e
      mantenere una riga *Saldo*.

   .. help-question:: Perché la fattura elettronica ha un'IVA diversa di 1 o 2 centesimi, e viene rifiutata?

      Odoo calcola l'imposta riga per riga e poi le somma: il totale può
      differire dall'imposta calcolata sul totale imponibile (ad es. 27,96 al
      22% dà 6,14 invece di 6,15).

      .. help-if:: module = account_tax_rounded

         Il modulo *account_tax_rounded* è installato: calcola l'imposta sul
         totale, come richiesto dalla norma italiana. Attenzione: ha dato
         problemi sui corrispettivi con scorporo.

      .. help-if:: module != account_tax_rounded

         Installare il modulo *account_tax_rounded*: calcola l'imposta sul
         totale, come richiesto dalla norma italiana.

   .. help-question:: Perché l'imposta viene rifiutata per la natura (N2, N3, N6...)?

      Dal 2021 le nature N2, N3 e N6 sono suddivise (N3.1 ... N3.6, N6.1 ...
      N6.9). In **Contabilità ‣ Configurazione ‣ Imposte** impostare la
      *Natura* corretta (ad es. art. 9 è *N3.4*, art. 10 è *N4*) e il
      *Riferimento legislativo* dell'imposta.

   .. help-question:: Perché il canale rifiuta la fattura elettronica per caratteri non validi?

      La descrizione contiene caratteri di controllo copiati da altri
      programmi. Riscrivere a mano la descrizione della riga, poi creare e
      inviare di nuovo l'XML.

   .. help-if:: module = l10n_it_withholding_tax

      .. help-question:: Come emetto una fattura con ritenuta d'acconto?

         Creare la ritenuta in **Contabilità ‣ Configurazione ‣ Contabilità ‣
         Ritenuta**, con tipo, aliquota e causale di pagamento, poi
         impostarla sulle righe della fattura. Usare una causale valida: *Z*
         non è più ammessa, usare *ZO*.

   .. help-question:: Come scrivo CIG, CUP, ordine o contratto nella fattura elettronica?

      Nella fattura, scheda **Documenti collegati**, aggiungere l'ordine di
      acquisto o il contratto con il suo CIG e CUP: una PA rifiuta la fattura
      senza CIG. L'IBAN viene dalla banca impostata sulla fattura o sul
      termine di pagamento.

   .. help-question:: Perché la fattura riporta la banca o l'IBAN sbagliati?

      Manca la banca aziendale sull'azienda o sul cliente; con più banche
      aziendali Odoo prende la prima. Impostare la banca sull'azienda.

      .. help-if:: module = assigned_bank

         Per dare a ogni cliente o fornitore la propria banca aziendale,
         impostarla nella scheda **Contabilità** del contatto.

   .. help-question:: Perché il tipo documento TD24 (fattura differita) non è impostato?

      Le fatture da DdT devono essere *TD24*; una modifica della fattura può
      riportare il tipo a *TD01*. Controllare il *Tipo documento fiscale*
      prima di validare la fattura. Se un tipo, ad es. *TD29*, non è
      nell'elenco, il software va aggiornato.

   .. help-question:: Perché non si trova la provincia o la nazione?

      La provincia non esiste con quella sigla (ad es. *PS* per Pesaro e
      Urbino), oppure la nazione ha un altro nome (ad es. *Olanda* invece di
      *Paesi Bassi*). Cercare la nazione con il nome alternativo; aggiungere
      la provincia mancante in modalità sviluppatore, in **Vendite ‣
      Configurazione ‣ Contatti ‣ Localizzazione ‣ Stati Federali**.

.. help-if:: module = l10n_it_einvoice_send2sdi

   .. help-question:: La fattura elettronica è stata inviata: perché non è nel cassetto fiscale, o perché il suo stato non cambia?

      Lo stato dipende dalle notifiche dello SdI, inoltrate dal canale
      (Evolve, certdoc). Le fatture alla PA notificano solo la consegna; a
      volte la notifica arriva in ritardo o non arriva.

      1. Controllare su certdoc lo stato reale e le ricevute.
      2. Nel file della fattura elettronica premere **Verifica invio**.
      3. Se lo stato resta errato, aprire un ticket con il canale.

      Per dimostrare la consegna al cliente scaricare da certdoc lo ZIP con
      l'XML, il PDF e la ricevuta.

   .. help-question:: Perché lo schedulatore smette di inviare le fatture elettroniche?

      L'azione pianificata è disattivata o in errore. In modalità
      sviluppatore aprire **Impostazioni ‣ Tecnico ‣ Automazione ‣ Azioni
      pianificate** e riattivare l'azione che invia e riceve le fatture
      elettroniche. Se si ripete, contattare l'assistenza.

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
