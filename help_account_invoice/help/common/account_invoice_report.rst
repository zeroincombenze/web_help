.. _report:

Report and export file
----------------------

.. help-version:: <13

   * **Invoices**: the PDF of the invoice. Print it with
     :version:`10|**Print**;11|**Print Invoice**;*|**Send & Print**` or from
     the **Print** menu, also from the list after selecting the invoices.
     Once the invoice is validated, the PDF is saved as an attachment and
     printed again unchanged.\ :version:`>=11| **Invoices without Payment**
     prints the same PDF without the payments received.`
   * :version:`<12|**Send by Email**;*|**Send & Print**` attaches the PDF to
     the email; the message stays in the chatter of the invoice.
     :version:`12|**Preview** shows the invoice as the customer sees it in the
     portal.`
   * Invoice analysis: :version:`10|**Invoicing ‣ Reports ‣ Business
     Intelligence ‣ Invoices**;*|**Invoicing ‣ Reporting ‣ Management ‣
     Invoices**` shows the invoiced amounts by period, partner, product or
     salesperson, as graph or pivot.

.. help-version:: >=13

   * :version:`<18|**Invoices**;*|**Invoice PDF**`: the PDF of the invoice.
     Print it from the **Print** menu\ :version:`>=17| (under the gear icon
     next to the record name)`, :version:`<18|with **Send &
     Print**;*|with **Print**`, or from the list after selecting the
     invoices. Once the invoice is posted, the PDF is saved as an attachment
     and printed again unchanged.
   * :version:`<18|**Invoices without Payment**;*|**PDF without Payment**`: the
     same PDF without the payments received, from the **Print** menu.
   * :version:`<18|**Send & Print**;*|**Send**` attaches the PDF to the email;
     the message stays in the chatter of the invoice. **Preview** shows the
     invoice as the customer sees it in the portal.
   * Invoice analysis: :version:`13|**Invoicing ‣ Reporting ‣ Management ‣
     Invoices**;*|**Invoicing ‣ Reporting ‣ Management ‣ Invoice Analysis**`
     shows the invoiced amounts by period, partner, product or salesperson, as
     graph or pivot.

* To get a file of the invoices, select them in the list view, then
  :version:`<=16|**Action ‣ Export**;*|**Actions ‣ Export**`: choose the
  fields and the format (xlsx or csv). See *Import and Export data* in the
  **Ready** page of the help.

.. help-version:: 17

   * To get the documents of several invoices in one file, select the posted
     customer invoices in the list view, then **Actions ‣ Export ZIP**: one
     ZIP file holds the PDF and the other legal documents of each invoice.

.. help-version:: >=18

   .. help-if:: module = l10n_it_edi

      * To get the e-invoices in one file, select the invoices in the list
        view, then **Print ‣ XML FatturaPA**: one invoice gives its XML file,
        more invoices give a ZIP file (*invoices.zip*) holding the XML of each
        of them. The invoices without an e-invoice are skipped. **Print ‣
        PDF** does the same with the PDFs.

   .. help-if:: module = l10n_it_edi_extension

      * To load e-invoices made outside Odoo (e.g. by another software, or
        downloaded from the SdI portal of the Revenue Agency), put the XML or
        P7M files in a ZIP file, then **Invoicing ‣ Vendors ‣ E-invoice Import
        Files**: upload the ZIP and press **Import Files**. Each e-invoice
        becomes a customer invoice or a vendor bill, according to the company
        being the seller or the buyer, with the e-invoice attached; a file
        with several invoices gives one invoice for each. At the end the list
        of the imported invoices is shown. The files that are not XML or P7M
        are skipped and listed in a *To-Do* activity of the user. If a file
        with the same name was already imported, nothing is imported and an
        error names the file.
