.. _configure:

Come configurare
----------------

.. help-if:: module != accountant

   * **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Registri** (solo
     *Amministratore*): ogni registro è una scheda della bacheca.

.. help-if:: module = accountant

   * **Contabilità ‣ Configurazione ‣ Contabilità ‣ Registri** (solo
     *Amministratore*): ogni registro è una scheda della bacheca.

* Nella maschera del registro: il :field:`Nome registro <name>` e la
  :field:`Tipologia <type>` mostrati sulla scheda; nella scheda
  *Registrazioni contabili* il conto predefinito, il cui saldo è seguito da
  una scheda banca o cassa, e il :field:`Codice breve <code>`.
* Un registro banca ha, nella stessa scheda, il *Numero conto*, la banca e i
  :field:`Flussi bancari <bank_statements_source>`, come arrivano le
  transazioni. Finché il numero di conto è vuoto e il flusso bancario non è
  ancora scelto, la scheda mostra **Configurazione banca**.
* Le schede *Pagamenti in entrata* e *Pagamenti in uscita* di un registro
  banca o cassa elencano i metodi di pagamento, usati da **Pagamento
  cliente** e **Pagamento fornitore**.
* **⋮ ‣ Configurazione** su una scheda apre la stessa maschera; **⋮ ‣ ☆**
  aggiunge il registro al filtro *Preferiti* o lo toglie; il colore scelto
  nel menu **⋮** contrassegna la scheda.
* Il diritto di accesso di ogni utente è in **Impostazioni ‣ Utenti e aziende
  ‣ Utenti**, campo *Fatturazione*.
