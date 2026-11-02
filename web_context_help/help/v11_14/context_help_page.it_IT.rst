.. help-page:: context_help_page
   :title: Pagine di aiuto
   :model: context.help.page
   :view: web_context_help.context_help_page_tree, web_context_help.context_help_page_form

Pagine di aiuto
===============

Ogni modulo può spiegare le proprie maschere con file RST nella cartella
``help/``. Sono letti a ogni avvio del server e trasformati nelle pagine qui
elencate. Il pulsante |sos| del pannello di controllo apre l'aiuto della vista
corrente in una finestra separata: la scheda di Odoo resta utilizzabile e, con
*Segui Odoo* attivo, la finestra di aiuto segue la navigazione.

.. |sos| unicode:: U+1F6DF

.. _page_fields:

Campi
-----

:field:`Chiave <key>` è ``<modulo>.<nome>``; :field:`Viste <view_xmlid>`,
:field:`Modello <model>` e :field:`Tipo vista <view_type>` decidono quale vista
apre la pagina.

.. _rules:

Regole
------

La scheda **Regole** sceglie la pagina in base a un campo del record aperto,
senza sorgente RST: campo (selezione, booleano o many2one), *è* o *non è*, e il
valore. I valori di un campo selezione si scrivono con le loro chiavi, separate
da virgola (ad es. ``draft, sent``): i *Valori ammessi* della maschera della
regola le elencano. La scheda è presente sulle pagine **Clear cut**: una pagina clear cut è
mostrata solo quando una delle sue regole è soddisfatta, ad es. l'aiuto di un
tipo di ordine. Quale pagina prevale lo stabilisce la sua **Priorità** (1 è la
più alta):

* le pagine clear cut vengono prima, in ordine di priorità: è mostrata la
  prima con una regola soddisfatta;
* se nessuna regola è soddisfatta, è mostrata la pagina generale (non clear
  cut) con la priorità più alta: le proprie pagine (predefinita 32) vengono
  prima delle pagine dei moduli (96), che sono l'ultima alternativa.

Una pagina clear cut, o di priorità 64 o inferiore, mostra il pulsante **Aiuto
generale**: apre l'aiuto generale dello stesso record, cioè la pagina generale
di priorità 64 o superiore con la priorità più alta, di solito la pagina del
modulo.

Tutte le regole sono elencate anche in *Regole di aiuto*. Una pagina creata con
**Nuovo** o **Duplica** non ha sorgente ed è conservata da **Ricostruisci tutte
le pagine**; un duplicato riceve la chiave della pagina seguita da " (copy)".

.. help-include:: editing.rst

Premere **Modifica** per cambiare la pagina e **Salva** al termine. Il
pulsante **Inserisci video** elenca i video della cartella dei video
(parametro di sistema ``web_help_video_path``): quello scelto è aggiunto in
fondo alla pagina, oppure dopo il paragrafo che contiene il testo scritto in
*Dopo il testo*.

.. _faq:

Domande
-------

.. help-question:: Perché la modifica al file RST non compare?

   Le pagine sono ricostruite all'avvio del server quando cambia il checksum
   di una sorgente. Riavviare il server o premere **Ricostruisci tutte le pagine**.

.. help-question::
   :auto:
