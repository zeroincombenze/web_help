.. help-page:: sale_order_form
   :title: Ordine di vendita
   :model: sale.order
   :view-type: form

Ordine di vendita
=================

.. _description:

Descrizione
-----------

Un ordine di vendita nasce come **preventivo**: una proposta inviata al
:field:`cliente <partner_id>` con prodotti, quantità e prezzi.
Quando il cliente lo accetta, il preventivo viene confermato e diventa un
**ordine di vendita**, dal quale Odoo crea le consegne e le fatture.
La barra dello :field:`stato <state>` in alto mostra a che punto è il
documento.

.. help-include:: sale_order_fields.rst

.. help-include:: sale_order_new.rst

.. help-include:: sale_order_update.rst

.. help-include:: sale_order_configure.rst

.. help-include:: sale_order_report.rst

.. help-include:: sale_order_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non riesco a creare la fattura?

   L'ordine deve prima essere confermato. Con la politica di fatturazione
   *quantità consegnate*, la merce deve anche essere consegnata: validare la
   consegna, poi premere di nuovo **Crea fattura**.

.. help-question:: Come si modifica un ordine confermato?

   Quantità e nuove righe si modificano direttamente, vedere *Modifica record*.
   Se l'ordine è bloccato, sbloccarlo prima. Per modifiche importanti,
   annullarlo, premere :version:`10|**Converti in preventivo**;*|**Imposta a
   preventivo**`, modificarlo e confermarlo di nuovo.

.. help-question:: Perché non riesco a eliminare una riga d'ordine?

   Dopo la conferma le righe sono conservate per tracciare consegne e fatture:
   impostare invece la quantità a 0.

.. help-question:: Perché non riesco a eliminare l'ordine?

   Si possono eliminare solo i preventivi non ancora inviati e gli ordini
   annullati: annullare prima l'ordine.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-01 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
