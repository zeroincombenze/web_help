.. _configure:

How to set up
-------------

.. help-version:: <13

   **Invoicing ‣ Configuration ‣ Settings**:

   * *Default Taxes* proposed on the lines (the purchase tax), and the
     *Rounding Method* of the taxes (per line or globally).
   * *Multi-Currencies*: bills in foreign currencies.
   * *Warnings*: a message shown when a partner or a product is chosen.

   Other menus:

   * **Invoicing ‣ Configuration ‣ Management ‣ Payment Terms**: the due
     dates, e.g. *30 days end of month* or 30% now and 70% in 60 days.
   * **Invoicing ‣ Configuration ‣ Accounting ‣ Journals**: the purchase
     journals and their number sequence. *Allow Cancelling Entries*
     (module *Cancel Journal Entries*) enables
     :version:`<12|[\`Cancel Invoice\`];*|[\`Cancel\`]` on the validated bills.
   * **Invoicing ‣ Configuration ‣ Accounting ‣ Taxes** and **Fiscal
     Positions**.
   * On the vendor, **Sales & Purchases** tab: the payment terms and the
     fiscal position proposed on the bills; **Invoicing** tab, for the
     accountants: the payable account.

.. help-version:: >=13

   **Invoicing ‣ Configuration ‣ Settings**:

   * *Default Taxes* proposed on the lines (the purchase tax), and the
     *Rounding Method* of the taxes (per line or globally).
   * *Currencies*: bills in foreign currencies.
   * *Vendor Bills* and *Vendor Payments*: the options to receive and to pay
     the vendor bills (for example the checks and the SEPA payments).

   .. help-version:: >=18

      In *Vendor Bills*, *Auto-post bills*: after three bills of a vendor
      imported without changes, Odoo suggests confirming the next ones
      automatically; the feature can be switched off in the profile of each
      vendor.

   Other menus:

   * **Invoicing ‣ Configuration ‣ Invoicing ‣ Payment Terms**: the due dates,
     e.g. *30 days end of month* or 30% now and 70% in 60 days.
   * **Invoicing ‣ Configuration ‣ Accounting ‣ Journals**: the purchase
     journals and their number sequence;
     :version:`<18|*Lock Posted Entries with Hash*;*|*Secure Posted Entries
     with Hash*` secures the posted bills, which can no longer be reset to
     draft.
   * **Invoicing ‣ Configuration ‣ Accounting ‣ Taxes** and **Fiscal
     Positions**.
   * On the vendor, **Invoicing** tab (*Accounting* tab for an accountant):
     the vendor payment terms, the fiscal position and the payable account
     proposed on the bills.
