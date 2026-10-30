.. _example:

Example
-------

**A T-shirt in 3 sizes and 2 colours**

#. Enable *Product Variants* in **Sales ‣ Configuration ‣ Settings**.
#. Create the product *T-shirt*, in the **Variants** tab add *Size* with *S,
   M, L* and *Colour* with *White, Red*, then **Save**: Odoo creates 6
   variants.
#. Press **Variant Prices** and set an extra price of 2.00 on *Red*: red
   T-shirts cost 2.00 more.

**An installation service invoiced when done**

Create the product with type *Service*, check *Can be Sold* and choose the
*Delivered quantities* invoicing policy: the quantity to invoice is the one
set as delivered on the order line.

**Bought by box of 12, sold by unit**

With the *Units of Measure* setting, set *Unit(s)* as unit of measure and a
*Dozen* as purchase unit of measure: purchase orders count dozens, stock and
sales count units.
