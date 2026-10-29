.. _example:

Esempi
------

**Il fornitore consegna in due spedizioni**

#. Confermare l'ordine di 100 unità e premere **Prodotti in entrata**.
#. Indicare 60 come quantità fatta e premere **Valida**, poi scegliere **Crea
   ordine arretrato**: le 40 unità mancanti restano in un nuovo ricevimento.
#. Con la politica *Quantitativi ricevuti*, la fattura fornitore creata ora
   propone 60 unità; l'ordine resta *Attesa fattura* finché il resto non è
   ricevuto e fatturato.

**Il fornitore aumenta il prezzo dopo la conferma**

Aprire l'ordine, premere **Modifica**, cambiare il **Prezzo Unitario** della
riga e **Salva**: il nuovo prezzo è proposto sulla fattura del fornitore.

**Gli ordini oltre 5.000 richiedono l'approvazione del responsabile**

#. In **Acquisti ‣ Configurazione ‣ Configurazione** scegliere *Ottieni 2
   livelli di approvazione per confermare un ordine d'acquisto* e impostare
   l'importo a 5.000.
#. Un utente acquisti che conferma un ordine di 8.000 ottiene lo stato *Da
   Approvare*; il responsabile lo apre e preme **Approva Ordine**.

**Il fornitore non può fornire la merce**

Premere **Annulla**; l'ordine resta nell'elenco con stato *Annullato* e si può
poi eliminare.
