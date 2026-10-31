.. _new_record:

How to insert a new record
--------------------------

#. Open **Sales ‣ Orders ‣ Quotations** and press **Create**.
#. Choose the :field:`customer <partner_id>` (required): type a few letters of
   the name, or pick *Create and Edit…* to add a new customer. Odoo fills in
   the :field:`pricelist <pricelist_id>` and the :field:`payment terms
   <payment_term_id>` from the customer and, with the *Customer Addresses*
   setting, the :field:`invoice address <partner_invoice_id>` and the
   :field:`delivery address <partner_shipping_id>`; change them if needed.
#. Set the :field:`expiration date <validity_date>` of the
   quotation\ :version:`>=12|, proposed from the *Default Quotation Validity*
   setting`.
#. In the **Order Lines** tab press :version:`11|**Add an item**;*|**Add a
   product**`, pick the product and set the quantity; price, taxes and
   discount are proposed by the pricelist and can be changed.
   :version:`>=12|**Add a section** and **Add a note** organise the lines.`
#. Write the :field:`terms and conditions <note>` under the lines.
#. Complete the :version:`<=12|**Other Information**;*|**Other Info**` tab
   (salesperson, sales team, customer reference, fiscal position, …).
#. Press **Save**: Odoo assigns the :field:`number <name>` (e.g. *SO042*).
#. Press **Send by Email** to send the quotation, its status becomes *Quotation
   Sent*; :version:`<=12|**Print** produces the PDF;*|the **Print** menu
   produces the PDF`.
#. Press :version:`11|**Confirm Sale**;*|**Confirm**` when the customer
   accepts: the quotation becomes a *Sales Order*, and the delivery is created
   if Inventory is installed.
