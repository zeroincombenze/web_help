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

L'azienda è il soggetto giuridico che emette i documenti di Odoo: nome, logo,
indirizzo, :field:`partita IVA <vat>` e :field:`valuta <currency_id>` sono
stampati su preventivi, fatture e ogni altra stampa, e la contabilità di ogni
azienda è tenuta separata. Un database può contenere più aziende; un'azienda
può avere delle **Filiali**, che condividono le impostazioni contabili
dell'azienda principale. Indirizzo, partita IVA e recapiti dell'azienda sono
memorizzati sul suo :field:`partner <partner_id>`, un contatto come gli altri.

.. help-if:: module = l10n_it_edi

   .. admonition:: Importante
      :class: important

      **Impostare il Regime fiscale.** La fattura elettronica italiana
      richiede il :field:`Regime fiscale <l10n_it_tax_system>` dell'azienda,
      ad es. *[RF01] Ordinario* o *[RF19] Regime forfettario*: finché è vuoto
      Odoo non crea le fatture elettroniche, e l'invio di una fattura si
      ferma con l'errore *La/e azienda/e deve/devono avere un Regime Fiscale*.
      Sceglierlo nella scheda **Informazioni generali**, sotto la partita
      IVA; il campo è visibile quando la nazione dell'azienda è l'Italia.

.. help-include:: res_company_new.rst

.. help-include:: res_company_update.rst

.. help-include:: res_company_configure.rst

.. help-include:: res_company_report.rst

.. _example:

Esempio
-------

**Un'azienda italiana pronta per la fattura elettronica.** Nella scheda
**Informazioni generali**:

* Indirizzo: *Via Roma 1*, *00100 Roma (RM)*, *Italia*
* Partita IVA: *IT01234567890*

.. help-if:: module = l10n_it_edi

   * Codice fiscale: *01234567890* (per una società di solito è la partita
     IVA senza *IT*)
   * Regime fiscale: *[RF01] Ordinario*

   e, nella scheda **Fatturazione Elettronica**, *L'azienda compare nel
   registro delle imprese* spuntato, con ufficio, numero, capitale sociale e
   stato di liquidazione del REA.

.. help-if:: module != l10n_it_edi

   poi installare i moduli della fattura elettronica descritti in *Come
   configurare* e compilare codice fiscale e Regime fiscale.

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non vedo il campo Regime fiscale?

   Il campo è aggiunto dal modulo *Italy - E-invoicing* (``l10n_it_edi``) ed
   è visibile solo quando la :field:`nazione <country_id>` dell'azienda è
   l'Italia: installare il modulo e impostare la nazione.

.. help-question:: La fattura dice "La/e azienda/e deve/devono avere un Regime Fiscale".

   Il :field:`Regime fiscale <l10n_it_tax_system>` dell'azienda è vuoto:
   impostarlo in questa maschera e inviare di nuovo la fattura.

.. help-question:: Perché non riesco a cambiare la valuta?

   La valuta non si può cambiare quando l'azienda ha già movimenti contabili:
   creare una nuova azienda se serve un'altra valuta contabile.

.. help-question:: Dove si cambiano il logo e l'aspetto delle stampe?

   Il logo si cambia qui, facendo clic sull'immagine. L'aspetto (caratteri,
   colori, intestazione e piè di pagina) si imposta in **Impostazioni ‣
   Impostazioni generali ‣ Aziende ‣ Configura struttura documento**.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-07 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
