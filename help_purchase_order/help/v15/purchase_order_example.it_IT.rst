.. _example:

Esempi
------

**Il fornitore consegna in due spedizioni**

#. Confermare l'ordine di 100 pezzi e aprire il ricevimento
   (:version:`<=14|**Ricevi prodotti**;*|il pulsante **Ricezione**`).
#. Indicare 60 come quantità fatta e premere **Valida**, poi scegliere **Crea
   ordine residuo**: i 40 pezzi mancanti restano in un nuovo ricevimento.
#. Con la politica *Su quantità ricevute*, la fattura fornitore creata ora
   propone 60 pezzi; l'ordine resta *In attesa di fatture* finché il resto non
   è ricevuto e fatturato.

**Il fornitore aumenta il prezzo dopo la conferma**

Aprire l'ordine, premere **Modifica**, cambiare il **Prezzo unitario** della
riga e **Salva**: il nuovo prezzo è proposto sulla fattura fornitore.

**Gli ordini oltre 5.000 richiedono l'approvazione del responsabile**

#. Nelle impostazioni selezionare :version:`11|*Approvazione
   Ordine*;*|*Approvazione ordine di acquisto*` e impostare l'*Importo minimo*
   a 5.000.
#. Un utente acquisti che conferma un ordine di 8.000 ottiene lo stato *Da
   approvare*; il responsabile lo apre e preme **Approva ordine**.

**Il fornitore non può fornire la merce**

Premere **Annulla**; l'ordine resta nell'elenco con stato *Annullato* e si può
poi eliminare.
