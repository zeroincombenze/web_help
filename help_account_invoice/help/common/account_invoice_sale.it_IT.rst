.. help-if:: module = sale

   .. _sale_order:

   Fatturazione da ordine di vendita
   ---------------------------------

   Con l'app Vendite le fatture clienti si creano di solito dagli ordini di
   vendita confermati: Odoo copia il cliente, i termini di pagamento, la
   posizione fiscale e le righe, e tiene traccia di quanto è già fatturato.

   Cosa si può fatturare dipende dal campo :version:`10|*Metodo di
   fatturazione*;*|*Politica di fatturazione*` di ogni prodotto, nella scheda
   :version:`10|**Fatturazione**;11-15|**Vendite**;*|**Informazioni
   generali**` del prodotto:

   * *Quantità ordinate*: tutta la quantità ordinata, appena l'ordine è
     confermato;
   * *Quantità consegnate*: solo la quantità già consegnata, ad esempio dopo
     la convalida del documento di consegna.

   Lo *Stato fattura* di un ordine mostra cosa resta: *Nulla da fatturare*,
   *Da fatturare*, *Interamente fatturato* o :version:`<14|*Opportunità di
   up-selling*;*|*Opportunità di incremento vendite*` (è stato consegnato più
   di quanto ordinato).

   #. Aprire l'ordine di vendita confermato e premere **Crea fattura**. Gli
      ordini in attesa di fattura sono elencati in
      :version:`10|**Vendite ‣ Fatturazione ‣ Vendite da fatturare**;11|**Vendite
      ‣ Fatturazione ‣ Ordini da fatturare**;*|**Vendite ‣ Da fatturare ‣
      Ordini da fatturare**`.
   #. Scegliere cosa fatturare:

      .. help-version:: <13

         * *Righe fatturabili*: le quantità da fatturare di ogni riga;
         * *Righe fatturabili (con anticipo dedotto)*: le stesse, meno gli
           anticipi già fatturati;

      .. help-version:: >=13

         * *Fattura normale*: le quantità da fatturare di ogni riga; spuntare
           :version:`13|*Dedurre gli acconti*;*|*Detrai anticipi*` per
           sottrarre gli anticipi già fatturati;

      * *Anticipo (percentuale)* o :version:`<13|*Anticipo (valore
        fisso)*;*|*Anticipo (importo fisso)*`: un acconto sul totale
        dell'ordine, dedotto poi dalla fattura normale.

   #. Premere :version:`10|**Crea e mostra fattura**;11|**Crea e visualizza
      fatture**;12|**Crea e mostra fattura**;13-16|**Crea e visualizza
      fattura**;17|**Crea bozza fattura**;*|**Crea bozza**`: la nuova fattura
      si apre in bozza, con il numero dell'ordine come *Documento di origine*.
   #. Controllare la fattura e confermarla, come descritto in *Come inserire
      un nuovo record*.

   Più ordini si fatturano insieme dall'elenco degli ordini: selezionarli e
   scegliere :version:`10|**Invoice Orders**;11|**Ordine di
   fatturazione**;12|**Fatturare ordine**;13-17|**Crea fatture**;*|**Crea
   fattura(e)**` nel menu :version:`<17|**Azione**;*|**Azioni** (icona
   dell'ingranaggio)`.
   :version:`>=17|*Fatturazione consolidata* crea una sola fattura per gli
   ordini dello stesso cliente e dello stesso indirizzo di fatturazione.`

   La fattura è collegata all'ordine: il pulsante **Fatture** dell'ordine apre
   le sue fatture, e annullare o eliminare una fattura in bozza rende di nuovo
   fatturabili le sue quantità.
