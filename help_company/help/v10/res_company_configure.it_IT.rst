.. _configure:

Come configurare
----------------

**Configurazione ‣ Impostazioni Generali**: **Configura i dati aziendali**
apre l'azienda corrente; *Gestione multi aziendale*, nella riga **Multi
Company**, attiva più aziende, poi premere **Salva**. Con più aziende la
maschera mostra l'*Azienda Principale*, nella barra in alto compare il
selettore delle aziende e gli utenti ricevono *Aziende consentite* e
*Azienda corrente* nella scheda **Diritti di accesso** della loro maschera
(**Configurazione ‣ Utenti ‣ Utenti**); l'azienda corrente è quella in cui
l'utente lavora. La sezione **Configurazione Report** imposta il piè di
pagina e il formato carta delle stampe.

Con la Fatturazione, ogni azienda ha il proprio piano dei conti e le proprie
imposte, scelti in **Contabilità ‣ Configurazione ‣ Impostazioni** (*Modello*
del **Piano dei conti**) lavorando in quell'azienda.

Fattura elettronica (Italia)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le aziende italiane inviano e ricevono le fatture come file XML
(*FatturaPA*) tramite il *Sistema di Interscambio* (SdI) dell'Agenzia delle
Entrate. In questa versione la fattura elettronica è data dai moduli
Zeroincombenze dei repository *l10n-italy* e *l10n-italy-supplemental*, da
installare da **Apps**:

* **Italy - Accounting** (``l10n_it``): il piano dei conti e le imposte
  italiani generici; oppure **ITA - Fiscal localization by
  Zeroincombenze(R)** (``l10n_it_coa``), un piano dei conti più dettagliato.
* **EInvoice + FatturaPA** (``l10n_it_einvoice_base``): la base della
  fattura elettronica. Installa con sé le tabelle dell'Agenzia delle Entrate
  (``l10n_it_ade``), il Codice Fiscale (``l10n_it_fiscalcode``), i dati del
  REA (``l10n_it_rea``), l'indirizzo PEC (``l10n_it_pec``) e la scheda
  **Fattura elettronica** dei contatti (``l10n_it_fiscal_ipa``); aggiunge la
  sezione **Fattura elettronica** a **Contabilità ‣ Configurazione ‣
  Impostazioni**.
* **Italian Localization - FatturaPA - Emissione**
  (``l10n_it_einvoice_out``): crea l'XML delle fatture clienti:
  selezionarle, poi **Azione ‣ Esportare fattura elettronica**.
* **ITA - Fattura elettronica - Ricezione** (``l10n_it_einvoice_in``):
  importa l'XML delle fatture fornitore ricevute, da **Contabilità ‣
  Acquisti ‣ Fattura fornitore elettronica**.
* **Send E-Invoice to SdI** (``l10n_it_einvoice_send2sdi``): invia le
  fatture elettroniche allo SdI, e riceve le fatture fornitore e le notifiche
  dello SdI, tramite un intermediario, il *Canale invio*.
* Facoltativi: **Fattura elettronica - Export ZIP**
  (``l10n_it_einvoice_export_zip``) esporta più fatture elettroniche in un
  file ZIP; i moduli ``l10n_it_einvoice_out_*`` aggiungono all'XML la
  ritenuta d'acconto (``_wt``), l'inversione contabile (``_rc``), i
  documenti di trasporto (``_ddt``), le lettere d'intento (``_li``);
  ``l10n_it_einvoice_stamp`` l'imposta di bollo.

Per attivare la fattura elettronica:

#. Impostare la :field:`nazione <country_id>` dell'azienda a *Italia* e
   compilare l'indirizzo completo (via, CAP, città, stato), la
   :field:`partita IVA <vat>`, il :field:`telefono <phone>` e l':field:`email
   <email>`: l'esportazione della fattura elettronica si ferma quando ne
   manca uno.
#. Compilare il *Codice Fiscale* sul contatto dell'azienda e, nella scheda
   **REA Data**, i dati del REA, se l'azienda è iscritta al registro delle
   imprese.
#. Aprire **Contabilità ‣ Configurazione ‣ Impostazioni**, sezione **Fattura
   elettronica**: scegliere la *Posizione fiscale* (il Regime fiscale) e la
   *Sequenza* dei file della fattura elettronica, entrambe obbligatorie, il
   *Canale invio per e-fattura* e, se serve, *Art. 73*, il *Rappresentante
   legale* e il *Terzo incaricato/Mittente*. Premere **Salva**.
#. Con ``l10n_it_einvoice_send2sdi``, configurare il canale in **Contabilità
   ‣ Configurazione ‣ Contabilità ‣ Definizioni dell'Agenzia delle Entrate ‣
   Canale invio** con i dati forniti dall'intermediario.
#. Su ogni cliente, nella scheda **Fattura elettronica**, spuntare *Soggetto
   a fattura elettronica* e compilare il *Codice destinatario* (7 caratteri)
   o la *PEC destinatario*.

.. help-if:: module = l10n_it_einvoice_base

   .. admonition:: Importante
      :class: important

      Le fatture elettroniche non vengono esportate finché la *Posizione
      fiscale* della sezione **Fattura elettronica** è vuota: controllarla
      ora in **Contabilità ‣ Configurazione ‣ Impostazioni**.

.. help-if:: module != l10n_it_einvoice_base

   Il modulo *EInvoice + FatturaPA* non è installato in questo database: la
   sezione **Fattura elettronica** delle impostazioni e la scheda **REA
   Data** compaiono dopo averlo installato.
