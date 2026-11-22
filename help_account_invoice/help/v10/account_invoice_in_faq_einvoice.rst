.. help-if:: module = l10n_it_einvoice_in

   .. help-question:: Why can't I validate a vendor bill imported from XML: "total and tax differ from e-invoice"?

      The totals of the bill do not match the XML: discounts on the header
      and on the lines, discounted stamp duty, reverse charge on some lines,
      roundings of the vendor. If the bill in Odoo is correct: **Edit**, tab
      **E-bill Inconsistencies**, check :field:`Force E-Invoice Validation
      <e_invoice_force_validation>`, **Save** and **Validate**.

   .. help-question:: Why is a vendor bill 1 cent different, and does not import or validate?

      The XML of the vendor holds roundings, and the rounding accounts are
      missing (often after an update). In **Invoicing ‣ Configuration ‣
      Settings**, section **Electronic Invoice**, set *Active Rounding
      Account*, *Passive Rounding Account* and *Rounding Tax*; then add a
      rounding line to the bill, or import the XML again.

   .. help-question:: Why do I get "No tax with rate X and nature Y" when importing the XML?

      No purchase tax has that rate and nature (e.g. 0% *N6.3*, *N6.7*,
      *N7*), or more taxes have it and the first one is the wrong one. Create
      the purchase tax with rate, nature and, for reverse charge, its reverse
      charge type; with more taxes change their sequence to put the right one
      first. Check also the default purchase tax in the settings.

   .. help-question:: Why do I get "duplicated REA code", or why did the company lose its REA code?

      A self-invoice to the company itself (TD17, TD20...) comes back from the
      SdI with the company as vendor: the import gives the REA to another
      contact and removes it from the company. Write the REA again in
      **Invoicing ‣ Configuration ‣ Settings**, section **Electronic
      Invoice**, and remove it from the duplicated vendor. Do not import the
      returned self-invoice: link it to the original one. Updated software
      (2024) fixes the problem.

   .. help-question:: Why are the vendor bills not imported after the company VAT number changed to EU...?

      Importing a self-invoice added the prefix *EU* to the VAT number of the
      company. Correct the VAT number (*IT...*) of the company, then import or
      link the bills again.

   .. help-question:: Why is the vendor bill assigned to the wrong vendor?

      The vendor is an address under another contact, has a similar name, or
      its VAT number is wrong. Correct VAT number and fiscal code of the right
      contact, detach it from the wrong parent, then delete the bill and
      import it again.

   .. help-question:: Why are vendor bills duplicated, or do I get "file already imported"?

      The same file cannot be imported twice. The bill was entered by hand
      and then downloaded from the SdI, or the channel sent the same bill
      signed (*.xml.p7m*) and not signed (*.xml*): delete the copy entered by
      hand. Since 2025 the software knows that *.xml* and *.xml.p7m* are the
      same bill.

   .. help-question:: How do I import an e-invoice received by PEC or in a ZIP?

      In **Invoicing ‣ Purchases ‣ Electronic Bill ‣ Incoming E-bill Files**
      upload the file *IT...xml* (or *.xml.p7m*) of the bill, not the metadata
      file *_MT_*.

      .. help-if:: module = l10n_it_einvoice_import_zip

         For a ZIP file use **Invoicing ‣ Purchases ‣ Electronic Bill ‣
         Import eInvoice from ZIP**.

   .. help-question:: How do I delete a vendor bill imported from XML to import it again?

      Cancel the bill, reset it to draft and delete it; then create the bill
      again from its incoming e-bill file.

   .. help-question:: Why doesn't the XML of the vendor import (EORI used as recipient code, missing data)?

      The vendor filled the XML wrong: ask the vendor for a corrected one;
      otherwise the support can correct the XML file before the import.

.. help-if:: module = rectify_negative_refund

   .. help-question:: How do I correct a negative invoice or credit note (e.g. a foreign credit note become a negative TD17)?

      The document was entered with the wrong type: a negative invoice
      instead of a credit note, or the other way round. Open it and press
      **Rectify** at the top: it becomes the right type, with positive
      amounts.
