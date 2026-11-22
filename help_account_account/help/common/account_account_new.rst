.. _new_record:

How to insert a new record
--------------------------

#. Open **Invoicing ‣ Configuration ‣ Accounting ‣ Chart of Accounts** and
   press [`New`]: a line opens at the top of the list. Accounts exist only
   after a *Fiscal Localization* package has been chosen, see *How to set up*.
#. Type the :field:`code <code>`, e.g. ``101000``: letters, digits and dots
   only, unique in the company. The new code is checked when the account is
   saved.
#. Type the :field:`account name <name>`, e.g. *Current Assets*, then choose
   the :field:`type <account_type>`. If you leave it empty, the type and the
   tags are copied from the account with the code just before the new one.
#. Leave or change the *Allow Reconciliation* switch: it is on for receivable
   and payable accounts and cannot be on for bank and cash, credit card and
   off-balance accounts; leave it off for the other accounts unless you match
   their journal items (e.g. a transit account).
#. Save the line, then press the arrow button at its end (*Open in form
   view*) to fill the other fields of the form: the :field:`Default Taxes
   <tax_ids>`, the :field:`Tags <tag_ids>`, the :field:`Allowed Journals <allowed_journal_ids>` and, with
   several currencies, the :field:`Account Currency <currency_id>`.
#. The record is saved automatically when you leave it; press the cloud icon
   next to the breadcrumb to save at once.

Another account is created from an existing one with the gear icon ‣
**Duplicate**: the code is increased to a free one and the name gets *(copy)*.
