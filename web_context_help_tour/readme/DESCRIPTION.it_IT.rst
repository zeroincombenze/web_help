Tour guidati per le pagine di aiuto contestuale di web_context_help.

Una pagina di aiuto scrive i suoi mini tour dove servono, ad es. un tour per
creare un record in *Come inserire un nuovo record* e un tour per modificarlo
in *Come modificare un record*. La finestra di aiuto mostra ogni tour come un
pulsante; premuto, il tour si svolge nella scheda di Odoo:

* lo schermo è oscurato intorno all'elemento del passo (campo e sua
  etichetta, pulsante, scheda, menu) e un anello pulsante lo indica;
* un fumetto spiega il passo, con **Indietro**, **Avanti** (**Fine**
  all'ultimo passo) e **Interrompi**; anche **Esc** interrompe il tour;
* lo schermo oscurato riceve comunque i clic: l'utente fa il lavoro, il tour
  mostra dove; un passo può anche premere il suo pulsante per l'utente, ad es.
  **Nuovo**;
* un passo il cui elemento non è sullo schermo lo attende, ad es. finché la
  maschera si apre.

I passi sono scritti in RST nelle pagine di aiuto (direttive ``help-tour`` e
``help-step``), quindi ogni tour ha il suo testo inglese e italiano e segue la
versione di Odoo, come il resto dell'aiuto. Senza questo modulo i tour non
sono mostrati.
