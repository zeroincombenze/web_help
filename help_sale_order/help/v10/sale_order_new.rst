.. _new_record:

New record
----------

#. Open **Sales ‣ Sales ‣ Quotations** and press **Create**.
#. Choose the :field:`customer <partner_id>` (required): type a few letters of
   the name, or pick *Create and Edit…* to add a new customer. Odoo fills in
   the :field:`pricelist <pricelist_id>` and the :field:`payment terms
   <payment_term_id>` from the customer and, with the *Addresses* setting, the
   :field:`invoice address <partner_invoice_id>` and the :field:`delivery
   address <partner_shipping_id>`; change them if needed.
#. Set the :field:`expiration date <validity_date>` of the quotation.
#. In the **Order Lines** tab press **Add an item**, pick the product and set
   the quantity; price, taxes and discount are proposed by the pricelist and
   can be changed.
#. Write the :field:`terms and conditions <note>` under the lines.
#. Complete the **Other Information** tab (salesperson, sales team, customer
   reference, fiscal position, …).
#. Press **Save**: Odoo assigns the :field:`number <name>` (e.g. *SO042*).
#. Press **Send by Email** to send the quotation, its status becomes *Quotation
   Sent*; **Print** produces the PDF.
#. Press **Confirm Sale** when the customer accepts: the quotation becomes a
   *Sales Order*, and the delivery is created if Inventory is installed.
