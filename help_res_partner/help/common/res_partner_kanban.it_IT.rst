.. help-page:: res_partner_kanban
   :title: Contatti (kanban)
   :model: res.partner
   :view-type: kanban
   :priority: 96

Contatti (kanban)
=================

.. _description:

Descrizione
-----------

Fare clic sul pulsante **Pronto** per sapere come usare questo aiuto; fare
clic sul pulsante **FAQ** per le domande più comuni già risolte.

.. help-version:: <16

   I contatti come schede, la vista predefinita dei menu dei contatti. Ogni
   scheda mostra l'immagine, il :field:`nome <display_name>`, la
   :field:`posizione lavorativa <function>`, città e nazione, l'email e i
   :field:`tag <category_id>`. Fare clic su una scheda per aprire il contatto; i
   pulsanti in alto a destra della barra di ricerca passano alla lista.

.. help-version:: >=16

   L'elenco di aziende, persone e indirizzi. Ogni scheda mostra il
   :field:`nome <name>`, l':field:`e-mail <email>`, il :field:`telefono
   <phone>` e la :field:`città <city>`. Fare clic per aprire il contatto.
   I pulsanti in alto a destra passano dal kanban alla lista e alle altre viste.

.. help-include:: res_partner_list_search.rst

.. help-include:: res_partner_configure.rst

.. help-include:: res_partner_report.rst

.. help-include:: res_partner_list_example.rst

.. _faq:

Domande frequenti
-----------------

Fare clic sul pulsante **Argomento** per tornare alla pagina di aiuto specifica.

.. help-version:: <16

   .. help-question:: Perché non vedo tutti i contatti?

      Il menu può mostrare solo i clienti o solo i fornitori: *Vendite ‣
      Vendite ‣ Clienti* parte con il filtro *Clienti*, *Acquisti ‣ Acquisto ‣
      Fornitori* con il filtro *Fornitori*. Togliere il filtro dalla barra di
      ricerca. I contatti archiviati si vedono solo con il filtro *Archiviato*.

   .. help-question:: Perché un contatto compare due volte?

      Una persona è mostrata con il nome dell'azienda (*Azienda, Persona*):
      l'azienda e le sue persone sono record distinti. Un vero duplicato si può
      archiviare; vedere *Esempi*.

.. help-version:: >=16

   .. help-question:: Dove sono i contatti archiviati?

      Scegliere il filtro *In archivio*; aprire un contatto e usare **Azioni ‣
      Annulla archiviazione** per recuperarlo.

   .. help-question:: Perché vedo più volte la stessa azienda?

      Anche gli indirizzi e le persone di un'azienda sono contatti: scegliere il
      filtro *Aziende* per vedere solo le aziende.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-30 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
