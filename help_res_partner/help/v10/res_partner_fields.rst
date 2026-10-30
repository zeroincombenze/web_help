.. _fields:

Main fields
~~~~~~~~~~~

* :field:`Company type <company_type>`: *Individual* or *Company*.
* :field:`Company <parent_id>`: the company a person belongs to.
* :field:`Address type <type>` (developer mode, on the contacts of a company):
  *Contact*, *Invoice address*, *Shipping address* or *Other address*; orders
  and invoices pick the right address by its type.
* Address: street, :field:`city <city>`, :field:`state <state_id>`,
  :field:`ZIP <zip>` and :field:`country <country_id>`.
* :field:`TIN <vat>` (with the *base_vat* module): the tax identification
  number, checked against the country format.
* :field:`Phone <phone>`, :field:`mobile <mobile>` and :field:`email <email>`:
  the email is used to send documents and messages.
* :field:`Tags <category_id>`: free labels used to classify and filter.
* :field:`Language <lang>`: the language of the documents and emails sent to
  the contact.
* **Sales & Purchases** tab: :field:`Is a Customer <customer>` and
  :field:`Is a Vendor <supplier>` choose where the contact is proposed,
  :field:`salesperson <user_id>`, :field:`internal reference <ref>`.
* **Accounting** tab (with Invoicing installed): customer and vendor payment
  terms, fiscal position, receivable and payable accounts, bank accounts.
