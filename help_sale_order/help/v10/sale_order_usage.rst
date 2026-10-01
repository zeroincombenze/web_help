.. _usage:

Usage
-----

#. Open **Sales ‣ Sales ‣ Quotations** and press **Create**.
#. Choose the :field:`customer <partner_id>`. Odoo fills in the
   :field:`pricelist <pricelist_id>` and the
   :field:`payment terms <payment_term_id>` from the customer and, with the
   *Customer Addresses* setting, the
   :field:`invoice address <partner_invoice_id>` and the
   :field:`delivery address <partner_shipping_id>`; change them if needed.
#. Set the :field:`expiration date <validity_date>` of the quotation.
#. In the **Order Lines** tab press **Add an item**, pick the product and set
   the quantity; price, taxes and discount are proposed by the pricelist.
#. Complete the **Other Information** tab (salesperson, customer reference,
   fiscal position, …) and write the :field:`terms and conditions <note>`.
#. Press **Send by Email** to send the quotation, its status becomes
   *Quotation Sent*; **Print** produces the PDF.
#. Press **Confirm Sale** when the customer accepts: the quotation becomes a
   *Sales Order*, and the delivery is created if Inventory is installed.
#. Press **Create Invoice** and choose what to invoice: *Invoiceable lines*,
   *Invoiceable lines (deduct down payments)* or a down payment (percentage
   or fixed amount), then **Create and View Invoices**.
#. **Cancel** drops the order and **Set to Quotation** brings it back to draft;
   **Lock** closes a confirmed order to further changes.
