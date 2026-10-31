.. _update_record:

Come modificare un record
-------------------------

#. Aprire il prodotto, premere **Modifica**, cambiare i campi e premere
   **Salva** (:version:`11|**Annulla**;*|**Abbandona**` scarta le modifiche).
#. Un nuovo :field:`prezzo di vendita <list_price>` o :field:`costo
   <standard_price>` è usato solo dai documenti successivi; ordini e fatture
   già fatti conservano i loro prezzi.
#. La :field:`tipologia prodotto <type>` e l':field:`unità di misura <uom_id>`
   non vanno cambiate quando il prodotto ha movimenti di magazzino: creare
   invece un nuovo prodotto.
#. Aggiungere un valore nella scheda :version:`<=14|**Varianti**;*|**Attributi
   & varianti**` crea le nuove varianti; togliere un valore elimina le
   varianti che lo usano, o le archivia quando sono già usate da documenti.
   :version:`11|**Prezzi Variante**;12-14|**Configura varianti**;*|**Configura**
   su una riga attributo` imposta il prezzo extra di ogni valore attributo: il
   prezzo di vendita di una variante è il prezzo del prodotto più i prezzi
   extra dei suoi valori.
#. Il pulsante **Varianti** apre le varianti, per impostare il loro
   riferimento, codice a barre, costo e peso.
#. :version:`11|**Aggiornare quantià disponibile**;12|**Aggiorna q.tà
   disponibile**;*|**Aggiorna quantità**` (prodotti stoccabili) imposta la
   quantità in magazzino dopo un conteggio.
#. :version:`<=12|**Attivo** in alto a destra archivia;*|**Azione ‣ Archivia**
   archivia` il prodotto e tutte le sue varianti: non è più proposto sui nuovi
   documenti ma resta su quelli vecchi. :version:`<=12|Premere di nuovo il
   pulsante per ripristinarlo.;*|**Azione ‣ Annulla archiviazione** lo
   ripristina.`
#. Per eliminare un prodotto selezionarlo nell'elenco e usare **Azione ‣
   Elimina**: un prodotto usato da ordini, fatture o movimenti di magazzino non
   si può eliminare, archiviarlo invece.
