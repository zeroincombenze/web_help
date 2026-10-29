.. help-page:: purchase_order_form
   :title: Ordine di acquisto
   :model: purchase.order
   :view-type: form
   :priority: 96

Ordine di acquisto
==================

.. _description:

Descrizione
-----------

Un ordine di acquisto nasce come **richiesta di preventivo** (RdP): una
richiesta inviata al :field:`fornitore <partner_id>` con prodotti, quantità e
prezzi. Quando il fornitore accetta, la RdP viene confermata e diventa un
**ordine di acquisto**: Odoo crea il ricevimento della merce in magazzino e la
fattura del fornitore viene poi controllata rispetto all'ordine. La barra dello
:field:`stato <state>` in alto mostra a che punto è il documento.

.. help-include:: purchase_order_fields.rst

.. help-include:: purchase_order_new.rst

.. help-include:: purchase_order_update.rst

.. help-include:: purchase_order_configure.rst

.. help-include:: purchase_order_report.rst

.. help-include:: purchase_order_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché il mio ordine è "Da Approvare" invece che confermato?

   L'impostazione *Livelli di Approvazione* richiede 2 livelli di approvazione
   e il totale dell'ordine supera l'*importo di doppia validazione*: un
   responsabile acquisti deve aprire l'ordine e premere **Approva Ordine**.

.. help-question:: Come si modifica un ordine confermato?

   Quantità, prezzi e nuove righe si modificano direttamente, vedere *Modifica
   record*. Se l'ordine è *Bloccato*, un responsabile acquisti deve prima
   premere **Sblocca**. Per modifiche importanti, annullarlo, premere
   **Imposta come Bozza**, modificarlo e confermarlo di nuovo.

.. help-question:: Perché non riesco ad annullare l'ordine?

   Un ordine non si può annullare se parte della merce è già stata ricevuta o
   se una fattura fornitore collegata è validata: annullare prima la fattura,
   oppure restituire la merce.

.. help-question:: Perché non riesco a eliminare una riga d'ordine?

   Dopo la conferma le righe sono conservate per tracciare ricevimenti e
   fatture: impostare invece la quantità a 0.

.. help-question:: Perché non riesco a eliminare l'ordine?

   Si possono eliminare solo gli ordini annullati: premere prima **Annulla**.

.. help-question:: Perché non c'è nulla da fatturare?

   Con la politica di controllo *Quantitativi ricevuti* del prodotto si possono
   fatturare solo le quantità già ricevute: validare prima il ricevimento.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-29 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
