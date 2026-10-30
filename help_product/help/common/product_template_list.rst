.. help-page:: product_template_list
   :title: Products
   :model: product.template
   :view-type: list
   :priority: 96

Products
========

.. _description:

Description
-----------

.. help-version:: <16

   The list of products. Each row shows the :field:`internal reference
   <default_code>`, the :field:`name <name>`, the :field:`sale price
   <list_price>`, the :field:`cost <standard_price>`, the :field:`category
   <categ_id>` and the :field:`product type <type>`. Click a row to open the
   product.

.. help-version:: >=16

   The catalog of the products. Each row shows the :field:`name <name>`, the
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

.. help-version:: <16

   .. help-question:: Why don't I see all the products?

      The menu may start with a filter, e.g. **Purchases ‣ Purchase ‣ Products**
      shows the products that *Can be Purchased*: remove the filter from the
      search bar. Archived products are shown by the *Archived* filter only.

   .. help-question:: Why does the same product appear several times?

      In the **Product Variants** menu each variant is a row, e.g. one per size
      and colour; the **Products** menu shows the product once.

.. help-version:: >=16

   .. help-question:: Where are the archived products?

      Choose the *Archived* filter; open a product and use **Actions ‣
      Unarchive** to restore it.

   .. help-question:: Why don't I find a product by its code?

      The search *Product* looks at name, internal reference and barcode: check
      that the product is not archived and that no other filter is active.

.. _footer:

Footer
------

Page created on 2026-10-30 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
