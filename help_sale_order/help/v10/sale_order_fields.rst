.. _fields:

Main fields
~~~~~~~~~~~

* :field:`Pricelist <pricelist_id>`: prices and automatic discounts for the
  customer (*Sale Price* setting).
* :field:`Payment terms <payment_term_id>`: due dates of the invoices.
* **Discount (%)** on the order lines (*Discount* setting).
* :field:`Salesperson <user_id>` and :field:`sales team <team_id>`: who follows
  the order, used in the reports.
* :field:`Customer reference <client_order_ref>`: the customer's own order
  number, printed on the documents.
* :field:`Fiscal position <fiscal_position_id>`: maps taxes and accounts, e.g.
  for foreign customers.
* :field:`Source document <origin>`: the document that generated the order.
* :field:`Invoice status <invoice_status>`: whether something is left to
  invoice.
* With the *Online Quotations* setting a quotation template fills lines,
  optional products and terms.
