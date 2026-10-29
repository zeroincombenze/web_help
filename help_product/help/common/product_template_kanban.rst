.. help-page:: product_template_kanban
   :title: Products (kanban)
   :model: product.template
   :view-type: kanban
   :priority: 96

Products (kanban)
=================

.. _description:

Description
-----------

The products as cards, the default view of the product menus. Each card shows
the picture, the :field:`internal reference <default_code>`, the :field:`name
<name>` and the price. Click a card to open the product; the buttons at the
top right of the search bar switch to the list.

.. help-include:: product_list_search.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-include:: product_list_example.rst

.. _faq:

FAQ
---

.. help-question:: Why don't I see all the products?

   The menu may start with a filter, e.g. **Purchases ‣ Purchase ‣ Products**
   shows the products that *Can be Purchased*: remove the filter from the
   search bar. Archived products are shown by the *Archived* filter only.

.. help-question:: Why does the same product appear several times?

   In the **Product Variants** menu each variant is a row, e.g. one per size
   and colour; the **Products** menu shows the product once.

.. _footer:

Footer
------

Page created on 2026-10-29 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
