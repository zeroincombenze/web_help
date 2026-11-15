Guided tours for the context help pages of web_context_help.

A help page writes its mini tours where they are needed, e.g. a tour to
create a record in *How to insert a new record* and a tour to change it in
*How to update a record*. The help window shows each tour as a button;
pressed, the tour plays in the Odoo tab:

* the screen is dimmed around the element of the step (field and its label,
  button, tab, menu) and a pulsing ring shows it;
* a popover explains the step, with **Previous**, **Next** (**Finish** on the
  last step) and **Stop**; **Esc** stops the tour too;
* the dimmed screen still takes the clicks: the user does the work, the tour
  shows where; a step can also press its button for the user, e.g. **New**;
* a step whose element is not on screen waits for it, e.g. until the form
  opens.

The steps are written in RST in the help pages (``help-tour`` and
``help-step`` directives), so every tour has its English and Italian text and
follows the Odoo version, like the rest of the help. Without this module the
tours are not shown.
