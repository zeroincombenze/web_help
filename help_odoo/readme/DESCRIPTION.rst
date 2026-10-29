Meta module: installing it installs web_context_help and all the help modules,
with their context help pages in English and Italian:

* **help_account_invoice**: customer invoices and vendor bills
* **help_payment_term**: payment terms
* **help_product**: products and product variants
* **help_purchase_order**: requests for quotation and purchase orders
* **help_res_partner**: contacts (partners)
* **help_sale_order**: quotations and sale orders

The module has no code nor data of its own. Each help module also installs
the Odoo application it explains (Invoicing, Sales, Purchases).
