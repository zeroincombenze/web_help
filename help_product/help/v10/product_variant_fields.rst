.. _fields:

Main fields
~~~~~~~~~~~

* :field:`Attribute values <attribute_value_ids>`: what makes the variant,
  e.g. *L* and *Red*.
* :field:`Internal reference <default_code>` and :field:`barcode <barcode>`:
  each variant has its own.
* :field:`Sale price <lst_price>`: the sale price of the product plus the
  extra prices of the attribute values; read-only when the product has
  several variants.
* :field:`Cost <standard_price>`, :field:`weight <weight>` and
  :field:`volume <volume>`: each variant has its own.
* Stock: the **On Hand** and **Forecasted** buttons count the quantity of this
  variant only.
