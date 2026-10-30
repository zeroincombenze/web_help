.. help-page:: res_partner_list
   :title: Contatti
   :model: res.partner
   :view-type: list
   :priority: 96

Contatti
========

.. _description:

Descrizione
-----------

.. help-version:: <16

   L'elenco dei contatti. Ogni riga mostra il :field:`nome <display_name>` (con
   l'azienda di una persona), il :field:`telefono <phone>` e l':field:`email
   <email>`. Fare clic su una riga per aprire il contatto.

.. help-version:: >=16

   L'elenco di aziende, persone e indirizzi. Ogni riga mostra il
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
