.. help-page:: product_template_kanban
   :title: Prodotti (kanban)
   :model: product.template
   :view-type: kanban
   :priority: 96

Prodotti (kanban)
=================

.. _description:

Descrizione
-----------

.. help-version:: <16

   I prodotti come schede, la vista predefinita dei menu dei prodotti. Ogni
   scheda mostra l'immagine, il :field:`riferimento interno <default_code>`, il
   :field:`nome <name>` e il prezzo. Fare clic su una scheda per aprire il
   prodotto; i pulsanti in alto a destra della barra di ricerca passano alla
   lista.

.. help-version:: >=16

   Il catalogo dei prodotti. Ogni scheda mostra il :field:`nome <name>`, il
   :field:`riferimento interno <default_code>`, il :field:`prezzo di vendita
   <list_price>` e gli altri dati principali. Fare clic per aprire il prodotto. I
   pulsanti in alto a destra passano dal kanban alla lista e alle altre viste.

.. help-include:: product_list_search.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-include:: product_list_example.rst

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

   .. help-question:: Dove sono i prodotti archiviati?

      Scegliere il filtro *In archivio*; aprire un prodotto e usare **Azioni ‣
      Annulla archiviazione** per recuperarlo.

   .. help-question:: Perché non trovo un prodotto dal suo codice?

      La ricerca *Prodotto* guarda nome, riferimento interno e codice a barre:
      controllare che il prodotto non sia archiviato e che non ci siano altri
      filtri attivi.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-30 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
