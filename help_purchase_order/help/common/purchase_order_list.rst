.. help-page:: purchase_order_list
   :title: Purchase orders
   :model: purchase.order
   :view-type: list
   :priority: 96

Purchase orders
===============

.. _description:

Description
-----------

The list of requests for quotation and purchase orders. Each row shows the
:field:`reference <name>`, the :field:`order date <date_order>`, the
:field:`vendor <partner_id>`, the :field:`source document <origin>`, the
:field:`total <amount_total>` and the :field:`status <state>` of the document.
Click a row to open the order.

.. help-include:: purchase_order_list_search.rst

.. help-include:: purchase_order_configure.rst

.. help-include:: purchase_order_report.rst

.. help-include:: purchase_order_list_example.rst

.. _faq:

FAQ
---

.. help-question:: Why don't I find a request for quotation among the purchase orders?

   The menus split the documents: *Requests for Quotation* lists the RFQs not
   yet confirmed, *Purchase Orders* the orders to approve, confirmed, locked or
   cancelled.

.. help-question:: Where are the cancelled orders?

   Cancelled orders are shown in grey: remove the filters, or group by status
   with a custom grouping.

.. help-question:: Who created these requests for quotation?

   Most RFQs are created automatically by Odoo from the stock replenishment
   rules or the *Buy* route: the :field:`source document <origin>` shows what
   generated them.

.. _footer:

Footer
------

Page created on 2026-10-29 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
