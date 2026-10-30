.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

* **Tipologia prodotto**: :version:`<=17|*Consumabile* (senza giacenze),
  *Servizio* oppure, con Magazzino, *Prodotto stoccabile* (con giacenze);*|*Beni*,
  *Servizio* o *Combo* (un insieme di scelte venduto come un solo prodotto).
  Per i beni, con Magazzino, **Traccia magazzino** gestisce le giacenze`.
* :version:`<=17|**Può essere venduto** e **Può essere acquistato**;*|**Vendita**
  e **Acquisto**` (caselle sotto il nome): se il prodotto è proposto nei
  documenti di vendita e di acquisto.
* :field:`Prezzo di vendita <list_price>` e :field:`costo <standard_price>`;
  con Fatturazione anche **Imposte vendite** e **Imposte d'acquisto**.
* :field:`Riferimento interno <default_code>` e :field:`codice a barre
  <barcode>`: codici stampati sui documenti e cercati dai lettori.
* :field:`Categoria prodotto <categ_id>`: raggruppa i prodotti e ne stabilisce
  conti e metodo di costo.
* :field:`Unità di misura <uom_id>` e :field:`unità acquisto <uom_po_id>`
  (impostazione *Unità di misura*).
* Scheda **Vendita**: la :field:`descrizione vendite <description_sale>`
  copiata in preventivi e fatture; con Vendite la **Politica di
  fatturazione**.
* Scheda **Acquisto** (con Acquisti installato): i fornitori con prezzi e tempi
  di consegna, la **Politica di controllo** e la descrizione di acquisto.
* Scheda **Magazzino** (con Magazzino installato): percorsi, responsabile,
  peso, volume, tempi di consegna e, con i lotti, la tracciabilità.
* :field:`Note interne <description>`: visibili solo agli utenti.
