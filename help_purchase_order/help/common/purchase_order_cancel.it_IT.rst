.. _cancel:

Come annullare o eliminare un record
------------------------------------

#. [`Annulla`] compare su :version:`10|*RFQ*, *RFQ Inviata*, *Da Approvare*
   e *Ordine di Acquisto*;11|*RDP*, *RDP Inviata*, *Da Approvare* e *Ordine
   di Acquisto*;*|*RdP*, *RdP inviata*, *Da approvare* e *Ordine di
   acquisto*`. :version:`<=18|Su un ordine *Bloccato*;*|Su un ordine
   bloccato` un responsabile acquisti preme prima [`Sblocca`].

   .. help-version:: <=18

      L'annullamento è rifiutato quando parte della merce è già ricevuta, o
      quando una fattura fornitore dell'ordine non è né in bozza né
      annullata: annullare prima la fattura. Altrimenti l'ordine diventa
      *Annullato* e anche i suoi ricevimenti sono annullati.

   .. help-version:: >=19

      L'annullamento è rifiutato quando una fattura fornitore dell'ordine non
      è né in bozza né annullata: annullare prima la fattura. L'ordine diventa
      *Annullato* e i suoi ricevimenti non ancora completati sono annullati;
      i ricevimenti già completati restano come sono, con una nota
      sull'ordine annullato.

#. :version:`10|[\`Imposta come Bozza\`];11|[\`Imposta a Bozza\`];*|[\`Imposta a
   bozza\`]` riporta un ordine *Annullato* a :version:`10|*RFQ*;11|*RDP*;*|*RdP*`,
   per modificarlo e confermarlo di nuovo.
#. Si possono eliminare solo gli ordini annullati: nella maschera usare
   :version:`<17|**Azione ‣ Elimina**;*|l'icona dell'ingranaggio ‣
   **Elimina**`, nell'elenco selezionare gli ordini e usare
   :version:`<17|**Azione ‣ Elimina**;*|**Azioni ‣ Elimina**`. Ogni altro
   ordine va prima annullato.
#. Gli ordini di acquisto non si possono archiviare: gli ordini annullati
   restano nell'elenco.
