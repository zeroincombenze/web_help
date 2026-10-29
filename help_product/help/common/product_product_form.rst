.. help-page:: product_product_form
   :title: Product variant
   :model: product.product
   :view-type: form
   :priority: 96

Product variant
===============

.. _description:

Description
-----------

A product variant is one version of a product, defined by its
:field:`attribute values <attribute_value_ids>`, e.g. *T-shirt (L, Red)*.
Orders, invoices and stock moves always use the variant. A product without
attributes has a single variant, created automatically. The name, the
category, the type and most settings belong to the product and are shared by
all its variants; reference, barcode, cost, weight, volume and stock belong to
each variant.

.. help-include:: product_variant_fields.rst

.. help-include:: product_variant_update.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-include:: product_example.rst

.. _faq:

FAQ
---

.. help-question:: Why did changing the name of a variant change all of them?

   Name, category, type and prices belong to the product: changing them on a
   variant changes the product and all its variants. In the variant form
   opened from the **Variants** button they are not even shown, press *the
   product template* to open the product.

.. help-question:: Why is the sale price of the variant read-only?

   With several variants it is computed: sale price of the product plus the
   extra price of the attribute values, set with **Variant Prices** on the
   product.

.. help-question:: Why can't I delete a variant?

   A variant used by orders, invoices or stock moves cannot be deleted:
   archive it instead (**Active**); to stop creating it, remove its attribute
   value from the **Variants** tab of the product.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-10-29 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
