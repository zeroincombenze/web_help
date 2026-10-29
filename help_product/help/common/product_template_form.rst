.. help-page:: product_template_form
   :title: Product
   :model: product.template
   :view-type: form
   :priority: 96

Product
=======

.. _description:

Description
-----------

A product is anything the company sells, buys or keeps in stock: goods,
services or\ :version:`>=18| combos of products`. Its :field:`sales price <list_price>`,
:field:`cost <standard_price>`, :field:`category <categ_id>` and
:field:`unit of measure <uom_id>` are proposed in orders, invoices and
transfers. A product sold in several versions (size, color, …) has
**variants**: each variant is a product of its own in orders and stock, all
sharing the data of the product.

.. help-include:: product_fields.rst

.. help-include:: product_new.rst

.. help-include:: product_update.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-include:: product_example.rst

.. _faq:

FAQ
---

.. help-question:: Why can't I delete the product?

   A product used in orders, invoices or stock moves cannot be deleted:
   archive it instead (**Actions ‣ Archive**).

.. help-question:: Why can't I change the unit of measure?

   Once the product has stock moves the unit of measure can only be changed
   to one of the same category (e.g. Units to Dozens), not from units to kg.

.. help-question:: Why doesn't the product appear in sales orders?

   The :version:`<=17|**Can be Sold**;*|**Sales**` checkbox is off, or the
   product is archived.

.. help-question:: Why did my changes not reach the orders already made?

   Orders and invoices keep the price and description they were created
   with; new documents use the new data.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-10-29 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
