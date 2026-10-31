.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

* :field:`Tipologia prodotto <type>`: *Consumabile*, *Servizio* o, con il
  Magazzino, :version:`11|*Prodotto Stoccabile*;12-13|*Prodotto
  immagazzinabile*;*|*Prodotto stoccabile*`.
* :field:`Categoria interna <categ_id>`: raggruppa i prodotti e fornisce i
  conti predefiniti di ricavo e di costo e il metodo di costo.
* :field:`Riferimento interno <default_code>` e :field:`codice a barre
  <barcode>`: stampati sui documenti e letti dai lettori di codici a barre
  (su ogni variante quando il prodotto ne ha più d'una).
* :field:`Prezzo di vendita <list_price>`: il prezzo base, cambiato dai
  listini; :field:`costo <standard_price>`: usato per i margini e la
  valorizzazione del magazzino.
* :field:`Unità di misura <uom_id>` e :field:`unità di misura d'acquisto
  <uom_po_id>` (impostazione *Unità di misura*), ad es. venduto a pezzi,
  acquistato a scatole.
* Scheda :version:`11|**Vendite**;13|**Vendite**;*|**Vendita**`: la
  :field:`politica di fatturazione <invoice_policy>`, *Quantità ordinate* o
  *Quantità consegnate*, e la descrizione per i clienti.
* Scheda **Acquisto**: i **Fornitori** con il loro prezzo e tempo di
  consegna, la *Politica di controllo* delle fatture fornitore.
* Scheda :version:`11|**Inventario**;*|**Magazzino**`: i percorsi
  (*Acquista*, *Produci su ordine*, …), il tempo di consegna al cliente, peso,
  volume, lotti e numeri di serie.
* Scheda :version:`11|**Fatturazione**;*|**Contabilità**`: :field:`imposte
  cliente <taxes_id>`, :field:`imposte fornitore <supplier_taxes_id>`, conti
  di ricavo e di costo.
