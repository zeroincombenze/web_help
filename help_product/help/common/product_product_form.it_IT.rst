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

Una variante prodotto è una versione di un prodotto, es. la *T-shirt* in
taglia *M* e colore *Blu*. È definita dai :field:`valori degli attributi
<product_template_variant_value_ids>` del prodotto e ha propri
:field:`riferimento interno <default_code>`, :field:`codice a barre <barcode>`,
giacenze e, se impostato, un prezzo aggiuntivo. Tutti gli altri dati
appartengono al :field:`prodotto <product_tmpl_id>` e sono condivisi dalle sue
varianti. Un prodotto senza attributi ha esattamente una variante.

.. help-include:: product_variant_fields.rst

.. help-include:: product_variant_new.rst

.. help-include:: product_variant_update.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-include:: product_variant_example.rst

.. _faq:

Domande frequenti
-----------------

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

Pagina creata il 2026-10-29 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
