.. help-if:: module = l10n_it_edi

   .. help-question:: Fattura elettronica a cliente estero: quale Codice destinatario devo impostare?

      Nessuno: per un cliente il cui paese non è l'Italia Odoo scrive da solo
      nell'XML il Codice destinatario *XXXXXXX* e il CAP *00000* (per San
      Marino il codice fisso del paese). Basta controllare che la
      :field:`nazione <country_id>` del cliente sia impostata.

   .. help-question:: Perché il CAP di un cliente italiano viene rifiutato?

      Il CAP deve avere esattamente 5 cifre, senza spazi prima o dopo.
      Correggerlo nell'indirizzo del cliente, poi inviare di nuovo la
      fattura.

   .. help-question:: Perché la partita IVA di un cliente UE viene rifiutata, o letta come italiana?

      Per un cliente UE la partita IVA deve iniziare con il codice ISO del
      paese (*ES*, *DE*, *FR*...), ad es. *ESB02876001*: Odoo toglie il
      prefisso nell'XML. Una partita IVA che inizia con cifre viene presa come
      italiana. Controllare che il prefisso sia quello del paese e che il
      numero sia valido sul VIES.

   .. help-question:: Cliente extra UE senza partita IVA (Giappone, Regno Unito...): come lo fatturo?

      Lasciare vuota la partita IVA e impostare la nazione: Odoo scrive il
      valore convenzionale *OO99999999999* (*0000000* per un cliente UE) che
      lo SdI accetta. Non scrivere a mano una partita IVA fittizia.

   .. help-question:: Come fatturo a un privato estero?

      Non scrivere un codice fiscale estero numerico: lo SdI lo rifiuta, e un
      contatto con *Codice Fiscale* viene preso come italiano. Per un privato
      estero con codice fiscale italiano scrivere il *Codice Fiscale* e
      l'indirizzo italiano.

   .. help-question:: Perché la fattura a una Pubblica Amministrazione viene rifiutata, o inviata come fattura a privati?

      Odoo considera PA un cliente italiano il cui :field:`Codice
      destinatario <l10n_it_pa_index>`, nella scheda **Fatturazione
      Elettronica** del contatto, ha 6 caratteri (il codice IPA); 7 caratteri
      indicano un'azienda privata. Scrivere il codice IPA; poi, nella scheda
      **Fatturazione Elettronica** della fattura, compilare *Tipo Documento
      Origine*, nome e data (l'ordine o il contratto della PA), con CIG e CUP
      quando richiesti.

      .. help-if:: module = universal_connector

         Se il cliente arriva da VG7 correggerlo anche su VG7, altrimenti la
         prossima sincronizzazione riscrive i vecchi dati.

   .. help-question:: Perché la fattura elettronica viene rifiutata per il Codice destinatario?

      Il Codice destinatario deve avere 7 lettere o cifre per un'azienda (6
      per una PA): ad es. *G4A/1U8* non è valido. Senza codice Odoo scrive
      *0000000*: lo SdI recapita la fattura alla *PEC destinatario* del
      contatto se presente, altrimenti resta nel cassetto fiscale del
      cliente.

   .. help-question:: Perché la fattura elettronica con quantità negative viene rifiutata?

      Lo SdI non accetta quantità negative. Nelle righe di storno o di
      acconto scrivere una quantità positiva e un prezzo unitario negativo;
      controllare che anche la riga di acconto abbia l'imposta.

   .. help-question:: Perché la fattura elettronica ha un'IVA diversa di 1 o 2 centesimi, e viene rifiutata?

      Con l'arrotondamento per riga Odoo calcola l'imposta riga per riga e
      poi le somma: il totale può differire dall'imposta calcolata sul totale
      imponibile (ad es. 27,96 al 22% dà 6,14 invece di 6,15). In
      **Fatturazione ‣ Configurazione ‣ Impostazioni**, *Metodo
      arrotondamento*, scegliere *Arrotondare globalmente*, come richiesto
      dalla norma italiana.

   .. help-question:: Perché la fattura elettronica viene rifiutata per la natura di un'imposta (N2, N3, N6...)?

      Un'imposta con aliquota 0% richiede sia l':field:`Esenzione
      <l10n_it_exempt_reason>` (la natura, ad es. art. 9 è *N3.4*, art. 10 è
      *N4*) sia il *Riferimento legislativo*. In **Fatturazione ‣
      Configurazione ‣ Imposte** aprire l'imposta e impostarli; le vecchie
      nature N2, N3 e N6 sono suddivise dal 2021 (N3.1 ... N3.6, N6.1 ...
      N6.9).

   .. help-question:: Perché il canale rifiuta la fattura elettronica per caratteri non validi?

      La descrizione contiene caratteri di controllo copiati da altri
      programmi. Riscrivere a mano la descrizione della riga, poi inviare di
      nuovo la fattura.

   .. help-if:: module = l10n_it_edi_withholding

      .. help-question:: Come emetto una fattura con ritenuta d'acconto?

         In **Fatturazione ‣ Configurazione ‣ Imposte** creare un'imposta con
         *Tipo Ritenuta (Italia)*, aliquota e *Causale Ritenuta (Italia)*, poi
         aggiungerla alle righe della fattura accanto all'IVA. *Z* è
         deprecata: usare *ZO*.

   .. help-question:: Come scrivo CIG, CUP, ordine o contratto nella fattura elettronica?

      Nella fattura, scheda **Fatturazione Elettronica**, impostare *Tipo
      Documento Origine* (ordine di acquisto, contratto...), il suo nome e la
      data, poi CIG e CUP: una PA rifiuta la fattura senza CIG.

   .. help-question:: Perché la fattura riporta la banca o l'IBAN sbagliati?

      L'IBAN viene dalla *Banca del beneficiario* della fattura, nella scheda
      **Altre informazioni**: con più banche aziendali Odoo propone la prima.
      Scegliere quella giusta prima di confermare la fattura.

      .. help-if:: module = assigned_bank

         Per dare a ogni cliente o fornitore la propria banca aziendale,
         impostarla nella scheda **Fatturazione** del contatto.

   .. help-if:: module = l10n_it_edi_ndd

      .. help-question:: Come scelgo il tipo documento (TD24, TD25...) o il metodo di pagamento (MPxx)?

         Odoo propone il *Tipo di documento* in base al tipo di fattura, e il
         metodo di pagamento *MP05* (bonifico). Prima di confermare la
         fattura cambiarli nella scheda **Fatturazione Elettronica**, ad es.
         *TD24* per una fattura differita da DdT.

   .. help-question:: Perché non si trova la provincia o la nazione?

      La provincia non esiste con quella sigla (ad es. *PS* per Pesaro e
      Urbino), oppure la nazione ha un altro nome (ad es. *Olanda* invece di
      *Paesi Bassi*). Cercare la nazione con il nome alternativo; aggiungere
      la provincia mancante in **Contatti ‣ Configurazione ‣ Localizzazione ‣
      Province/Stati federali**.

   .. help-question:: La fattura elettronica è stata inviata: perché non è nel cassetto fiscale, o perché il suo stato non cambia?

      Lo stato della fattura, nella scheda **Fatturazione Elettronica**,
      dipende dalle notifiche dello SdI: *Elaborazione SdI*, poi ad es.
      *Accettato dall'SdI, Consegnato al Partner* o *Rifiutato SdI*. Le
      fatture alla PA notificano solo consegna ed esito; a volte la notifica
      arriva in ritardo. Premere **Controlla Invio** sulla fattura per
      chiedere subito lo stato; se resta errato, aprire un ticket con
      l'assistenza.

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

      In **Fatturazione ‣ Fornitori ‣ Fatture** premere **Carica** e
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
      **Rettificare** in alto: diventa del tipo corretto, con importi
      positivi.
