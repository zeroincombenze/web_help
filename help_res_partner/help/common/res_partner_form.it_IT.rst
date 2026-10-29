.. help-page:: res_partner_form
   :title: Contatto
   :model: res.partner
   :view-type: form
   :priority: 96

Contatto
========

.. _description:

Descrizione
-----------

Un contatto (partner) è chiunque abbia rapporti con l'azienda: clienti,
fornitori, dipendenti di altre aziende. Un contatto è un'**Azienda** o una
**Persona** (:field:`tipo azienda <company_type>`); una persona può
appartenere a un':field:`azienda <parent_id>`. Un'azienda conserva le sue
persone e gli altri indirizzi (fatturazione, consegna, …) nella scheda
**Contatti e indirizzi**: ordini di vendita, fatture e consegne scelgono da lì
l'indirizzo giusto.

.. help-include:: res_partner_fields.rst

.. help-include:: res_partner_new.rst

.. help-include:: res_partner_update.rst

.. help-include:: res_partner_configure.rst

.. help-include:: res_partner_report.rst

.. help-include:: res_partner_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non riesco a cambiare l'indirizzo di un contatto?

   Un contatto di tipo *Contatto* che appartiene a un'azienda condivide
   l'indirizzo dell'azienda: cambiarlo sull'azienda, oppure impostare per il
   contatto un altro tipo di indirizzo.

.. help-question:: Perché non riesco a cambiare la partita IVA?

   La partita IVA di una persona che appartiene a un'azienda è quella
   dell'azienda: cambiarla sull'azienda.

.. help-question:: Odoo avvisa che esiste un partner con la stessa partita IVA.

   Probabilmente il contatto è un doppione: aprire quello esistente, oppure
   unire i due dall'elenco (vedere *Modifica record*).

.. help-question:: Perché non riesco a eliminare il contatto?

   Un contatto usato da documenti (ordini, fatture, pagamenti, …) non si può
   eliminare: archiviarlo.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-29 22:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
