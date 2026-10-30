.. help-page:: product_product_list
   :title: Varianti prodotto
   :model: product.product
   :view-type: list
   :priority: 96

Varianti prodotto
=================

.. _description:

Descrizione
-----------

.. help-version:: <16

   L'elenco delle varianti di prodotto. Ogni riga mostra il :field:`riferimento
   interno <default_code>`, il :field:`nome <name>`, i :field:`valori attributo
   <attribute_value_ids>`, il :field:`prezzo di vendita <lst_price>`, l'unità di
   misura e il :field:`codice a barre <barcode>`. Fare clic su una riga per
   aprire la variante.

.. help-version:: >=16

   L'elenco di tutte le varianti prodotto: una riga per ogni combinazione di
   valori degli attributi, con il :field:`riferimento interno <default_code>`, i
   :field:`valori degli attributi <product_template_variant_value_ids>` e il
   :field:`prezzo di vendita <lst_price>`. Fare clic per aprire la variante.

.. help-include:: product_variant_list_search.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-version:: <16

   .. help-include:: product_list_example.rst

.. help-version:: >=16

   .. help-include:: product_variant_list_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-version:: <16

   .. help-question:: Perché non vedo tutti i prodotti?

      Il menu può partire con un filtro, ad es. **Acquisti ‣ Acquisto ‣
      Prodotti** mostra i prodotti che *Può essere acquistato*: togliere il filtro
      dalla barra di ricerca. I prodotti archiviati si vedono solo con il filtro
      *Archiviato*.

   .. help-question:: Perché lo stesso prodotto compare più volte?

      Nel menu **Varianti Prodotto** ogni variante è una riga, ad es. una per
      taglia e colore; il menu **Prodotti** mostra il prodotto una sola volta.

.. help-version:: >=16

   .. help-question:: Perché manca il menu delle varianti?

      **Varianti prodotto** è visibile solo con l'impostazione *Varianti* attiva.

   .. help-question:: Dove sono le varianti archiviate?

      Scegliere il filtro *In archivio*: le varianti tolte dagli attributi del
      prodotto sono archiviate, non eliminate.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-30 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
