.. help-page:: res_partner_kanban
   :title: Contacts (kanban)
   :model: res.partner
   :view-type: kanban
   :priority: 96

Contacts (kanban)
=================

.. _description:

Description
-----------

The contacts as cards, the default view of the contacts menus. Each card
shows the picture, the :field:`name <display_name>`, the :field:`job position
<function>`, the city and the country, the email and the :field:`tags
<category_id>`. Click a card to open the contact; the buttons at the top
right of the search bar switch to the list.

.. help-include:: res_partner_list_search.rst

.. help-include:: res_partner_configure.rst

.. help-include:: res_partner_report.rst

.. help-include:: res_partner_list_example.rst

.. _faq:

FAQ
---

.. help-question:: Why don't I see all the contacts?

   The menu may show only customers or only vendors: *Sales ‣ Sales ‣
   Customers* starts with the *Customers* filter, *Purchases ‣ Purchase ‣
   Vendors* with the *Vendors* filter. Remove the filter from the search bar.
   Archived contacts are shown by the *Archived* filter only.

.. help-question:: Why does a contact appear twice?

   A person is shown with the name of the company (*Company, Person*): the
   company and its people are separate records. A real duplicate can be
   archived; see *Example*.

.. _footer:

Footer
------

Page created on 2026-10-29 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
