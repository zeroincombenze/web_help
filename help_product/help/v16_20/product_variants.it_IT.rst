.. _variants:

Varianti prodotto
-----------------

Le varianti sono prodotti che hanno caratteristiche aggiuntive rispetto al
prodotto originale, ad esempio colore, taglia, un'opzione aggiuntiva o altri
attributi. In Odoo si possono impostare regole per gestire queste varianti.

Per creare le varianti di un prodotto, attivare l'impostazione *Varianti*
(:version:`<=16|**Vendite ‣ Configurazione ‣ Impostazioni**;*|**Vendite ‣
Configurazione ‣ Impostazioni** o **Magazzino ‣ Configurazione ‣
Impostazioni**`), poi definire nella scheda **Attributi e varianti** gli
attributi da assegnare e i loro valori possibili: Odoo crea una variante per
ogni combinazione, a meno che la *Modalità di creazione varianti*
dell'attributo le crei solo quando ordinate. Poiché non tutti i prodotti hanno
bisogno di varianti, un prodotto senza attributi è considerato senza varianti.

⚠ **Attenzione!** Dopo che le varianti sono state create, potrebbe non essere
più possibile riportare un prodotto con varianti a uno senza, o aggiungere
varianti a un prodotto che ora non ne ha: cambiare gli attributi in seguito
elimina le varianti che non corrispondono più, o le archivia se sono già
usate da documenti, e ne crea di nuove; giacenze, codici e storico restano
sulle vecchie varianti.

⚠ **Attenzione!** Alcuni campi, come il nome e le descrizioni, sono condivisi
tra le varianti e il prodotto radice (base). Ciò significa che cambiare la
descrizione di una variante la aggiorna per tutte le varianti. Le singole
righe dei documenti possono però avere un proprio testo, diverso dalla
descrizione predefinita del prodotto. Il :field:`riferimento interno
<default_code>`, il :field:`codice a barre <barcode>`, il costo, il peso e il
volume appartengono invece a ogni variante.

Campi condivisi:

* Categoria prodotto
* Codici imposta (IVA) di vendita e acquisto
* Conti di ricavo e di costo
* Descrizioni
* Elenco fornitori (un prezzo fornitore può valere per una sola variante)
* Codice HS / codice Intrastat (con i moduli Intrastat)
* Prezzo di vendita (le differenze di prezzo si impostano come *Prezzo extra*
  dei valori attributo, con **Configura** nella scheda **Attributi e
  varianti**)
* Flag :version:`<=17|*Può essere venduto* e *Può essere acquistato*;*|*Vendita*
  e *Acquisto*`
* Tempi di consegna
* Tipo di prodotto
* Unità di misura
