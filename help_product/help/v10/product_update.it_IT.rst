.. _update_record:

Modifica record
---------------

#. Aprire il prodotto, premere **Modifica**, cambiare i campi e premere
   **Salva** (**Annulla** scarta le modifiche).
#. Un nuovo :field:`prezzo di vendita <list_price>` o :field:`costo
   <standard_price>` è usato solo dai documenti successivi; ordini e fatture
   già fatti mantengono i loro prezzi.
#. Il :field:`tipo di prodotto <type>` e l':field:`unità di misura <uom_id>`
   non vanno cambiati quando il prodotto ha movimenti di magazzino: creare
   invece un nuovo prodotto.
#. Aggiungere un valore nella scheda **Varianti** crea le nuove varianti;
   togliere un valore elimina le varianti che lo usano, o le archivia se
   sono già usate da documenti. **Prezzi Variante**
   imposta il prezzo extra di ogni valore attributo: il prezzo di vendita di
   una variante è il prezzo di vendita del prodotto più i prezzi extra dei
   suoi valori.
#. Il pulsante **Varianti** apre le varianti, per impostarne riferimento,
   codice a barre, costo e peso.
#. **Aggiorna Qtà in Possesso** (prodotti stoccabili) imposta la quantità in
   magazzino dopo un conteggio.
#. **Attivo** in alto a destra archivia il prodotto e tutte le sue varianti:
   non è più proposto sui nuovi documenti ma resta su quelli vecchi. Premere
   **Archiviato** per ripristinarlo.
#. Per eliminare un prodotto selezionarlo nell'elenco e usare **Azione ‣
   Elimina**: un prodotto usato da ordini, fatture o movimenti di magazzino non
   si può eliminare, archiviarlo invece.
