.. _configure:

Configurazione
--------------

* I termini di pagamento sono in **Fatturazione ‣ Configurazione ‣**
  :version:`<12|**Gestione**;12|**Amministrazione**;*|**Fatturazione**` **‣
  Termini di pagamento**, per gli utenti con i diritti di contabile.
* Sul partner, scheda :version:`10|**Contabilità**;*|**Vendite e acquisti**`:
  i *Termini di pagamento* del cliente (proposti su ordini di vendita e
  fatture cliente) e quelli del fornitore (proposti su ordini di acquisto e
  fatture fornitore).
* In un database multi-azienda l':field:`azienda <company_id>` limita il
  termine a un'azienda; vuota significa tutte le aziende.

.. help-version:: >=16

   * :version:`16|*Mostra termini sulla fattura*;*|*Mostra date versamento*`
     stampa sulla fattura le scadenze con i loro importi.
   * Lo sconto per pagamento anticipato: :version:`16|*Sconto %* e *Giorni
     sconto* sulla riga;*|*Sconto anticipato* con percentuale e giorni`, e la
     riduzione fiscale dello sconto in **Fatturazione ‣ Configurazione ‣
     Impostazioni**.

**Modulo OCA account_payment_term_extension**

Il modulo OCA ``account_payment_term_extension`` (repository
:version:`<13|account-invoicing;*|account-payment`) aggiunge alle righe:

* :field:`Giorno/i di pagamento <payment_days>`: i giorni del mese in cui il
  partner paga, ad es. ``31`` (fine mese) o ``10,20``: la scadenza si sposta
  al primo di questi giorni uguale o successivo alla data calcolata.
* il numero di settimane\ :version:`<16|, e il numero di mesi`\
  :version:`>=17|: tipi di ritardo in settimane e mesi, abilitati da *Tipi
  ritardo termini di pagamento* in **Fatturazione ‣ Configurazione ‣
  Impostazioni**`.
* l':field:`arrotondamento importo <amount_round>` delle rate\
  :version:`>=13|, e il tipo *Percentuale (importo imponibile)*`.

e al termine le *Righe sequenziali* (ogni riga parte dalla scadenza della
precedente) e le *Festività* con la loro data posticipata.

.. help-version:: 12-15

   Con il modulo, il campo *giorno del mese* della riga è
   :version:`12|ignorato dal calcolo;*|nascosto`: usare *Giorno/i di
   pagamento*.
