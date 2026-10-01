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

.. help-include:: sale_order_fields.rst

.. help-include:: sale_order_new.rst

.. help-include:: sale_order_update.rst

.. help-include:: sale_order_configure.rst

.. help-include:: sale_order_report.rst

.. help-include:: sale_order_example.rst

.. _faq:

FAQ
---

.. help-question:: Why can't I create the invoice?

   The order must be confirmed first. With the *delivered quantities* invoicing
   policy, the goods must also be delivered: validate the delivery, then press
   **Create Invoice** again.

.. help-question:: How do I change a confirmed order?

   Quantities and new lines can be changed directly, see *Update record*.
   If the order is locked, unlock it first. To change it a lot, cancel it,
   press **Set to Quotation**, change it and confirm it again.

.. help-question:: Why can't I delete an order line?

   Once the order is confirmed its lines are kept to track deliveries and
   invoices: set the quantity to 0 instead.

.. help-question:: Why can't I delete the order?

   Only quotations not yet sent and cancelled orders can be deleted: cancel
   the order first.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-10-01 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
