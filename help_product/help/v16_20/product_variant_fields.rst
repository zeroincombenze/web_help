.. _fields:

Main fields
~~~~~~~~~~~

* :field:`Attribute values <product_template_variant_value_ids>`: the
  combination that defines the variant, e.g. *Size: M, Color: Blue*.
* :field:`Internal reference <default_code>` and :field:`barcode <barcode>`
  of the variant.
* :field:`Sales price <lst_price>`: the product sales price plus the extra
  prices of the variant values.
* :field:`Cost <standard_price>`, weight and volume can differ per variant.
* All the other fields (name, type, category, taxes, descriptions, vendors,
  routes, …) belong to the :field:`product <product_tmpl_id>`: changing them
  here changes every variant.
