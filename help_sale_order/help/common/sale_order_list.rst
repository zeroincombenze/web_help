.. help-page:: sale_order_list
   :title: Sale orders
   :model: sale.order
   :view-type: list
   :priority: 96

Sale orders
===========

.. _description:

Description
-----------

Click on button [`Ready`] for help about how to use this help; click on
button [`FAQ`] for the most common solved questions.

The list of quotations and sales orders. Each row shows the
:field:`number <name>`, the :field:`customer <partner_id>`, the
:field:`salesperson <user_id>`, the :field:`total <amount_total>` and the
progress of the document. Click a row to open the order.

.. _new_record:

How to insert a new record
--------------------------

Press :version:`<16|[\`Create\`];*|[\`New\`]` at the top left: an empty form
opens, see its help for the fields to fill in.

.. help-include:: sale_order_list_search.rst

.. _update_record:

How to update a record
----------------------

Click on a line of the list to open its form, then follow the help of the
form to change it.

.. help-include:: sale_order_cancel.rst

.. help-include:: sale_order_configure.rst

.. help-include:: sale_order_report.rst

.. help-include:: sale_order_list_example.rst

.. _faq:

FAQ
---

Click on button [`Topic`] to return to the specific help page.

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
