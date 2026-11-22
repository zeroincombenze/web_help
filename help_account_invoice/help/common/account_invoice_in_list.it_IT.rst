.. help-version:: <13

   .. help-page:: account_invoice_in_list
      :title: Fatture fornitore
      :model: account.invoice
      :view: account.invoice_supplier_tree
      :view-type: list
      :priority: 96

.. help-version:: 13

   .. help-page:: account_invoice_in_list
      :title: Fatture fornitore
      :model: account.move
      :view: account.view_invoice_tree, account.view_in_invoice_tree
      :view-type: list
      :when: type = in_invoice, in_refund, in_receipt
      :priority: 96

.. help-version:: >=14

   .. help-page:: account_invoice_in_list
      :title: Fatture fornitore
      :model: account.move
      :view: account.view_invoice_tree, account.view_in_invoice_tree, account.view_in_invoice_bill_tree, account.view_in_invoice_refund_tree, account.view_in_invoice_receipt_tree
      :view-type: list
      :when: move_type = in_invoice, in_refund, in_receipt
      :priority: 96

Fatture fornitore
=================

.. _description:

Descrizione
-----------

Fare clic sul pulsante [`Pronto`] per sapere come usare questo aiuto; fare
clic sul pulsante [`FAQ`] per le domande più comuni già risolte.

.. help-version:: <13

   La lista delle fatture fornitore e delle loro note di credito, secondo il
   menu: quanto i fornitori chiedono di pagare. Ogni riga mostra il
   :field:`fornitore <partner_id>`, la :field:`data fattura <date_invoice>`, il
   :field:`numero <number>`, il :field:`riferimento fornitore <reference>`, la
   :field:`data di scadenza <date_due>`, il totale, l'importo ancora da pagare
   e lo :field:`stato <state>`. Fare clic su una riga per aprire la fattura.

.. help-version:: >=13

   La lista delle fatture fornitore e delle loro note di credito, secondo il
   menu: quanto i fornitori chiedono di pagare. Ogni riga mostra il
   :field:`numero <name>`, il :field:`fornitore <partner_id>`, la :field:`data
   fattura <invoice_date>`, la :field:`data di scadenza <invoice_date_due>`, il
   totale, l'importo ancora dovuto e lo :field:`stato <state>`\
   :version:`>=14|, con lo stato del pagamento`. Fare clic su una riga per
   aprire la fattura.

.. _new_record:

Come inserire un nuovo record
-----------------------------

Premere :version:`<16|[\`Crea\`];*|[\`Nuovo\`]` in alto a sinistra: si apre una
maschera vuota, vedere il suo aiuto per i campi da compilare.
:version:`>=17|[\`Carica\`] crea una fattura dal PDF inviato dal fornitore.`

.. help-include:: account_invoice_in_list_search.rst

.. _update_record:

Come modificare un record
-------------------------

Fare clic su una riga dell'elenco per aprire la sua maschera, poi seguire
l'aiuto della maschera per modificarla.

.. help-include:: account_invoice_in_cancel.rst

.. help-include:: account_invoice_in_list_actions.rst

.. help-include:: account_invoice_in_configure.rst

.. help-include:: account_invoice_in_report.rst

.. help-include:: account_invoice_in_list_example.rst

.. _faq:

Domande frequenti
-----------------

Fare clic sul pulsante [`Argomento`] per tornare alla pagina di aiuto specifica.

.. help-question:: Perché non vedo le note di credito fornitore?

   .. help-version:: 10

      Le note di credito sono nella stessa lista delle fatture: usare il filtro
      *Note credito*, o *Fatture* per nasconderle.

   .. help-version:: >=11

      Hanno un loro menu:
      :version:`11|**Fatturazione ‣ Acquisti ‣ Note di credito
      fornitore**;12|**Fatturazione ‣ Fornitori ‣ Rimborsi**;13|**Fatturazione
      ‣ Fornitori ‣ Rimborso**;*|**Fatturazione ‣ Fornitori ‣ Note di
      credito**`.

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

      Una fattura fornitore è una registrazione contabile di tipo fattura: i
      menu dei fornitori mostrano solo i tipi fattura, mentre la lista delle
      registrazioni contabili dei contabili mostra ogni registrazione, fatture
      comprese, e non ha l'aiuto delle fatture.

.. help-if:: module = purchase

   .. help-question:: Dove compaiono le fatture di un ordine di acquisto?

      Anche in questa lista: una fattura creata da un ordine di acquisto è una
      normale fattura fornitore, collegata all'ordine. Vedere l'aiuto della
      maschera per come crearla.

.. help-version:: 18

   .. help-include:: account_invoice_in_faq_einvoice.rst

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-11-20 10:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
