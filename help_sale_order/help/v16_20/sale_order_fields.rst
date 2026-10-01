.. _fields:

Main fields
~~~~~~~~~~~

* :field:`Quotation template <sale_order_template_id>`: fills lines, optional
  products and terms from a template (*Quotation Templates* setting).
* :field:`Pricelist <pricelist_id>`: prices and automatic discounts for the
  customer (*Pricelists* setting).
* :field:`Payment terms <payment_term_id>`: due dates of the invoices.
* **Optional Products** tab: products the customer can add to the order from
  the portal.
* :field:`Online signature <require_signature>` and :field:`online payment
  <require_payment>`: the customer must sign, or pay, to confirm online.
  :version:`>=18|The payment can be a percentage of the total.`
* :field:`Salesperson <user_id>` and :field:`sales team <team_id>`: who follows
  the order, used in the reports.
* :field:`Customer reference <client_order_ref>`: the customer's own order
  number, printed on the documents.
* :field:`Tags <tag_ids>`: free labels to classify the orders.
* :field:`Delivery date <commitment_date>`: the date promised to the customer.
* :field:`Fiscal position <fiscal_position_id>`: maps taxes and accounts, e.g.
  for foreign customers.
* :field:`Source document <origin>`: the document that generated the order.
