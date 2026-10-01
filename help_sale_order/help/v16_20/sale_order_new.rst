.. _new_record:

New record
----------

#. Open **Sales ‣ Orders ‣ Quotations** and press **New**. A quotation can also
   be started from a CRM opportunity with **New Quotation**.
#. Choose the :field:`customer <partner_id>` (required): type a few letters of
   the name, or pick *Create and edit…* to add a new customer. Odoo fills in
   the :field:`invoice address <partner_invoice_id>`, the :field:`delivery
   address <partner_shipping_id>` (visible with the *Customer Addresses*
   setting), the :field:`pricelist <pricelist_id>` and the :field:`payment
   terms <payment_term_id>` from the customer; change them if needed. Empty
   payment terms mean *Immediate Payment*.
#. Optionally choose a :field:`quotation template <sale_order_template_id>`: it
   fills the lines, the optional products, the terms and the validity.
#. Check the :field:`expiration date <validity_date>`, proposed from the
   *Default Quotation Validity* setting: after it the customer can no longer
   accept the quotation online.
#. In the **Order Lines** tab press **Add a product**, pick the product and set
   the quantity; price, taxes and discount are proposed by the pricelist and
   can be changed. :version:`>=17|**Catalog** adds several products at once.`
   **Add a section** and **Add a note** organise the lines; drag the handle on
   the left to reorder them. **Discount** (*Discounts* setting) applies a
   global discount to all the lines.
#. Write the :field:`terms and conditions <note>` under the lines, if they are
   not taken from the settings or the template.
#. Complete the **Other Info** tab: :field:`salesperson <user_id>`,
   :field:`sales team <team_id>`, :field:`customer reference
   <client_order_ref>`, :field:`tags <tag_ids>`, :field:`online signature
   <require_signature>` and :field:`online payment <require_payment>`,
   :field:`delivery date <commitment_date>`, :field:`fiscal position
   <fiscal_position_id>`. In **Optional Products** list the products the
   customer may add from the portal.
#. The record is saved automatically when you leave it; press the cloud icon
   next to the breadcrumb to save at once. Odoo assigns the :field:`number
   <name>` (e.g. *S00042*).
#. Press **Send by Email** to send the quotation with its PDF: its status
   becomes *Quotation Sent*. **Preview** shows it as the customer sees it in
   the portal.
#. Press **Confirm** when the customer accepts (or let the customer sign or pay
   online): the quotation becomes a *Sales Order* and, if Inventory is
   installed, the delivery is created. Odoo refuses to confirm when a line has
   no product.
