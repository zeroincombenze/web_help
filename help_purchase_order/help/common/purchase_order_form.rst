.. help-page:: purchase_order_form
   :title: Purchase order
   :model: purchase.order
   :view-type: form
   :priority: 96

Purchase order
==============

.. _description:

Description
-----------

A purchase order starts as a **request for quotation** (RFQ): a request sent
to the :field:`vendor <partner_id>` listing products, quantities and prices.
When the vendor's offer is accepted, the RFQ is confirmed and becomes a
**purchase order**, from which Odoo expects the receipts of the goods and the
vendor bills. The :field:`status <state>` bar at the top shows where the
document stands.

.. help-include:: purchase_order_fields.rst

.. help-include:: purchase_order_new.rst

.. help-include:: purchase_order_update.rst

.. help-include:: purchase_order_configure.rst

.. help-include:: purchase_order_report.rst

.. help-include:: purchase_order_example.rst

.. _faq:

FAQ
---

.. help-question:: Why is the order in *To Approve* status?

   The *Purchase Order Approval* setting is active and the total exceeds its
   minimum amount: a purchase manager must open the order and press
   **Approve Order**.

.. help-question:: Why can't I create the bill?

   The order must be confirmed first. With the *Received quantities* bill
   control, the goods must also be received: validate the receipt, then press
   **Create Bill** again.

.. help-question:: How do I change a confirmed order?

   Quantities, prices and new lines can be changed directly, see *Update
   record*. If the order is locked, a purchase manager must unlock it first.
   To change the vendor, cancel the order, press **Set to Draft**, change it
   and confirm it again.

.. help-question:: Why can't I cancel the order?

   An order with vendor bills cannot be cancelled: cancel the bills first.

.. help-question:: Why can't I delete the order?

   Only cancelled orders can be deleted: cancel the order first.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-10-29 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
