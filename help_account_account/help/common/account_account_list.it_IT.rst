.. help-page:: account_account_list
   :title: Piano dei conti
   :model: account.account
   :view: account.view_account_list
   :view-type: list
   :priority: 96

Piano dei conti
===============

.. _description:

Descrizione
-----------

Fare clic sul pulsante [`Pronto`] per sapere come usare questo aiuto; fare
clic sul pulsante [`FAQ`] per le domande più comuni già risolte.

Il piano dei conti: l'elenco dei conti di contabilità generale su cui si
registrano le righe delle scritture. Ogni riga mostra il :field:`codice
<code>`, il :field:`nome conto <name>`, la :field:`tipologia <account_type>` e
l'interruttore *Consentire riconciliazione*; le altre colonne (gruppo,
imposte predefinite, etichette, registri autorizzati, *Non commerciale*) si
mostrano con l'interruttore a destra dell'intestazione. Le righe sono ordinate
per codice. Le righe si possono modificare sul posto, senza aprire la
maschera.

.. _new_record:

Come inserire un nuovo record
-----------------------------

Premere [`Nuovo`] in alto a sinistra: in cima all'elenco si apre una riga
vuota, dove scrivere il codice, il nome e la tipologia del conto. Vedere
l'aiuto della maschera per il significato dei campi e per gli altri.

.. help-include:: account_account_list_search.rst

.. _update_record:

Come modificare un record
-------------------------

Fare clic su una riga dell'elenco per modificarla sul posto; per vedere tutti
i suoi campi premere il pulsante con la freccia a fine riga (*Apri nella vista
modulo*) e seguire l'aiuto della maschera.

.. help-include:: account_account_cancel.rst

.. help-include:: account_account_configure.rst

.. help-include:: account_account_report.rst

.. help-include:: account_account_example.rst

.. _faq:

Domande frequenti
-----------------

Fare clic sul pulsante [`Argomento`] per tornare alla pagina di aiuto specifica.

.. help-question:: Perché non vedo alcuni conti?

   L'elenco si apre con il filtro *Conto attivo*, che nasconde i conti non
   attivi. Togliere il filtro per vederli tutti. In un database multi-azienda
   si vedono i conti dell'azienda in cui si lavora: cambiarla con il selettore
   delle aziende nella barra in alto.

.. help-question:: Perché non vedo il menu Piano dei conti?

   Il menu **Fatturazione ‣ Configurazione** è mostrato agli utenti con il
   diritto di accesso *Contabilità / Amministratore*; il piano dei conti è
   vuoto finché non si sceglie un pacchetto di *Localizzazione fiscale*,
   vedere *Come configurare*.

.. help-question:: Come mostro le imposte predefinite o le etichette dei conti?

   Usare l'interruttore a destra dei titoli delle colonne e spuntare
   *Imposte predefinite*, *Etichette*, *Registri autorizzati*, *Gruppo* o
   *Non commerciale*.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-22 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
