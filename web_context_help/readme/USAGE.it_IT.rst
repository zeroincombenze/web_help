Premere il pulsante |sos| del pannello di controllo. La pagina è cercata per
xmlid della vista, poi per modello e tipo vista, poi per modello; altrimenti
una pagina automatica elenca l'aiuto dei campi.

Scrivere l'aiuto di un modulo: mettere i file RST in ``help/common/`` o nella
cartella di un gruppo di versioni Odoo (``help/v10``, ``help/v11_14``,
``help/v15``, ``help/v16_20``); il file del gruppo prevale su quello comune con
lo stesso nome. I gemelli italiani si chiamano ``pagina.it_IT.rst``.

Ogni pagina ha queste sezioni, in quest'ordine, con la loro etichetta:
``description`` (sintesi della vista / modello),
``new_record`` (solo form: passi per inserire un record),
``update_record`` (solo form: passi per modificare un record),
``search`` (solo lista: come cercare e raggruppare),
``configure`` (come configurare il modello),
``report`` (come visualizzare la stampa o l'allegato pdf),
``example`` (esempi utili),
``faq`` (domande frequenti, blocchi ``help-question``),
``footer`` (data e ora di creazione della pagina e nota di copyright).
Una sezione che non si applica contiene una riga che lo dice.

::

    .. help-page:: partner
       :title: Partner
       :model: res.partner
       :view: base.view_partner_form
       :view-type: form

    .. help-include:: parte_comune.rst

    .. help-inherit:: altro_modulo.partner
       :section: usage
       :position: after

       RST aggiunto dopo la sezione con etichetta "usage"

    .. help-question:: Come aggiungo un'etichetta?

       Usare il campo :field:`Etichette <category_id>`.

    .. help-question::
       :auto:

``:position:`` vale ``before``, ``after``, ``replace`` o ``remove``.
``:auto:`` costruisce le domande dall'aiuto dei campi del modello della pagina.

Una pagina mostra solo il testo della versione di Odoo in uso: mettere i
blocchi specifici di una versione in ``help-version`` e le parole specifiche
nel ruolo ``:version:``; le cartelle per versione restano per i file interi
che cambiano.

::

    .. help-version:: >=17

       RST mostrato da Odoo 17 in poi (sezioni ammesse)

    Premere :version:`16|**Crea e visualizza fattura**;17|**Crea bozza fattura**;*|**Crea bozza**`.

Condizioni: ``16``, ``16-18``, ``>=17``, ``>17``, ``<=16``, ``<17``, ``*``
(qualsiasi versione), più condizioni separate da virgola (``10,16``). Il ruolo
mostra il testo della prima condizione soddisfatta, con il markup in linea ma
senza altri ruoli; scrivere ``\ `` prima del ruolo quando è attaccato alla
parola precedente.
I ruoli ``:field:`` e ``:tour:`` evidenziano un campo o avviano un tour nella scheda di Odoo.

.. |sos| unicode:: U+1F6DF
