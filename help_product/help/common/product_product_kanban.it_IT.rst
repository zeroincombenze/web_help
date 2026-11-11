.. help-page:: product_product_kanban
   :title: Varianti prodotto (kanban)
   :model: product.product
   :view-type: kanban
   :priority: 96

Varianti prodotto (kanban)
==========================

.. _description:

Descrizione
-----------

Fare clic sul pulsante **Pronto** per sapere come usare questo aiuto; fare
clic sul pulsante **FAQ** per le domande più comuni già risolte.

.. help-version:: <13

   Le varianti di prodotto come schede. Ogni scheda mostra l'immagine, il
   :field:`nome <name>`, i :field:`valori attributo <attribute_value_ids>` e il
   prezzo. Fare clic su una scheda per aprire la variante; i pulsanti in alto a
   destra della barra di ricerca passano alla lista.

.. help-version:: 13-15

   Le varianti di prodotto come schede. Ogni scheda mostra l'immagine, il
   :field:`nome <name>`, i :field:`valori attributo
   <product_template_attribute_value_ids>` e il prezzo. Fare clic su una scheda
   per aprire la variante; i pulsanti in alto a destra della barra di ricerca
   passano alla lista.

.. help-version:: >=16

   L'elenco di tutte le varianti prodotto: una scheda per ogni combinazione di
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

Fare clic sul pulsante **Argomento** per tornare alla pagina di aiuto specifica.

.. help-version:: <16

   .. help-question:: Perché non vedo tutti i prodotti?

      Il menu può partire con un filtro, ad es.
      :version:`<=11|**Acquisti ‣ Acquisto ‣ Prodotti**;12|**Acquisti ‣ Acquisti
      ‣ Prodotti**;*|**Acquisti ‣ Prodotti ‣ Prodotti**` mostra i prodotti che *Può essere acquistato*: togliere il filtro
      dalla barra di ricerca. I prodotti archiviati si vedono solo con il filtro
      *Archiviato*.

   .. help-question:: Perché lo stesso prodotto compare più volte?

      Nel menu :version:`12|**Varianti prodotto**;*|**Varianti Prodotto**` ogni variante è una riga, ad es. una per
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
