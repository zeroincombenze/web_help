.. _cancel:

Come annullare o eliminare un record
------------------------------------

#. [`Annulla`] compare su *Preventivo*, *Preventivo inviato* e *Ordine di
   vendita*. :version:`10|Un ordine *Bloccato* non si può annullare né
   sbloccare.;<=16|Su un ordine *Bloccato* premere prima [\`Sblocca\`].;*|Su un
   ordine bloccato (icona del lucchetto) premere prima [\`Sblocca\`].`

   .. help-version:: 10

      L'ordine diventa *Annullato*. Le fatture già create non cambiano:
      annullarle dalla fattura.

   .. help-version:: 11-12

      L'ordine diventa *Annullato* e, con Magazzino, le sue consegne sono
      annullate: l'ordine non si può annullare se una consegna è già
      completata. Le fatture già create non cambiano: annullarle dalla
      fattura.

   .. help-version:: 13

      L'ordine diventa *Annullato* e, con Magazzino, le consegne non ancora
      completate sono annullate. Le fatture già create non cambiano:
      annullarle dalla fattura.

   .. help-version:: 14-15

      Quando l'ordine ha fatture in bozza una finestra chiede conferma:
      premere [`Conferma`]. L'ordine diventa *Annullato*, le sue fatture in
      bozza sono annullate e, con Magazzino, le consegne non ancora completate
      sono annullate. Le fatture confermate non cambiano: emettere una nota di
      credito.

   .. help-version:: 16-18

      Su un ordine che non è più un preventivo in bozza una finestra propone
      un'e-mail al cliente: premere [`Invia e annulla`] per inviarla,
      [`Annulla`] per annullare senza e-mail, [`Abbandona`] per fermarsi.
      L'ordine diventa *Annullato*, le sue fatture in bozza sono annullate e,
      con Magazzino, le consegne non ancora completate sono annullate. Le
      fatture confermate non cambiano: emettere una nota di credito.

   .. help-version:: >=19

      Confermare con :version:`19|**Ok**;*|[\`Sì, annulla l'ordine\`]`.
      L'ordine diventa *Annullato*, le sue fatture in bozza sono annullate e,
      con Magazzino, le consegne non ancora completate sono annullate. Le
      fatture confermate non cambiano: emettere una nota di credito.

#. :version:`10|[\`Converti in preventivo\`];*|[\`Imposta a preventivo\`]` riporta
   un ordine *Annullato* a *Preventivo*, per modificarlo e confermarlo di
   nuovo.
#. Si possono eliminare solo i preventivi (mai inviati) e gli ordini
   annullati: nella maschera usare :version:`<17|**Azione ‣
   Elimina**;*|l'icona dell'ingranaggio ‣ **Elimina**`, nell'elenco
   selezionare gli ordini e usare :version:`<17|**Azione ‣
   Elimina**;*|**Azioni ‣ Elimina**`. Un preventivo inviato o un ordine
   confermato va prima annullato.
#. Gli ordini di vendita non si possono archiviare: gli ordini annullati
   restano nell'elenco, e i filtri :version:`10|*Preventivi* e
   *Vendite*;*|*Preventivi* e *Ordini di vendita*` li nascondono.
