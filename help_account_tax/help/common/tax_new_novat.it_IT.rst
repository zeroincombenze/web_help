.. _new_record_novat:

Come inserire un'imposta senza IVA
----------------------------------

Le operazioni senza IVA usano un'imposta allo 0% con il codice *natura*, che
finisce nell'XML della fattura elettronica. Nella scheda **Opzioni avanzate**
dell'imposta il campo :field:`Esenzione <l10n_it_exempt_reason>` ha la natura
e :field:`Riferimento legislativo <l10n_it_law_reference>` la norma che la
giustifica; entrambi sono obbligatori quando l'importo è 0%. Il :field:`Gruppo
imposta <tax_group_id>` è *Fuori Campo IVA* (o *Imponibile Escluso Art.15*).

Le opzioni del campo *Esenzione* sono le nature dell'Agenzia delle Entrate
(codice *Natura* della fattura elettronica). Ecco la descrizione completa di
ciascuna, come caricata dal modulo ``l10n_it_ade``:

**[N1] Escluse ex art. 15** - Escluso dalla base imponibile (art. 15 DPR
633/72):

* interessi moratori
* beni ceduti a titolo di sconto o abbuono
* rimborsi di anticipazioni
* imballi a spesa concordata
* rivalse

**[N2.1] Non soggette ad IVA ai sensi degli artt. da 7 a 7-septies del DPR
633/72** - Operazioni che non determinano il giro d'affari, che non rientrano
nell'attività dell'impresa, conferimenti in denaro, attività di enti pubblici.
In dettaglio:

* cessione di beni art. 7-bis (extra UE e UE)
* servizi art. 7-ter, 7-quater e 7-quinquies (extra UE e UE)
* servizi art. 7-sexies e art. 7-septies (extra UE)
* escluso artt. 7 e seguenti senza diritto alla detrazione (art. 19, co. 3,
  lett. b)
* servizi art. 7-octies di telecomunicazione, teleradiodiffusione ed
  elettronici, verso committenti non soggetti passivi

**[N2.2] Non soggette - altri casi**:

* fuori campo IVA (*FC*) art. 1; art. 2 (campioni gratuiti, CM 13/E/94;
  cessioni di denaro, crediti, aziende; art. 2 c. 3 lett. a, b, d, f con diritto
  alla detrazione, art. 19 c. 3 lett. c); art. 3 (es. diritti d'autore); art. 4
  (operazioni non commerciali); art. 5 (es. co.co.co., associazioni in
  partecipazione)
* passaggi interni non soggetti a IVA
* art. 7-ter, art. 7-quater c. 1 lett. a) e c); non territoriali art. 38 c. 5
  DL 331/93; escluso artt. 7 e seguenti con diritto alla detrazione (art. 19,
  co. 3, lett. b)
* art. 13 c. 3: escluso base imponibile (anche cessioni di beni acquistati con
  IVA parzialmente indetraibile)
* art. 17 c. 3: vendite del rappresentante fiscale di non residente
  (risoluzione n. 89/E del 25/8/2010)
* art. 26-bis L. 196/97 (interinali); variazione imponibile art. 26 c. 3;
  rimborso oneri lavoro temporaneo art. 26 lett. b L. 196/97
* art. 74 c. 1-2 (tabacchi, quotidiani...), anche con diritto alla detrazione
  (art. 19, co. 3, lett. e)
* vendite contribuenti minimi, art. 27 c. 1 e 2 DL 98/2011 (e art. 1 c. 100 L.
  244/2007)
* vendite contribuenti forfetari, art. 1 c. 54-89 L. 190/2014
* cessioni libri acquistati UE, DM 9/4/93
* art. 8 c. 35 L. 67/1988 (distacco del personale)
* operazioni effettuate con terremotati

**[N3.1] Non imponibili - esportazioni** - Art. 8 c. 1 lett. a) e b) DPR
633/72.

**[N3.2] Non imponibili - cessioni intracomunitarie** - Artt. 41-42 DL 331/93.

**[N3.3] Non imponibili - cessioni verso San Marino** - Art. 71 DPR 633/72.

**[N3.4] Non imponibili - operazioni assimilate alle cessioni
all'esportazione** - Art. 8-bis DPR 633/72.

**[N3.5] Non imponibili - a seguito di dichiarazioni d'intento** - Art. 8 c. 1
lett. c) DPR 633/72.

**[N3.6] Non imponibili - altre operazioni che non concorrono alla formazione
del plafond** - Es. art. 38-quater c. 1 (cessioni a viaggiatori extra UE, non
concorrono al plafond).

**[N4] Esenti** - Operazioni escluse dal campo di applicazione dell'IVA per
presupposto di legge; art. 10 DPR 633/72 e art. 42 DL 331/93:

* art. 10 (operazioni abituali o occasionali soggette a pro rata)
* art. 10 nn. 1-9 (operazioni non rientranti nell'attività propria
  dell'impresa)
* art. 10 n. 11 (oro da investimento)
* art. 10 n. 18 (prestazioni sanitarie) e n. 19 (prestazioni di ricovero e cura)
* art. 10 n. 22 (prestazioni di biblioteche, discoteche, visite a musei,
  gallerie, pinacoteche, monumenti, parchi, giardini botanici, zoologici ecc.)
* art. 10 n. 27-quinquies (beni con IVA totalmente indetraibile)
* art. 19 c. 3 lett. a-bis (operazioni attive art. 10 nn. da 1 a 4 extra UE)
* art. 124 c. 2 DL 34/2020, con diritto alla detrazione art. 19 c. 1 (beni
  necessari per il contenimento e la gestione dell'emergenza epidemiologica da
  Covid esenti IVA)
* passaggi interni esenti
* operazioni esenti effettuate verso condomini

**[N5] Regime del margine / IVA non esposta in fattura**:

* regime del margine art. 36 DL 41/95: analitico (c. 1), forfait (c. 5) e
  globale (c. 6)
* cessioni di prodotti usati, art. 37 DL 41/95
* cessioni in regime del margine non imponibili
* cessione giornali, art. 74 c. 1 lett. c)
* regime speciale agenzie di viaggio, art. 74-ter: prestazioni UE, extra UE e
  miste

**[N6.1] - [N6.9] Inversione contabile** - IVA assolta dal fornitore, solo per
gli acquisti; vedere *Come inserire un'imposta
per l'inversione contabile*:

* *N6.1*: cessione di rottami e altri materiali di recupero, art. 74 c. 7 e 8
* *N6.2*: cessione di oro e argento puro, art. 17 c. 5
* *N6.3*: subappalto nel settore edile, art. 17 c. 6 lett. a)
* *N6.4*: cessione di fabbricati, art. 17 c. 6 lett. a-bis)
* *N6.5*: cessione di telefoni cellulari, art. 17 c. 6 lett. b)
* *N6.6*: cessione di prodotti elettronici, art. 17 c. 6 lett. c)
* *N6.7*: prestazioni del comparto edile e settori connessi, art. 17 c. 6
  lett. a-ter)
* *N6.8*: operazioni del settore energetico, art. 17 c. 6 lett. d-bis), d-ter)
  e d-quater)
* *N6.9*: altri casi

Tutti riferiti al DPR 633/72.

**[N7] IVA assolta in altro stato UE** - IVA per operazione con soggetto in un
altro stato UE; art. 40 c. 3 e 4 e art. 41 DL 331/93, ad es. art. 41 c. 1 lett.
b) (fattura emessa nello stato di origine per vendite a distanza a privati UE,
sopra soglia, con IVA in altro stato UE). Condizioni:

* cedente/prestatore e cessionario/committente devono essere soggetti IVA
* trasferimento di proprietà di beni (non usati) tra stati diversi della UE
* fatturazione con importo diverso da zero

.. note::

   Le nature generiche *N2* (*Non soggette*) e *N3* (*Non imponibili*) erano
   valide fino al 31-12-2020: ora usare *N2.1*, *N2.2* e da *N3.1* a *N3.6*. Il
   codice *FC* (*FC applicazione IVA*, operazione esclusa dall'IVA e dalle
   comunicazioni fiscali) è archiviato.

Il pacchetto *Italia* carica queste imposte senza IVA:

.. list-table::
   :header-rows: 1

   * - Imposta
     - Tipo
     - Esenzione
     - Riferimento legislativo
   * - *0%*
     - Vendita
     - N1
     - Art. 15 DPR 633/1972
   * - *0% M*, *0% S*
     - Acquisti
     - N1
     - Art. 15 DPR 633/1972
   * - *0% Art.15*
     - Vendita e acquisti
     - N1
     - Art. 15 DPR 633/1972
   * - *0% EU G*
     - Vendita
     - N3.2
     - Art. 41, DL 331/93
   * - *0% EU S*
     - Vendita
     - N2.1
     - Art. 7ter, DPR 633/1972
   * - *0% EX*
     - Vendita
     - N2.2
     - Fuori dall'Unione Europea
   * - *0% EX N7*
     - Vendita
     - N7
     - Fuori dall'Unione Europea

#. Aprire **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Imposte**, cercare
   ``0%`` e aprire l'imposta della natura che serve. L'imposta *0% EU G* è
   applicata automaticamente alle vendite intracomunitarie dalla posizione
   fiscale *Intra-Comunitario*, e *0% EX* alle vendite fuori UE dalla
   posizione *Importazione/Esportazione*.
#. Quando la natura non è nell'elenco sopra (N3.1, da N3.3 a N3.6, N4, N5...)
   creare l'imposta duplicando la più vicina, ad es. *0%*, come in *Come
   inserire un nuovo record per duplicazione*.
#. Scrivere il :field:`nome imposta <name>`, ad es. *0% N4*, lasciare
   :field:`Importo <amount>` 0, poi scegliere :field:`Esenzione
   <l10n_it_exempt_reason>`, ad es. *[N4] Esenti*, e scrivere il
   :field:`Riferimento legislativo <l10n_it_law_reference>`, ad es. *Art. 10
   DPR 633/1972* (il riferimento da usare è quello confermato dal
   commercialista).
#. Scegliere il :field:`Tipo imposta <type_tax_use>` (la stessa natura richiede
   un'imposta per ogni tipo) e, per gli acquisti, l':field:`Ambito imposta
   <tax_scope>`.
#. Scegliere l'imposta sui prodotti, oppure far sostituire l'imposta del
   prodotto da una posizione fiscale, nella scheda **Mappatura imposta**.

