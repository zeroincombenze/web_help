.. _fields:

Main fields
~~~~~~~~~~~

* :field:`Address type <type>` (individuals only): *Contact*, *Invoice
  Address*, *Delivery Address*, *Other Address*\ :version:`16|, *Private
  Address*`. A *Contact* shares the address of its company.
* :field:`Tax ID <vat>`: the VAT number, checked against the country rules
  (and online with *Verify VAT Numbers*); Odoo warns when another
  partner has the same one.
* :field:`Job position <function>` and :field:`title <title>` of an
  individual.
* :field:`Phone <phone>`, :field:`mobile <mobile>`, :field:`email <email>`
  and :field:`website <website>`.
* :field:`Language <lang>`: language of the documents and emails sent to the
  contact (shown with more than one language installed).
* :field:`Tags <category_id>`: free labels to classify the contacts.
* **Sales & Purchase** tab: :field:`salesperson <user_id>`,
  :field:`reference <ref>`, :field:`company ID <company_registry>`,
  :field:`industry <industry_id>`; with Sales, Purchase or Invoicing also the
  payment terms, the pricelist and the fiscal position.
* **Invoicing** tab (Invoicing installed): bank accounts and the receivable
  and payable accounts.
* **Internal Notes** tab: :field:`notes <comment>` seen only by the users.
