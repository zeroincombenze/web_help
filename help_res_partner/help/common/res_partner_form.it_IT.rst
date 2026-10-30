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

.. help-version:: <16

   Un contatto (partner) è chiunque abbia rapporti con l'azienda: clienti,
   fornitori, indirizzi privati dei dipendenti e l'azienda stessa. Il :field:`tipo
   di azienda <company_type>` distingue un'**Azienda** da una **Persona**; una
   persona può appartenere a un'azienda tramite il campo :field:`azienda
   <parent_id>`. Un'azienda raggruppa le sue persone e i suoi indirizzi
   (fatturazione, spedizione, altro) nella scheda **Contatti & Indirizzi**; i dati
   commerciali (partita IVA, termini di pagamento, listino, conti) si gestiscono
   sull'azienda e sono condivisi con tutti loro.

.. help-version:: >=16

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

.. help-version:: <16

   .. help-question:: Perché non riesco a cambiare l'indirizzo di un contatto?

      Un contatto di tipo *Contatto* usa l'indirizzo della sua azienda: premere
      **(edit)** accanto all'indirizzo per cambiarlo sull'azienda, oppure
      cambiare il tipo indirizzo in *Indirizzo fattura*, *Indirizzo di
      Spedizione* o *Altro Indirizzo* per dare al contatto un indirizzo proprio.

   .. help-question:: Perché la scheda Contabilità è vuota per una persona di un'azienda?

      Termini di pagamento, posizione fiscale e conti si gestiscono sull'azienda:
      premere *the parent company* nella scheda per aprirla.

   .. help-question:: Perché non riesco a eliminare il contatto?

      Un contatto usato da ordini, fatture o registrazioni contabili non si può
      eliminare: archiviarlo invece con il pulsante **Attivo** in alto a destra.

   .. help-question:: Dov'è un contatto che ho archiviato?

      I contatti archiviati sono nascosti: nella lista usare il filtro
      *Archiviato*, aprire il contatto e premere il pulsante **Archiviato** per
      ripristinarlo.

   .. help-question:: Perché l'email è obbligatoria?

      Il contatto è collegato a un utente, che ha bisogno dell'email per
      accedere e ricevere le notifiche.

.. help-version:: >=16

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

Pagina creata il 2026-10-30 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
