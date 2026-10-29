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

L'elenco dei contatti. Ogni riga mostra il :field:`nome <display_name>` (con
l'azienda di una persona), il :field:`telefono <phone>` e l':field:`email
<email>`. Fare clic su una riga per aprire il contatto.

.. help-include:: res_partner_list_search.rst

.. help-include:: res_partner_configure.rst

.. help-include:: res_partner_report.rst

.. help-include:: res_partner_list_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non vedo tutti i contatti?

   Il menu può mostrare solo i clienti o solo i fornitori: *Vendite ‣
   Vendite ‣ Clienti* parte con il filtro *Clienti*, *Acquisti ‣ Acquisto ‣
   Fornitori* con il filtro *Fornitori*. Togliere il filtro dalla barra di
   ricerca. I contatti archiviati si vedono solo con il filtro *Archiviato*.

.. help-question:: Perché un contatto compare due volte?

   Una persona è mostrata con il nome dell'azienda (*Azienda, Persona*):
   l'azienda e le sue persone sono record distinti. Un vero duplicato si può
   archiviare; vedere *Esempi*.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-29 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
