.. help-page:: res_company_list
   :title: Companies
   :model: res.company
   :view: base.view_company_tree
   :view-type: list
   :priority: 96

Companies
=========

.. _description:

Description
-----------

Click on button **Ready** for help about how to use this help; click on
button **FAQ** for the most common solved questions.

The list of the companies managed in the database. Each row shows the
:field:`company name <name>`, its :field:`partner <partner_id>` (the contact
holding address and Tax ID of the company) and its :field:`branches
<child_ids>`. The order of the rows, changed by dragging the handle at the
left, is the order in which the companies are proposed. Click a row to open
the company.

.. _search:

Suggestions for search
----------------------

* **Settings ‣ Users & Companies ‣ Companies** lists the companies; the
  menu is visible to the administrators.
* Type in the search bar to search the companies by name.
* **Filters ‣ Archived** shows the companies no longer used.
* **Group By ‣ Add Custom Group** groups the companies, e.g. by parent
  company, to see the branches under their main company.

.. help-include:: res_company_configure.rst

.. help-include:: res_company_report.rst

.. _example:

Example
-------

**A second company in the same database.** Press **New**, type the name,
the address and the Tax ID and leave the form. Then open **Settings ‣ Users
& Companies ‣ Users**, open every user who must work for the new company
and add it to the *Allowed Companies*. The users switch from one company to
the other with the company switcher in the top bar.

.. _faq:

FAQ
---

Click on button **Topic** to return to the specific help page.

.. help-question:: Why don't I see the Companies menu?

   The menu is shown to the administrators (*Settings* rights) only.

.. help-question:: Why can't I see a company in the company switcher?

   The switcher shows the *Allowed Companies* of your user: ask an
   administrator to add the company to your user.

.. help-question:: How do I remove a company?

   A company used by documents cannot be deleted: archive it instead, opening
   it and pressing the gear icon ‣ **Archive**. A company that is still the default company
   of an active user cannot be archived: change the default company of the
   user first.

.. _footer:

Footer
------

Page created on 2026-11-07 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
