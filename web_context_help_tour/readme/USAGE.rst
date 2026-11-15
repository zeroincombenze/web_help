Open the help window with the |sos| button and press the tour button of a
chapter, e.g. **Show me how to create a contact** in the contact help. The
Odoo tab comes to the front and the tour starts:

* read the step and do it, or press **Next** to go on;
* **Previous** goes back one step;
* **Stop**, the **×** of the popover or **Esc** end the tour.

While the tour plays, its button in the help window reads **Return to record
view**: it brings the Odoo tab back. When the tour ends, the button shows its
label again.

A step whose element is not on screen shows *Waiting for this step*: open the
screen it refers to, or do what the previous step asks; the tour goes on by
itself. **Next** skips the step.

To write a tour see *Guided tours* in the usage of web_context_help: the
``help-tour`` directive, its ``help-step`` steps and their targets.

.. |sos| unicode:: U+1F6DF
