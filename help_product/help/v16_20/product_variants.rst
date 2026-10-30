.. _variants:

Product variants
----------------

Variants are products that include additional characteristics beyond the
original product, for example colour, size, an extra option or other
attributes. In Odoo, you can set up rules to manage these variants.

To create variants for a product, activate the *Variants* setting
(:version:`<=16|**Sales ‣ Configuration ‣ Settings**;*|**Sales ‣
Configuration ‣ Settings** or **Inventory ‣ Configuration ‣ Settings**`), then
define in the **Attributes & Variants** tab the attributes to be assigned and
their possible values: Odoo creates one variant for each combination, unless
the *Variants Creation Mode* of the attribute creates them only when ordered.
Since not all products require variants, a product is treated as having no
variants if no attributes are specified.

⚠ **Caution!** Once variants have been created, it may no longer be possible
to convert a product with variants back into one without them, or to add
variants to a product that currently has none: changing the attributes later
deletes the variants that no longer match, or archives them when they are
already used by documents, and creates new ones; stock, codes and history
stay on the old variants.

⚠ **Caution!** Certain fields, such as the name and the descriptions, are
shared between the variants and the root (base) product. This means that
changing the description of one variant will update it for all variants.
However, individual document lines can have their own specific text, which
may differ from the product's default description. The :field:`internal
reference <default_code>`, the :field:`barcode <barcode>`, the cost, the
weight and the volume belong to each variant instead.

Shared fields include:

* Product category
* Sales and purchase tax (VAT) codes
* Income and expense accounts
* Descriptions
* Vendor list (a vendor price may be limited to one variant)
* HS code / Intrastat code (with the Intrastat modules)
* Sales price (price differences are set as the *Extra price* of the
  attribute values, with **Configure** in the **Attributes & Variants** tab)
* :version:`<=17|*Can be Sold* and *Can be Purchased*;*|*Sales* and
  *Purchase*` flags
* Lead times (delivery times)
* Product type
* Unit of measure
