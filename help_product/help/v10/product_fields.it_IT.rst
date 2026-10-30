.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

* :field:`Tipo di prodotto <type>`: *Consumabile*, *Servizio* o, con
  Magazzino, *Prodotto Stoccabile*.
* :field:`Categoria interna <categ_id>`: raggruppa i prodotti e fornisce i
  conti di ricavo e di costo predefiniti e il metodo di costo.
* :field:`Riferimento interno <default_code>` e :field:`codice a barre
  <barcode>`: stampati sui documenti e letti dai lettori di codici a barre
  (su ogni variante quando il prodotto ne ha più d'una).
* :field:`Prezzo di vendita <list_price>`: il prezzo base, modificato dai
  listini; :field:`costo <standard_price>`: usato per margini e valorizzazione
  del magazzino.
* :field:`Unità di misura <uom_id>` e :field:`unità di misura di acquisto
  <uom_po_id>` (impostazione *Unità di Misura*), ad es. venduto a pezzi,
  acquistato a scatole.
* Scheda **Vendite**: il :field:`metodo di fatturazione <invoice_policy>`,
  *Quantità ordinate* o *Quantità consegnate*, e i prezzi dei listini.
* Scheda **Inventario**: le rotte (*Acquista*, *Produrre su Ordine*, …), tempi
  di consegna cliente, peso, volume, lotti e numeri di serie, e i
  **Fornitori** con prezzo e tempo di consegna.
* Scheda **Fatturazione**: :field:`imposte cliente <taxes_id>`, :field:`IVA da
  fornitori <supplier_taxes_id>`, conti di ricavo e di costo.
* Scheda **Note**: le descrizioni stampate su preventivi, ordini di acquisto e
  picking.
