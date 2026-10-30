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

Products are the items or services purchased and sold by a company. They
may be assigned specific codes or left uncoded, managed as inventory stock,
tracked via serial numbers or batch numbers—or handled without any specific
identification—and they impact the company's accounting records. They may
have an expiration date and can be quantified using one or more units of
measurement. They may also have a purchase price and/or a selling price.
Furthermore, they can be managed either as monolithic items or as products
with variants.

In Odoo the :field:`product type <type>` tells **Consumable** and **Stockable
Product** goods from a **Service**; :field:`Can be Sold <sale_ok>` and
:field:`Can be Purchased <purchase_ok>` decide where the product is proposed.
The :field:`internal reference <default_code>` is the code, the
:field:`cost <standard_price>` and the :field:`sale price <list_price>` are the
prices, the :field:`unit of measure <uom_id>` the quantity. The tabs show the
data of the installed applications: sales, purchase, inventory (lots and
serial numbers; expiration dates with the *Product Expiry* module) and
invoicing (taxes and accounts). The **variants** (e.g. sizes and colours) are
built from the attributes of the product.

.. help-include:: product_fields.rst

.. help-include:: product_variants.rst

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
