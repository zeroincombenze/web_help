.. _new_record:

How to insert a new record
--------------------------

.. help-version:: <13

   #. Open :version:`<12|**Invoicing ‣ Purchases ‣ Vendor Bills**;*|**Invoicing
      ‣ Vendors ‣ Bills**` and press [`Create`].
   #. Choose the :field:`vendor <partner_id>` (required): Odoo fills in the
      :field:`payment terms <payment_term_id>` and the :field:`fiscal position
      <fiscal_position_id>` from the vendor; change them if needed.
   #. Write the :field:`vendor reference <reference>`, the number written by the
      vendor on its bill, and the :field:`bill date <date_invoice>`, or leave
      it empty to use the validation date. Without payment terms, write the
      :field:`due date <date_due>`.
   #. In the **Bill** tab press :version:`<12|[\`Add an item\`];*|[\`Add
      a line\`]`, pick the product and set the quantity: description, account,
      price and purchase taxes are proposed and can be changed. A line without
      product needs a description and an account.
   #. Check the totals under the lines against the paper bill and write the
      :field:`additional information <comment>`, if any.
   #. Complete the **Other Info** tab: :field:`journal <journal_id>` and, if
      needed, the :field:`accounting date <date>`. The :field:`source document
      <origin>` is written by the document that generates the bill, e.g. the
      purchase order, and is shown only when filled in.
   #. Press [`Save`].
   #. Press [`Validate`]: Odoo assigns the :field:`number <number>`, writes the
      journal entry and the status becomes *Open*. :version:`10|Odoo 10.0 does
      not stop a bill with a total below zero, but do not validate it: create a
      refund instead.;*|Odoo refuses to validate a bill with a total below
      zero: create a credit note instead.`
   #. To pay it, see *Other actions*.

.. help-version:: >=13

   #. Open **Invoicing ‣ Vendors ‣ Bills** and press
      :version:`<17|[\`Create\`];*|[\`New\`]`\ :version:`>=17|, or press
      [\`Upload\`] to create the bill from the PDF sent by the vendor`.

      .. help-if:: module = purchase

         The bills are also created from the purchase orders, see *Invoice from
         supplier order*.

   #. Choose the :field:`vendor <partner_id>` (required): Odoo fills in the
      :field:`payment terms <invoice_payment_term_id>` and the
      :field:`fiscal position <fiscal_position_id>` from the vendor; change
      them if needed.
   #. Write the :field:`bill reference <ref>`, the number written by the vendor
      on its bill, and the :field:`bill date <invoice_date>` (required).
      Without payment terms, write the :field:`due date <invoice_date_due>`.
      The :field:`accounting date <date>` books the bill in another period.

      .. help-version:: 13

         The :field:`payment reference <invoice_payment_ref>` is the reference
         to write on the payment; :field:`bank account
         <invoice_partner_bank_id>` is the vendor account where you pay.

      .. help-version:: >=14

         The :field:`payment reference <payment_reference>` is the reference
         to write on the payment; the :field:`recipient bank <partner_bank_id>`
         is the vendor account where you pay.

   #. In the **Invoice Lines** tab press [`Add a line`], pick the product and
      set the quantity: description, account, price and purchase taxes are
      proposed and can be changed. [`Add a section`] and [`Add a note`]
      organise the lines.
      :version:`>=18|**Catalog** adds several products at once.`
   #. Check the totals under the lines against the paper bill and write the
      :field:`terms and conditions <narration>`, if any.
   #. Complete the **Other Info** tab: :field:`fiscal position
      <fiscal_position_id>` and, if needed, the other fields of the tab.
   #. :version:`<17|Press [\`Save\`].;*|The record is saved automatically when
      you leave it, or at once with the cloud icon next to the breadcrumb.`
   #. Press :version:`13|[\`Post\`];*|[\`Confirm\`]`: Odoo assigns the
      :field:`number <name>` from the sequence of the journal and the status
      becomes *Posted*. Odoo refuses to confirm a bill with a total below zero:
      create a credit note instead.
   #. To pay it, see *Other actions*.
