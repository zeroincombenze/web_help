.. _new_record:

New record
----------

#. Open **Sales ‣ Products ‣ Products** (or **Inventory ‣ Products ‣
   Products**, **Purchase ‣ Products ‣ Products**) and press **New**.
#. Type the :field:`product name <name>` (required) and choose the **Product
   Type**\ :version:`>=18| (for stocked goods also check **Track Inventory**)`.
#. Check :version:`<=17|**Can be Sold** and **Can be Purchased**;*|**Sales**
   and **Purchase**` as needed.
#. Set the :field:`sales price <list_price>`, the taxes and the :field:`cost
   <standard_price>`; choose the :field:`category <categ_id>` and, with the
   *Units of Measure* setting, the :field:`unit of measure <uom_id>`.
#. Type the :field:`internal reference <default_code>` and the
   :field:`barcode <barcode>`, if any.
#. In the **Sales** tab write the description for the customers; in the
   **Purchase** tab add the vendors with their price; in the **Inventory**
   tab set routes, weight and volume.
#. For a product sold in several versions open the **Attributes & Variants**
   tab (*Variants* setting), press **Add a line**, choose the attribute (e.g.
   *Size*) and its values: Odoo creates one variant for each combination.
#. The record is saved automatically when you leave it; press the cloud icon
   next to the breadcrumb to save at once.
