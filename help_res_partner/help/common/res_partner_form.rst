.. help-page:: res_partner_form
   :title: Contact
   :model: res.partner
   :view-type: form
   :priority: 96

Contact
=======

.. _description:

Description
-----------

.. help-version:: <16

   A contact (partner) is anyone the company deals with: customers, vendors,
   employees' private addresses and the company itself. The :field:`company type
   <company_type>` tells a **Company** from an **Individual**; an individual can
   belong to a company through the :field:`company <parent_id>` field. A company
   groups its people and its addresses (invoice, shipping, other) in the
   **Contacts & Addresses** tab; the commercial data (tax id, payment terms,
   pricelist, accounts) is managed on the company and shared with all of them.

.. help-version:: >=16

   A contact (partner) is anyone the company deals with: customers, vendors,
   employees of other companies. A contact is a **Company** or an
   **Individual** (:field:`company type <company_type>`); an individual can
   belong to a :field:`company <parent_id>`. A company keeps its people and its
   other addresses (invoice, delivery, …) in the **Contacts & Addresses** tab:
   sales orders, invoices and deliveries pick the right address from there.

.. help-include:: res_partner_fields.rst

.. help-include:: res_partner_new.rst

.. help-include:: res_partner_update.rst

.. help-include:: res_partner_configure.rst

.. help-include:: res_partner_report.rst

.. help-include:: res_partner_example.rst

.. _faq:

FAQ
---

.. help-version:: <16

   .. help-question:: Why can't I change the address of a contact?

      A contact of type *Contact* uses the address of its company: press
      **(edit)** next to the address to change it on the company, or change the
      address type to *Invoice address*, *Shipping address* or *Other address* to
      give the contact its own address.

   .. help-question:: Why is the Accounting tab empty for a person of a company?

      Payment terms, fiscal position and accounts are managed on the company:
      press *the parent company* in the tab to open it.

   .. help-question:: Why can't I delete the contact?

      A contact used by orders, invoices or journal entries cannot be deleted:
      archive it instead with the **Active** button at the top right.

   .. help-question:: Where is a contact I archived?

      Archived contacts are hidden: in the list use the *Archived* filter, open
      the contact and press the **Archived** button to restore it.

   .. help-question:: Why is the email required?

      The contact is linked to a user, who needs an email to log in and get
      notifications.

.. help-version:: >=16

   .. help-question:: Why can't I change the address of a contact?

      A contact of type *Contact* belonging to a company shares the company
      address: change it on the company, or set the contact type to another
      address type.

   .. help-question:: Why can't I change the Tax ID?

      The Tax ID of a person belonging to a company is the company's one: change
      it on the company.

   .. help-question:: Odoo warns that a partner with the same Tax ID exists.

      The contact is probably a duplicate: open the existing one instead, or
      merge the two from the list (see *Update record*).

   .. help-question:: Why can't I delete the contact?

      A contact used by documents (orders, invoices, payments, …) cannot be
      deleted: archive it instead.

.. help-question::
   :auto:

.. _footer:

Footer
------

Page created on 2026-10-30 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
