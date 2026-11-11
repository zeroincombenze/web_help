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
:field:`company name <name>` and its :field:`partner <partner_id>` (the
contact holding address and Tax ID of the company). The order of the rows,
changed by dragging the handle at the left, is the order in which the
companies are proposed. Click a row to open the company.

.. _search:

Suggestions for search
----------------------

* **Settings ‣ Users ‣ Companies** lists the companies; the menu is visible
  to the administrators.
* Type in the search bar to search the companies by name.
* **Group By ‣ Add custom group** groups the companies, e.g. by *Parent
  Company*, to see the companies of a group under their parent company.

.. help-include:: res_company_configure.rst

.. help-include:: res_company_report.rst

.. _example:

Example
-------

**A second company in the same database.** In **Settings ‣ General
Settings** check *Manage multiple companies* and press **Apply**. Then press
**Create** in this list, type the name, the address and the Tax ID and press
**Save**. Open **Settings ‣ Users ‣ Users**, open every user who must work
for the new company, press **Edit** and add it to the *Allowed Companies* of
the **Access Rights** tab. The users switch from one company to the other
with the company switcher in the top bar.

.. _faq:

FAQ
---

Click on button **Topic** to return to the specific help page.

.. help-question:: Why don't I see the Companies menu?

   The **Settings** menu is shown to the administrators only.

.. help-question:: Why can't I see a company in the company switcher?

   The switcher shows the *Allowed Companies* of your user, and appears only
   when they are more than one: ask an administrator to add the company to
   your user.

.. help-question:: How do I remove a company?

   In this version a company cannot be archived. It can be deleted (select it
   in the list, then **Action ‣ Delete**) only while no document, user or
   other record refers to it; a company already used must be kept.

.. _footer:

Footer
------

Page created on 2026-11-07 18:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
