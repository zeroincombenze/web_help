.. help-page:: home
   :title: Aiuto

Pronto aiuto
============

.. _developer_mode:

Attivare la modalità sviluppatore
---------------------------------

In alcuni menu viene richiesto di "Attivare la modalità sviluppatore". Questa
modalità mostra alcuni menu e funzioni che altrimenti sono nascosti.

.. image:: /web_context_help/static/description/devel_mode.png
   :alt: Attiva la modalità sviluppatore
   :width: 100%

.. _list_search:

Trovare, filtrare e raggruppare un elenco
-----------------------------------------

Ogni elenco ha una barra di ricerca in alto a destra, per trovare, filtrare e
raggruppare i suoi record.

.. help-version:: >=17

   .. image:: /web_context_help/static/description/search_bar.png
      :alt: Barra di ricerca
      :width: 100%

.. _search_bar:

Cercare
~~~~~~~

Scrivere un valore nella casella di ricerca: un menu a discesa propone i campi
in cui cercarlo, ad es. *Cerca Cliente per: Rossi*. Sceglierne uno con i tasti
freccia e Invio, oppure con un clic; la piccola freccia accanto a un campo
elenca i record corrispondenti, per sceglierne esattamente uno. La ricerca
semplice usa l'operatore *contiene*, quindi maiuscole e minuscole non contano.

Ogni ricerca diventa un riquadro (un *facet*) dentro la barra di ricerca: si
toglie con la sua **×** o con il tasto Backspace. Le ricerche sullo stesso
campo sono unite da *o*, quelle su campi diversi da *e*.

.. _several_words:

Ricerche con più parole
~~~~~~~~~~~~~~~~~~~~~~~

A volte occorre cercare un testo di due o più parole. Si supponga di cercare
*Mario Rossi*, senza sapere se sia stato inserito come *Mario Rossi* oppure
come *Rossi Mario*, e che in archivio siano presenti i seguenti nominativi:

#. Dr. Rossi Mario
#. Mario De Rossi
#. Rossi Forniture
#. Rossi e Bianchi
#. Mario Bianchi

Cercando ``Rossi`` si trovano i nominativi da 1 a 4, compresi *Rossi
Forniture* e *Rossi e Bianchi*. Aggiungendo una seconda ricerca ``Mario`` la
lista non si restringe: appaiono tutti e cinque i nominativi.

Questo comportamento è dovuto al modo in cui Odoo combina più ricerche: le
ricerche sullo stesso campo sono unite da *oppure* (OR; il riquadro nella barra
di ricerca mostra *Rossi o Mario*), quelle su campi diversi da *e anche* (AND).
``Rossi`` e ``Mario`` sono cercati nello stesso campo, quindi Odoo mostra i
nominativi con *Rossi* oppure con *Mario*.

Per restringere la ricerca ci sono due modi.

**1. Un filtro personalizzato con AND.** È il metodo più preciso, ma richiede
più dati da inserire:

.. help-version:: >=17

   in **Filtri ‣ Aggiungi filtro personalizzato** scrivere una regola *Nome
   contiene Rossi* e una seconda regola *Nome contiene Mario*, scegliere che
   corrispondano *tutte* le regole e premere **Aggiungi**.

.. help-version:: <17

   le condizioni di un singolo filtro personalizzato sono unite da *oppure*,
   quindi applicare due filtri personalizzati: **Filtri ‣ Aggiungi filtro
   personalizzato**, condizione *Nome contiene Rossi*, **Applica**; poi di nuovo
   **Aggiungi filtro personalizzato**, condizione *Nome contiene Mario*,
   **Applica**. Due filtri personalizzati sono uniti da *e anche*.

Il risultato sono i nominativi 1 e 2.

**2. Il carattere jolly.** È più rapido da impostare e sfrutta l'*oppure* tra le
ricerche sullo stesso campo: cercare ``Rossi%Mario`` e poi ``Mario%Rossi``. Il
``%`` (percentuale) vale qualsiasi testo, vedere *Ricerche con il carattere
jolly*: la prima ricerca trova i nominativi con *Rossi* prima di *Mario*
(nominativo 1), la seconda quelli con *Mario* prima di *Rossi* (nominativo 2).
Notare che ``Mario%Rossi`` trova sia *Mario Rossi* (non presente in archivio)
sia *Mario De Rossi*.

Il ``_`` (trattino basso) vale esattamente un carattere: ``Ross_`` trova
*Rossi*, *Rosso* e *Rossa*. Per lo stesso motivo un ``%`` o un ``_`` scritto in
una ricerca non è mai cercato come carattere normale.

.. help-include:: search_wildcard.rst

Filtri, raggruppamenti e preferiti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. help-version:: >=17

   Il pulsante **▾** a destra della casella di ricerca apre tre colonne:
   **Filtri**, **Raggruppa per** e **Preferiti**.

.. help-version:: <17

   I pulsanti **Filtri**, **Raggruppa per** e **Preferiti** sotto la casella di
   ricerca aprono i loro menu.

* **Filtri**: selezioni dei record già pronte. I filtri dello stesso gruppo
  (tra due linee di separazione) sono uniti da *o*, quelli di gruppi diversi da
  *e*. **Aggiungi filtro personalizzato** costruisce una condizione con un
  campo, un operatore e un valore\ :version:`>=17|, unite da *una qualsiasi* o
  da *tutte* le regole, e può includere i record archiviati`. I record
  archiviati sono nascosti: il filtro *Archiviato*, quando presente, li mostra.
* **Raggruppa per**: raggruppa le righe per un campo, ad es. per cliente;
  scegliendo un secondo raggruppamento ogni gruppo è diviso di nuovo. Fare clic
  sull'intestazione di un gruppo per aprirlo o chiuderlo: mostra il numero di
  record e i totali delle colonne numeriche. **Aggiungi gruppo
  personalizzato** raggruppa per qualsiasi campo.
* **Preferiti**: **Salva ricerca corrente** conserva ricerca, filtri e
  raggruppamenti con un nome; :version:`<=10|*Usa come predefinito*;*|*Filtro
  predefinito*` la applica ogni volta che il menu viene aperto e
  :version:`<=10|*Condividi con tutti gli utenti*;*|*Condiviso*` la rende
  visibile a tutti.

.. _navigation:

Muoversi
~~~~~~~~

* **Percorso** (breadcrumb), in alto a sinistra: la sequenza delle viste
  aperte, ad es. *Ordini di vendita / S00042*. Fare clic su un passo per
  tornarci; è meglio del pulsante Indietro del browser, che può perdere la
  ricerca.
* **Cambio vista**, in alto a destra: mostra gli stessi record come schede
  kanban, elenco o, dove disponibili, calendario, pivot e grafico, mantenendo
  la ricerca.
* **Paginatore**, accanto al cambio vista: *1-80 / 97* indica i record da 1 a
  80 su 97. Le frecce passano alla pagina successiva o precedente; fare clic
  sui numeri per cambiarli, ad es. *1-200* per vedere più righe. In una
  maschera il paginatore mostra la posizione del record, e le frecce aprono il
  record successivo o precedente dell'elenco.

.. help-version:: >=13

   Alcuni elenchi hanno un pannello laterale a sinistra (ad es. le categorie
   delle **App**): un clic su una voce filtra l'elenco.

.. _import_export:

Importare ed esportare dati
---------------------------

Ogni elenco può essere salvato in un file di foglio di calcolo ed essere
caricato da uno: per portare i dati altrove, per caricare molti record in una
volta o per modificare molti record insieme.

.. _export:

Esportare
~~~~~~~~~

#. Aprire l'elenco, cercare e filtrare i record che servono e spuntarli. La
   casella nell'intestazione spunta tutti i record della pagina\ :version:`<=12|,
   e con essa sono esportati tutti i record trovati;*|, poi **Seleziona tutto**
   spunta tutti i record trovati`.
#. Premere :version:`<=10|**Azione ‣ Esportazione**;<=16|**Azione ‣
   Esporta**;*|**⚙ Azioni ‣ Esporta**`.
   :version:`>=17|Senza alcun record spuntato, **⚙ ‣ Esporta tutto** (l'ingranaggio
   accanto al titolo della vista) esporta tutti i record trovati.`
#. Scegliere i campi: cercarli in *Campi disponibili* e aggiungerli a *Campi da
   esportare*, poi trascinarli per cambiarne l'ordine. Un elenco di campi usato
   spesso si può salvare e riprendere:
   :version:`<=12|**Salva l'elenco dei campi**;*|**Modello ‣ Nuovo modello**`.
#. Spuntare :version:`<=10|*Esportazione compatibile alla successiva
   importazione*;<=12|*Esportazione compatibile con l'importazione*;*|*È un
   aggiornamento dati (compatibile con l'importazione)*` quando il file sarà
   reimportato: sono proposti solo i campi importabili ed è esportato anche
   l'identificativo del record (*ID esterno*).
#. Scegliere il formato, :version:`<=10|*CSV* o *Excel*;*|*XLSX* o *CSV*`, e
   premere **Esporta**: il browser scarica il file.

.. _import:

Importare
~~~~~~~~~

#. Aprire l'elenco in cui vanno i record e premere
   :version:`<=12|il pulsante **Importa** accanto a **Crea**;13-16|**Preferiti ‣
   Importa record**;*|**⚙ ‣ Importa record** (l'ingranaggio accanto al titolo
   della vista)`.
#. Premere :version:`<=10|**Carica File**;*|**Carica file dati**` e scegliere
   il file, :version:`<=10|CSV o Excel;*|XLSX, XLS, ODS o CSV`. Per un file CSV
   controllare la codifica, il separatore e il delimitatore di testo
   (:version:`<=10|opzioni;*|**Formattazione**`): Odoo si aspetta virgole e
   doppi apici.
#. Odoo abbina ogni colonna del file a un campo in base al titolo: controllare
   gli abbinamenti e scegliere il campo delle colonne non riconosciute; una
   colonna senza campo non viene importata. I campi dei record collegati sono
   mostrati da *Visualizzare i campi di relazione (avanzato)*.
#. Premere :version:`<=10|**Valida**;*|**Prova**`: Odoo controlla tutto il file
   senza salvare nulla ed elenca gli errori con le loro righe. Correggere il
   file e caricarlo di nuovo.
#. Premere **Importa**.

⚠ **Attenzione!** Un'importazione non si può annullare. Per trovare i record
appena importati, raggruppare o filtrare l'elenco per *Creato il*.

Buono a sapersi:

* **Modificare molti record**: esportarli come compatibili con l'importazione,
  cambiare le colonne nel foglio di calcolo, mantenere la colonna *ID esterno*
  (``id``) e reimportare il file. Le righe con un ID aggiornano il loro record,
  quelle senza ID creano nuovi record: un'importazione senza ID ripetuta due
  volte crea ogni record due volte.
* **I record collegati** (cliente, nazione, prodotto, …) sono trovati per nome,
  oppure per identificativo in una colonna intitolata ad es. ``Country/External
  ID``. Importare prima i record collegati.
* **Le date** sono lette senza dubbi nella forma ``AAAA-MM-GG`` (ad es.
  ``2026-03-01``); in un file Excel usare vere celle di tipo data.
* **I file grandi** possono fermarsi per un time-out: dividerli in file più
  piccoli.

Aiuto sull'aiuto
================

.. _description:

Benvenuto
---------

Questo è l'aiuto del tuo Odoo. Premere **Sommario** nell'intestazione per
vedere tutte le pagine di aiuto disponibili: l'elenco cresce con ogni modulo
di aiuto installato (ad es. fatture, ordini di vendita, termini di pagamento).

.. _usage:

Aiuto della vista corrente
--------------------------

Premere il pulsante |sos| nel pannello di controllo di qualsiasi vista: la
finestra di aiuto apre la pagina che spiega quella vista. La scheda di Odoo
resta utilizzabile e, con *Segui Odoo* attivo, la finestra di aiuto segue la
navigazione. Se una vista non ha una pagina, una pagina automatica elenca
l'aiuto dei suoi campi.

.. |sos| unicode:: U+1F6DF

.. _search:

Cercare un testo nell'aiuto
---------------------------

La casella nell'intestazione cerca un testo nella pagina, come Ctrl+F del
browser. Maiuscole e accenti sono ignorati; il testo tra virgolette è cercato
come frase esatta.

.. _configure:

Modificare questa pagina
------------------------

Gli amministratori vedono il pulsante **Modifica** nell'intestazione: apre la
pagina in *Impostazioni > Tecnico > Aiuto contestuale > Pagine di aiuto*, dove
il contenuto può essere adattato all'azienda, compresa questa pagina. Una
pagina modificata mantiene la versione dell'utente all'aggiornamento del
modulo.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-14 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
