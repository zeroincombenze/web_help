.. _configure:

Come configurare
----------------

**Impostazioni ‣ Impostazioni generali**, sezione **Multi azienda**:
*Gestione multi azienda* attiva più aziende, poi premere **Salva**; il
pulsante **Aziende** le elenca. Con più aziende la maschera mostra
l'*Azienda madre*, nella barra in alto compare il selettore delle aziende e
gli utenti ricevono *Aziende ammesse* e *Azienda corrente* nella scheda
**Diritti di accesso** della loro maschera (**Impostazioni ‣ Utenti e aziende
‣ Utenti**); l'azienda corrente è quella in cui l'utente lavora. La sezione
**Documenti commerciali** imposta il *Formato* carta e il *Modello documento*
delle stampe. **Impostazioni ‣ Bacheca**, riquadro dell'azienda, **Imposta**
apre l'azienda corrente.

Con la Fatturazione, ogni azienda ha il proprio piano dei conti e le proprie
imposte, scelti in **Fatturazione ‣ Configurazione ‣ Impostazioni**
(*Pacchetto* della **Localizzazione fiscale**) lavorando in quell'azienda.

Fattura elettronica (Italia)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le aziende italiane inviano e ricevono le fatture come file XML
(*FatturaPA*) tramite il *Sistema di Interscambio* (SdI) dell'Agenzia delle
Entrate. Il piano dei conti è **Italy - Accounting** (``l10n_it``), oppure
**ITA - Fiscal localization by Zeroincombenze(R)** (``l10n_it_coa``), più
dettagliato. Per la fattura elettronica ci sono due alternative, che non si
possono installare insieme; installarne una da **Applicazioni**.

**Modulo di Odoo: Italy - E-invoicing** (``l10n_it_edi``). Quando una
fattura di un'azienda italiana viene validata, crea l'XML e lo invia via PEC
allo SdI; legge le fatture fornitore e le notifiche dello SdI dalla casella
PEC. Aggiunge all'azienda *Codice Fiscale*, *Tax System*, i campi della PEC
e la scheda **Electronic Invoicing**, e ai contatti *PEC e-mail*, *Codice
Fiscale* e *PA index*. Le sue etichette non sono tradotte. Per attivarlo:

#. Impostare la :field:`nazione <country_id>` dell'azienda a *Italia* e
   compilare l'indirizzo completo (via, CAP di 5 cifre, città), la
   :field:`partita IVA <vat>`, il *Codice Fiscale* e il *Tax System*: la
   validazione di una fattura si ferma quando ne manca uno.
#. In modalità sviluppatore, configurare la casella PEC dell'azienda in
   **Impostazioni ‣ Funzioni tecniche ‣ E-mail ‣ Server posta in uscita**, e
   in **Impostazioni ‣ Funzioni tecniche ‣ E-mail ‣ Server posta in arrivo**
   (IMAP) con *PEC server* spuntato.
#. In questa maschera, sotto l'indirizzo, scegliere il *Server PEC* e
   compilare *Company PEC-mail* e *Government PEC-mail* (l'indirizzo PEC
   dello SdI, ad es. *sdi01@pec.fatturapa.it*).
#. Nella scheda **Electronic Invoicing**, spuntare *Company listed on the
   register of companies* e compilarne i dati, se l'azienda è iscritta;
   spuntare *Company have a tax representative* per un'azienda estera con un
   rappresentante fiscale in Italia.
#. Su ogni cliente compilare il *PA index* (il codice destinatario di 7
   caratteri) o la *PEC e-mail*; per una persona fisica il Codice Fiscale. Le
   fatture alla Pubblica Amministrazione (PA index di 6 caratteri) non sono
   inviate: scaricare l'XML e inviarlo da sé.

**Moduli OCA: ITA - Fattura elettronica - Base** (``l10n_it_fatturapa``) del
repository *l10n-italy*, con **ITA - Fattura elettronica - Emissione**
(``l10n_it_fatturapa_out``) per le fatture clienti, **ITA - Fattura
elettronica - Ricezione** (``l10n_it_fatturapa_in``) per le fatture
fornitore, e il canale verso lo SdI: **ITA - Fattura elettronica - Supporto
PEC** (``l10n_it_fatturapa_pec``) o **ITA - Fattura elettronica - Supporto
SDICoop** (``l10n_it_fatturapa_sdicoop``), entrambi basati su
``l10n_it_sdi_channel``. Installano il Codice Fiscale
(``l10n_it_fiscalcode``) e i dati del REA (``l10n_it_rea``); il facoltativo
``l10n_it_fatturapa_export_zip`` esporta più fatture elettroniche in un file
ZIP. Per attivarli:

#. Impostare la :field:`nazione <country_id>` dell'azienda a *Italia* e
   compilare l'indirizzo completo, la :field:`partita IVA <vat>`, il *Codice
   Fiscale* e, nella scheda **Dati REA**, i dati del REA, se l'azienda è
   iscritta.
#. Configurare il canale in **Fatturazione ‣ Configurazione ‣ Contabilità ‣
   Canali SdI**.
#. Nella scheda **E-fattura** di questa maschera scegliere la *Posizione
   fiscale* (il Regime fiscale) e il *Canale SdI*, entrambi obbligatori.
#. In **Fatturazione ‣ Configurazione ‣ Impostazioni**, sezione **Fatture
   elettroniche**, controllare la *Posizione fiscale* e compilare, se serve,
   *Art. 73*, il *Rappresentante legale (fiscale)*, la *Stabile
   organizzazione* e il *Terzo / Trasmittente*. Premere **Salva**.
#. Su ogni cliente, nella scheda **Fattura elettronica**, spuntare
   *Abilitare fatturazione elettronica* e compilare il *Codice destinatario*
   (7 caratteri) o la *PEC destinatario*.

.. help-if:: module = l10n_it_edi

   .. admonition:: Importante
      :class: important

      Le fatture dell'azienda non si possono validare finché il suo **Tax
      System** è vuoto: controllarlo ora nella scheda **Informazioni
      generali**.

.. help-if:: module != l10n_it_edi and module != l10n_it_fatturapa

   In questo database non è installato nessun modulo della fattura
   elettronica: i campi del Regime fiscale e della fattura elettronica
   compaiono dopo averne installato uno.
