.. help-page:: purchase_order_list
   :title: Ordini di acquisto
   :model: purchase.order
   :view-type: list
   :priority: 96

Ordini di acquisto
==================

.. _description:

Descrizione
-----------

L'elenco delle richieste di preventivo e degli ordini di acquisto. Ogni riga
mostra il :field:`riferimento <name>`, il :field:`fornitore <partner_id>`,
l':field:`acquirente <user_id>`, il :field:`totale <amount_total>` e
l'avanzamento del documento. Fare clic su una riga per aprire l'ordine.

.. help-include:: purchase_order_list_search.rst

.. help-include:: purchase_order_configure.rst

.. help-include:: purchase_order_report.rst

.. help-include:: purchase_order_list_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non vedo gli ordini dei colleghi?

   Togliere il filtro *I miei acquisti* o *I miei ordini* dalla barra di
   ricerca.

.. help-question:: Dove sono gli ordini annullati?

   I filtri *RdP* e *Ordini di acquisto* li nascondono: togliere i filtri e
   raggruppare per stato, o aggiungere un filtro personalizzato sullo stato.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-29 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
