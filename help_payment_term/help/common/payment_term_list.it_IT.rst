.. help-page:: payment_term_list
   :title: Termini di pagamento
   :model: account.payment.term
   :view: account.view_payment_term_tree
   :view-type: list

Termini di pagamento
====================

.. _description:

Descrizione
-----------

La lista dei termini di pagamento: ognuno calcola le scadenze delle fatture
che lo usano. Ogni riga mostra il :field:`nome <name>` e, in un database
multi-azienda, l':field:`azienda <company_id>`. I termini sono elencati
:version:`<11|per nome;*|nell'ordine degli elenchi di scelta`. Cliccare una
riga per aprire il termine e vederne le righe.

.. help-include:: payment_term_list_search.rst

.. help-include:: payment_term_configure.rst

.. help-include:: payment_term_report.rst

.. help-include:: payment_term_list_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Perché non vedo alcuni termini di pagamento?

   I termini archiviati sono nascosti: :version:`<13|cercarli con un filtro
   personalizzato *Attivo* non impostato;*|usare il filtro *Archiviati* per
   vederli`, aprirli e :version:`<17|usare **Azione ‣ Annulla
   archiviazione**;*|usare l'icona dell'ingranaggio ‣ **Annulla
   archiviazione**` per usarli di nuovo. In un database multi-azienda si
   vedono solo i termini delle proprie aziende, e quelli senza azienda.

.. help-question:: Come cambio l'ordine dei termini negli elenchi di scelta?

   .. help-version:: <11

      I termini sono ordinati per nome: rinominarli, ad es. con un numero
      davanti.

   .. help-version:: >=11

      Trascinare le righe con la maniglia a sinistra: i termini sono proposti
      in quell'ordine.

.. help-question:: Quali termini di pagamento fornisce già Odoo?

   Il modulo ``account`` installa i più comuni:
   :version:`<12|*Immediate Payment*, *15 Days* e *30 Net Days*;12-13|*Immediate
   Payment*, *15 Days*, *30 Net Days*, *45 Days* e *2 Months*;14-15|*Immediate
   Payment*, *15 Days*, *21 Days*, *30 Days*, *45 Days*, *2 Months*, *End of
   Following Month* e *30% Now, Balance 60 Days*;16|*Immediate Payment*, *15
   Days*, *21 Days*, *30 Days*, *45 Days*, *2 Months*, *End of Following
   Month*, *30 days End of Month on the 10th*, *30% Now, Balance 60 Days* e
   *2/7 Net 30*;*|*Immediate Payment*, *15 Days*, *21 Days*, *30 Days*, *45
   Days*, *End of Following Month*, *10 Days after End of Next Month*, *30%
   Now, Balance 60 Days* e *2/7 Net 30*`, con il nome tradotto se la lingua
   italiana è caricata. Cambiare o archiviare quelli che non si usano.

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-12 06:38 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
