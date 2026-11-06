.. _actions:

Altre azioni
------------

I pulsanti in cima alla fattura; ognuno compare solo quando lo stato della
fattura lo consente.

Confermare la fattura
~~~~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   Su una fattura in *Bozza* premere **Valida**: Odoo controlla la fattura,
   assegna il :field:`numero <number>`, scrive la registrazione contabile e lo
   stato diventa *Aperta*. Da quel momento la fattura non può più essere
   modificata: vedere *Come modificare un record* per correggerla.

.. help-version:: >=13

   Su una fattura in *Bozza* premere **Conferma**: Odoo controlla la fattura,
   assegna il :field:`numero <name>` dalla sequenza del registro e lo stato
   diventa *Confermata*. Da quel momento la fattura non può più essere
   modificata: premere **Reimposta a bozza** per correggerla.

   .. help-version:: >=14

      Con *Conferma automatica* impostata nella scheda **Altre informazioni**
      e una data futura, il pulsante è nascosto: Odoo conferma la fattura da
      solo in quella data.

Registrare un pagamento
~~~~~~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   Su una fattura *Aperta* premere :version:`10|**Registra
   pagamenti**;11|**Registrazione pagamento**;*|**Registra pagamento**`:
   controllare il registro di pagamento (banca o cassa), il metodo di
   pagamento, l'importo, la data e la causale, poi premere **Valida**. Un
   importo minore lascia aperto il resto (:version:`10|*Lasciare
   aperto*;11|*Tenere aperto*;*|*Lasciare aperta*`) o lo storna su un conto
   differenze (:version:`10|*Marca la fattura come pagata
   interamente*;11|*Indicazione fattura saldata*;*|*Segnare fattura come
   pagata*`). Quando i pagamenti coprono l'intero importo lo stato diventa
   *Pagata*.

.. help-version:: >=13

   Su una fattura *Confermata*\ :version:`13| non ancora pagata;*| non ancora
   pagata, o pagata solo in parte,` premere **Registra pagamento**:
   controllare il registro (banca o cassa), il metodo di pagamento, l'importo,
   la data e la causale, poi premere **Crea pagamento**. Un importo minore
   lascia da pagare il resto (:version:`13|*Lasciare aperta*;*|*Tieni
   aperta*`) o lo storna su un conto differenze (:version:`13|*Impostare
   fattura come pagata*;*|*Segna come totalmente pagata*`). Quando i
   pagamenti coprono l'intero importo la fattura è *Pagata*, o *In pagamento*
   finché il pagamento non è riconciliato con l'estratto conto.

Un pagamento già ricevuto, ad es. dall'estratto conto, è mostrato sotto i
totali come *credito in sospeso*: premere **Aggiungi** accanto a esso per
usarlo per questa fattura.

Come creare una nota di debito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. help-version:: <13

   Una nota di debito chiede al cliente un importo aggiuntivo su una fattura
   già emessa (ad es. un aumento di prezzo o un addebito dimenticato). Questa
   versione non ha una funzione apposita: creare una nuova fattura per
   l'importo aggiuntivo, e scrivere il numero della fattura originale nel
   suo riferimento.

.. help-version:: >=13

   Una nota di debito chiede al cliente un importo aggiuntivo su una fattura
   già emessa (ad es. un aumento di prezzo o un addebito dimenticato), o
   registra l'importo aggiuntivo chiesto da un fornitore.

   .. help-if:: module != account_debit_note

      La funzione richiede il modulo *Note di debito*: l'amministratore lo
      installa dal menu **Applicazioni**.

   .. help-if:: module = account_debit_note

      Su una fattura, fattura fornitore o nota di credito *Confermata* che
      non sia essa stessa una nota di debito, premere :version:`<17|**Aggiungi
      nota di debito**;*|l'icona dell'ingranaggio accanto al nome del record ‣
      **Nota di debito**`. Compilare la *Causale*, la *Data nota di debito*,
      il *Registro* e, per partire da una copia delle righe della fattura,
      *Copia righe*; poi premere **Crea nota di debito**. La nuova nota di
      debito si apre in bozza: correggerne righe e importi, poi confermarla.
      Mostra la fattura originale in *Fattura di origine addebitata*, mentre
      la fattura originale riceve il pulsante *Note di debito* per aprire le
      sue note di debito.

   .. help-version:: >=18

      .. help-if:: module = l10n_it_edi_ndd_account_dn

         La fattura elettronica di una nota di debito è inviata con il tipo
         documento *TD05*.
