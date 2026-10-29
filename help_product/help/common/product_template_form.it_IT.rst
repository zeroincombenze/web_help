.. help-page:: product_template_form
   :title: Prodotto
   :model: product.template
   :view-type: form
   :priority: 96

Prodotto
========

.. _description:

Descrizione
-----------

Un prodotto è qualsiasi cosa l'azienda venda, acquisti o tenga a magazzino:
beni, servizi o\ :version:`>=18| combo di prodotti`. Il suo :field:`prezzo di vendita
<list_price>`, il :field:`costo <standard_price>`, la :field:`categoria <categ_id>`
e l':field:`unità di misura <uom_id>` sono proposti in ordini, fatture e
trasferimenti. Un prodotto venduto in più versioni (taglia, colore, …) ha delle
**varianti**: ogni variante è un prodotto a sé in ordini e magazzino, e tutte
condividono i dati del prodotto.

.. help-include:: product_fields.rst

.. help-include:: product_new.rst

.. help-include:: product_update.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-include:: product_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non riesco a eliminare il prodotto?

   Un prodotto usato in ordini, fatture o movimenti di magazzino non si può
   eliminare: archiviarlo (**Azioni ‣ Archivia**).

.. help-question:: Perché non riesco a cambiare l'unità di misura?

   Quando il prodotto ha movimenti di magazzino l'unità di misura si può
   cambiare solo con una della stessa categoria (es. Unità in Dozzine), non da
   unità a kg.

.. help-question:: Perché il prodotto non compare negli ordini di vendita?

   La casella :version:`<=17|**Può essere venduto**;*|**Vendita**` è
   disattivata, oppure il prodotto è archiviato.

.. help-question:: Perché le modifiche non arrivano agli ordini già fatti?

   Ordini e fatture conservano il prezzo e la descrizione con cui sono stati
   creati; i nuovi documenti usano i nuovi dati.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-29 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
