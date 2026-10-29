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

Page created on 2026-10-29 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
