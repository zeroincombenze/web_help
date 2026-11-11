.. help-if:: module = l10n_it_edi

   .. help-question:: E-invoice to a foreign customer: which Destination Code must I set?

      None: for a customer whose country is not Italy Odoo writes by itself
      the Destination Code *XXXXXXX* and the ZIP *00000* in the XML (for San
      Marino the fixed code of the country). Just check that the
      :field:`country <country_id>` of the customer is set.

   .. help-question:: Why is the ZIP of an Italian customer refused?

      The ZIP must have exactly 5 digits, with no space before or after it.
      Correct it in the address of the customer, then send the invoice again.

   .. help-question:: Why is the VAT number of a foreign EU customer refused, or read as Italian?

      For a EU customer the VAT number must start with the ISO code of the
      country (*ES*, *DE*, *FR*...), e.g. *ESB02876001*: Odoo removes the
      prefix in the XML. A VAT number starting with digits is taken as
      Italian. Check that the prefix is the one of the country and that the
      number is valid on VIES.

   .. help-question:: Non-EU customer without VAT number (Japan, United Kingdom...): how do I invoice it?

      Leave the VAT number empty and set the country: Odoo writes the
      conventional value *OO99999999999* (*0000000* for a EU customer) that
      the SdI accepts. Do not write a dummy VAT number yourself.

   .. help-question:: How do I invoice a foreign private person?

      Do not write a numeric foreign fiscal code: the SdI refuses it, and a
      contact with a *Codice Fiscale* is taken as Italian. For a foreign
      person with an Italian fiscal code write the *Codice Fiscale* and the
      Italian address.

   .. help-question:: Why is the invoice to a Public Administration refused, or sent as an invoice to private persons?

      Odoo takes a customer as a PA when it is Italian and its
      :field:`Destination Code <l10n_it_pa_index>`, in the **Electronic
      Invoicing** tab of the contact, has 6 characters (the IPA code); 7
      characters mean a private company. Write the IPA code; then, in the
      **Electronic Invoicing** tab of the invoice, fill *Origin Document
      Type*, name and date (the order or contract of the PA), with CIG and
      CUP when required.

      .. help-if:: module = universal_connector

         If the customer comes from VG7 correct it on VG7 too, otherwise the
         next synchronization writes the old data again.

   .. help-question:: Why is the e-invoice refused for the Destination Code?

      The Destination Code must have 7 letters or digits for a company (6
      for a PA): e.g. *G4A/1U8* is not valid. Without a code Odoo writes
      *0000000*: the SdI delivers the invoice to the *PEC e-mail* of the
      contact if any, otherwise it stays in the tax drawer (*cassetto
      fiscale*) of the customer.

   .. help-question:: Why is the e-invoice with negative quantities refused?

      The SdI does not accept negative quantities. On the lines of a
      reversal or of a down payment write a positive quantity and a negative
      unit price; check that the down payment line has its tax too.

   .. help-question:: Why does the e-invoice show a tax amount 1 or 2 cents different, and gets refused?

      With rounding per line Odoo computes the tax line by line and then adds
      them up: the total may differ from the tax computed on the total
      untaxed amount (e.g. 27.96 at 22% gives 6.14 instead of 6.15). In
      **Invoicing ‣ Configuration ‣ Settings**, *Rounding Method*, choose
      *Round Globally*, as Italian law requires.

   .. help-question:: Why is the e-invoice refused for the nature of a tax (N2, N3, N6...)?

      A tax with rate 0% needs both the :field:`Exoneration
      <l10n_it_exempt_reason>` (the nature, e.g. art. 9 is *N3.4*, art. 10 is
      *N4*) and the *Law Reference*. In **Invoicing ‣ Configuration ‣ Taxes**
      open the tax and set them; the old natures N2, N3 and N6 are split since
      2021 (N3.1 ... N3.6, N6.1 ... N6.9).

   .. help-question:: Why does the channel refuse the e-invoice for invalid characters?

      The description holds control characters copied from other programs.
      Write the description of the line again, by hand, then send the
      invoice again.

   .. help-if:: module = l10n_it_edi_withholding

      .. help-question:: How do I issue an invoice with withholding tax?

         In **Invoicing ‣ Configuration ‣ Taxes** create a tax with
         *Withholding tax type (Italy)*, rate and *Withholding tax reason
         (Italy)*, then add it to the invoice lines next to the VAT. *Z* is
         deprecated: use *ZO*.

   .. help-question:: How do I write CIG, CUP, order or contract in the e-invoice?

      In the invoice, tab **Electronic Invoicing**, set *Origin Document
      Type* (purchase order, contract...), its name and date, then CIG and
      CUP: a PA refuses the invoice without the CIG.

   .. help-question:: Why does the invoice show the wrong bank or IBAN?

      The IBAN comes from the *Recipient Bank* of the invoice, in the **Other
      Info** tab: with several company banks Odoo proposes the first one.
      Choose the right one before confirming the invoice.

      .. help-if:: module = assigned_bank

         To give each customer or vendor its own company bank, set it in the
         **Invoicing** tab of the contact.

   .. help-if:: module = l10n_it_edi_ndd

      .. help-question:: How do I choose the document type (TD24, TD25...) or the payment method (MPxx)?

         Odoo proposes the *Document Type* from the kind of invoice, and
         payment method *MP05* (bank transfer). Before confirming the
         invoice change them in the **Electronic Invoicing** tab, e.g. *TD24*
         for a deferred invoice from delivery notes.

   .. help-question:: Why can't the province or the country be found?

      The province does not exist with that code (e.g. *PS* for Pesaro e
      Urbino), or the country has another name (e.g. *Olanda* instead of
      *Paesi Bassi*). Search the country by its other name; add the missing
      province in **Contacts ‣ Configuration ‣ Localization ‣ Fed. States**.

   .. help-question:: The e-invoice was sent: why is it missing in the tax drawer, or why does its state not change?

      The state of the invoice, in the **Electronic Invoicing** tab, comes
      from the notifications of the SdI: *SdI Processing*, then e.g. *SdI
      Accepted, Forwarded to Partner* or *SdI Rejected*. The invoices to a PA
      notify only the delivery and the outcome; sometimes the notification is
      late. Press **Check Sending** on the invoice to ask for the state now;
      if it is still wrong, open a ticket with the support.

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

      In **Invoicing ‣ Vendors ‣ Bills** press **Upload** and choose the file
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
      **Rectify** at the top: it becomes the right type, with positive
      amounts.
