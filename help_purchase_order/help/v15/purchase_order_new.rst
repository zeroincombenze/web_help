.. _new_record:

How to insert a new record
--------------------------

#. Open :version:`11|**Purchases ‣ Purchase**;12|**Purchase ‣
   Purchase**;*|**Purchase ‣ Orders**` **‣ Requests for Quotation** and press
   **Create**.
#. Choose the :field:`vendor <partner_id>` (required): type a few letters of
   the name, or pick *Create and Edit…* to add a new vendor. Odoo fills in the
   :field:`payment terms <payment_term_id>`, the :field:`fiscal position
   <fiscal_position_id>` and the currency from the vendor.
#. Type the :field:`vendor reference <partner_ref>` if the vendor already sent
   a quotation.
#. In the **Products** tab press :version:`11|**Add an item**;*|**Add a
   product**`, pick the product and set the quantity; description, scheduled
   date, unit price and taxes are proposed from the vendor list of the product
   and can be changed.
#. Write the :field:`terms and conditions <notes>` under the lines.
#. Complete the :version:`11|**Deliveries & Invoices**;*|**Other
   Information**` tab: :field:`scheduled date <date_planned>`,
   :field:`incoterm <incoterm_id>`, payment terms.
#. Press **Save**: Odoo assigns the :field:`reference <name>` (e.g. *PO00042*).
#. Press :version:`11|**Send RFQ by Email**;*|**Send by Email**` to send the
   request to the vendor, the status becomes *RFQ Sent*; **Print RFQ**
   produces the PDF.
#. Press **Confirm Order** when the vendor agrees: the RFQ becomes a *Purchase
   Order*, the vendor is added to the vendors of the products and, if
   Inventory is installed, the receipt is created. With the order approval the
   status becomes *To Approve* instead.
