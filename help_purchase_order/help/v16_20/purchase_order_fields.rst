.. _fields:

Main fields
~~~~~~~~~~~

* :field:`Vendor reference <partner_ref>`: the number of the vendor's offer or
  order confirmation, used to match the vendor bill.
* :field:`Order deadline <date_order>`: the date by which the RFQ should be
  confirmed; after confirmation the :field:`confirmation date <date_approve>`
  is shown instead.
* :field:`Expected arrival <date_planned>`: when the goods should arrive,
  proposed from the vendor lead time of the products.
* :field:`Ask confirmation <receipt_reminder_email>` (*Receipt Reminder*
  setting): emails the vendor some days before the expected arrival, asking
  to confirm the date.
* :field:`Buyer <user_id>`: who follows the order, used in the reports.
* :field:`Source document <origin>`: the document that generated the order,
  e.g. a reordering rule or a sale order.
* :field:`Payment terms <payment_term_id>`: due dates of the vendor bills.
* :field:`Fiscal position <fiscal_position_id>`: maps taxes and accounts, e.g.
  for foreign vendors.
* :field:`Billing status <invoice_status>`: whether something is left to
  bill.
* With Inventory installed, **Deliver To** chooses the receipt operation
  (warehouse) and **Incoterm** the delivery terms agreed with the vendor.
