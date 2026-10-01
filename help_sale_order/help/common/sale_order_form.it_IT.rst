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
La barra dello :field:`stato <state>` in alto mostra a che punto è il documento.

.. help-include:: sale_order_usage.rst

.. help-include:: sale_order_options.rst

.. help-include:: sale_order_configuration.rst

.. _faq:

Domande
-------

.. help-question:: Perché non riesco a creare la fattura?

   L'ordine deve prima essere confermato. Con la politica di fatturazione
   *quantità consegnate*, la merce deve anche essere consegnata: validare la
   consegna, poi premere di nuovo **Crea fattura**.

.. help-question:: Come si modifica un ordine confermato?

   Se l'ordine è bloccato, sbloccarlo prima. Per modifiche importanti,
   annullarlo, premere **Imposta come preventivo**, modificarlo e confermarlo
   di nuovo.

.. help-question::
   :auto:
