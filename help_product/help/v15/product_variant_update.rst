.. _update_record:

How to update a record
----------------------

#. Variants are created by the product: add attribute values in the
   :version:`<=14|**Variants**;*|**Attributes & Variants**` tab of the product,
   never create a variant by hand.
#. Open the variant from the **Product Variants** menu or the **Variants**
   button of the product, press **Edit**, change the fields and press
   **Save**.
#. Change on the variant its :field:`internal reference <default_code>`,
   :field:`barcode <barcode>`, :field:`cost <standard_price>`, weight and
   volume.
#. Name, category, type, taxes, routes and vendors belong to the product:
   changing them here changes all the variants.
#. :version:`<=12|**Active**;*|**Action ‣ Archive**` archives this variant
   only: it is no longer proposed on new documents. A variant used by
   documents cannot be deleted.
