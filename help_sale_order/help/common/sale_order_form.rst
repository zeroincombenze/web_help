.. help-page:: sale_order_form
   :title: Sale order
   :model: sale.order
   :view-type: form

Sale order
==========

.. _description:

Description
-----------

A sale order starts as a **quotation**: a proposal sent to the
:field:`customer <partner_id>` listing products, quantities and prices.
When the customer accepts it, the quotation is confirmed and becomes a
**sales order**, from which Odoo creates the deliveries and the invoices.
The :field:`status <state>` bar at the top shows where the document stands.

.. help-include:: sale_order_usage.rst

.. help-include:: sale_order_options.rst

.. help-include:: sale_order_configuration.rst

.. _faq:

Questions
---------

.. help-question:: Why can't I create the invoice?

   The order must be confirmed first. With the *delivered quantities* invoicing
   policy, the goods must also be delivered: validate the delivery, then press
   **Create Invoice** again.

.. help-question:: How do I change a confirmed order?

   If the order is locked, unlock it first. To change it a lot, cancel it,
   press **Set to Quotation**, change it and confirm it again.

.. help-question::
   :auto:
