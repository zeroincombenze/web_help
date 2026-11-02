.. _configure:

Come configurare
----------------

.. help-if:: module != account_accountant

   * **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Registri sezionali**
     (solo *Consulente*): ogni registro è una scheda della bacheca.

.. help-if:: module = account_accountant

   * **Contabilità ‣ Configurazione ‣ Contabilità ‣ Registri sezionali**
     (solo *Consulente*): ogni registro è una scheda della bacheca.

* Nella maschera del registro: il :field:`Nome sezionale <name>` e il
  :field:`Tipo <type>` mostrati sulla scheda; nella scheda *Registrazioni
  contabili* il :field:`Codice corto <code>` e i conti predefiniti dare e
  avere, il cui saldo è il *Saldo su libro mastro* di una scheda banca o
  cassa.
* Un registro banca ha la scheda *Conto bancario*: il numero del conto, la
  banca e le :field:`Spese bancarie <bank_statements_source>`, che scelgono i
  pulsanti dell'estratto conto della scheda.
* **Altro ‣ Impostazioni** su una scheda apre la stessa maschera; **Altro ‣
  Preferito** aggiunge il registro al filtro *Preferiti* o lo toglie. In
  modalità sviluppatore la stessa scelta è la :field:`casella di spunta
  <show_on_dashboard>` che mostra il registro nella bacheca, nella scheda
  *Impostazioni avanzate*.
* Il diritto di accesso di ogni utente è in **Configurazione ‣ Utenti ‣
  Utenti**, campo *Contabilità e finanza*: la bacheca è per *Contabile* e
  *Consulente*.
