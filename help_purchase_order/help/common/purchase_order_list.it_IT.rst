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
mostra il :field:`riferimento <name>`, la :field:`data ordine <date_order>`,
il :field:`fornitore <partner_id>`, il :field:`documento di origine <origin>`,
il :field:`totale <amount_total>` e lo :field:`stato <state>` del documento.
Fare clic su una riga per aprire l'ordine.

.. help-include:: purchase_order_list_search.rst

.. help-include:: purchase_order_configure.rst

.. help-include:: purchase_order_report.rst

.. help-include:: purchase_order_list_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non trovo una richiesta di preventivo tra gli ordini di acquisto?

   I menu separano i documenti: *Richieste di preventivo* elenca le RdP non
   ancora confermate, *Ordini di acquisto* gli ordini da approvare,
   confermati, bloccati o annullati.

.. help-question:: Dove sono gli ordini annullati?

   Gli ordini annullati sono mostrati in grigio: togliere i filtri, oppure
   raggrupparli per stato con un raggruppamento personalizzato.

.. help-question:: Chi ha creato queste richieste di preventivo?

   Molte RdP sono create automaticamente da Odoo dalle regole di
   riapprovvigionamento del magazzino o dalla rotta *Acquista*: il
   :field:`documento di origine <origin>` indica cosa le ha generate.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-29 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
