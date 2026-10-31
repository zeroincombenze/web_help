.. _example:

Example
-------

**A T-shirt in 3 sizes and 2 colours**

#. Enable :version:`11|*Attributes and Variants*;12|*Variants and
   Options*;*|*Variants*` in **Sales ‣ Configuration ‣ Settings**.
#. Create the product *T-shirt*, in the :version:`<=14|**Variants**;*|**Attributes
   & Variants**` tab add *Size* with *S, M, L* and *Colour* with *White, Red*,
   then **Save**: Odoo creates 6 variants.
#. Set an extra price of 2.00 on *Red* with :version:`11|**Variant
   Prices**;12-14|**Configure Variants**;*|**Configure** on the *Colour* line`:
   red T-shirts cost 2.00 more.

**An installation service invoiced when done**

Create the product with type *Service*, check *Can be Sold* and choose the
*Delivered quantities* invoicing policy: the quantity to invoice is the one
set as delivered on the order line.

**Bought by box of 12, sold by unit**

With the *Units of Measure* setting, set *Units* as unit of measure and a
*Dozens* as purchase unit of measure: purchase orders count dozens, stock and
sales count units.
