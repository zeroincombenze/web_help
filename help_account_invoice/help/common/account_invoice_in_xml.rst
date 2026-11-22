.. help-version:: 18

   .. help-if:: module = l10n_it_edi

      .. _new_from_xml:

      How to create invoice from xml
      ------------------------------

      A vendor e-invoice (FatturaPA, file *.xml* or *.xml.p7m*) is loaded
      instead of typing the bill: Odoo reads the file and creates a draft
      vendor bill with the data of the vendor.

      #. Open **Invoicing ‣ Vendors ‣ Bills** and press [`Upload`] (or drop the
         file on the list), or press [`Upload`] on the card of the purchase
         journal in the Accounting Dashboard. Choose the file received from the
         vendor, the *IT...xml* (or *.xml.p7m*) one, not the metadata file
         *_MT_*. Several files create several bills.
      #. The bill is created in the purchase journal of the card, or in the
         first purchase journal of the company when the button is the one of
         the list. One file opens its bill, more files open the list of the
         generated documents.
      #. Check the draft bill, described below, then press [`Confirm`].

      Odoo also creates the bills by itself when it receives the e-invoices
      from the SdI (scheduled action *IT EDI: Receive invoices from the SdI*):
      they are found in the same list, in draft.

      What Odoo fills in:

      * the :field:`vendor <partner_id>`: searched by Fiscal Code, then by VAT
        number, name, phone and email; when it is not found a new contact is
        created and the chatter says *Could not retrieve a partner
        corresponding to ...*;
      * the :field:`bill reference <ref>` (the number of the document), the
        :field:`bill date <invoice_date>`, the currency when it is not the one
        of the company, the stamp duty, the reasons as :field:`terms and
        conditions <narration>` and the order references as
        :field:`source document <invoice_origin>`;
      * the lines of the document, with the taxes found by rate and nature (a
        line without tax is logged in the chatter as *Tax not found for
        line ...*);
      * the :field:`due date <invoice_date_due>` (the latest of the payment
        deadlines of the file, without payment terms), the payment reference
        and the bank account (IBAN) of the vendor;
      * the type of the document: invoices, credit notes (*TD04*) and the other
        types known by Odoo become the right type of bill; an unknown type
        becomes a vendor bill;
      * orders, contracts, delivery notes and the attachments of the XML are
        written in the chatter; the XML file stays attached to the bill, in the
        **Electronic Invoicing** tab.

      .. help-if:: module = l10n_it_edi_withholding

         The withholding tax of the document is imported as a withholding tax
         on the lines: check the amounts.

      .. help-if:: module = l10n_it_edi_extension

         With *Italy - E-invoicing - Base Feature* a ZIP file with several
         e-invoices is loaded from **Invoicing ‣ Vendors ‣ E-invoice Import
         Files** (see *Report and export file*). In addition:

         * the detail of the lines depends on the *E-bills import detail level*
           (**Invoicing ‣ Configuration ‣ Settings**, or the setting of the
           vendor): *Minimum* creates the bill with no lines, *Tax rate* one
           line for each tax rate, *Maximum* (default) every line of the file;
         * the data of the vendor (province, EORI, registers...) update the
           contact, unless *Do not update the contact from Electronic Invoice
           Details* is set on it;
         * a blue message at the top of the bill warns when the untaxed
           amount, the tax or the total of the file differ from the ones of the
           bill; the **E-Invoice Details** tab shows the amounts of the file and
           *Imported Electronic Bill* with its [`Preview`].

      Before pressing [`Confirm`] check:

      * the vendor (a new contact? the right one?), the bill reference and date;
      * the totals against the document and the taxes of the lines, in
        particular the zero-rate lines;
      * the due date and the bank account;
      * the warning *Warning: this document might be a duplicate of ...* at the
        top of the bill: same vendor, reference, date and total. Odoo also
        refuses a file whose name was already received from the SdI, and the
        ZIP import stops with *E-invoice already exists*; the [`Upload`] button
        does not check the file name.

      Common errors: if the company VAT number and Fiscal Code are not in the
      buyer section of the file, nothing is imported and the chatter says *Your
      company's VAT number and Fiscal Code haven't been found in the buyer
      and/or seller sections inside the document*: the file is for another
      company. A file that is not a FatturaPA stays attached to an empty draft
      bill. For the other cases (tax not found, wrong vendor, duplicates, the
      file that does not import) see the **FAQ**.
