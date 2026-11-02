.. _configure:

Come configurare
----------------

* **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Registri** (solo
  *Responsabile fatturazione*): ogni registro è una scheda della bacheca; le
  schede seguono l'ordine di questa lista, che si cambia trascinando le
  righe.
* Nella maschera del registro: il :field:`Nome registro <name>` e la
  :field:`Tipologia <type>` mostrati sulla scheda; nella scheda
  *Registrazioni contabili* il :field:`Codice breve <code>` e il
  :field:`Conto dare predefinito <default_debit_account_id>` e il
  :field:`Conto avere predefinito <default_credit_account_id>`, il cui saldo
  è il *Saldo nel libro mastro* di una scheda banca o cassa.
* Un registro banca ha la scheda *Conto bancario*: il conto bancario, la
  banca e i :field:`Feed bancari <bank_statements_source>`, che decidono se
  la scheda mostra **Configura**.
* **⋮ ‣ Impostazioni** su una scheda apre la stessa maschera; **⋮ ‣
  Aggiungi a preferiti** / **Rimuovi dai preferiti** aggiunge il registro al
  filtro *Preferiti* o lo toglie.
* Il diritto di accesso di ogni utente è in **Impostazioni ‣ Utenti e
  aziende ‣ Utenti**: campo *Contabilità e finanza* (*Fatturazione* o
  *Responsabile fatturazione*) e, in modalità sviluppatore, *Mostrare
  funzionalità contabili complete* nella sezione *Impostazioni tecniche*,
  necessario per vedere la bacheca.
