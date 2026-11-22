.. _fields:

Main fields
~~~~~~~~~~~

.. help-version:: <13

   * :field:`Customer <partner_id>`: it proposes the payment terms, the fiscal
     position and the :field:`receivable account <account_id>`.
   * :field:`Invoice date <date_invoice>`: empty means the validation date.
   * :field:`Payment terms <payment_term_id>` or :field:`due date <date_due>`:
     with payment terms the due dates are computed, otherwise write the due
     date.
   * :field:`Journal <journal_id>`: the sales journal, which gives the number
     sequence.
   * :field:`Salesperson <user_id>`: who follows the invoice, used in the
     reports.
   * :field:`Source document <origin>`: the document that generated the
     invoice, e.g. the sale order.
   * :field:`Fiscal position <fiscal_position_id>`: maps taxes and accounts,
     e.g. for foreign partners.
   * :field:`Currency <currency_id>` (*Multi-Currencies* setting).
   * :field:`Additional information <comment>`: free text printed on the
     invoice.

   .. help-version:: >=11

      :field:`Cash rounding method <cash_rounding_id>` (*Cash Rounding*
      setting) rounds the total, e.g. to 0.05.

   .. help-version:: 12

      :field:`Payment reference <reference>` is the
      reference the customer writes on the payment;
      :field:`bank account <partner_bank_id>` is the account where the
      customer pays; :field:`Incoterm <incoterm_id>` is the international
      commercial term.

.. help-version:: >=13

   * :field:`Customer <partner_id>`: it proposes the payment terms and the
     fiscal position.
   * :field:`Invoice date <invoice_date>`: empty means the confirmation date.
     :field:`Accounting date <date>` books the document in another period.
   * :field:`Payment terms <invoice_payment_term_id>` or :field:`due date
     <invoice_date_due>`: with payment terms the due dates are computed,
     otherwise write the due date.
   * :field:`Journal <journal_id>` and :field:`currency <currency_id>`: shown
     when there are several sales journals, or several currencies.
   * :field:`Customer reference <ref>`: the reference of the customer order.
   * :field:`Salesperson <invoice_user_id>`: who follows the invoice.
   * :field:`Source document <invoice_origin>`: the document that generated
     the invoice, e.g. the sale order.
   * :field:`Fiscal position <fiscal_position_id>`: maps taxes and accounts,
     e.g. for foreign partners.
   * :field:`Incoterm <invoice_incoterm_id>`: the international commercial
     term.
   * :field:`Cash rounding method <invoice_cash_rounding_id>` (*Cash Rounding*
     setting): rounds the total, e.g. to 0.05.
   * :field:`Terms and conditions <narration>`: free text printed under the
     lines.

   .. help-version:: 13

      :field:`Payment reference <invoice_payment_ref>` is the reference the
      customer writes on the payment; :field:`bank account
      <invoice_partner_bank_id>` is the account where the customer pays.

   .. help-version:: >=14

      :field:`Payment reference <payment_reference>` is the reference the
      customer writes on the payment; :field:`recipient bank <partner_bank_id>`
      is the account where the customer pays.

   .. help-version:: >=16

      :field:`Delivery address <partner_shipping_id>` (*Customer Addresses*
      setting) is the address where the goods are delivered.

   .. help-version:: >=17

      :field:`Delivery date <delivery_date>` is the date the goods were
      delivered, printed on the invoice when the law asks for it.
