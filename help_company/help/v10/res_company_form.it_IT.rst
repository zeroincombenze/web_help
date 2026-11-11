.. help-page:: res_company_form
   :title: Azienda
   :model: res.company
   :view-type: form
   :priority: 96

Azienda
=======

.. _description:

Descrizione
-----------

Fare clic sul pulsante **Pronto** per sapere come usare questo aiuto; fare
clic sul pulsante **FAQ** per le domande più comuni già risolte.

L'azienda è il soggetto giuridico che emette i documenti di Odoo: nome, logo,
:field:`Slogan aziendale <rml_header1>`, indirizzo e :field:`partita IVA
<vat>` sono stampati su preventivi, fatture e ogni altra stampa, e la
contabilità di ogni azienda è tenuta separata, nella sua :field:`valuta
<currency_id>`. Un database può contenere più aziende, dopo aver attivato
*Gestione multi aziendale*; un'azienda di un gruppo può avere
un':field:`Azienda Principale <parent_id>`. Indirizzo, partita IVA, telefono
ed email dell'azienda sono memorizzati sul suo partner, un contatto come gli
altri.

.. help-if:: module = l10n_it_einvoice_base

   .. admonition:: Importante
      :class: important

      **Impostare la Posizione fiscale della fattura elettronica.** La
      fattura elettronica italiana richiede la *Posizione fiscale* (il Regime
      fiscale) dell'azienda, ad es. *Regime ordinario* (RF01) o *Regime
      forfettario* (RF19): finché è vuota l'esportazione della fattura
      elettronica si ferma con l'errore *Posizione fiscale non impostata.* Il
      campo non è in questa maschera: impostarlo in **Contabilità ‣
      Configurazione ‣ Impostazioni**, sezione **Fattura elettronica**,
      insieme alla *Sequenza* dei file della fattura elettronica.

.. help-include:: res_company_new.rst

.. help-include:: res_company_update.rst

.. help-include:: res_company_configure.rst

.. help-include:: res_company_report.rst

.. _example:

Esempio
-------

**Un'azienda italiana pronta per la fattura elettronica.** Premere
**Modifica** e, nella scheda **Informazioni generali**, compilare:

* Indirizzo: *Via Roma 1*, *00100 Roma*, stato *Roma*, nazione *Italia*
* Partita IVA: *IT01234567890*
* Telefono ed Email: entrambi sono scritti nella fattura elettronica

.. help-if:: module = l10n_it_einvoice_base

   poi:

   * nella scheda **REA Data**, ufficio, numero, capitale sociale, tipo socio
     e stato di liquidazione del REA, se l'azienda è iscritta al registro
     delle imprese;
   * sul contatto dell'azienda, il *Codice Fiscale* (per un'azienda di solito
     è la partita IVA senza *IT*);
   * in **Contabilità ‣ Configurazione ‣ Impostazioni**, sezione **Fattura
     elettronica**, la *Posizione fiscale* *Regime ordinario* e la
     *Sequenza*.

.. help-if:: module != l10n_it_einvoice_base

   poi installare i moduli della fattura elettronica descritti in *Come
   configurare*.

.. _faq:

Domande frequenti
-----------------

Fare clic sul pulsante **Argomento** per tornare alla pagina di aiuto specifica.

.. help-question:: Dov'è il Regime fiscale dell'azienda?

   È la *Posizione fiscale* della sezione **Fattura elettronica** in
   **Contabilità ‣ Configurazione ‣ Impostazioni**, aggiunta dal modulo
   *EInvoice + FatturaPA* (``l10n_it_einvoice_base``). I valori possibili
   sono elencati in **Contabilità ‣ Configurazione ‣ Contabilità ‣
   Definizioni dell'Agenzia delle Entrate ‣ Posizione Fiscale Fattura
   Elettronica**.

.. help-question:: L'esportazione dice "Posizione fiscale non impostata."

   La *Posizione fiscale* della fattura elettronica è vuota: impostarla in
   **Contabilità ‣ Configurazione ‣ Impostazioni**, sezione **Fattura
   elettronica**, ed esportare di nuovo la fattura.

.. help-question:: Dove si scrive il Codice Fiscale dell'azienda?

   Il *Codice Fiscale* (modulo ``l10n_it_fiscalcode``) è memorizzato sul
   contatto dell'azienda, non in questa maschera: aprire il contatto (in
   modalità sviluppatore il campo *Partner* di questa maschera vi porta),
   premere **Modifica** e compilare *Codice Fiscale*, accanto alla partita
   IVA.

.. help-question:: Perché non riesco a cambiare la valuta?

   La valuta non si può cambiare quando l'azienda ha già movimenti contabili
   (*Non è possibile cambiare la divisa dell'azienda perchè esistono già delle
   registrazioni contabili.*): creare una nuova azienda se serve un'altra
   valuta contabile.

.. help-question:: Dove si cambiano il logo e l'aspetto delle stampe?

   Il logo si cambia qui: premere **Modifica** e fare clic sull'immagine. Lo
   *Slogan aziendale*, sotto il nome, è stampato nell'intestazione delle
   stampe. Il piè di pagina e il formato carta si impostano in
   **Configurazione ‣ Impostazioni Generali**, sezione **Configurazione
   Report**.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-07 18:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
