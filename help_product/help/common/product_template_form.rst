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

A product is anything the company sells, buys or keeps in stock. Its
:field:`product type <type>` tells **Consumable** and **Stockable Product**
goods from a **Service**; :field:`Can be Sold <sale_ok>` and :field:`Can be
Purchased <purchase_ok>` decide where it is proposed. A product can come in
several **variants** (e.g. sizes and colours), built from its attributes; the
tabs show the data of the installed applications: sales, purchase, inventory
and invoicing.

.. help-include:: product_fields.rst

.. help-include:: product_new.rst

.. help-include:: product_update.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-include:: product_example.rst

.. _faq:

FAQ
---

.. help-question:: What is the difference between a consumable and a stockable product?

   Both are goods delivered and received. Odoo counts the quantity on hand of
   a *Stockable Product* only (Inventory installed); a *Consumable* is assumed
   to be always available. A *Service* is never delivered.

.. help-question:: Why can't I change the product type or the unit of measure?

   Once the product has stock moves, changing them would make the existing
   quantities wrong: create a new product instead and archive the old one.

.. help-question:: Why can't I delete the product?

   A product used by orders, invoices or stock moves cannot be deleted:
   archive it instead with the **Active** button at the top right.

.. help-question:: Why is the sale price read-only?

   The product has several variants: the price of each variant is the sale
   price of the product plus its extra price, see *Update record*.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-10-29 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
