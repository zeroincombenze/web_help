.. _new_record:

New record
----------

#. Open **Purchases ‣ Purchase ‣ Requests for Quotation** and press
   **Create**.
#. Choose the :field:`vendor <partner_id>` (required): type a few letters of
   the name, or pick *Create and Edit…* to add a new vendor. Odoo fills in the
   :field:`payment terms <payment_term_id>`, the :field:`fiscal position
   <fiscal_position_id>` and the currency from the vendor.
#. Type the :field:`vendor reference <partner_ref>` if the vendor already sent
   a quotation.
#. In the **Products** tab press **Add an item**, pick the product and set the
   quantity; description, scheduled date, unit price and taxes are proposed
   from the vendor list of the product and can be changed.
#. Write the :field:`terms and conditions <notes>` under the lines.
#. Complete the **Deliveries & Invoices** tab: :field:`scheduled date
   <date_planned>` (the calendar button copies it to all the lines),
   :field:`incoterm <incoterm_id>`, payment terms.
#. Press **Save**: Odoo assigns the :field:`reference <name>` (e.g. *PO00042*).
#. Press **Send RFQ by Email** to send the request to the vendor, the status
   becomes *RFQ Sent*; **Print RFQ** produces the PDF.
#. Press **Confirm Order** when the vendor agrees: the RFQ becomes a *Purchase
   Order*, the vendor is added to the vendors of the products and, if
   Inventory is installed, the receipt is created. With 2 levels of approval
   the status becomes *To Approve* instead.
