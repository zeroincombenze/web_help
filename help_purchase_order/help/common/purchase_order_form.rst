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

.. help-version:: <16

   A purchase order starts as a **request for quotation** (RFQ): a request sent
   to the :field:`vendor <partner_id>` listing products, quantities and prices.
   When the vendor agrees, the RFQ is confirmed and becomes a **purchase order**:
   Odoo creates the receipt of the goods in the warehouse, and the vendor bill is
   then checked against the order. The :field:`status <state>` bar at the top
   shows where the document stands.

.. help-version:: >=16

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

.. help-version:: <16

   .. help-question:: Why is my order "To Approve" instead of confirmed?

      The *Levels of Approvals* setting requires 2 levels of approval and the
      order total is over the *Double validation amount*: a purchase manager must
      open the order and press **Approve Order**.

   .. help-question:: How do I change a confirmed order?

      Quantities, prices and new lines can be changed directly, see *Update
      record*. If the order is *Locked*, a purchase manager must press **Unlock**
      first. To change it a lot, cancel it, press **Set to Draft**, change it and
      confirm it again.

   .. help-question:: Why can't I cancel the order?

      An order cannot be cancelled once some goods are received or a vendor bill
      linked to it is validated: cancel the vendor bill first, or return the goods.

   .. help-question:: Why can't I delete an order line?

      Once the order is confirmed its lines are kept to track receipts and bills:
      set the quantity to 0 instead.

   .. help-question:: Why can't I delete the order?

      Only cancelled orders can be deleted: press **Cancel** first.

   .. help-question:: Why is there nothing to bill?

      With the *On received quantities* control policy of the product, only the
      quantities already received can be billed: validate the receipt first.

.. help-version:: >=16

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

Page created on 2026-10-30 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
