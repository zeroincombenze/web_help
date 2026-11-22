.. _example:

Example
-------

All the examples use the rate 22% and the Italian package (``l10n_it``). Open
**Invoicing ‣ Configuration ‣ Accounting ‣ Taxes** and, to avoid typing the
distribution lines, duplicate the tax named in each example (gear icon ‣
**Duplicate**), then change what is written here.

**How to set the nature and the tax grids**

* The **nature** is the field :field:`Exoneration <l10n_it_exempt_reason>` of
  the tab **Advanced Options**, with the :field:`Law Reference
  <l10n_it_law_reference>` below it. It is required only when the amount is
  0%: the taxes with an amount have no nature.
* The **tax grids** are in the tab **Definition**, column **Tax Grids** of the
  tables **Distribution for Invoices** and **Distribution for Refunds**. Click
  the cell of a line, type the code of the grid, e.g. ``vj12``, and choose
  it: the grid ``+vj12`` adds the amount to the line VJ12 of the VAT report,
  ``-vj12`` subtracts it. The invoices use the grids with ``+``, the refunds
  the same grid with ``-``. A line may have more grids, e.g. ``+03`` and
  ``+vj12``.
* The grids used here are: ``02`` (VP2, total active operations), ``03``
  (VP3, total passive operations), ``4v`` (VP4, VAT due), ``5v`` (VP5, VAT
  deductible), ``ve38`` (VE38, operations with the parties of art. 17-ter),
  ``vj3``, ``vj9`` and ``vj12`` to ``vj17`` (the lines VJ of the reverse
  charge).

**1. Tax with VAT 22%**

*1a. Sales*: duplicate *22%* (type *Sales*) and write the name, e.g. *22% new*.

#. Tab **Definition**, **Distribution for Invoices**: the line *Base* has the
   grid ``+02``; the line *of tax* (100%) has the account *VAT debt* and the
   grid ``+4v``.
#. **Distribution for Refunds**: the same lines in the same order, with the
   grids ``-02`` and ``-4v``.
#. Tab **Advanced Options**: :field:`Tax Group <tax_group_id>` *22% VAT*,
   :field:`Country <country_id>` *Italy*. No nature.

An invoice line of 100.00 gets a tax of 22.00 and a total of 122.00; the
report has 100.00 in VP2 and 22.00 in VP4.

*1b. Purchases*: duplicate *22% G* (goods) or *22% S* (services) and write the
name, e.g. *22% G new*.

#. :field:`Tax Type <type_tax_use>` *Purchases* and :field:`Tax Scope
   <tax_scope>` *Goods* or *Services*.
#. **Distribution for Invoices**: the line *Base* has the grid ``+03``; the
   line *of tax* (100%) has the account *VAT credit* and the grid ``+5v``.
#. **Distribution for Refunds**: the same lines with the grids ``-03`` and
   ``-5v``.
#. Tab **Advanced Options**: :field:`Tax Group <tax_group_id>` *22% VAT*,
   :field:`Country <country_id>` *Italy*. No nature.

A bill line of 100.00 gets a tax of 22.00 and a total of 122.00; the report
has 100.00 in VP3 and 22.00 in VP5.

**2. Tax without VAT, nature N4 (exempt)**

The steps of the two sides are the same: the amount is 0, the nature and the
law reference are required and the tax group is *VAT-free* (in Italian *Fuori
Campo IVA*).

*2a. Sales*: duplicate *22%* (type *Sales*) and write the name *0% N4*.

#. Write 0 in :field:`Amount <amount>`.
#. Tab **Advanced Options**: choose :field:`Exoneration
   <l10n_it_exempt_reason>` *[N4] Esenti*, write the :field:`Law Reference
   <l10n_it_law_reference>` *Art. 10 DPR 633/1972* and choose the :field:`Tax
   Group <tax_group_id>` *VAT-free*.
#. Tab **Definition**: delete the grid ``+4v`` of the line *of tax* (and
   ``-4v`` of the refunds): there is no VAT to report. The package leaves the
   grids of the taxes without VAT empty (e.g. the tax *0%*, nature N1): add
   ``+02`` / ``-02`` to the line *Base* only if the accountant wants the
   operation in VP2.

An invoice line of 100.00 has a tax of 0.00 and a total of 100.00; the
electronic invoice has the nature N4 and the law reference.

*2b. Purchases*: duplicate *22% G* (or *22% S*) and write the name *0% N4 G*
(or *0% N4 S*).

#. Write 0 in :field:`Amount <amount>`; keep :field:`Tax Type
   <type_tax_use>` *Purchases* and the :field:`Tax Scope <tax_scope>`.
#. Tab **Advanced Options**: the same nature *[N4] Esenti*, the same law
   reference and the tax group *VAT-free*.
#. Tab **Definition**: delete the grid ``+5v`` of the line *of tax* (and
   ``-5v`` of the refunds); add ``+03`` / ``-03`` to the line *Base* only if
   the accountant wants the operation in VP3.

A bill line of 100.00 has a tax of 0.00 and a total of 100.00. The same steps
with another nature, e.g. [N3.1] and *Art. 8 c. 1 lett. a) e b) DPR 633/72*,
give the tax of an export (sales).

**3. Tax with split payment 22%**

Three taxes, as in *How to insert a tax for split payment*. Duplicate *22% SP
pos.*, *22% SP neg.* and *22% SP* (or all the set of another rate), then:

#. *22% SP pos.*: amount 22, type *None*, tax group *22% VAT*; invoice lines
   *Base* with grids ``+02`` and ``+ve38``, and *of tax* on the account *VAT
   Split Payment*, with no grid; refunds ``-02`` and ``-ve38``.
#. *22% SP neg.*: amount -22, type *None*, tax group *Split Payment*,
   :field:`Included in Price <price_include_override>` *Tax Excluded*; no grids,
   the line *of tax* on the account *VAT Split Payment*.
#. *22% SP*: type *Sales*, :field:`Tax Computation <amount_type>` *Group of
   Taxes*, :field:`Tax Group <tax_group_id>` *Split Payment*, and the two taxes
   above in **Children Taxes**.

An invoice line of 100.00 with *22% SP* has +22.00 and -22.00: the total is
100.00, the VAT of 22.00 is not paid to the supplier and the report has 100.00
in VP2 and VE38.

**4. Tax with reverse charge 22%, nature N6.3 (construction subcontractors)**

Two taxes, one for each side of the operation.

*Purchase tax*: duplicate *22% RC N6.3* (or *22% G* and rename it *22% RC
N6.3*).

#. **Distribution for Invoices**: the line *Base* has the grids ``+03`` and
   ``+vj12`` (VJ12, subcontracting in the construction field); then two lines
   *of tax*: +100% on *VAT credit* with the grid ``+5v``, and -100% on *VAT
   debt* with the grid ``-4v``.
#. **Distribution for Refunds**: the same lines in the same order, with the
   grids ``-03`` and ``-vj12``, ``-5v`` on +100% and ``+4v`` on -100%.
#. Tab **Advanced Options**: :field:`Tax Group <tax_group_id>` *22% VAT*.

The grid of the base changes with the nature: ``vj6`` for N6.1, ``vj7`` for
N6.2, ``vj8`` for N6.2b, ``vj12`` for N6.3, ``vj13`` for N6.4, ``vj14`` for
N6.5, ``vj15`` for N6.6, ``vj16`` for N6.7 and ``vj17`` for N6.8. For the
purchases from abroad use ``vj3`` (services, and goods already in Italy) or
``vj9`` (goods from the EU).

On a bill of 100.00 the two taxes of 22.00 cancel each other: the total stays
100.00 and the VAT is both deductible (VP5) and due (VP4).

*Sales tax*: duplicate *0% RC N6.3* (or *22%* and write 0 in the amount). In
the tab **Advanced Options** choose :field:`Exoneration
<l10n_it_exempt_reason>` *[N6.3]* and write the :field:`Law Reference
<l10n_it_law_reference>` *art.17, comma 6, lett. a, D.P.R. 633/1972*; the
:field:`Tax Group <tax_group_id>` is *VAT-free*; the grids are ``+02`` on the
base and ``+4v`` on the line *of tax* (refunds ``-02`` and ``-4v``).
