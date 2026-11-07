.. _configure:

Come configurare
----------------

**Impostazioni ‣ Impostazioni generali ‣ Aziende** mostra l'azienda corrente:
**Aggiorna informazioni** la apre, **Gestisci aziende** le elenca tutte, e
**Configura struttura documento** imposta l'aspetto delle stampe. Ogni utente
lavora per le aziende indicate nelle *Aziende consentite* dell'utente, scelte
in **Impostazioni ‣ Utenti e aziende ‣ Utenti**; l'azienda predefinita è
quella usata all'accesso.

Con Fatturazione, ogni azienda ha la propria *Localizzazione fiscale* (piano
dei conti e imposte), scelta in **Fatturazione ‣ Configurazione ‣
Impostazioni** lavorando in quell'azienda.

Fattura elettronica (Italia)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le aziende italiane inviano e ricevono le fatture come file XML
(*FatturaPA*) tramite il *Sistema di Interscambio* (SdI) dell'Agenzia delle
Entrate. Servono questi moduli, da **App**:

* **Italy - Accounting** (``l10n_it``): piano dei conti e imposte italiani;
  si installa scegliendo *Italia* come *Localizzazione fiscale*.
* **Italy - Accounting Zeroincombenze** (``l10n_it_coa``): piano dei conti
  alternativo, più dettagliato, di Zeroincombenze.
* **Italy - E-invoicing** (``l10n_it_edi``): installato insieme a
  ``l10n_it``. Crea l'XML di fatture e note di credito clienti, le invia allo
  SdI e importa le fatture fornitori ricevute, tramite il proxy di Odoo
  (modulo ``account_edi_proxy_client``, installato con esso). Aggiunge
  all'azienda il :field:`codice fiscale <l10n_it_codice_fiscale>`, il
  **Regime fiscale** e la scheda **Fatturazione Elettronica**, e ai contatti
  *Codice fiscale*, *Codice destinatario* e *PEC destinatario*.
* **Italy - E-invoicing - Additional module to support the debit notes**
  (``l10n_it_edi_ndd``) e **Italy - Sale E-invoicing**
  (``l10n_it_edi_sale``): installati automaticamente, aggiungono all'XML i
  tipi documento e i dati degli ordini di vendita.
* Facoltativi: **Italy - E-invoicing (Withholding)**
  (``l10n_it_edi_withholding``) per ritenute d'acconto e casse
  previdenziali, **Italy - Declaration of Intent** (``l10n_it_edi_doi``) per
  gli esportatori abituali.

Il repository OCA *l10n-italy* aggiunge, se servono:

* ``l10n_it_edi_extension``: anteprima e scaricamento dell'XML, più dati
  nell'XML (Art. 73, riferimento amministrazione, stabile organizzazione),
  importazione migliore dei file XML ricevuti.
* ``l10n_it_edi_pec`` (con ``l10n_it_edi_sdi``): invia e riceve le fatture
  elettroniche via PEC invece che tramite il proxy di Odoo.
* ``l10n_it_edi_sender_partner``: il terzo intermediario che emette le
  fatture per conto dell'azienda.
* ``l10n_it_edi_related_document``: i documenti collegati (ordine,
  contratto, convenzione, …) scritti nell'XML.

Per attivare la fattura elettronica:

#. Impostare la :field:`nazione <country_id>` dell'azienda a *Italia* e
   compilare l'indirizzo completo (via, CAP, città), la :field:`partita IVA
   <vat>` e il codice fiscale.
#. Impostare il **Regime fiscale** dell'azienda (vedere l'avviso in cima
   alla pagina).
#. Nella scheda **Fatturazione Elettronica**, spuntare *L'azienda compare
   nel registro delle imprese* e compilare i dati del REA, se l'azienda è
   iscritta; spuntare *L'azienda ha un rappresentante fiscale* per
   un'azienda estera con un rappresentante fiscale in Italia.
#. Aprire **Fatturazione ‣ Configurazione ‣ Impostazioni ‣ Fatturazione
   Elettronica Italiana**: scegliere la *Modalità fattura elettronica*
   (*Demo* simula soltanto l'invio, *Test (sperimentale)* invia al servizio di
   prova, *Ufficiale* allo SdI) e spuntare *Consenti a Odoo di inviare le
   fatture*. La registrazione ufficiale o di test non si può più cambiare.
   Con ``l10n_it_edi_pec``, spuntare invece *Canale PEC* e scegliere i server
   PEC in uscita e in entrata e l'indirizzo PEC dello SdI.
#. Su ogni cliente compilare il *Codice destinatario* (7 caratteri, 6 per la
   Pubblica Amministrazione) o la *PEC destinatario*; per un privato il
   codice fiscale.

.. help-if:: module = l10n_it_edi

   .. admonition:: Importante
      :class: important

      Le fatture elettroniche non vengono create finché il **Regime fiscale**
      dell'azienda è vuoto: controllarlo ora nella scheda **Informazioni
      generali**.

.. help-if:: module != l10n_it_edi

   Il modulo *Italy - E-invoicing* non è installato in questo database:
   codice fiscale, Regime fiscale e scheda **Fatturazione Elettronica**
   compaiono dopo averlo installato.
