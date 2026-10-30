.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

* :field:`Riferimento fornitore <partner_ref>`: il numero dell'offerta o della
  conferma d'ordine del fornitore, usato per abbinare la fattura fornitore.
* :field:`Scadenza per ordine <date_order>`: la data entro cui confermare la
  RdP; dopo la conferma è mostrata invece la :field:`data conferma
  <date_approve>`.
* :field:`Arrivo previsto <date_planned>`: quando la merce dovrebbe arrivare,
  proposto dai tempi di consegna del fornitore dei prodotti.
* :field:`Richiesta di conferma <receipt_reminder_email>` (impostazione
  *Promemoria ricezione*): invia un'e-mail al fornitore alcuni giorni prima
  dell'arrivo previsto, chiedendo di confermare la data.
* :field:`Acquirente <user_id>`: chi segue l'ordine, usato nei report.
* :field:`Documento di origine <origin>`: il documento che ha generato
  l'ordine, ad es. una regola di riordino o un ordine di vendita.
* :field:`Termini di pagamento <payment_term_id>`: scadenze delle fatture
  fornitore.
* :field:`Posizione fiscale <fiscal_position_id>`: converte imposte e conti, ad
  es. per i fornitori esteri.
* :field:`Stato fatturazione <invoice_status>`: indica se resta qualcosa da
  fatturare.
* Con Magazzino installato, **Consegna** sceglie l'operazione di ricezione
  (magazzino) e **Incoterm** le condizioni di consegna concordate con il
  fornitore.
