.. _example:

Esempi
------

**Fatture scadute di un cliente**

Scegliere il filtro :version:`10|*Scaduto*;11|*Ritardi*;*|*In ritardo*`,
scrivere il nome del cliente nella barra di ricerca e scegliere la ricerca
per partner: il totale ancora dovuto è in fondo alla colonna.

**Ricerche con il carattere jolly**

Il carattere ``%`` (percento) in un valore di ricerca significa *qualsiasi
testo*. Cercando il partner ``Rossi%Milano`` si trovano *Rossi S.r.l. -
Milano* e *Rossi Mario Milano*, ma non *Rossi S.p.A. - Roma*. Cercando il
numero ``%/2026/%`` si trovano le fatture numerate nel 2026, in qualsiasi
registro.

**Importo fatturato di ogni mese**

:version:`<13|Scegliere i filtri *Aperta* e *Pagata*;13|Scegliere il filtro
*Confermato*;*|Scegliere il filtro *Confermata*`, poi **Raggruppa per ‣ Data
fattura ‣ Mese**: ogni gruppo mostra il suo subtotale. Salvare la ricerca con
**Preferiti ‣ Salva ricerca attuale** per riusarla.

**Stampare più fatture**

Selezionare le fatture con le caselle di spunta, poi
:version:`<18|**Stampa ‣ Fatture**;*|**Stampa ‣ PDF fattura**`: un solo PDF
le contiene tutte.
