.. _new_record:

Come inserire un nuovo record
-----------------------------

#. Aprire **Configurazione ‣ Utenti ‣ Aziende** e premere **Crea** (solo
   amministratori). Per lavorare con più aziende, attivare prima *Gestione
   multi aziendale*: vedere *Come configurare*.
#. Scrivere il :field:`nome dell'azienda <name>` (obbligatorio) e, sotto,
   lo :field:`Slogan aziendale <rml_header1>` stampato nell'intestazione
   delle stampe; fare clic sull'immagine per caricare il logo.
#. Nella scheda **Informazioni generali** compilare l'indirizzo, scegliendo
   la :field:`nazione <country_id>` (l'elenco degli stati la segue), e il
   :field:`sito web <website>`.
#. Compilare :field:`telefono <phone>`, :field:`fax <fax>`, :field:`email
   <email>`, :field:`partita IVA <vat>` e :field:`valuta <currency_id>`; con
   più aziende, l':field:`Azienda Principale <parent_id>` quando l'azienda
   fa parte di un gruppo.

   .. help-if:: module = l10n_it_rea

      Il *Company Registry* è nella scheda **REA Data**: è compilato dai dati
      del REA scritti lì.

   .. help-if:: module != l10n_it_rea

      Compilare anche il :field:`Company Registry <company_registry>`
      (registro delle imprese).

#. Premere **Salva**.
#. Permettere agli utenti di lavorare per la nuova azienda: aprire
   **Configurazione ‣ Utenti ‣ Utenti**, aprire ogni utente, premere
   **Modifica** e aggiungere l'azienda alle *Aziende consentite* della scheda
   **Diritti di accesso**.
#. Con la Fatturazione installata, passare alla nuova azienda nella barra in
   alto, aprire **Contabilità ‣ Configurazione ‣ Impostazioni**, spuntare
   *Questa azienda ha il proprio piano dei conti*, scegliere il *Modello* del
   **Piano dei conti** (ad es. *Italy - Generic Chart of Accounts*) e premere
   **Salva**: vengono creati i conti e le imposte dell'azienda.
