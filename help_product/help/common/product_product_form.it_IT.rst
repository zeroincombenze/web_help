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

.. help-version:: <16

   Una variante di prodotto è una versione di un prodotto, definita dai suoi
   :field:`valori attributo <attribute_value_ids>`, ad es. *Maglietta (L,
   Rosso)*. Ordini, fatture e movimenti di magazzino usano sempre la variante. Un
   prodotto senza attributi ha un'unica variante, creata automaticamente. Nome,
   categoria, tipo e quasi tutte le impostazioni appartengono al prodotto e sono
   condivisi da tutte le sue varianti; riferimento, codice a barre, costo, peso,
   volume e giacenza appartengono a ogni variante.

.. help-version:: >=16

   Una variante prodotto è una versione di un prodotto, es. la *T-shirt* in
   taglia *M* e colore *Blu*. È definita dai :field:`valori degli attributi
   <product_template_variant_value_ids>` del prodotto e ha propri
   :field:`riferimento interno <default_code>`, :field:`codice a barre <barcode>`,
   giacenze e, se impostato, un prezzo aggiuntivo. Tutti gli altri dati
   appartengono al :field:`prodotto <product_tmpl_id>` e sono condivisi dalle sue
   varianti. Un prodotto senza attributi ha esattamente una variante.

.. help-include:: product_variant_fields.rst

.. help-version:: >=16

   .. help-include:: product_variant_new.rst

.. help-include:: product_variant_update.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-version:: <16

   .. help-include:: product_example.rst

.. help-version:: >=16

   .. help-include:: product_variant_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-version:: <16

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

.. help-version:: >=16

   .. help-question:: Perché non riesco a creare una variante con Nuovo?

      Le varianti sono generate dagli attributi del prodotto: aggiungere il valore
      nella scheda **Attributi e varianti** del prodotto.

   .. help-question:: Perché una modifica alla variante cambia tutte le altre?

      Nome, prezzi, categoria, imposte e gli altri dati comuni appartengono al
      prodotto: solo riferimento, codice a barre, prezzo aggiuntivo, peso e
      volume sono per variante.

   .. help-question:: Perché non riesco a eliminare la variante?

      Una variante usata in documenti non si può eliminare: archiviarla, oppure
      togliere il suo valore dagli attributi del prodotto (la variante viene
      allora archiviata).

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-30 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
