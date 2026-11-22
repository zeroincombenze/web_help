.. _fields:

Main fields
~~~~~~~~~~~

.. help-version:: <13

   * :field:`Vendor <partner_id>`: it proposes the payment terms, the fiscal
     position and the :field:`payable account <account_id>`.
   * :field:`Vendor reference <reference>`: the number written by the vendor
     on the bill.
   * :field:`Bill date <date_invoice>`: empty means the validation date.
     :field:`Accounting date <date>` books the bill in another period.
   * :field:`Payment terms <payment_term_id>` or :field:`due date <date_due>`:
     with payment terms the due dates are computed, otherwise write the due
     date.
   * :field:`Journal <journal_id>`: the purchase journal, which gives the
     number sequence.
   * :field:`Source document <origin>`: the document that generated the bill,
     e.g. the purchase order.
   * :field:`Fiscal position <fiscal_position_id>`: maps taxes and accounts,
     e.g. for foreign vendors.
   * :field:`Currency <currency_id>` (*Multi-Currencies* setting).
   * :field:`Additional information <comment>`: free text.

   .. help-version:: >=11

      :field:`Cash rounding method <cash_rounding_id>` (*Cash Rounding*
      setting) rounds the total, e.g. to 0.05.

.. help-version:: >=13

   * :field:`Vendor <partner_id>`: it proposes the payment terms and the
     fiscal position.
   * :field:`Bill reference <ref>`: the number written by the vendor on the
     bill.
   * :field:`Bill date <invoice_date>`: the date written by the vendor, required.
     :field:`Accounting date <date>` books the bill in another period.
   * :field:`Payment terms <invoice_payment_term_id>` or :field:`due date
     <invoice_date_due>`: with payment terms the due dates are computed,
     otherwise write the due date.
   * :field:`Journal <journal_id>` and :field:`currency <currency_id>`: shown
     when there are several purchase journals, or several currencies.
   * :field:`Source document <invoice_origin>`: the document that generated
     the bill, e.g. the purchase order.
   * :field:`Fiscal position <fiscal_position_id>`: maps taxes and accounts,
     e.g. for foreign vendors.
   * :field:`Cash rounding method <invoice_cash_rounding_id>` (*Cash Rounding*
     setting): rounds the total, e.g. to 0.05.
   * :field:`Terms and conditions <narration>`: free text.

   .. help-version:: 13

      :field:`Payment reference <invoice_payment_ref>` is the reference to write
      on the payment to the vendor; :field:`bank account
      <invoice_partner_bank_id>` is the vendor account where you pay.

   .. help-version:: >=14

      :field:`Payment reference <payment_reference>` is the reference to write
      on the payment to the vendor; :field:`recipient bank <partner_bank_id>`
      is the vendor account where you pay.
