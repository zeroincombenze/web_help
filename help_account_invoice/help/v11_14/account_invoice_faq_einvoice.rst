.. help-if:: module = l10n_it_fatturapa_out

   .. help-question:: E-invoice to a foreign customer: why does the export stop on the ZIP?

      The Italian address data are skipped only when the customer has the
      :field:`Addressee Code <codice_destinatario>` *XXXXXXX* (seven capital
      X): the XML then gets ZIP *00000* and province *EE*. With *0000000* or
      a lowercase *xxxxxxx* the export stops with *Customer ZIP not set*. In
      the customer form, tab **Electronic Invoice**, set *XXXXXXX*, then
      export the e-invoice again.

   .. help-question:: Why is the ZIP of an Italian customer refused?

      The ZIP must have exactly 5 digits, with no space before or after it.
      Correct it in the address of the customer and export the e-invoice
      again.

   .. help-question:: Why is the VAT number of a foreign customer refused?

      The VAT number must start with the ISO code of the country (*ES*, *DE*,
      *CH*...) with no space, e.g. *ESB02876001*. Check that the prefix is the
      one of the country (e.g. *CH*, not *IT*, for a Swiss customer); for
      France write *FR* and the 11 digits that follow. A EU VAT number must be
      valid on VIES. For Switzerland add *MWST* or *TVA* after a space.

   .. help-question:: Non-EU customer without VAT number (Japan, United Kingdom...): how do I invoice it?

      Do not write a dummy VAT number: leave both VAT number and fiscal code
      empty and set the Addressee Code *XXXXXXX*. For a foreign customer Odoo
      fills the XML with the country code and a conventional identifier,
      which the SdI accepts.

   .. help-question:: How do I invoice a foreign private person?

      Do not write a numeric foreign fiscal code: the SdI refuses it. For a
      foreign person with an Italian fiscal code set the Addressee Code
      *XXXXXXX* and the correct Italian fiscal code.

   .. help-question:: Why is the button Export E-invoice missing?

      The button appears on validated invoices of customers having *Enable
      electronic invoicing* checked, in the **Electronic Invoice** tab of the
      customer. Check it and verify the Addressee Code or the *Addressee PEC*.
      When the e-invoice was already exported, use its file instead.

      .. help-if:: module = universal_connector

         If the customer comes from VG7 correct it on VG7 too, otherwise the
         next synchronization clears the flag again.

   .. help-question:: Why is the e-invoice refused for the Addressee Code?

      The Addressee Code must have 7 letters or digits (e.g. *G4A/1U8* is not
      valid), otherwise Odoo stops with *Addressee Code must be 7 characters
      long*. Without a code and without a PEC the SdI cannot deliver the
      invoice: write a valid code, or *0000000* and the PEC. With no data at
      all use *0000000*: the invoice stays in the tax drawer (*cassetto
      fiscale*) of the customer.

   .. help-question:: Why are the payment data missing in the e-invoice?

      Odoo stops with *Payment term ... does not have a linked e-invoice
      payment term* (or *payment method*). In **Invoicing ‣ Configuration ‣
      Management ‣ Payment Terms** set *Fiscal Payment Term* and *Fiscal
      Payment Method* (*MPxx*) on the term.

   .. help-question:: Why does the e-invoice show a tax amount 1 or 2 cents different, and gets refused?

      By default Odoo computes the tax line by line and then adds them up:
      the total may differ from the tax computed on the total untaxed amount
      (e.g. 27.96 at 22% gives 6.14 instead of 6.15). In **Invoicing ‣
      Configuration ‣ Settings**, *Rounding Method*, choose *Round globally
      calculation of taxes*, as Italian law requires.

   .. help-question:: Why is the e-invoice refused for the nature of a tax (N2, N3, N6...)?

      Since 2021 the natures N2, N3 and N6 are split (N3.1 ... N3.6, N6.1 ...
      N6.9). In **Invoicing ‣ Configuration ‣ Accounting ‣ Taxes** set the
      right *Exemption Kind* (e.g. art. 9 is *N3.4*, art. 10 is *N4*) and the
      *Law reference* of the tax.

   .. help-question:: Why does the channel refuse the e-invoice for invalid characters?

      The description holds control characters copied from other programs.
      Write the description of the line again, by hand, then export and send
      the e-invoice again.

   .. help-if:: module = l10n_it_withholding_tax

      .. help-question:: How do I issue an invoice with withholding tax?

         Create the withholding tax in **Invoicing ‣ Configuration ‣
         Accounting ‣ Withholding Tax**, with type, rate and payment reason,
         then set it on the invoice lines. Use a valid payment reason: *Z* is
         no longer accepted, use *ZO*.

   .. help-question:: How do I write CIG, CUP, order or contract in the e-invoice?

      In the invoice, tab **Related Documents**, add the purchase order or the
      contract with its CIG and CUP: a PA refuses the invoice without the CIG.

   .. help-question:: Why does the invoice show the wrong bank or IBAN?

      The IBAN comes from the *Bank Account* of the invoice: with several
      company banks Odoo proposes the first one. Choose the right one on the
      invoice, before validating it.

      .. help-if:: module = assigned_bank

         To give each customer or vendor its own company bank, set it in the
         **Accounting** tab of the contact.

   .. help-if:: module = l10n_it_fiscal_document_type

      .. help-question:: Why is the document type TD24 (deferred invoice) not set?

         The invoices created from delivery notes get *TD24*; an invoice
         made by hand, or changed afterwards, may keep *TD01*. Check the
         *Fiscal Document Type* before validating the invoice. If a type,
         e.g. *TD29*, is not in the list, the software must be updated.

   .. help-question:: Why can't the province or the country be found?

      The province does not exist with that code (e.g. *PS* for Pesaro e
      Urbino), or the country has another name (e.g. *Olanda* instead of
      *Paesi Bassi*). Search the country by its other name; add the missing
      province in developer mode, in **Contacts ‣ Configuration ‣
      Localization ‣ Fed. States**.

.. help-if:: module = l10n_it_ipa

   .. help-question:: Why is the invoice to a Public Administration refused, or sent as an invoice to private persons?

      The customer is set as a private company (Addressee Code of 7
      characters) instead of a PA. In the customer form check *Public
      administration* and write the 6 characters *IPA Code*. Delete the
      refused e-invoice and export it again.

      .. help-if:: module = universal_connector

         If the customer comes from VG7 correct it on VG7 too, otherwise the
         next synchronization writes the old data again.

.. help-if:: module = l10n_it_efattura_sdi

   .. help-question:: The e-invoice was sent: why is it missing in the tax drawer, or why does its state not change?

      The state comes from the notifications of the SdI, passed on by the
      channel. The invoices to a PA notify only the delivery; sometimes the
      notification is late or missing.

      1. Check on the portal of the channel the real state and the receipts.
      2. In **Invoicing ‣ Customers ‣ Electronic Invoice ‣ E-invoice Export
         Files** open the file and press **Check invoice state on SDI**.
      3. If the state is still wrong, open a ticket with the channel.

      To prove the delivery to the customer download from the channel the
      XML, the PDF and the receipt.

   .. help-question:: Why does the scheduler stop sending the e-invoices?

      The scheduled action is disabled or in error. In developer mode open
      **Settings ‣ Technical ‣ Automation ‣ Scheduled Actions** and activate
      again the action that sends and receives the e-invoices. If it happens
      again, call the support.

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
