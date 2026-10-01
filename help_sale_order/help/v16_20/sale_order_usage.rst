.. _usage:

Usage
-----

#. Open **Sales ‣ Orders ‣ Quotations** and press **New**.
#. Choose the :field:`customer <partner_id>`. Odoo fills in the
   :field:`invoice address <partner_invoice_id>`, the
   :field:`delivery address <partner_shipping_id>`, the
   :field:`pricelist <pricelist_id>` and the
   :field:`payment terms <payment_term_id>` from the customer; change them if
   needed.
#. Set the :field:`expiration date <validity_date>`: after it the customer can
   no longer accept the quotation online.
#. In the **Order Lines** tab press **Add a product**, pick the product and set
   the quantity; price, taxes and discount are proposed by the pricelist.
   On Odoo 18 **Catalog** adds several products at once.
   **Add a section** and **Add a note** organise the lines; drag the handle on
   the left to reorder them.
#. Complete the **Other Info** tab (salesperson, customer reference, delivery
   date, …) and write the :field:`terms and conditions <note>`.
#. Press **Send by Email** to send the quotation: its status becomes
   *Quotation Sent*. **Preview** shows it as the customer sees it in the portal.
#. Press **Confirm** when the customer accepts: the quotation becomes a
   *Sales Order*, and the delivery is created if Inventory is installed.
#. Press **Create Invoice** and choose *Regular invoice* or a down payment
   (percentage or fixed amount), then **Create and View Invoice**.
#. **Cancel** drops the order; **Lock** prevents further changes to a confirmed
   order.
