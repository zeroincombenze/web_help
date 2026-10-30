.. _variants:

Varianti prodotto
-----------------

Le varianti sono prodotti che hanno caratteristiche aggiuntive rispetto al
prodotto originale, ad esempio colore, taglia, un'opzione aggiuntiva o altri
attributi. In Odoo si possono impostare regole per gestire queste varianti.

Per creare le varianti di un prodotto, definire nella scheda
**Varianti** gli attributi da assegnare e i loro valori possibili: Odoo crea
una variante per ogni combinazione. Poiché non tutti i prodotti hanno bisogno
di varianti, un prodotto senza attributi è considerato senza varianti.

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
* Conti di costo e di ricavo
* Descrizioni
* Elenco fornitori
* Codice HS / codice Intrastat (con i moduli Intrastat)
* Prezzo di vendita (le differenze di prezzo si gestiscono tramite gli
  attributi, con **Prezzi Variante**)
* Flag *Può essere venduto* e *Può essere acquistato*
* Tempi di consegna
* Tipo di prodotto
* Unità di misura
