.. help-if:: module = sale

   .. _sale_order:

   Invoicing from sale order
   -------------------------

   With the Sales app the customer invoices are usually created from the
   confirmed sale orders: Odoo copies the customer, the payment terms, the
   fiscal position and the lines, and keeps track of what is already invoiced.

   What can be invoiced depends on the *Invoicing Policy* of each product, in
   the :version:`10|**Invoicing**;11-15|**Sales**;*|**General Information**`
   tab of the product:

   * *Ordered quantities*: the whole ordered quantity, as soon as the order is
     confirmed;
   * *Delivered quantities*: only the quantity already delivered, e.g. after
     the validation of the delivery order.

   The *Invoice Status* of an order shows what is left: *Nothing to Invoice*,
   *To Invoice*, *Fully Invoiced* or *Upselling Opportunity* (more was
   delivered than ordered).

   #. Open the confirmed sale order and press **Create Invoice**. The orders
      waiting for an invoice are listed in :version:`10|**Sales ‣ Invoicing ‣
      Sales to Invoice**;11|**Sales ‣ Invoicing ‣ Orders to
      Invoice**;*|**Sales ‣ To Invoice ‣ Orders to Invoice**`.
   #. Choose what to invoice:

      .. help-version:: <13

         * *Invoiceable lines*: the quantities to invoice of every line;
         * *Invoiceable lines (deduct down payments)*: the same, minus the
           down payments already invoiced;

      .. help-version:: >=13

         * *Regular invoice*: the quantities to invoice of every line; check
           *Deduct down payments* to subtract the down payments already
           invoiced;

      * *Down payment (percentage)* or *Down payment (fixed amount)*: an
        advance on the order total, deducted later from the regular invoice.

   #. Press :version:`10-12|**Create and View Invoices**;13-16|**Create and
      View Invoice**;17|**Create Draft Invoice**;*|**Create Draft**`: the new
      invoice opens as a draft, with the order number as *Source Document*.
   #. Check the invoice and confirm it, as described in *How to insert a new
      record*.

   Several orders are invoiced at once from the list of the orders: select
   them and choose :version:`10|**Invoice Orders**;11-12|**Invoice
   Order**;13-17|**Create invoices**;*|**Create invoice(s)**` in the
   :version:`<17|**Action**;*|**Actions** (gear icon)` menu.
   :version:`>=17|*Consolidated Billing* makes one invoice for the orders of
   the same customer and invoice address.`

   The invoice is linked to the order: the **Invoices** button of the order
   opens its invoices, and cancelling or deleting a draft invoice makes its
   quantities invoiceable again.
