.. _fields:

Main fields
~~~~~~~~~~~

* :field:`Vendor reference <partner_ref>`: the number of the vendor's
  quotation or sales order, used to match the vendor bill.
* :field:`Order date <date_order>`: the date of the RFQ, then of the
  confirmation.
* :field:`Source document <origin>`: the document that generated the order,
  e.g. a replenishment rule or a sale order.
* :field:`Scheduled date <date_planned>`: when the goods are expected; each
  line has its own date, computed from the vendor lead time.
* :field:`Deliver To <picking_type_id>`: the warehouse receipt operation (with
  multiple locations); with dropshipping, the :field:`drop ship address
  <dest_address_id>` of the customer.
* :field:`Incoterm <incoterm_id>`: the international commercial terms of the
  delivery.
* :field:`Payment terms <payment_term_id>`: proposed on the vendor bill.
* :field:`Fiscal position <fiscal_position_id>`: maps taxes and accounts, e.g.
  for foreign vendors.
* :field:`Billing status <invoice_status>`: *Nothing to Bill*, *Waiting Bills*
  or *Bills Received*.
