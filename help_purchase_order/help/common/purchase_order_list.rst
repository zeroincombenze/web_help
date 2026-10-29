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
:field:`reference <name>`, the :field:`vendor <partner_id>`, the
:field:`buyer <user_id>`, the :field:`total <amount_total>` and the
progress of the document. Click a row to open the order.

.. help-include:: purchase_order_list_search.rst

.. help-include:: purchase_order_configure.rst

.. help-include:: purchase_order_report.rst

.. help-include:: purchase_order_list_example.rst

.. _faq:

FAQ
---

.. help-question:: Why don't I see the orders of my colleagues?

   Remove the *My Purchases* or *My Orders* filter from the search bar.

.. help-question:: Where are the cancelled orders?

   The *RFQs* and *Purchase Orders* filters hide them: remove the filters and
   group by status, or add a custom filter on the status.

.. _footer:

Footer
------

Page created on 2026-10-29 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
