.. _report:

Report and export file
----------------------

.. help-version:: <13

   * Bill analysis: :version:`10|**Invoicing ‣ Reports ‣ Business
     Intelligence ‣ Invoices**;*|**Invoicing ‣ Reporting ‣ Management ‣
     Invoices**` shows the invoiced amounts by period, partner or product, as
     graph or pivot: the vendor bills are among them, filter them by their
     type.

.. help-version:: >=13

   * Bill analysis: :version:`13|**Invoicing ‣ Reporting ‣ Management ‣
     Invoices**;*|**Invoicing ‣ Reporting ‣ Management ‣ Invoice Analysis**`
     shows the invoiced amounts by period, partner or product, as graph or
     pivot: the vendor bills are among them, filter them by their type.

* To get a file of the bills, select them in the list view, then
  :version:`<=16|**Action ‣ Export**;*|**Actions ‣ Export**`: choose the
  fields and the format (xlsx or csv). See *Import and Export data* in the
  **Ready** page of the help.

.. help-version:: >=18

   .. help-if:: module = l10n_it_edi_extension

      * To load e-invoices made outside Odoo (e.g. by another software, or
        downloaded from the SdI portal of the Revenue Agency), put the XML or
        P7M files in a ZIP file, then **Invoicing ‣ Vendors ‣ E-invoice Import
        Files**: upload the ZIP and press [`Import Files`]. Each e-invoice
        becomes a vendor bill (or a customer invoice, when the company is the
        seller), with the e-invoice attached; a file with several invoices
        gives one document for each. At the end the list of the imported
        documents is shown. The files that are not XML or P7M are skipped and
        listed in a *To-Do* activity of the user. If a file with the same name
        was already imported, nothing is imported and an error names the file.
