.. _new_record:

New record
----------

Variants are not created one by one: they are generated from the attributes
of the product.

#. Activate the *Variants* setting (**Sales ‣ Configuration ‣ Settings**).
#. Open the product, tab **Attributes & Variants**, press **Add a line**,
   choose the attribute and its values.
#. Odoo creates one variant for each combination of values; open them from the
   **Variants** smart button of the product or from **Sales ‣ Products ‣
   Product Variants**.
#. Attributes set to create variants *Dynamically* or
   :version:`<=17|*Never (option)*;*|*Never*` do not generate
   variants in advance: the variant is created when first ordered, or the
   value is only a description of the order line.
