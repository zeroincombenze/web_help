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
indirizzo e :field:`partita IVA <vat>` sono stampati su preventivi, fatture e
ogni altra stampa, e la contabilità di ogni azienda è tenuta separata, nella
sua :field:`valuta <currency_id>`. Un database può contenere più aziende,
dopo aver attivato *Gestione multi azienda*; un'azienda di un gruppo può
avere un':field:`Azienda madre <parent_id>`. Indirizzo, partita IVA, telefono
ed e-mail dell'azienda sono memorizzati sul suo partner, un contatto come gli
altri.

.. help-if:: module = l10n_it_edi

   .. admonition:: Importante
      :class: important

      **Impostare il Tax System.** La fattura elettronica italiana richiede
      il :field:`Tax System <l10n_it_tax_system>` (il Regime fiscale)
      dell'azienda, ad es. *[RF01] Ordinario* o *[RF19] Regime forfettario*:
      finché è vuoto, la validazione di una fattura si ferma con l'errore
      *The seller's company must have a tax system.* Sceglierlo nella scheda
      **Informazioni generali**, sotto la partita IVA.

.. help-if:: module = l10n_it_fatturapa

   .. admonition:: Importante
      :class: important

      **Impostare la Posizione fiscale della fattura elettronica.** La
      fattura elettronica italiana richiede la :field:`Posizione fiscale
      <fatturapa_fiscal_position_id>` (il Regime fiscale) dell'azienda, ad es.
      *Regime ordinario* (RF01) o *Regime forfettario* (RF19): sceglierla
      nella scheda **E-fattura**. Il campo è obbligatorio: la maschera non si
      può salvare finché è vuoto.

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

.. help-if:: module = l10n_it_edi

   * Codice Fiscale: *01234567890* (per un'azienda di solito è la partita
     IVA senza *IT*)
   * Tax System: *[RF01] Ordinario*
   * Server PEC, Company PEC-mail e Government PEC-mail, come descritto in
     *Come configurare*

   e, nella scheda **Electronic Invoicing**, *Company listed on the register
   of companies* spuntato, con ufficio, numero, capitale sociale e stato di
   liquidazione del registro.

.. help-if:: module = l10n_it_fatturapa

   * Codice Fiscale: *01234567890* (per un'azienda di solito è la partita
     IVA senza *IT*)

   poi, nella scheda **Dati REA**, i dati del REA e, nella scheda
   **E-fattura**, la Posizione fiscale *Regime ordinario* e il Canale SdI.

.. help-if:: module != l10n_it_edi and module != l10n_it_fatturapa

   poi installare i moduli della fattura elettronica descritti in *Come
   configurare* e compilare Codice Fiscale e Regime fiscale.

.. _faq:

Domande frequenti
-----------------

Fare clic sul pulsante **Argomento** per tornare alla pagina di aiuto specifica.

.. help-question:: Perché non vedo il campo Regime fiscale?

   È aggiunto dai moduli della fattura elettronica: il *Tax System* sotto la
   partita IVA con *Italy - E-invoicing* (``l10n_it_edi``), la *Posizione
   fiscale* della scheda **E-fattura** con *ITA - Fattura elettronica - Base*
   (``l10n_it_fatturapa``). Installarne uno: non si possono installare
   insieme.

.. help-question:: La validazione della fattura dice "The seller's company must have a tax system."

   Il :field:`Tax System <l10n_it_tax_system>` dell'azienda è vuoto:
   impostarlo in questa maschera e validare di nuovo la fattura.

.. help-question:: Perché non riesco a cambiare la valuta?

   La valuta non si può cambiare quando l'azienda ha già movimenti contabili:
   creare una nuova azienda se serve un'altra valuta contabile.

.. help-question:: Perché non riesco a duplicare un'azienda?

   Odoo non lo permette (*La duplicazione di un'azienda non è possibile.
   Creare una nuova azienda.*): creare la nuova azienda dall'elenco.

.. help-question:: Dove si cambiano il logo e l'aspetto delle stampe?

   Il logo si cambia qui: premere **Modifica** e fare clic sull'immagine. Il
   formato carta e l'aspetto delle stampe si impostano in **Impostazioni ‣
   Impostazioni generali**, sezione **Documenti commerciali**: *Formato* e
   *Modello documento* (**Modifica modello documento**).

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-07 18:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
