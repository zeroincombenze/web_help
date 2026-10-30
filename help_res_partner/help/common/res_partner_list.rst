.. help-page:: res_partner_list
   :title: Contacts
   :model: res.partner
   :view-type: list
   :priority: 96

Contacts
========

.. _description:

Description
-----------

.. help-version:: <16

   The list of contacts. Each row shows the :field:`name <display_name>` (with
   the company of a person), the :field:`phone <phone>` and the :field:`email
   <email>`. Click a row to open the contact.

.. help-version:: >=16

   The list of companies, individuals and addresses. Each row shows the
   :field:`name <name>`, the :field:`email <email>`, the :field:`phone
   <phone>` and the :field:`city <city>`. Click it to open the contact.
   The buttons at the top right switch between kanban, list and the other
   views.

.. help-include:: res_partner_list_search.rst

.. help-include:: res_partner_configure.rst

.. help-include:: res_partner_report.rst

.. help-include:: res_partner_list_example.rst

.. _faq:

FAQ
---

.. help-version:: <16

   .. help-question:: Why don't I see all the contacts?

      The menu may show only customers or only vendors: *Sales ‣ Sales ‣
      Customers* starts with the *Customers* filter, *Purchases ‣ Purchase ‣
      Vendors* with the *Vendors* filter. Remove the filter from the search bar.
      Archived contacts are shown by the *Archived* filter only.

   .. help-question:: Why does a contact appear twice?

      A person is shown with the name of the company (*Company, Person*): the
      company and its people are separate records. A real duplicate can be
      archived; see *Example*.

.. help-version:: >=16

   .. help-question:: Where are the archived contacts?

      Choose the *Archived* filter; open a contact and use **Actions ‣
      Unarchive** to restore it.

   .. help-question:: Why do I see the same company several times?

      The addresses and the people of a company are contacts too: choose the
      *Companies* filter to see the companies only.

.. _footer:

Footer
------

Page created on 2026-10-30 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
