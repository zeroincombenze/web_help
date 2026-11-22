.. help-if:: module = l10n_it_fatturapa_in

   .. help-question:: Why can't I validate a vendor bill imported from XML: the totals differ from the e-invoice?

      The totals of the bill do not match the XML: discounts on the header
      and on the lines, discounted stamp duty, reverse charge on some lines,
      roundings of the vendor. If the bill in Odoo is correct: **Edit**, tab
      **E-bill Inconsistencies**, check :field:`Force E-Invoice Validation
      <e_invoice_force_validation>`, **Save** and **Validate**.

   .. help-question:: Why is a vendor bill 1 cent different, and does not import or validate?

      The XML of the vendor holds roundings, and the rounding accounts are
      missing. In **Invoicing ‣ Configuration ‣ Settings**, section
      **Electronic Invoices**, set *Round Up Account*, *Round Down Account*
      and *Rounding Tax*; then import the XML again.

   .. help-question:: Why do I get "No tax with percentage X and nature Y found" when importing the XML?

      No purchase tax has that rate and nature (e.g. 0% *N6.3*, *N6.7*,
      *N7*), or more taxes have it and the one chosen is the wrong one.
      Create the purchase tax with rate and *Exemption Kind*; with more taxes
      change their sequence to put the right one first.

   .. help-question:: Why is the vendor bill assigned to the wrong vendor?

      The vendor is an address under another contact, has a similar name, or
      its VAT number is wrong. Correct VAT number and fiscal code of the right
      contact, detach it from the wrong parent, then delete the bill and
      import it again.

   .. help-question:: Why are vendor bills duplicated, or do I get "The name of the e-bill file must be unique"?

      The same file cannot be imported twice. If the bill was entered by hand
      and then downloaded from the SdI, delete the copy entered by hand.

   .. help-question:: How do I import an e-invoice received by PEC or in a ZIP?

      In **Invoicing ‣ Vendors ‣ Electronic Bill ‣ Incoming E-bill Files**
      upload the file *IT...xml* (or *.xml.p7m*) of the bill, not the metadata
      file *_MT_*.

      .. help-if:: module = l10n_it_einvoice_import_zip

         For a ZIP file use **Invoicing ‣ Vendors ‣ Electronic Bill ‣ Import
         eInvoice from ZIP**.

   .. help-question:: How do I delete a vendor bill imported from XML to import it again?

      Cancel the bill, reset it to draft and delete it; then create the bill
      again from its incoming e-bill file.

   .. help-question:: Why doesn't the XML of the vendor import (EORI used as addressee code, missing data)?

      The vendor filled the XML wrong: ask the vendor for a corrected one;
      otherwise the support can correct the XML file before the import.
