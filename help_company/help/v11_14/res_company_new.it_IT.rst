.. _new_record:

Come inserire un nuovo record
-----------------------------

#. Aprire **Impostazioni ‣ Utenti e aziende ‣ Aziende** e premere **Crea**
   (solo amministratori). Per lavorare con più aziende, attivare prima
   *Gestione multi azienda*: vedere *Come configurare*.
#. Scrivere il :field:`nome dell'azienda <name>` (obbligatorio) e fare clic
   sull'immagine per caricare il logo.
#. Nella scheda **Informazioni generali** compilare l'indirizzo, scegliendo
   la :field:`nazione <country_id>` (l'elenco degli stati la segue).
#. Compilare :field:`sito web <website>`, :field:`telefono <phone>`,
   :field:`e-mail <email>`, :field:`partita IVA <vat>` e :field:`valuta
   <currency_id>`; con più aziende, l':field:`Azienda madre <parent_id>`
   quando l'azienda fa parte di un gruppo.

   .. help-if:: module = l10n_it_rea

      Il *Registro Imprese* è nella scheda **Dati REA**: è compilato dai dati
      del REA scritti lì.

   .. help-if:: module != l10n_it_rea

      Compilare anche il :field:`Registro Imprese <company_registry>`.

   .. help-if:: module = l10n_it_edi

      Sotto la partita IVA compilare :field:`Codice Fiscale
      <l10n_it_codice_fiscale>` e :field:`Tax System <l10n_it_tax_system>`.

   .. help-if:: module = l10n_it_fatturapa

      Sotto la partita IVA compilare il *Codice Fiscale*; nella scheda
      **E-fattura** scegliere la *Posizione fiscale*, obbligatoria.

#. Premere **Salva**.
#. Permettere agli utenti di lavorare per la nuova azienda: aprire
   **Impostazioni ‣ Utenti e aziende ‣ Utenti**, aprire ogni utente, premere
   **Modifica** e aggiungere l'azienda alle *Aziende ammesse* della scheda
   **Diritti di accesso**.
#. Con la Fatturazione installata, passare alla nuova azienda nella barra in
   alto, aprire **Fatturazione ‣ Configurazione ‣ Impostazioni**, scegliere
   il *Pacchetto* della **Localizzazione fiscale** (ad es. *Italy - Generic
   Chart of Accounts*) e premere **Salva**: vengono creati i conti e le
   imposte dell'azienda.
