.. _example:

Esempi
------

**Ordine sopra l'importo di approvazione**

#. Con *Approvazione ordine di acquisto* impostata a 5.000, un acquirente
   conferma un ordine di 8.000: lo stato diventa *Da approvare*.
#. Il responsabile acquisti lo apre dal filtro *Da approvare* e preme
   **Approva ordine**: l'ordine diventa un *Ordine di acquisto* e viene creata
   la ricezione.

**Fatturare solo quanto ricevuto**

#. Il prodotto ha *Quantità ricevute* come politica di controllo; si ordinano
   100 unità e ne arrivano 60: validare la ricezione con 60.
#. Premere **Crea fattura**: la fattura in bozza ha 60 unità. Quando arrivano
   le altre 40, validare il backorder e premere di nuovo **Crea fattura**.

**Il fornitore aumenta il prezzo dopo la conferma**

Cambiare il prezzo unitario sulla riga dell'ordine confermato; le fatture già
create mantengono il prezzo precedente.

**Il fornitore non può consegnare**

Premere **Annulla**; l'ordine resta nell'elenco con stato *Annullato* e anche
la sua ricezione viene annullata.
