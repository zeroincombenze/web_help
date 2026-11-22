.. help-page:: tax_form
   :title: Imposte
   :model: account.tax
   :view: account.view_tax_form
   :view-type: form
   :priority: 96

Imposte
=======

.. _description:

Descrizione
-----------

Fare clic sul pulsante [`Pronto`] per sapere come usare questo aiuto; fare
clic sul pulsante [`FAQ`] per le domande più comuni già risolte.

Un'imposta dice a Odoo come calcolare l'imposta di una riga fattura (ad es.
l'IVA) e dove registrarla. Le imposte sono scelte sui prodotti, proposte dalla
posizione fiscale del partner e scritte sulle righe fattura.

Ogni imposta ha un :field:`nome <name>`, un :field:`calcolo <amount_type>`
(percentuale, fisso, percentuale imposte incluse o gruppo di imposte), un
:field:`tipo <type_tax_use>` (*Vendita*, *Acquisti* o *Nessuno*), un
:field:`ambito <tax_scope>` facoltativo (*Servizi* o *Beni*) e l':field:`importo
<amount>`. La scheda **Definizione** contiene la ripartizione dell'imposta sui
conti e sulle griglie imposta, per le fatture e per i rimborsi; la scheda
**Opzioni avanzate** l'etichetta su fatture, il gruppo imposta, la nazione e
le opzioni contabili (ad es. *Determinare imponibile imposte successive*,
*Esigibilità fiscale*). Con la localizzazione italiana mostra anche
:field:`Esenzione <l10n_it_exempt_reason>` (il codice natura N1...N7) e
:field:`Riferimento legislativo <l10n_it_law_reference>`.

.. help-include:: tax_new.rst

.. help-include:: tax_new_duplicate.rst

.. help-if:: module = l10n_it

   .. help-include:: tax_new_vat.rst

   .. help-include:: tax_new_novat.rst

   .. help-include:: tax_new_split.rst

   .. help-include:: tax_new_rc.rst

.. help-include:: tax_update.rst

.. help-include:: tax_cancel.rst

.. help-include:: tax_configure.rst

.. help-include:: tax_report.rst

.. help-include:: tax_example.rst

.. _faq:

FAQ
---

Fare clic sul pulsante [`Argomento`] per tornare alla pagina di aiuto
specifica.

.. help-question:: Perché non riesco a salvare un'imposta con 0%?

   Con la localizzazione italiana un'imposta con Calcolo imposta *Percentuale*
   e importo 0 richiede :field:`Esenzione <l10n_it_exempt_reason>` e
   :field:`Riferimento legislativo <l10n_it_law_reference>`: Odoo dice *Se
   l'importo della tassa è 0%, devi inserire il codice di esenzione ed il
   relativo riferimento legislativo*.

.. help-question:: Perché Odoo dice "I nomi delle imposte devono essere unici!"?

   Due imposte della stessa azienda non possono avere lo stesso nome, tipo,
   ambito e nazione. Cambiare il nome, ad es. aggiungendo una lettera, o
   l'ambito.

.. help-question:: Perché Odoo dice che la ripartizione deve avere un totale dei fattori pari a 100?

   Le righe *dell'imposta* di **Ripartizione per fatture** devono sommare
   +100% (e, quando ci sono righe negative, come nell'inversione contabile,
   -100%); **Ripartizione per rimborsi** deve avere le stesse righe nello
   stesso ordine, e ogni tabella esattamente una riga *Riferimento*.

.. help-question:: Perché non posso scegliere le figlie della mia imposta di gruppo?

   La tabella :field:`Imposte figlie <children_tax_ids>` è mostrata quando
   Calcolo imposta è *Gruppo di imposte* e il tipo imposta non è *Nessuno*. Le
   figlie devono essere di tipo *Nessuno* o dello stesso tipo del gruppo, e non
   essere a loro volta gruppi.

.. help-question:: Perché l'imposta non compare sulla riga fattura?

   Un'imposta archiviata non è proposta. Controllare anche il :field:`Tipo
   imposta <type_tax_use>` (le imposte di vendita non sono proposte sulle
   fatture fornitore) e la *Posizione fiscale* del partner, che può sostituire
   l'imposta del prodotto.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-22 16:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
