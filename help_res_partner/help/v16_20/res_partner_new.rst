.. _new_record:

How to insert a new record
--------------------------

.. help-version:: 18

   .. help-tour:: res_partner_new
      :label: Show me how to create a contact

      .. help-step:: new
         :click:

         Press **New** to open an empty contact form.

      .. help-step:: field:company_type

         Choose *Individual* for a person, *Company* for a company.

      .. help-step:: field:name

         Type the name: it is the only required field.

      .. help-step:: field:email

         Type the email; phone, address and Tax ID go in the fields around
         it.

      .. help-step:: field:category_id

         Add tags to group the contacts, e.g. by kind of business.

      .. help-step:: tab:sales_purchases

         In **Sales & Purchase** set the salesperson, the payment terms and
         the pricelist.

      .. help-step:: save

         Press the cloud icon to save at once; the contact is saved anyway
         when you leave it.

#. Open **Contacts** and press [`New`]. Contacts are also created on the fly
   from any document, e.g. typing a new customer in a sales order and
   choosing *Create and edit…*.
#. Choose **Company** or **Individual** and type the :field:`name <name>`
   (required).
#. For an individual, choose the :field:`company <parent_id>` they work for;
   if it does not exist yet, type its name and press [`Create company`].
#. Fill in the address, the :field:`Tax ID <vat>`, phone, email and website.
   For an individual of a company the address and the Tax ID come from the
   company.
#. Add :field:`tags <category_id>` and, for an individual, the :field:`job
   position <function>`.
#. For a company, open the **Contacts & Addresses** tab and press [`Add`] for
   each person or address: choose the type (*Contact*, *Invoice Address*,
   *Delivery Address*, *Other Address*), type the name and, for an address,
   the street; press [`Save & Close`] or [`Save & New`].
#. Complete the **Sales & Purchase** tab (salesperson, payment terms,
   pricelist, reference) and, with Invoicing, the **Invoicing** tab (bank
   accounts).
#. The record is saved automatically when you leave it; press the cloud icon
   next to the breadcrumb to save at once.
