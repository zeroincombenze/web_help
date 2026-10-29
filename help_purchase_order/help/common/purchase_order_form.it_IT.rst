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
prezzi. Quando l'offerta del fornitore è accettata, la RdP viene confermata e
diventa un **ordine di acquisto**, dal quale Odoo attende le ricezioni della
merce e le fatture fornitore. La barra dello :field:`stato <state>` in alto
mostra a che punto è il documento.

.. help-include:: purchase_order_fields.rst

.. help-include:: purchase_order_new.rst

.. help-include:: purchase_order_update.rst

.. help-include:: purchase_order_configure.rst

.. help-include:: purchase_order_report.rst

.. help-include:: purchase_order_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché l'ordine è nello stato *Da approvare*?

   L'impostazione *Approvazione ordine di acquisto* è attiva e il totale supera
   il suo importo minimo: un responsabile acquisti deve aprire l'ordine e
   premere **Approva ordine**.

.. help-question:: Perché non riesco a creare la fattura?

   L'ordine deve prima essere confermato. Con il controllo fatture *Quantità
   ricevute*, la merce deve anche essere ricevuta: validare la ricezione, poi
   premere di nuovo **Crea fattura**.

.. help-question:: Come si modifica un ordine confermato?

   Quantità, prezzi e nuove righe si modificano direttamente, vedere *Modifica
   record*. Se l'ordine è bloccato, un responsabile acquisti deve prima
   sbloccarlo. Per cambiare il fornitore, annullare l'ordine, premere
   **Imposta a bozza**, modificarlo e confermarlo di nuovo.

.. help-question:: Perché non riesco ad annullare l'ordine?

   Un ordine con fatture fornitore non si può annullare: annullare prima le
   fatture.

.. help-question:: Perché non riesco a eliminare l'ordine?

   Si possono eliminare solo gli ordini annullati: annullare prima l'ordine.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-29 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
