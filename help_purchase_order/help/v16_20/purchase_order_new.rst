.. _new_record:

New record
----------

#. Open **Purchase ‣ Orders ‣ Requests for Quotation** and press **New**. RFQs
   are also created automatically by the reordering rules and by the
   *Buy* route of the products.
#. Choose the :field:`vendor <partner_id>` (required): type a few letters of
   the name, the VAT number or the email, or pick *Create and edit…* to add a
   new vendor. Odoo fills in the :field:`payment terms <payment_term_id>`, the
   :field:`fiscal position <fiscal_position_id>` and the currency from the
   vendor; change them if needed.
#. Type the :field:`vendor reference <partner_ref>` if the vendor has already
   sent an offer.
#. Check the :field:`order deadline <date_order>` and the :field:`expected
   arrival <date_planned>`.
#. In the **Products** tab press **Add a product**, pick the product and set
   the quantity; the unit price comes from the vendor pricelist of the product
   and can be changed. :version:`>=17|**Catalog** adds several products at
   once.` **Add a section** and **Add a note** organise the lines; drag the
   handle on the left to reorder them.
#. Write the :field:`terms and conditions <notes>` under the lines.
#. Complete the **Other Information** tab: :field:`buyer <user_id>`,
   :field:`source document <origin>`, :field:`payment terms
   <payment_term_id>`, :field:`fiscal position <fiscal_position_id>`.
#. The record is saved automatically when you leave it; press the cloud icon
   next to the breadcrumb to save at once. Odoo assigns the :field:`reference
   <name>` (e.g. *P00042*).
#. Press **Send by Email** to send the RFQ to the vendor with its PDF: its
   status becomes *RFQ Sent*. **Print RFQ** produces the PDF.
#. Press **Confirm Order** when the vendor's offer is accepted: the RFQ
   becomes a *Purchase Order*, the vendor is added to the vendor pricelist of
   the products not yet bought from them and, if Inventory is installed, the
   receipt is created. With the *Purchase Order Approval* setting an order
   above the minimum amount goes to *To Approve* instead, unless you are a
   purchase manager.
