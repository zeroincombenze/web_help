.. _new_record_novat:

How to insert a tax without VAT
-------------------------------

The operations without VAT use a 0% tax with the *nature* code, which goes
to the XML of the electronic invoice. In the tab **Advanced Options** of the
tax the field :field:`Exoneration <l10n_it_exempt_reason>` has the nature and
:field:`Law Reference <l10n_it_law_reference>` the rule that justifies it; both
are required when the amount is 0%. The :field:`Tax Group <tax_group_id>` is
*VAT-free* (or *VAT Excluded Art.15*).

The options of the field *Exoneration* are the natures of the Italian Revenue
Agency (code *Natura* of the electronic invoice). Here is the complete
description of each one, as loaded by the module ``l10n_it_ade``:

**[N1] Escluse ex art. 15** - Excluded from the taxable base (art. 15 DPR
633/72):

* late-payment interest
* goods given as a discount or an allowance
* refunds of advances
* packaging charged at an agreed cost
* recharges (*rivalse*)

**[N2.1] Non soggette ad IVA ai sensi degli artt. da 7 a 7-septies del DPR
633/72** - Out of scope: operations that do not form part of the turnover, are
not part of the company activity, money contributions, activities of public
bodies. In detail:

* supply of goods, art. 7-bis (extra EU and EU)
* services, art. 7-ter, 7-quater and 7-quinquies (extra EU and EU)
* services, art. 7-sexies, and art. 7-septies (extra EU)
* operations excluded by the articles 7 and following without the right to
  deduction (art. 19, par. 3, letter b)
* art. 7-octies: telecommunication, broadcasting and electronic services to
  customers that are not taxable persons

**[N2.2] Non soggette - altri casi** - Out of scope, other cases:

* out of VAT field (*FC*, *fuori campo*) art. 1; art. 2 (free samples, CM
  13/E/94; transfers of money, credits and businesses; art. 2 par. 3 letters
  a, b, d, f with the right to deduction, art. 19 par. 3 letter c); art. 3
  (e.g. copyrights); art. 4 (non-commercial operations); art. 5 (e.g.
  co.co.co., participation associations)
* internal transfers not subject to VAT
* art. 7-ter, art. 7-quater par. 1 letters a) and c); non-territorial
  operations, art. 38 par. 5 DL 331/93; operations excluded by art. 7 and
  following with the right to deduction (art. 19 par. 3 letter b)
* art. 13 par. 3: excluded from the taxable base (including the sale of goods
  bought with partially non-deductible VAT)
* art. 17 par. 3: sales of the fiscal representative of a non-resident
  (resolution 89/E of 25/8/2010)
* art. 26-bis L. 196/97 (temporary work agencies); change of the taxable
  amount, art. 26 par. 3; refund of temporary work costs, art. 26 letter b
  L. 196/97
* art. 74 par. 1-2 (tobacco, newspapers...), also with the right to deduction
  (art. 19 par. 3 letter e)
* sales of the *minimi* taxpayers, art. 27 par. 1 and 2 DL 98/2011 (and art. 1
  par. 100 L. 244/2007)
* sales of the *forfetari* taxpayers, art. 1 par. 54-89 L. 190/2014
* sales of books bought in the EU, DM 9/4/93
* art. 8 par. 35 L. 67/1988 (secondment of staff)
* operations with earthquake victims

**[N3.1] Non imponibili - esportazioni** - Exports, art. 8 par. 1 letters a)
and b) DPR 633/72.

**[N3.2] Non imponibili - cessioni intracomunitarie** - Intra-Community
supplies, art. 41-42 DL 331/93.

**[N3.3] Non imponibili - cessioni verso San Marino** - Supplies to San Marino,
art. 71 DPR 633/72.

**[N3.4] Non imponibili - operazioni assimilate alle cessioni
all'esportazione** - Operations treated as exports, art. 8-bis DPR 633/72.

**[N3.5] Non imponibili - a seguito di dichiarazioni d'intento** - Operations
following a declaration of intent, art. 8 par. 1 letter c) DPR 633/72.

**[N3.6] Non imponibili - altre operazioni che non concorrono alla formazione
del plafond** - Other non-taxable operations that do not form the *plafond*,
e.g. art. 38-quater par. 1 (supplies to extra-EU travellers).

**[N4] Esenti** - Operations excluded from the VAT field by law, art. 10 DPR
633/72 and art. 42 DL 331/93:

* art. 10, habitual or occasional operations subject to *pro rata*
* art. 10 nn. 1-9, operations that are not part of the company activity
* art. 10 n. 11 (investment gold)
* art. 10 n. 18 (health services) and n. 19 (hospitalisation and care)
* art. 10 n. 22 (libraries, record libraries, visits to museums, galleries,
  picture galleries, monuments, parks, botanical and zoological gardens...)
* art. 10 n. 27-quinquies (goods with totally non-deductible VAT)
* art. 19 par. 3 letter a-bis (active operations of art. 10 nn. 1 to 4 extra
  EU)
* art. 124 par. 2 DL 34/2020, with the right to deduction art. 19 par. 1
  (goods needed to contain and manage the Covid epidemic, VAT exempt)
* exempt internal transfers
* exempt operations towards condominiums

**[N5] Regime del margine / IVA non esposta in fattura** - Margin scheme / VAT
not shown on the invoice:

* margin scheme, art. 36 DL 41/95: analytical (par. 1), flat-rate (par. 5) and
  global (par. 6)
* sales of used products, art. 37 DL 41/95
* margin scheme sales that are not taxable
* sale of newspapers, art. 74 par. 1 letter c)
* special scheme of travel agencies, art. 74-ter: EU, extra EU and mixed
  services

**[N6.1] to [N6.9] Inversione contabile** - Reverse charge (the supplier does
not charge the VAT), only for purchases; see *How to insert a tax for
reverse charge*:

* *N6.1*: sale of scrap and other recovered materials, art. 74 par. 7 and 8
* *N6.2*: sale of gold and pure silver, art. 17 par. 5
* *N6.3*: subcontracting in the building sector, art. 17 par. 6 letter a)
* *N6.4*: sale of buildings, art. 17 par. 6 letter a-bis)
* *N6.5*: sale of mobile phones, art. 17 par. 6 letter b)
* *N6.6*: sale of electronic products, art. 17 par. 6 letter c)
* *N6.7*: services of the building sector and related, art. 17 par. 6 letter
  a-ter)
* *N6.8*: energy sector operations, art. 17 par. 6 letters d-bis), d-ter) and
  d-quater)
* *N6.9*: other cases

All of them refer to the DPR 633/72.

**[N7] IVA assolta in altro stato UE** - VAT paid in another EU state: VAT for
an operation with a person of another EU state, art. 40 par. 3 and 4, and
art. 41 DL 331/93, e.g. art. 41 par. 1 letter b) (invoice issued in the state of
origin for distance sales to EU consumers, above the threshold, with VAT in
the other EU state). Conditions:

* the supplier and the customer must be taxable persons
* transfer of ownership of goods (not used) between different EU states
* the invoice has an amount different from zero

.. note::

   The generic natures *N2* (*Non soggette*) and *N3* (*Non imponibili*) were
   valid until 31-12-2020: now use *N2.1*, *N2.2* and *N3.1* to *N3.6*. The
   code *FC* (*FC applicazione IVA*, operation excluded from the VAT and from the
   fiscal communications) is archived.

The package *Italy* loads these taxes without VAT:

.. list-table::
   :header-rows: 1

   * - Tax
     - Type
     - Exoneration
     - Law Reference
   * - *0%*
     - Sales
     - N1
     - Art. 15 DPR 633/1972
   * - *0% G*, *0% S*
     - Purchases
     - N1
     - Art. 15 DPR 633/1972
   * - *0% Art.15*
     - Sales and purchases
     - N1
     - Art. 15 DPR 633/1972
   * - *0% EU G*
     - Sales
     - N3.2
     - Art. 41, DL 331/93
   * - *0% EU S*
     - Sales
     - N2.1
     - Art. 7ter, DPR 633/1972
   * - *0% EX*
     - Sales
     - N2.2
     - Fuori dall'Unione Europea
   * - *0% EX N7*
     - Sales
     - N7
     - Fuori dall'Unione Europea

#. Open **Invoicing ‣ Configuration ‣ Accounting ‣ Taxes**, search ``0%`` and
   open the tax of the nature you need. The tax *0% EU G* is applied
   automatically to the intra-Community sales by the fiscal position
   *Intra-Community*, and *0% EX* to the sales outside the EU by the position
   *Import/Export*.
#. When the nature is not in the list above (N3.1, N3.3 to N3.6, N4, N5...)
   create the tax by duplicating the nearest one, e.g. *0%*, as in *How to
   insert a new record by duplicate*.
#. Write the :field:`tax name <name>`, e.g. *0% N4*, leave :field:`Amount
   <amount>` 0, then choose :field:`Exoneration <l10n_it_exempt_reason>`,
   e.g. *[N4] Esenti*, and write the :field:`Law Reference
   <l10n_it_law_reference>`, e.g. *Art. 10 DPR 633/1972* (the reference to
   use is the one confirmed by the accountant).
#. Choose the :field:`Tax Type <type_tax_use>` (the same nature needs a tax of
   each type) and, for the purchases, the :field:`Tax Scope <tax_scope>`.
#. Choose the tax on the products or let a fiscal position replace the
   tax of the product with it, in the tab **Tax Mapping**.

