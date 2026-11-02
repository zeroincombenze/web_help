.. _fields:

Main fields
~~~~~~~~~~~

.. help-version:: 11

   * :field:`Quotation template <template_id>`: fills lines, optional products
     and terms from a template (*Quotations Templates* setting).

.. help-version:: >=12

   * :field:`Quotation template <sale_order_template_id>`: fills lines,
     optional products and terms from a template (*Quotation Templates*
     setting).

* :field:`Pricelist <pricelist_id>`: prices and automatic discounts for the
  customer (pricelist setting).
* :field:`Payment terms <payment_term_id>`: due dates of the invoices.
* :version:`<13|**Discount (%)**;*|**Disc.%**` on the order lines (*Discounts* setting).
* :field:`Salesperson <user_id>` and :field:`sales team <team_id>`: who follows
  the order, used in the reports.
* :field:`Customer reference <client_order_ref>`: the customer's own order
  number, printed on the documents.
* :field:`Fiscal position <fiscal_position_id>`: maps taxes and accounts, e.g.
  for foreign customers.
* :field:`Source document <origin>`: the document that generated the order.
* :field:`Invoice status <invoice_status>`: whether something is left to
  invoice.
