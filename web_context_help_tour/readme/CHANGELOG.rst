10.0.1.0.0 (2026-11-13)
~~~~~~~~~~~~~~~~~~~~~~~

* [NEW] Tour player of the help-tour tours: dimmed screen around the target, ring, popover with Previous / Next / Stop, waiting for a missing target
* [NEW] The help window is told when the tour ends (Finish, Stop, Esc), so the tour button gets back its label
* [IMP] A press on the tour popover (mouse or Enter on Next) does not close an Odoo dropdown opened by the tour, e.g. the Filters menu; new test of the contact search tour
* [IMP] Tests: before_test.sh installs PhantomJS 2.1.1 locally in tests/.phantomjs/ (Odoo 10 runs the browser tests with PhantomJS, without it the tour player test is skipped, not run)
* [FIX] Tour player on the browser of Odoo 10 tests (PhantomJS 2.1): no Element.closest, isConnected, CSS.escape nor classList.toggle with two arguments; ES5 helpers instead
* [FIX] Odoo 10 form widgets carry no field name in the DOM: the odoo10 adapter writes data-wch-field, so the field: targets of a tour are found
