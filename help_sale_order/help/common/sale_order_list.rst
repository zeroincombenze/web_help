.. help-page:: sale_order_list
   :title: Sale orders
   :model: sale.order
   :view-type: list

Sale orders
===========

.. _description:

Description
-----------

The list of quotations and sales orders. Each row shows the
:field:`number <name>`, the :field:`customer <partner_id>`, the
:field:`salesperson <user_id>`, the :field:`total <amount_total>` and the
progress of the document. Click a row to open the order.

.. help-include:: sale_order_list_search.rst

.. help-include:: sale_order_configure.rst

.. help-include:: sale_order_report.rst

.. help-include:: sale_order_list_example.rst

.. _faq:

FAQ
---

.. help-question:: Why don't I see the orders of my colleagues?

   Remove the :version:`10|*My Orders*;*|*My Orders* / *My Quotations*` filter
   from the search bar. A user with the *User: Own Documents Only* sales access
   right sees only their own orders.

.. help-question:: Where are the cancelled orders?

   The *Quotations* and *Sales Orders* filters hide them: remove the filters
   and group by status, or add a custom filter on the status.

.. _footer:

Footer
------

Page created on 2026-10-01 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
