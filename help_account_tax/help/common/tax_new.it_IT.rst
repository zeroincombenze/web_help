.. _new_record:

Come inserire un nuovo record
-----------------------------

I passi caricano un'imposta con IVA, *21%* sulle vendite. Per i codici imposta
italiani con la natura (senza IVA, scissione dei pagamenti, inversione
contabile) vedere i capitoli *Come inserire un'imposta senza IVA*, *Come
inserire un'imposta per la scissione dei pagamenti* e *Come inserire
un'imposta per l'inversione contabile*.

.. help-version:: 18

   .. help-tour:: account_tax_new
      :label: Mostrami come creare un'imposta

      .. help-step:: new
         :click:

         Premere **Nuovo** per aprire una maschera imposta vuota.

      .. help-step:: field:name
         :position: right

         Scrivere il nome imposta, mostrato quando l'imposta è scelta su una
         riga.

      .. help-step:: field:amount_type
         :position: right

         Scegliere come è calcolata l'imposta: *Percentuale* per l'IVA.

      .. help-step:: field:type_tax_use
         :position: left

         Scegliere *Vendita* o *Acquisti*.

      .. help-step:: field:amount
         :position: left

         Scrivere l'aliquota.

      .. help-step:: tab:advanced_options
         :position: bottom
         :click:

         Aprire **Opzioni avanzate** per impostare l'etichetta, il gruppo
         imposta e la nazione.

#. Aprire **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Imposte** e premere
   [`Nuovo`].
#. Scrivere il :field:`nome imposta <name>`, ad es. *21%*: è il testo mostrato
   quando l'imposta è scelta su una riga. Il nome deve essere unico per lo
   stesso tipo, ambito e nazione.
#. Lasciare :field:`Calcolo imposta <amount_type>` su *Percentuale*; le altre
   opzioni sono *Fisso*, *Gruppo di imposte* e *Percentuale imposte incluse*.
#. Scegliere il :field:`Tipo imposta <type_tax_use>`: *Vendita* per le fatture
   cliente, *Acquisti* per le fatture fornitore; *Nessuno* per le imposte usate
   solo come figlie di un gruppo.
#. Scegliere l':field:`Ambito imposta <tax_scope>`, *Servizi* o *Beni*, oppure
   lasciarlo vuoto. L'ambito serve per gli acquisti in inversione contabile,
   vedere *Come inserire un'imposta per l'inversione contabile*.
#. Scrivere l'aliquota in :field:`Importo <amount>`, ad es. 21.
#. Nella scheda **Opzioni avanzate** l':field:`Etichetta su fatture
   <invoice_label>` è già compilata con l'aliquota (*21%*); scegliere il
   :field:`Gruppo imposta <tax_group_id>` (ad es. *IVA 21%*) e controllare la
   :field:`Nazione <country_id>` (*Italia*).
#. Nella scheda **Definizione** le tabelle **Ripartizione per fatture** e
   **Ripartizione per rimborsi** hanno una riga *Riferimento* e una riga
   *dell'imposta*, 100%: sulla riga *dell'imposta* scegliere il :field:`Conto
   <account_id>` (per il pacchetto italiano *Debito IVA* sulle vendite,
   *Credito IVA* sugli acquisti) e le **Griglie imposta** del report fiscale. È
   più facile **Duplicare** un'imposta simile del pacchetto e cambiarne nome e
   aliquota.
#. Con la localizzazione italiana, quando l'importo è 0% compilare
   :field:`Esenzione <l10n_it_exempt_reason>` e :field:`Riferimento
   legislativo <l10n_it_law_reference>`: vedere *Come inserire un'imposta
   senza IVA*.
#. Il record è salvato automaticamente uscendo dalla maschera, o subito con
   l'icona della nuvola accanto al percorso di navigazione.
