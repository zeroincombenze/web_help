.. _search:

Come cercare
------------

* **Vendite ‣ Ordini ‣ Preventivi** elenca i preventivi, **Vendite ‣ Ordini ‣
  Ordini** gli ordini confermati, **Vendite ‣ Da fatturare ‣ Ordini da
  fatturare** gli ordini in attesa di fattura.
* Scrivere nella barra di ricerca e scegliere cosa cercare: *Ordine* (numero o
  riferimento cliente), *Cliente*, *Addetto vendite*, *Team di vendita* o
  *Prodotto*. Più criteri si combinano; toglierne uno con la sua ✕.
* **Filtri**: *I miei preventivi* e *I miei ordini* mostrano solo i propri
  documenti; *Preventivi*, *Ordini di vendita*, *Da fatturare* e *Da
  incrementare* restringono l'elenco; *Data ordine* / *Data creazione* scelgono
  un periodo; *Aggiungi filtro personalizzato* costruisce qualsiasi condizione.
* **Raggruppa per**: *Addetto vendite*, *Cliente* o *Data ordine* (anno,
  trimestre, mese, settimana, giorno), con i subtotali; *Aggiungi gruppo
  personalizzato* raggruppa per qualsiasi campo, ad es. :field:`stato
  fatturazione <invoice_status>` (*Nulla da fatturare*, *Da fatturare*,
  *Interamente fatturato*, *Opportunità di incremento vendite*) o stato.
* **Preferiti ‣ Salva ricerca corrente** conserva filtri e raggruppamenti.
* Le colonne opzionali si mostrano o nascondono dal menu a destra delle
  intestazioni delle colonne; le viste kanban, calendario, pivot e grafico sono
  in alto a destra.

.. _wildcard:

Ricerche con il carattere jolly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A volte è necessario effettuare ricerche più specifiche oppure con un maggior
grado di difficoltà. Si supponga, ad esempio, di cercare gli ordini dei clienti
di *Settimo Torinese*.

.. help-version:: >=17

   Usare **Filtri ‣ Aggiungi filtro personalizzato**, scegliere il campo
   *Cliente ‣ Città* e l'operatore *contiene*.

.. help-version:: 16

   Il filtro personalizzato degli ordini non raggiunge i campi del cliente:
   fare la ricerca nell'elenco **Vendite ‣ Ordini ‣ Clienti** con **Filtri ‣
   Aggiungi filtro personalizzato**, campo *Città* e operatore *contiene*.

* Con il campo *Città*, l'operatore *contiene* e il valore ``Settimo`` si
  ottengono anche i record di altre città, ad esempio *Settimo Milanese*.
* Con il valore ``Settimo Torinese`` la ricerca è precisa, anzi troppo precisa:
  i clienti in cui la città è scritta *Settimo T.se* non sono trovati.

Per risolvere si usa il carattere ``%`` (percento), chiamato carattere jolly,
che significa *qualsiasi valore*. Con il valore ``Settimo T%se`` si trovano sia
*Settimo Torinese* sia *Settimo T.se*, ma non *Settimo Milanese*.
La ricerca con *contiene* non distingue maiuscole e minuscole.

Un esempio più complesso è la ricerca di comuni con nomi di santi, ad esempio
*Santa Maria Capua Vetere*. Questo comune potrebbe essere scritto:

* Santa Maria di Capua Vetere
* Santa Maria Capua Vetere
* Santa Maria di C.V.
* Santa Maria CV
* S\. Maria di Capua Vetere
* S\. Maria di CV

Inoltre ci sono numerosi comuni con il nome Santa Maria, ad esempio *Santa
Maria a Vico*, *Santa Maria della Versa* e *Santa Maria Maggiore*, per citarne
solo alcuni. Il trucco per una buona ricerca è cercare le parti che compongono
sicuramente il nome cercato. Nell'esempio le parti sono:

#. ``S`` iniziale, per *S.* o *Santa*
#. ``Maria``, per esteso, senza abbreviazioni
#. ``C``, per *Capua* o la sua abbreviazione
#. ``V``, per *Vetere* o la sua abbreviazione

Il valore del filtro diventa quindi ``S%Maria%C%V``, che si legge: contiene,
nell'ordine, "S", "Maria", "C" e "V". *Santa Maria Maggiore* non viene
incluso perché mancano i caratteri "C" e "V"; *Santa Maria della Versa* non è
incluso perché, pur contenendo il carattere "V", manca il carattere "C".
