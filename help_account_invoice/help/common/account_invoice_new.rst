.. _new_record:

New record
----------

.. help-version:: <13

   #. Open :version:`<12|**Invoicing ‣ Sales ‣ Customer Invoices**;*|**Invoicing
      ‣ Customers ‣ Invoices**` and press **Create**. For a vendor bill open
      :version:`<12|**Invoicing ‣ Purchases ‣ Vendor Bills**;*|**Invoicing ‣
      Vendors ‣ Bills**`. Invoices are also created from the sale orders
      (**Create Invoice**) and the purchase orders.
   #. Choose the :field:`customer <partner_id>` (required): Odoo fills in the
      :field:`payment terms <payment_term_id>` and the :field:`fiscal position
      <fiscal_position_id>` from the customer; change them if needed.
   #. Write the :field:`invoice date <date_invoice>`, or leave it empty to use
      the validation date. Without payment terms, write the :field:`due date
      <date_due>`. On a bill write the :field:`vendor reference <reference>`.
   #. In the **Invoice Lines** tab press :version:`<12|**Add an item**;*|**Add
      a line**`, pick the product and set the quantity: description, account,
      price and taxes are proposed and can be changed. A line without product
      needs a description and an account.
   #. Check the totals under the lines and write the :field:`additional
      information <comment>` printed on the invoice, if any.
   #. Complete the **Other Info** tab: :field:`salesperson <user_id>`,
      :field:`journal <journal_id>`, :field:`source document <origin>`.
   #. Press **Save**.
      :version:`10|**PRO-FORMA** (*Allow pro-forma invoices* setting) marks the
      draft as a pro-forma to send to the customer.`
   #. Press **Validate**: Odoo assigns the :field:`number <number>`, writes the
      journal entry and the status becomes *Open*. Odoo refuses to validate an
      invoice with a total below zero: create a
      :version:`10|refund;*|credit note` instead.
   #. Press :version:`<12|**Send by Email**;*|**Send & Print**` to send the
      invoice with its PDF to the customer.

.. help-version:: >=13

   #. Open **Invoicing ‣ Customers ‣ Invoices** and press
      :version:`<17|**Create**;*|**New**`. For a vendor bill open **Invoicing ‣
      Vendors ‣ Bills**\ :version:`>=17|, or press **Upload** to create the
      bill from its PDF`. Invoices are also created from the sale orders
      (**Create Invoice**) and the purchase orders (**Create Bill**).
   #. Choose the :field:`customer <partner_id>` (required): Odoo fills in the
      :field:`payment terms <invoice_payment_term_id>` and the
      :field:`fiscal position <fiscal_position_id>` from the customer; change
      them if needed.
   #. Write the :field:`invoice date <invoice_date>`, or leave it empty to use
      the confirmation date (on a bill it is required). Without payment terms,
      write the :field:`due date <invoice_date_due>`. On a bill write the
      :field:`bill reference <ref>`.
   #. In the **Invoice Lines** tab press **Add a line**, pick the product and
      set the quantity: description, account, price and taxes are proposed and
      can be changed. **Add a section** and **Add a note** organise the
      lines.
      :version:`>=18|**Catalog** adds several products at once.`
   #. Check the totals under the lines and write the :field:`terms and
      conditions <narration>`, if any.
   #. Complete the **Other Info** tab: :field:`customer reference <ref>`,
      :field:`salesperson <invoice_user_id>`, :field:`fiscal position
      <fiscal_position_id>`, :field:`Incoterm <invoice_incoterm_id>`.
   #. :version:`<17|Press **Save**.;*|The record is saved automatically when
      you leave it, or at once with the cloud icon next to the breadcrumb.`
   #. Press :version:`13|**Post**;*|**Confirm**`: Odoo assigns the
      :field:`number <name>` from the sequence of the journal and the status
      becomes *Posted*. Odoo refuses to confirm an invoice with a total below
      zero: create a credit note instead.
   #. Press :version:`<18|**Send & Print**;*|**Send**` to send the invoice with
      its PDF to the customer.
