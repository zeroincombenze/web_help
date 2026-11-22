.. _configure:

Come configurare
----------------

.. help-version:: <13

   **Fatturazione ‣ Configurazione ‣ Impostazioni**:

   * *Imposte predefinite* proposte sulle righe (l'imposta di acquisto), e il
     *Metodo di arrotondamento* delle imposte (per riga o globale).
   * *Multi-valute*: fatture in valute estere.
   * *Avvisi*: un messaggio mostrato quando si sceglie un partner o un
     prodotto.
     :version:`>=11|*Arrotondamento di cassa* arrotonda il totale, ad es. a
     0,05.`

   Altri menu:

   * **Fatturazione ‣ Configurazione ‣**
     :version:`<12|**Gestione**;*|**Amministrazione**` **‣ Termini di
     pagamento**: le scadenze, ad es. *30 giorni fine mese* o 30% subito e 70%
     a 60 giorni.
   * **Fatturazione ‣ Configurazione ‣ Contabilità ‣**
     :version:`10|**Registri sezionali**;*|**Registri**`: i registri acquisti e
     la loro sequenza dei numeri.
     :version:`10|*Consenti cancellazione registrazioni*;*|*Consentire
     annullamento registrazioni*` (modulo *Annullamento registrazioni
     contabili*) abilita :version:`<12|[\`Annulla fattura\`];*|[\`Annulla\`]`
     sulle fatture fornitore validate.
   * **Fatturazione ‣ Configurazione ‣ Contabilità ‣**
     :version:`10|**IVA**;*|**Imposte**` e **Posizioni fiscali**.
   * Sul fornitore, scheda **Fatturazione** (scheda *Contabilità* per un
     contabile): i termini di pagamento del fornitore, la posizione fiscale e
     il conto debiti proposti sulle fatture fornitore.

.. help-version:: >=13

   **Fatturazione ‣ Configurazione ‣ Impostazioni**:

   * *Imposte predefinite* proposte sulle righe (l'imposta di acquisto), e il
     *Metodo di arrotondamento* delle imposte (per riga o globale).
   * *Valute*: fatture in valute estere.
   * *Fatture fornitore* e *Pagamenti fornitore*: le opzioni per ricevere e per
     pagare le fatture fornitore (ad esempio gli assegni e i pagamenti SEPA).

   .. help-version:: >=18

      In *Fatture fornitore*, *Registrazione automatica fatture*: dopo tre
      fatture di un fornitore importate senza modifiche, Odoo suggerisce di
      confermare automaticamente le successive; la funzione si può disattivare
      nel profilo di ogni fornitore.

   Altri menu:

   * **Fatturazione ‣ Configurazione ‣ Fatturazione ‣ Termini di pagamento**:
     le scadenze, ad es. *30 giorni fine mese* o 30% subito e 70% a 60 giorni.
   * **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Registri**: i registri
     acquisti e la loro sequenza dei numeri;
     :version:`13|*Chiusura registrazioni confermate con hash*;14-17|*Chiudere
     registrazioni confermate con hash*;*|*Proteggi registrazioni confermate
     con hash*` protegge le fatture confermate, che non si possono più
     reimpostare a bozza.
   * **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Imposte** e **Posizioni
     fiscali**.
   * Sul fornitore, scheda **Fatturazione** (scheda *Contabilità* per un
     contabile): i termini di pagamento del fornitore, la posizione fiscale e
     il conto debiti proposti sulle fatture fornitore.
