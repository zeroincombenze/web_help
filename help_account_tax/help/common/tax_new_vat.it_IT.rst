.. _new_record_vat:

Come inserire un'imposta con IVA
--------------------------------

Il pacchetto *Italia* carica, per le vendite, le imposte *22%*, *10%*, *5%* e
*4%* e, per gli acquisti, le stesse aliquote in due serie: *22% M*, *10% M*,
*5% M*, *4% M* con :field:`Ambito imposta <tax_scope>` *Beni* (*M* per merci)
e *22% S*, *10% S*, *5% S*, *4% S* con ambito *Servizi*. Le imposte predefinite
dell'azienda sono *22%* sulle vendite e *22% M* sugli acquisti.

#. Aprire **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Imposte** e cercare
   l'aliquota, ad es. ``22%``.
#. Le imposte *5%* e *4%*, vendite e acquisti, sono archiviate quando il
   pacchetto viene installato: fare clic sull'interruttore **Attivo** di
   quelle che servono.
#. Aprire un'imposta per controllarla. Nella scheda **Opzioni avanzate** il
   :field:`Gruppo imposta <tax_group_id>` è quello dell'aliquota (*IVA 22%*,
   *IVA 10%*, *IVA 5%* o *IVA 4%*) e la :field:`Nazione <country_id>` è
   *Italia*. Nella scheda **Definizione** la ripartizione ha la riga di
   riferimento e una riga *dell'imposta* sul conto *Debito IVA* (vendite) o
   *Credito IVA* (acquisti), con le griglie imposta del report IVA.
#. Per un'altra aliquota (il pacchetto ha i gruppi imposta anche per 2%, 12%,
   20% e 21%) seguire *Come inserire un nuovo record per duplicazione*,
   duplicando l'imposta dello stesso tipo, ad es. *22%* per una vendita al
   21%.

