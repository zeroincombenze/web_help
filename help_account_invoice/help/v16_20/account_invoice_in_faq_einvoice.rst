.. help-if:: module = l10n_it_edi

   .. help-question:: Why does Odoo stop receiving the e-invoices and the notifications?

      The scheduled action *IT EDI: Receive invoices from the SdI* is
      disabled or in error. In developer mode open **Settings ‣ Technical ‣
      Automation ‣ Scheduled Actions** and activate it again. If it happens
      again, call the support.

   .. help-question:: Why does an imported vendor bill have lines without tax ("Tax not found")?

      No purchase tax has the rate and the nature of the XML (e.g. 0%
      *N6.3*, *N6.7*, *N7*): Odoo logs *Tax not found for line* in the
      chatter of the bill. Create the purchase tax with that rate and
      *Exoneration*, then set it on the lines, or delete the bill and import
      it again.

   .. help-question:: Why is the vendor bill assigned to the wrong vendor, or to a new one?

      Odoo looks for the vendor by VAT number and fiscal code; when none
      matches it creates a new contact and writes *Could not retrieve a
      partner* in the chatter. Correct VAT number and fiscal code of the
      right contact, archive the wrong one, then delete the bill and import
      it again.

   .. help-question:: Why are vendor bills duplicated, or why isn't an e-invoice imported again?

      Odoo skips an e-invoice received from the SdI when a file with the same
      name is already imported. A copy entered by hand is not recognized:
      delete it and keep the imported bill.

   .. help-question:: How do I import an e-invoice received by PEC or in a ZIP?

      In **Invoicing ‣ Vendors ‣ Bills** press [`Upload`] and choose the file
      *IT...xml* (or *.xml.p7m*) of the bill, not the metadata file *_MT_*.

      .. help-if:: module = l10n_it_edi_extension

         For a ZIP file use **Invoicing ‣ Vendors ‣ E-invoice Import Files**,
         see *Report and export file*.

   .. help-question:: How do I delete a vendor bill imported from XML to import it again?

      Reset the bill to draft and delete it; then upload the XML again.

   .. help-question:: Why doesn't the XML of the vendor import (EORI used as destination code, missing data)?

      The vendor filled the XML wrong: ask the vendor for a corrected one;
      otherwise the support can correct the XML file before the import.

.. help-if:: module = rectify_negative_refund

   .. help-question:: How do I correct a negative invoice or credit note (e.g. a foreign credit note become a negative TD17)?

      The document was entered with the wrong type: a negative invoice
      instead of a credit note, or the other way round. Open it and press
      [`Rectify`] at the top: it becomes the right type, with positive
      amounts.
