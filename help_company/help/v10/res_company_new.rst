.. _new_record:

How to insert a new record
--------------------------

#. Open **Settings ‣ Users ‣ Companies** and press **Create**
   (administrators only). To work with several companies, enable *Manage
   multiple companies* first: see *How to set up*.
#. Type the :field:`company name <name>` (required) and, under it, the
   :field:`Company Tagline <rml_header1>` printed in the header of the
   reports; click the image to load the logo.
#. In the **General Information** tab fill in the address, choosing the
   :field:`country <country_id>` (the list of the states follows it), and the
   :field:`website <website>`.
#. Fill in the :field:`phone <phone>`, :field:`fax <fax>`, :field:`email
   <email>`, the :field:`Tax ID <vat>` and the :field:`currency
   <currency_id>`; with several companies, the :field:`Parent Company
   <parent_id>` when the company belongs to a group.

   .. help-if:: module = l10n_it_rea

      The *Company Registry* is in the **REA Data** tab: it is filled in from
      the REA data written there.

   .. help-if:: module != l10n_it_rea

      Fill in also the :field:`Company Registry <company_registry>`.

#. Press **Save**.
#. Allow the users to work for the new company: open **Settings ‣ Users ‣
   Users**, open each user, press **Edit** and add the company to the
   *Allowed Companies* of the **Access Rights** tab.
#. With Invoicing installed, switch to the new company in the top bar, open
   **Invoicing ‣ Configuration ‣ Settings**, check *This company has its own
   chart of accounts*, choose the *Template* of the **Chart of Accounts**
   (e.g. *Italy - Generic Chart of Accounts*) and press **Apply**: the
   accounts and the taxes of the company are created.
