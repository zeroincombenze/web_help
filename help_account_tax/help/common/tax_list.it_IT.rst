.. help-page:: tax_list
   :title: Imposte
   :model: account.tax
   :view: account.view_tax_tree
   :view-type: list
   :priority: 96

Imposte
=======

.. _description:

Descrizione
-----------

Fare clic sul pulsante [`Pronto`] per sapere come usare questo aiuto; fare
clic sul pulsante [`FAQ`] per le domande più comuni già risolte.

La lista delle imposte: i codici che Odoo applica alle righe fattura per
calcolare l'IVA (o un'altra imposta) e per compilare i registri e le
liquidazioni. Ogni riga mostra il :field:`nome imposta <name>`, la
:field:`descrizione <description>`, il :field:`tipo imposta <type_tax_use>`
(*Vendita*, *Acquisti* o *Nessuno*), l':field:`ambito imposta <tax_scope>`
(*Servizi* o *Beni*), l':field:`etichetta su fatture <invoice_label>`, in un
database multi-azienda l':field:`azienda <company_id>`, e l'interruttore
**Attivo**. Le imposte archiviate sono mostrate anch'esse, in grigio. Fare clic
su una riga per aprire l'imposta.

.. _new_record:

Come inserire un nuovo record
-----------------------------

Premere [`Nuovo`] in alto a sinistra: si apre una maschera vuota, vedere il
suo aiuto per i campi da compilare.

.. help-include:: tax_list_search.rst

.. _update_record:

Come modificare un record
-------------------------

Fare clic su una riga dell'elenco per aprire la sua maschera, poi seguire
l'aiuto della maschera per modificarla.

.. help-include:: tax_cancel.rst

.. help-include:: tax_configure.rst

.. help-include:: tax_report.rst

.. help-include:: tax_list_example.rst

.. _faq:

FAQ
---

Fare clic sul pulsante [`Argomento`] per tornare alla pagina di aiuto
specifica.

.. help-question:: Perché non vedo alcune imposte?

   La lista si apre con i filtri **Vendita** e **Acquisto**: le imposte di
   tipo *Nessuno*, ad es. le figlie delle imposte di scissione dei pagamenti,
   sono nascoste. Togliere i filtri, o cercare per nome, per vederle. Le
   imposte archiviate sono nella lista, in grigio.

.. help-question:: Come attivo un'imposta arrivata con la localizzazione fiscale?

   Fare clic sul suo interruttore **Attivo** a fine riga. Alcune imposte del
   pacchetto italiano, ad es. 5% e 4% o la maggior parte di quelle di
   inversione contabile, sono archiviate quando il pacchetto viene
   installato. Vedere *Come configurare*.

.. help-question:: Quali imposte fornisce Odoo per l'Italia?

   Quelle del modulo ``l10n_it`` (**Italy - Accounting**), caricate quando si
   sceglie *Italia* come *Pacchetto* in **Fatturazione ‣ Configurazione ‣
   Impostazioni**. Vedere *Come configurare*.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-22 16:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
