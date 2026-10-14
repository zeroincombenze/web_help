Il menu **Aiuto**, in cima all'albero dei menu, apre la pagina iniziale
dell'aiuto nella finestra di aiuto. Il pulsante **Sommario** nell'intestazione
elenca, raggruppate per modulo, le pagine di ogni modulo di aiuto installato;
**Inizio** torna alla pagina iniziale. Gli utenti abilitati a modificare le
pagine di aiuto vedono anche **Modifica**, che apre la pagina nel backend:
anche la pagina iniziale può essere adattata come ogni altra pagina.

Premere il pulsante |sos| del pannello di controllo. La pagina è cercata per
xmlid della vista, poi per modello e tipo vista, poi per modello; altrimenti
una pagina automatica elenca l'aiuto dei campi.

La casella nell'intestazione della finestra di aiuto cerca un testo nella
pagina, come Ctrl+F del browser (che la seleziona). Maiuscole e accenti sono
ignorati, come gli a capo e le parole in grassetto o con link. Con più parole
quelle di 1-2 lettere sono ignorate e sono mostrati solo i punti in cui sono tutte entro 12 parole nello stesso
paragrafo; se non ce ne sono, è mostrata ogni occorrenza di ogni parola e il
contatore indica *qualsiasi parola*. Il testo tra virgolette
(``"bozza fattura"``) è cercato come frase esatta.
**Invio** / ▼ e **Maiusc+Invio** / ▲ passano all'occorrenza successiva /
precedente, **Esc** annulla la ricerca.

La sezione *Domande frequenti* di una pagina e l'aiuto dei campi del suo
modello sono mostrati in pagine a parte, aperte dai pulsanti **FAQ** e
**Campi** nell'intestazione della finestra di aiuto; il pulsante **Aiuto**
torna alla pagina. Le domande costruite da ``help-question`` ``:auto:`` sono
lasciate alla pagina **Campi**.

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
Ogni pagina lista riceve il testo *Ricerche con il carattere jolly* di
web_context_help (``help/common/search_wildcard.it_IT.rst``) in fondo alla
sezione ``search``: non scriverlo nel modulo; una sezione della pagina con
etichetta ``wildcard`` viene sostituita.

::

    .. help-page:: partner
       :title: Partner
       :model: res.partner
       :view: base.view_partner_form
       :view-type: form
       :when: is_company = True

    .. help-include:: parte_comune.rst

    .. help-inherit:: altro_modulo.partner
       :section: usage
       :position: after

       RST aggiunto dopo la sezione con etichetta "usage"

    .. help-question:: Come aggiungo un'etichetta?

       Usare il campo :field:`Etichette <category_id>`.

    .. help-question::
       :auto:

``:when:`` mostra la pagina solo quando il record aperto (i suoi campi di
selezione e booleani) o il menu (le sue chiavi di contesto ``default_<campo>``)
corrispondono: condizioni ``campo = valore``, ``campo != valore``, più valori
separati da virgola, più condizioni unite da ``and``. Quando il valore non è
noto la pagina non è usata, ad es. ``move_type != entry`` tiene l'aiuto delle
fatture lontano dalle registrazioni contabili, che usano la stessa maschera
delle fatture.

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
