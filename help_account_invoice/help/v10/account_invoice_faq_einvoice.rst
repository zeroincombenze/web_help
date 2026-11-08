.. help-if:: module = l10n_it_einvoice_base

   .. help-question:: E-invoice to a foreign customer: why does the XML stop on the ZIP or the province?

      The Italian checks on ZIP and province are skipped only when the
      customer has the :field:`Recipient Code <codice_destinatario>`
      *XXXXXXX* (seven capital X): *0000000* or a lowercase *xxxxxxx* do not
      work. In the customer form, tab **Electronic Invoice**, set *XXXXXXX*,
      then create the XML again.

   .. help-question:: Why is the ZIP of an Italian customer refused?

      The ZIP must have exactly 5 digits, with no space before or after it.
      Correct it in the address of the customer and create the e-invoice
      again.

   .. help-question:: Why is the VAT number of a foreign customer refused?

      The VAT number must start with the ISO code of the country (*ES*, *DE*,
      *CH*...) with no space, e.g. *ESB02876001*. Check that the prefix is the
      one of the country (e.g. *CH*, not *IT*, for a Swiss customer); for
      France write *FR* and the 11 digits that follow. A EU VAT number must be
      valid on VIES. For Switzerland add *MWST* or *TVA* after a space.

   .. help-question:: Non-EU customer without VAT number (Japan, United Kingdom...): how do I invoice it?

      Do not write a dummy VAT number (e.g. *OO99999999999*): leave the VAT
      number empty and set the Recipient Code *XXXXXXX*, Odoo fills the XML
      by itself. A foreign customer with an Italian VAT number needs an
      Italian address, or a foreign VAT number, or no VAT number at all.

   .. help-question:: How do I invoice a foreign private person?

      Do not write a numeric foreign fiscal code: the SdI refuses it. For a
      foreign person with an Italian fiscal code set the Recipient Code
      *XXXXXXX* and the correct Italian fiscal code.

   .. help-question:: Why is the invoice to a Public Administration refused, or sent as an invoice to private persons?

      The customer is set as a private company (Recipient Code of 7
      characters) instead of a PA. In the customer form check *Public
      administration* and write the 6 characters *IPA Code*. Delete the
      refused e-invoice and create it again.

      .. help-if:: module = universal_connector

         If the customer comes from VG7 correct it on VG7 too, otherwise the
         next synchronization writes the old data again.

   .. help-question:: Why do I get the error "not subjected to electronic invoice"?

      The customer does not have *Subjected to electronic invoice* checked,
      or it is a duplicate created without the e-invoice data. Check it and
      verify the Recipient Code or the *PEC destinatario*.

      .. help-if:: module = universal_connector

         If the customer comes from VG7 correct it on VG7 too, otherwise the
         next order clears the flag again.

   .. help-question:: Why is the e-invoice refused for the Recipient Code?

      The Recipient Code must have 7 letters or digits (e.g. *G4A/1U8* is not
      valid), otherwise the export stops with *Addressee Code must be 7
      characters long*. Without a code and without a PEC the SdI cannot
      deliver the invoice: write a valid code, or *0000000* and the PEC. With
      no data at all use *0000000*: the invoice stays in the tax drawer
      (*cassetto fiscale*) of the customer.

   .. help-question:: Why is the e-invoice with negative quantities refused?

      The SdI does not accept negative quantities. On the lines of a
      reversal or of a down payment write a positive quantity and a negative
      unit price; check that the down payment line has its tax too.

   .. help-question:: Why can't I send the e-invoice when the customer name is long?

      The SdI accepts 80 characters at most for the name of the company:
      shorten it in the customer form and create the XML again.

   .. help-question:: Why are the long notes of the e-invoice refused?

      Each line of the notes (*Causale*) can hold 200 characters at most:
      split the text on more lines.

   .. help-question:: Why is the payment term refused, or not printed, in the e-invoice?

      The description of the term may exceed 60 characters (the limit of the
      SdI) or hold just a space. In **Invoicing ‣ Configuration ‣ Payment
      Terms** shorten the description, set the payment method and the
      e-invoice data (*MPxx*) on each line, and keep a *Balance* line.

   .. help-question:: Why does the e-invoice show a tax amount 1 or 2 cents different, and gets refused?

      Odoo computes the tax line by line and then adds them up: the total may
      differ from the tax computed on the total untaxed amount (e.g. 27.96 at
      22% gives 6.14 instead of 6.15).

      .. help-if:: module = account_tax_rounded

         The module *account_tax_rounded* is installed: it computes the tax
         on the total, as Italian law requires. Mind that it gave troubles on
         the receipts with tax included.

      .. help-if:: module != account_tax_rounded

         Install the module *account_tax_rounded*: it computes the tax on the
         total, as Italian law requires.

   .. help-question:: Why is the tax refused for its nature (N2, N3, N6...)?

      Since 2021 the natures N2, N3 and N6 are split (N3.1 ... N3.6, N6.1 ...
      N6.9). In **Invoicing ‣ Configuration ‣ Taxes** set the right *Nature*
      (e.g. art. 9 is *N3.4*, art. 10 is *N4*) and the *Law reference* of the
      tax.

   .. help-question:: Why does the channel refuse the e-invoice for invalid characters?

      The description holds control characters copied from other programs.
      Write the description of the line again, by hand, then create and send
      the XML again.

   .. help-if:: module = l10n_it_withholding_tax

      .. help-question:: How do I issue an invoice with withholding tax?

         Create the withholding tax in **Invoicing ‣ Configuration ‣
         Accounting ‣ Withholding Tax**, with type, rate and payment reason,
         then set it on the invoice lines. Use a valid payment reason: *Z* is
         no longer accepted, use *ZO*.

   .. help-question:: How do I write CIG, CUP, order or contract in the e-invoice?

      In the invoice, tab **Related Documents**, add the purchase order or the
      contract with its CIG and CUP: a PA refuses the invoice without the CIG.
      The IBAN comes from the bank set on the invoice or on the payment term.

   .. help-question:: Why does the invoice show the wrong bank or IBAN?

      The company bank is missing on the company or on the customer; with
      several company banks Odoo takes the first one. Set the bank on the
      company.

      .. help-if:: module = assigned_bank

         To give each customer or vendor its own company bank, set it in the
         **Accounting** tab of the contact.

   .. help-question:: Why is the document type TD24 (deferred invoice) not set?

      The invoices from delivery notes must be *TD24*; a change of the
      invoice may bring the type back to *TD01*. Check the *Fiscal Document
      Type* before validating the invoice. If a type, e.g. *TD29*, is not in
      the list, the software must be updated.

   .. help-question:: Why can't the province or the country be found?

      The province does not exist with that code (e.g. *PS* for Pesaro e
      Urbino), or the country has another name (e.g. *Olanda* instead of
      *Paesi Bassi*). Search the country by its other name; add the missing
      province in developer mode, in **Sales ‣ Configuration ‣ Contacts ‣
      Localization ‣ Fed. States**.

.. help-if:: module = l10n_it_einvoice_send2sdi

   .. help-question:: The e-invoice was sent: why is it missing in the tax drawer, or why does its state not change?

      The state comes from the notifications of the SdI, passed on by the
      channel (Evolve, certdoc). The invoices to a PA notify only the
      delivery; sometimes the notification is late or missing.

      1. Check on certdoc the real state and the receipts.
      2. In the e-invoice file press **Verifica invio**.
      3. If the state is still wrong, open a ticket with the channel.

      To prove the delivery to the customer download from certdoc the ZIP
      with the XML, the PDF and the receipt.

   .. help-question:: Why does the scheduler stop sending the e-invoices?

      The scheduled action is disabled or in error. In developer mode open
      **Settings ‣ Technical ‣ Automation ‣ Scheduled Actions** and activate
      again the action that sends and receives the e-invoices. If it happens
      again, call the support.

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
