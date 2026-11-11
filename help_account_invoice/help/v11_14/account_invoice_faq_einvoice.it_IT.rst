.. help-if:: module = l10n_it_fatturapa_out

   .. help-question:: Fattura elettronica a cliente estero: perché l'esportazione si ferma sul CAP?

      I dati dell'indirizzo italiano vengono saltati solo se il cliente ha il
      :field:`Codice destinatario <codice_destinatario>` *XXXXXXX* (sette X
      maiuscole): l'XML riceve allora CAP *00000* e provincia *EE*. Con
      *0000000* o *xxxxxxx* minuscolo l'esportazione si ferma con *CAP del
      cliente non impostato*. Nella scheda cliente, scheda **Fattura
      elettronica**, impostare *XXXXXXX*, poi esportare di nuovo la fattura
      elettronica.

   .. help-question:: Perché il CAP di un cliente italiano viene rifiutato?

      Il CAP deve avere esattamente 5 cifre, senza spazi prima o dopo.
      Correggerlo nell'indirizzo del cliente ed esportare di nuovo la fattura
      elettronica.

   .. help-question:: Perché la partita IVA di un cliente estero viene rifiutata?

      La partita IVA deve iniziare con il codice ISO del paese (*ES*, *DE*,
      *CH*...) senza spazi, ad es. *ESB02876001*. Controllare che il prefisso
      sia quello del paese (ad es. *CH*, non *IT*, per un cliente svizzero);
      per la Francia scrivere *FR* e le 11 cifre che seguono. Una partita IVA
      UE deve essere valida sul VIES. Per la Svizzera aggiungere *MWST* o
      *TVA* dopo uno spazio.

   .. help-question:: Cliente extra UE senza partita IVA (Giappone, Regno Unito...): come lo fatturo?

      Non scrivere una partita IVA fittizia: lasciare vuoti partita IVA e
      codice fiscale e impostare il Codice destinatario *XXXXXXX*. Per un
      cliente estero Odoo compila l'XML con il codice del paese e un
      identificativo convenzionale, che lo SdI accetta.

   .. help-question:: Come fatturo a un privato estero?

      Non scrivere un codice fiscale estero numerico: lo SdI lo rifiuta. Per
      un privato estero con codice fiscale italiano impostare il Codice
      destinatario *XXXXXXX* e il codice fiscale italiano corretto.

   .. help-question:: Perché manca il bottone Esporta e-fattura?

      Il bottone compare sulle fatture validate dei clienti che hanno
      spuntato *Abilitare fatturazione elettronica*, nella scheda **Fattura
      elettronica** del cliente. Spuntarlo e controllare il Codice
      destinatario o la *PEC destinatario*. Se la fattura elettronica è già
      stata esportata, usare il suo file.

      .. help-if:: module = universal_connector

         Se il cliente arriva da VG7 correggerlo anche su VG7, altrimenti la
         prossima sincronizzazione toglie di nuovo la spunta.

   .. help-question:: Perché la fattura elettronica viene rifiutata per il Codice destinatario?

      Il Codice destinatario deve avere 7 lettere o cifre (ad es. *G4A/1U8*
      non è valido), altrimenti Odoo si ferma con *Il codice destinatario del
      partner ... deve essere lungo 7 caratteri*. Senza codice e senza PEC lo
      SdI non può recapitare la fattura: scrivere un codice valido, oppure
      *0000000* e la PEC. Senza alcun dato usare *0000000*: la fattura resta
      nel cassetto fiscale del cliente.

   .. help-question:: Perché mancano i dati di pagamento nella fattura elettronica?

      Odoo si ferma con *Il termine di pagamento ... non ha una modalità di
      pagamento e-fattura* (o un *termine*). In **Fatturazione ‣
      Configurazione ‣ Amministrazione ‣ Termini di pagamento** impostare sul
      termine *Termini di pagamento fiscali* e *Metodo di pagamento fiscale*
      (*MPxx*).

   .. help-question:: Perché la fattura elettronica ha un'IVA diversa di 1 o 2 centesimi, e viene rifiutata?

      Normalmente Odoo calcola l'imposta riga per riga e poi le somma: il
      totale può differire dall'imposta calcolata sul totale imponibile (ad
      es. 27,96 al 22% dà 6,14 invece di 6,15). In **Fatturazione ‣
      Configurazione ‣ Impostazioni**, *Metodo di arrotondamento*, scegliere
      *Round globally calculation of taxes* (arrotondamento globale), come
      richiesto dalla norma italiana.

   .. help-question:: Perché la fattura elettronica viene rifiutata per la natura di un'imposta (N2, N3, N6...)?

      Dal 2021 le nature N2, N3 e N6 sono suddivise (N3.1 ... N3.6, N6.1 ...
      N6.9). In **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Imposte**
      impostare la *Natura esenzione* corretta (ad es. art. 9 è *N3.4*, art.
      10 è *N4*) e il *Riferimento normativo* dell'imposta.

   .. help-question:: Perché il canale rifiuta la fattura elettronica per caratteri non validi?

      La descrizione contiene caratteri di controllo copiati da altri
      programmi. Riscrivere a mano la descrizione della riga, poi esportare e
      inviare di nuovo la fattura elettronica.

   .. help-if:: module = l10n_it_withholding_tax

      .. help-question:: Come emetto una fattura con ritenuta d'acconto?

         Creare la ritenuta in **Fatturazione ‣ Configurazione ‣ Contabilità
         ‣ Ritenuta**, con tipo, aliquota e causale di pagamento, poi
         impostarla sulle righe della fattura. Usare una causale valida: *Z*
         non è più ammessa, usare *ZO*.

   .. help-question:: Come scrivo CIG, CUP, ordine o contratto nella fattura elettronica?

      Nella fattura, scheda **Documenti collegati**, aggiungere l'ordine di
      acquisto o il contratto con il suo CIG e CUP: una PA rifiuta la fattura
      senza CIG.

   .. help-question:: Perché la fattura riporta la banca o l'IBAN sbagliati?

      L'IBAN viene dal *Conto bancario* della fattura: con più banche
      aziendali Odoo propone la prima. Scegliere quella giusta sulla
      fattura, prima di validarla.

      .. help-if:: module = assigned_bank

         Per dare a ogni cliente o fornitore la propria banca aziendale,
         impostarla nella scheda **Contabilità** del contatto.

   .. help-if:: module = l10n_it_fiscal_document_type

      .. help-question:: Perché il tipo documento TD24 (fattura differita) non è impostato?

         Le fatture create dai DdT ricevono *TD24*; una fattura fatta a
         mano, o modificata dopo, può restare *TD01*. Controllare il *Tipo di
         documento fiscale* prima di validare la fattura. Se un tipo, ad es.
         *TD29*, non è nell'elenco, il software va aggiornato.

   .. help-question:: Perché non si trova la provincia o la nazione?

      La provincia non esiste con quella sigla (ad es. *PS* per Pesaro e
      Urbino), oppure la nazione ha un altro nome (ad es. *Olanda* invece di
      *Paesi Bassi*). Cercare la nazione con il nome alternativo; aggiungere
      la provincia mancante in modalità sviluppatore, in **Contatti ‣
      Configurazione ‣ Localizzazione ‣ Province/Stati Federali**.

.. help-if:: module = l10n_it_ipa

   .. help-question:: Perché la fattura a una Pubblica Amministrazione viene rifiutata, o inviata come fattura a privati?

      Il cliente è impostato come privato (Codice destinatario di 7
      caratteri) invece che come PA. Nella scheda cliente spuntare *Pubblica
      amministrazione* e scrivere il *Codice IPA* di 6 caratteri. Eliminare
      la fattura elettronica rifiutata ed esportarla di nuovo.

      .. help-if:: module = universal_connector

         Se il cliente arriva da VG7 correggerlo anche su VG7, altrimenti la
         prossima sincronizzazione riscrive i vecchi dati.

.. help-if:: module = l10n_it_efattura_sdi

   .. help-question:: La fattura elettronica è stata inviata: perché non è nel cassetto fiscale, o perché il suo stato non cambia?

      Lo stato dipende dalle notifiche dello SdI, inoltrate dal canale. Le
      fatture alla PA notificano solo la consegna; a volte la notifica
      arriva in ritardo o non arriva.

      1. Controllare sul portale del canale lo stato reale e le ricevute.
      2. In **Fatturazione ‣ Clienti ‣ Fattura elettronica ‣ File e-fattura
         esportati** aprire il file e premere **Check invoice state on SDI**.
      3. Se lo stato resta errato, aprire un ticket con il canale.

      Per dimostrare la consegna al cliente scaricare dal canale l'XML, il
      PDF e la ricevuta.

   .. help-question:: Perché lo schedulatore smette di inviare le fatture elettroniche?

      L'azione pianificata è disattivata o in errore. In modalità
      sviluppatore aprire **Impostazioni ‣ Tecnico ‣ Automazione ‣ Azioni
      pianificate** e riattivare l'azione che invia e riceve le fatture
      elettroniche. Se si ripete, contattare l'assistenza.

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
