.. help-page:: product_product_form
   :title: Variante prodotto
   :model: product.product
   :view-type: form
   :priority: 96

Variante prodotto
=================

.. _description:

Descrizione
-----------

Una variante di prodotto è una versione di un prodotto, definita dai suoi
:field:`valori attributo <attribute_value_ids>`, ad es. *Maglietta (L,
Rosso)*. Ordini, fatture e movimenti di magazzino usano sempre la variante. Un
prodotto senza attributi ha un'unica variante, creata automaticamente. Nome,
categoria, tipo e quasi tutte le impostazioni appartengono al prodotto e sono
condivisi da tutte le sue varianti; riferimento, codice a barre, costo, peso,
volume e giacenza appartengono a ogni variante.

.. help-include:: product_variant_fields.rst

.. help-include:: product_variant_update.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-include:: product_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché cambiare il nome di una variante le ha cambiate tutte?

   Nome, categoria, tipo e prezzi appartengono al prodotto: cambiarli su una
   variante cambia il prodotto e tutte le sue varianti. Nella maschera della
   variante aperta dal pulsante **Varianti** non sono nemmeno mostrati,
   premere *Modello prodotto* per aprire il prodotto.

.. help-question:: Perché il prezzo di vendita della variante non è modificabile?

   Con più varianti è calcolato: prezzo di vendita del prodotto più il prezzo
   extra dei valori attributo, impostato con **Prezzi Variante** sul prodotto.

.. help-question:: Perché non riesco a eliminare una variante?

   Una variante usata da ordini, fatture o movimenti di magazzino non si può
   eliminare: archiviarla invece (**Attivo**); per non crearla più, togliere il
   suo valore attributo dalla scheda **Varianti** del prodotto.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-29 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
