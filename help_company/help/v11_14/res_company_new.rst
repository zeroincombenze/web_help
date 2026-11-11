.. _new_record:

How to insert a new record
--------------------------

#. Open **Settings ‣ Users & Companies ‣ Companies** and press **Create**
   (administrators only). To work with several companies, enable *Manage
   multiple companies* first: see *How to set up*.
#. Type the :field:`company name <name>` (required) and click the image to
   load the logo.
#. In the **General Information** tab fill in the address, choosing the
   :field:`country <country_id>` (the list of the states follows it).
#. Fill in the :field:`website <website>`, :field:`phone <phone>`,
   :field:`email <email>`, the :field:`Tax ID <vat>` and the
   :field:`currency <currency_id>`; with several companies, the
   :field:`Parent Company <parent_id>` when the company belongs to a group.

   .. help-if:: module = l10n_it_rea

      The *Company Registry* is in the **REA Data** tab: it is filled in from
      the REA data written there.

   .. help-if:: module != l10n_it_rea

      Fill in also the :field:`Company Registry <company_registry>`.

   .. help-if:: module = l10n_it_edi

      Under the Tax ID fill in the :field:`Codice Fiscale
      <l10n_it_codice_fiscale>` and the :field:`Tax System
      <l10n_it_tax_system>`.

   .. help-if:: module = l10n_it_fatturapa

      Under the Tax ID fill in the *Fiscal Code*; in the **E-invoice** tab
      choose the *Fiscal Position*, required.

#. Press **Save**.
#. Allow the users to work for the new company: open **Settings ‣ Users &
   Companies ‣ Users**, open each user, press **Edit** and add the company to
   the *Allowed Companies* of the **Access Rights** tab.
#. With Invoicing installed, switch to the new company in the top bar, open
   **Invoicing ‣ Configuration ‣ Settings**, choose the *Package* of the
   **Fiscal Localization** (e.g. *Italy - Generic Chart of Accounts*) and
   press **Save**: the accounts and the taxes of the company are created.
