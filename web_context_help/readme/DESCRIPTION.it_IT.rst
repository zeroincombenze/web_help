Aggiunge un pulsante |sos| al pannello di controllo di ogni vista: apre l'aiuto
della vista corrente in una finestra separata, così la scheda di Odoo resta
utilizzabile.

Le pagine di aiuto sono su due livelli:

* **Livello standard**: le pagine fornite dai moduli di aiuto (ad es.
  help_account_invoice, help_sale_order), che mostrano l'aiuto dei moduli
  standard di Odoo. Hanno una priorità di 64 o più (96 per default), quindi sono
  l'ultima alternativa, sempre disponibile
* **Livello personalizzato**: le pagine costruite per i moduli custom, o le
  copie delle pagine standard modificate per adattarle all'azienda. Hanno una
  priorità minore di 64 (32 per default), dove 1 è la più alta: una pagina
  personalizzata è mostrata al posto della pagina standard della stessa vista.
  Gli editor le scrivono in *Aiuto ‣ Editor dell'aiuto ‣ Pagine di aiuto*, o
  nella cartella ``help/`` del modulo custom

* Gli amministratori possono modificare una pagina di aiuto dall'interfaccia
  di Odoo, con l'editor della scheda della pagina: nel database una pagina è
  HTML, quindi non serve RST. La versione modificata è mantenuta quando il
  modulo è aggiornato, e un avviso compare quando in seguito cambia la
  sorgente RST, così la modifica può essere verificata rispetto alla nuova
  sorgente
* La sorgente di una pagina di aiuto è un file RST, scritto dallo sviluppatore
  nella cartella ``help/`` del modulo (un file per lingua); il server lo
  trasforma nella pagina HTML del database, all'avvio e quando la sorgente
  cambia
* Le immagini si aggiungono alla sorgente RST (direttiva ``image``, file nella
  ``static/`` di un modulo), i video dagli editor nella pagina HTML; i tour
  guidati richiedono il modulo *Context help tours*
  (``web_context_help_tour``)
* La finestra di aiuto segue la navigazione (*Segui Odoo*), evidenzia i campi
  citati dalla pagina e può avviare un tour guidato
* Le domande hanno risposta da una ricerca testuale nelle sezioni di aiuto;
  ogni domanda è registrata per l'amministratore
* Una pagina può essere scelta in base a un campo del record aperto, anche
  many2one: con il ``:when:`` della sua sorgente RST o con regole impostate
  dall'amministratore, ad es. un aiuto diverso per ogni tipo di ordine di vendita
* Le viste senza pagina ricevono una pagina automatica costruita dall'aiuto dei campi
* Il menu **Aiuto** apre la pagina iniziale dell'aiuto; il suo pulsante
  **Sommario** elenca le pagine di ogni modulo di aiuto installato (ad es.
  help_account_invoice, help_sale_order)

.. |sos| unicode:: U+1F6DF
