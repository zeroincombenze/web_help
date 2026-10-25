.. help-page:: payment_term_form
   :title: Termini di pagamento
   :model: account.payment.term
   :view: account.view_payment_term_form
   :view-type: form
   :priority: 96

Termini di pagamento
====================

.. _description:

Descrizione
-----------

I termini di pagamento dicono quando un cliente deve pagare una fattura, o
quando si deve pagare una fattura fornitore: Odoo calcola
:version:`<13|la data di scadenza;*|le scadenze` della fattura dalla data
fattura e dalle righe del termine. I termini di pagamento si scelgono sul
partner e sono proposti sugli ordini di vendita, sugli ordini di acquisto e
sulle fatture.

Ogni termine ha un :field:`nome <name>`, mostrato negli elenchi di scelta (ad
es. *30 giorni*), una :field:`descrizione in fattura <note>`, stampata sul
PDF, e una o più :field:`righe <line_ids>`: ogni riga è una rata, con il suo
importo e la sua scadenza. Una riga calcola la scadenza dalla data fattura:
aggiunge giorni (o mesi) e può spostare la data alla fine del mese o a un
giorno fisso del mese.

.. help-include:: payment_term_lines.rst

.. help-include:: payment_term_new.rst

.. help-include:: payment_term_update.rst

.. help-include:: payment_term_configure.rst

.. help-include:: payment_term_report.rst

.. help-include:: payment_term_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non riesco a salvare il termine di pagamento?

   .. help-version:: <17

      Il termine richiede esattamente una riga di tipo *Saldo*,
      :version:`<16|e deve essere l'ultima riga;*|per il resto dell'importo`.
      Le percentuali devono essere tra 0 e 100.

   .. help-version:: >=17

      Le righe *Percentuale* devono sommare 100%: ad es. 30% e 70%, o una sola
      riga al 100%. Una riga *Fisso* si aggiunge a queste.

.. help-question:: Ho cambiato il termine di pagamento: perché le fatture mantengono la vecchia scadenza?

   Le scadenze si calcolano quando la fattura è
   :version:`<13|validata;*|creata o quando si sceglie il termine`, e restano
   salvate sulla fattura. Le fatture già
   :version:`<13|validate;*|registrate` mantengono le loro scadenze; il nuovo
   termine vale per le nuove fatture, o per una fattura in bozza quando si
   sceglie di nuovo il termine.

.. help-question:: Perché non riesco a eliminare il termine di pagamento?

   I termini usati dalle fatture non si possono eliminare: archiviarli, così
   non sono più proposti ma le vecchie fatture li mantengono.

.. help-question:: Cosa significa il giorno 31 in un mese di 30 giorni?

   Un giorno oltre la fine del mese significa l'ultimo giorno del mese: 31 è
   il 30 aprile e il 28 (o 29) febbraio. Usare 31 per dire *fine mese*.

.. help-question:: Perché "fine mese + 30 giorni" non è "30 giorni fine mese"?

   *Fine mese + 30 giorni* conta i giorni dalla fine del mese della fattura:
   una fattura del 15 gennaio scade il 2 marzo. *30 giorni fine mese* conta 30
   giorni dalla data fattura e poi va alla fine di quel mese: la stessa
   fattura scade il 28 febbraio. Vedere *Esempi*.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-12 06:38 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
