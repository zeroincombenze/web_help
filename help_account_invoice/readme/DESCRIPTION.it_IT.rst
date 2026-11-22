Pagine di aiuto contestuale per la lista e la maschera delle fatture, mostrate
da web_context_help: fatture clienti, fatture fornitori e le loro note di
credito.

Il modello dipende dalla versione di Odoo: prima della 13.0 le pagine seguono
``account.invoice``, dalla 13.0 ``account.move``, dove una fattura è una
registrazione contabile di tipo fattura.

Le fatture clienti e le fatture fornitore hanno pagine di aiuto separate
(fatture clienti: tipi out_invoice, out_refund, out_receipt; fatture
fornitore: in_invoice, in_refund, in_receipt), ognuna con il proprio testo,
menu e domande frequenti. Le pagine delle fatture fornitore comprendono
**Fattura da ordine fornitore**, mostrata solo con l'app Acquisti installata, e **Come creare una fattura da XML** (Odoo 18.0 con
l10n_it_edi): creare una fattura fornitore caricando una fattura elettronica.

Ogni pagina segue la struttura standard di web_context_help:

* **Indice**: le sezioni della pagina, costruito dalla finestra di aiuto
* **Descrizione**: cosa sono le fatture, i loro stati e i campi principali
* **Come inserire un nuovo record** (maschera): guida passo passo per creare,
  validare e inviare una fattura o una fattura fornitore
* **Fatturazione da ordine di vendita** (maschera fattura cliente, solo con l'app Vendite
  installata): politica di fatturazione, stato fattura, fatture normali e
  anticipi, più ordini insieme
* **Suggerimenti per la ricerca** (lista): menu, ricerca, filtri e
  raggruppamenti
* **Come modificare un record** (maschera): modificare una fattura, registrare
  i pagamenti, note di credito
* **Come annullare o eliminare un record** (maschera e lista): annullare una
  fattura in bozza o confermata, riportarla in bozza, quali fatture si
  possono eliminare
* **Come configurare**: le impostazioni di Fatturazione, registri, termini di
  pagamento e imposte
* **Stampe ed esportazione**: il PDF della fattura, l'invio, l'analisi fatture
  e l'esportazione delle fatture in un file
* Pulsante **Esempio**: casi comuni, ad es. pagamenti parziali o correzione di
  una fattura registrata
* Pulsante **FAQ** e **Piè di pagina**

Una pagina per la Bacheca della contabilità (kanban dei registri) spiega le
schede dei registri, i loro pulsanti e importi, il menu **⋮**, e come si
archiviano o eliminano i registri.

Le pagine sono in inglese e in italiano, con i menu, i pulsanti e gli stati
della versione di Odoo in uso.
