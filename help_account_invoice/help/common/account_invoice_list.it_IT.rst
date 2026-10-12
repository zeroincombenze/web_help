.. help-version:: <13

   .. help-page:: account_invoice_list
      :title: Fatture
      :model: account.invoice
      :view: account.invoice_tree, account.invoice_tree_with_onboarding, account.invoice_supplier_tree
      :view-type: list

.. help-version:: 13

   .. help-page:: account_invoice_list
      :title: Fatture
      :model: account.move
      :view: account.view_invoice_tree, account.view_out_invoice_tree, account.view_in_invoice_tree
      :view-type: list
      :when: type != entry

.. help-version:: >=14

   .. help-page:: account_invoice_list
      :title: Fatture
      :model: account.move
      :view: account.view_invoice_tree, account.view_out_invoice_tree, account.view_in_invoice_tree
      :view-type: list
      :when: move_type != entry

Fatture
=======

.. _description:

Descrizione
-----------

.. help-version:: <13

   La lista delle fatture clienti, o delle fatture fornitore, secondo il menu.
   Ogni riga mostra il :field:`numero <number>`, il :field:`partner
   <partner_id>`, la :field:`data fattura <date_invoice>`, la :field:`data di
   scadenza <date_due>`, il totale, l'importo ancora dovuto e lo
   :field:`stato <state>`. Fare clic su una riga per aprire la fattura.

.. help-version:: >=13

   La lista delle fatture clienti, note di credito, fatture fornitore o note
   di credito fornitore, secondo il menu. Ogni riga mostra il :field:`numero
   <name>`, il :field:`partner <partner_id>`, la :field:`data fattura
   <invoice_date>`, la :field:`data di scadenza <invoice_date_due>`, il
   totale, l'importo ancora dovuto e lo :field:`stato <state>`\
   :version:`>=14|, con lo stato del pagamento`. Fare clic su una riga per
   aprire la fattura.

.. help-include:: account_invoice_list_search.rst

.. help-include:: account_invoice_configure.rst

.. help-include:: account_invoice_report.rst

.. help-include:: account_invoice_list_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non vedo le note di credito?

   .. help-version:: 10

      Le note di credito sono nella stessa lista delle fatture: usare il filtro
      *Note credito*, o *Fatture* per nasconderle.

   .. help-version:: 11

      Hanno un loro menu: **Fatturazione ‣ Vendite ‣ Note di credito
      cliente**, e **Fatturazione ‣ Acquisti ‣ Note di credito fornitore** per
      i fornitori.

   .. help-version:: >=12

      Hanno un loro menu: **Fatturazione ‣ Clienti ‣ Note di credito**, e
      **Fatturazione ‣ Fornitori ‣**
      :version:`12|**Rimborsi**;13|**Rimborso**;*|**Note di credito**` per i
      fornitori.

.. help-question:: Come vedo le fatture ancora da pagare?

   Usare il filtro :version:`10|*Non pagato*;11-12|*Aperta*;13|*Non
   pagato*;14|*Non pagata*;15-17|*Non pagato*;*|*Da pagare*`;
   :version:`10|*Scaduto*;11|*Ritardi*;*|*In ritardo*` mostra solo quelle con
   la scadenza passata.

.. help-question:: Perché vedo qui delle registrazioni contabili?

   .. help-version:: <13

      La lista mostra solo fatture; le registrazioni contabili sono nei menu
      della contabilità, visibili ai contabili.

   .. help-version:: >=13

      Una fattura è una registrazione contabile di tipo fattura: i menu delle
      fatture mostrano solo i tipi fattura, mentre la lista delle registrazioni
      contabili dei contabili mostra ogni registrazione, fatture comprese, e
      non ha l'aiuto delle fatture.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-02 07:23 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
