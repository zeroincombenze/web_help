.. help-page:: product_template_kanban
   :title: Products
   :model: product.template
   :view-type: kanban
   :priority: 96

Products
========

.. _description:

Description
-----------

The catalog of the products. Each card shows the :field:`name <name>`, the
:field:`internal reference <default_code>`, the :field:`sales price <list_price>`
and the other main data. Click it to open the product. The buttons at the top
right switch between kanban, list and the other views.

.. help-include:: product_list_search.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-include:: product_list_example.rst

.. _faq:

FAQ
---

.. help-question:: Where are the archived products?

   Choose the *Archived* filter; open a product and use **Actions ‣
   Unarchive** to restore it.

.. help-question:: Why don't I find a product by its code?

   The search *Product* looks at name, internal reference and barcode: check
   that the product is not archived and that no other filter is active.

.. _footer:

Footer
------

Page created on 2026-10-29 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
