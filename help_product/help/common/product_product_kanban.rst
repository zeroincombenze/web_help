.. help-page:: product_product_kanban
   :title: Product variants (kanban)
   :model: product.product
   :view-type: kanban
   :priority: 96

Product variants (kanban)
=========================

.. _description:

Description
-----------

.. help-version:: <16

   The product variants as cards. Each card shows the picture, the :field:`name
   <name>`, the :field:`attribute values <attribute_value_ids>` and the price.
   Click a card to open the variant; the buttons at the top right of the search
   bar switch to the list.

.. help-version:: >=16

   The list of all the product variants: one card for each combination of
   attribute values, with its :field:`internal reference <default_code>`, its
   :field:`attribute values <product_template_variant_value_ids>` and its
   :field:`sales price <lst_price>`. Click it to open the variant.

.. help-include:: product_variant_list_search.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-version:: <16

   .. help-include:: product_list_example.rst

.. help-version:: >=16

   .. help-include:: product_variant_list_example.rst

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

   .. help-question:: Why is the variants menu missing?

      **Product Variants** is shown only with the *Variants* setting active.

   .. help-question:: Where are the archived variants?

      Choose the *Archived* filter: variants removed from the product attributes
      are archived, not deleted.

.. _footer:

Footer
------

Page created on 2026-10-30 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
