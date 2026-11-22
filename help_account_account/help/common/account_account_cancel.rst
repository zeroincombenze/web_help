.. _cancel:

How to archive or delete record
-------------------------------

An account has no state or archive button: when no longer used, it is
*deprecated*.

#. To deprecate an account, open its form and tick :field:`Deprecated
   <deprecated>`. A deprecated
   account is no longer proposed in the choices, and a new journal item cannot
   use it; the old entries keep it. An account that is on a tax distribution
   line of a tax cannot be deprecated: change the tax first.
#. To restore it, untick *Deprecated*; the filter **Active Account** of the
   list, on by default, hides the deprecated accounts: remove it to see them.
#. To delete an account, open it and use the gear icon ‣ **Delete**, or
   select the accounts in the list and use **Actions ‣ Delete**. An account
   that has journal items cannot be deleted: deprecate it instead. An account
   set in the mapping of a fiscal position, or on a tax distribution line,
   cannot be deleted either: change the fiscal position or the tax first.
