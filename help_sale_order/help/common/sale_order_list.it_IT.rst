.. help-page:: sale_order_list
   :title: Ordini di vendita
   :model: sale.order
   :view-type: list
   :priority: 96

Ordini di vendita
=================

.. _description:

Descrizione
-----------

L'elenco dei preventivi e degli ordini di vendita. Ogni riga mostra il
:field:`numero <name>`, il :field:`cliente <partner_id>`, l'
:field:`addetto vendite <user_id>`, il :field:`totale <amount_total>` e
l'avanzamento del documento. Fare clic su una riga per aprire l'ordine.

.. help-include:: sale_order_list_search.rst

.. help-include:: sale_order_configure.rst

.. help-include:: sale_order_report.rst

.. help-include:: sale_order_list_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non vedo gli ordini dei colleghi?

   Togliere il filtro :version:`10|*Miei ordini*;*|*I miei ordini* / *I miei
   preventivi*` dalla barra di ricerca. Un utente con il diritto vendite
   :version:`10|*Utente: Solo i propri Documenti*;*|*Utente: solo documenti
   personali*` vede solo i propri ordini.

.. help-question:: Dove sono gli ordini annullati?

   I filtri *Preventivi* e *Ordini di vendita* li nascondono: togliere i filtri
   e raggruppare per stato, o aggiungere un filtro personalizzato sullo stato.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-01 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
