.. _example:

Esempio
-------

Tutti gli esempi usano l'aliquota 22% e il pacchetto italiano (``l10n_it``).
Aprire **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Imposte** e, per non
scrivere le righe di ripartizione, duplicare l'imposta indicata in ogni
esempio (icona dell'ingranaggio ‣ **Duplica**), poi cambiare quanto scritto
qui.

**Come impostare la natura e le griglie imposta**

* La **natura** è il campo :field:`Esenzione <l10n_it_exempt_reason>` della
  scheda **Opzioni avanzate**, con sotto il :field:`Riferimento legislativo
  <l10n_it_law_reference>`. È obbligatoria solo quando l'importo è 0%: le
  imposte con un importo non hanno la natura.
* Le **griglie imposta** sono nella scheda **Definizione**, colonna **Griglie
  imposta** delle tabelle **Ripartizione per fatture** e **Ripartizione per
  note di credito**. Fare clic sulla cella di una riga, scrivere il codice
  della griglia, ad es. ``vj12``, e sceglierlo: la griglia ``+vj12`` somma
  l'importo alla riga VJ12 del report IVA, ``-vj12`` lo sottrae. Le fatture
  usano le griglie con ``+``, le note di credito la stessa griglia con ``-``.
  Una riga può avere più griglie, ad es. ``+03`` e ``+vj12``.
* Le griglie usate qui sono: ``02`` (VP2, totale operazioni attive), ``03``
  (VP3, totale operazioni passive), ``4v`` (VP4, IVA esigibile), ``5v`` (VP5,
  IVA detraibile), ``ve38`` (VE38, operazioni con i soggetti dell'art.
  17-ter), ``vj3``, ``vj9`` e da ``vj12`` a ``vj17`` (le righe VJ
  dell'inversione contabile).

**1. Imposta con IVA 22%**

*1a. Vendite*: duplicare *22%* (tipo *Vendita*) e scrivere il nome, ad es.
*22% nuova*.

#. Scheda **Definizione**, **Ripartizione per fatture**: la riga *Base* ha la
   griglia ``+02``; la riga *dell'imposta* (100%) ha il conto *Debito IVA* e la
   griglia ``+4v``.
#. **Ripartizione per note di credito**: le stesse righe nello stesso ordine,
   con le griglie ``-02`` e ``-4v``.
#. Scheda **Opzioni avanzate**: :field:`Gruppo imposta <tax_group_id>` *IVA
   22%*, :field:`Nazione <country_id>` *Italia*. Nessuna natura.

Una riga fattura di 100,00 ha un'imposta di 22,00 e un totale di 122,00; il
report ha 100,00 in VP2 e 22,00 in VP4.

*1b. Acquisti*: duplicare *22% M* (merci) o *22% S* (servizi) e scrivere il
nome, ad es. *22% M nuova*.

#. :field:`Tipo imposta <type_tax_use>` *Acquisti* e :field:`Ambito imposta
   <tax_scope>` *Beni* o *Servizi*.
#. **Ripartizione per fatture**: la riga *Base* ha la griglia ``+03``; la riga
   *dell'imposta* (100%) ha il conto *Credito IVA* e la griglia ``+5v``.
#. **Ripartizione per note di credito**: le stesse righe con le griglie ``-03``
   e ``-5v``.
#. Scheda **Opzioni avanzate**: :field:`Gruppo imposta <tax_group_id>` *IVA
   22%*, :field:`Nazione <country_id>` *Italia*. Nessuna natura.

Una riga fattura fornitore di 100,00 ha un'imposta di 22,00 e un totale di
122,00; il report ha 100,00 in VP3 e 22,00 in VP5.

**2. Imposta senza IVA, natura N4 (esente)**

I passi dei due lati sono uguali: l'importo è 0, la natura e il riferimento
legislativo sono obbligatori e il gruppo imposta è *Fuori Campo IVA*.

*2a. Vendite*: duplicare *22%* (tipo *Vendita*) e scrivere il nome *0% N4*.

#. Scrivere 0 in :field:`Importo <amount>`.
#. Scheda **Opzioni avanzate**: scegliere :field:`Esenzione
   <l10n_it_exempt_reason>` *[N4] Esenti*, scrivere il :field:`Riferimento
   legislativo <l10n_it_law_reference>` *Art. 10 DPR 633/1972* e scegliere il
   :field:`Gruppo imposta <tax_group_id>` *Fuori Campo IVA*.
#. Scheda **Definizione**: eliminare la griglia ``+4v`` della riga *dell'imposta*
   (e ``-4v`` delle note di credito): non c'è IVA da riportare. Il pacchetto
   lascia vuote le griglie delle imposte senza IVA (ad es. l'imposta *0%*,
   natura N1): aggiungere ``+02`` / ``-02`` alla riga *Base* solo se il
   commercialista vuole l'operazione in VP2.

Una riga fattura di 100,00 ha un'imposta di 0,00 e un totale di 100,00; la
fattura elettronica ha la natura N4 e il riferimento legislativo.

*2b. Acquisti*: duplicare *22% M* (o *22% S*) e scrivere il nome *0% N4 M* (o
*0% N4 S*).

#. Scrivere 0 in :field:`Importo <amount>`; mantenere :field:`Tipo imposta
   <type_tax_use>` *Acquisti* e l':field:`Ambito imposta <tax_scope>`.
#. Scheda **Opzioni avanzate**: la stessa natura *[N4] Esenti*, lo stesso
   riferimento legislativo e il gruppo imposta *Fuori Campo IVA*.
#. Scheda **Definizione**: eliminare la griglia ``+5v`` della riga
   *dell'imposta* (e ``-5v`` delle note di credito); aggiungere ``+03`` /
   ``-03`` alla riga *Base* solo se il commercialista vuole l'operazione in
   VP3.

Una riga fattura fornitore di 100,00 ha un'imposta di 0,00 e un totale di
100,00. Gli stessi passi con un'altra natura, ad es. [N3.1] e *Art. 8 c. 1
lett. a) e b) DPR 633/72*, danno l'imposta di una esportazione (vendite).

**3. Imposta con scissione dei pagamenti 22%**

Tre imposte, come in *Come inserire un'imposta per la scissione dei
pagamenti*. Duplicare *22% SP pos.*, *22% SP neg.* e *22% SP* (o tutto il
gruppo di un'altra aliquota), poi:

#. *22% SP pos.*: importo 22, tipo *Nessuno*, gruppo imposta *IVA 22%*; righe
   fattura *Base* con le griglie ``+02`` e ``+ve38``, e *dell'imposta* sul conto
   *IVA c/Split Payment*, senza griglia; note di credito ``-02`` e ``-ve38``.
#. *22% SP neg.*: importo -22, tipo *Nessuno*, gruppo imposta *Scissione dei
   Pagamenti*, :field:`Compresa nel prezzo <price_include_override>`
   *Imponibile*; nessuna griglia, la riga *dell'imposta* sul conto *IVA c/Split
   Payment*.
#. *22% SP*: tipo *Vendita*, :field:`Calcolo imposta <amount_type>` *Gruppo di
   imposte*, :field:`Gruppo imposta <tax_group_id>` *Scissione dei Pagamenti*,
   e le due imposte sopra in **Imposte figlie**.

Una riga fattura di 100,00 con *22% SP* ha +22,00 e -22,00: il totale è
100,00, l'IVA di 22,00 non è pagata al fornitore e il report ha 100,00 in VP2
e in VE38.

**4. Imposta con inversione contabile 22%, natura N6.3 (subappalto edile)**

Due imposte, una per ogni lato dell'operazione.

*Imposta di acquisto*: duplicare *22% IC N6.3* (o *22% M* e rinominarla *22% IC
N6.3*).

#. **Ripartizione per fatture**: la riga *Base* ha le griglie ``+03`` e
   ``+vj12`` (VJ12, subappalto nel settore edile); poi due righe *dell'imposta*:
   +100% su *Credito IVA* con la griglia ``+5v``, e -100% su *Debito IVA* con
   la griglia ``-4v``.
#. **Ripartizione per note di credito**: le stesse righe nello stesso ordine,
   con le griglie ``-03`` e ``-vj12``, ``-5v`` sul +100% e ``+4v`` sul -100%.
#. Scheda **Opzioni avanzate**: :field:`Gruppo imposta <tax_group_id>` *IVA
   22%*.

La griglia della base cambia con la natura: ``vj6`` per N6.1, ``vj7`` per N6.2,
``vj8`` per N6.2b, ``vj12`` per N6.3, ``vj13`` per N6.4, ``vj14`` per N6.5,
``vj15`` per N6.6, ``vj16`` per N6.7 e ``vj17`` per N6.8. Per gli acquisti
dall'estero usare ``vj3`` (servizi, e merci già in Italia) o ``vj9`` (merci
dalla UE).

Su una fattura fornitore di 100,00 le due imposte di 22,00 si annullano: il
totale resta 100,00 e l'IVA è sia detraibile (VP5) sia dovuta (VP4).

*Imposta di vendita*: duplicare *0% IC N6.3* (o *22%* e scrivere 0 nell'importo).
Nella scheda **Opzioni avanzate** scegliere :field:`Esenzione
<l10n_it_exempt_reason>` *[N6.3]* e scrivere il :field:`Riferimento legislativo
<l10n_it_law_reference>` *art.17, comma 6, lett. a, D.P.R. 633/1972*; il
:field:`Gruppo imposta <tax_group_id>` è *Fuori Campo IVA*; le griglie sono
``+02`` sulla base e ``+4v`` sulla riga *dell'imposta* (note di credito ``-02``
e ``-4v``).
