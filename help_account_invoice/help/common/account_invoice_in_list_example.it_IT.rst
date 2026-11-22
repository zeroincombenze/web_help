.. _example:

Esempi
------

**Fatture scadute di un fornitore**

Scegliere il filtro :version:`10|*Scaduto*;11|*Ritardi*;*|*In ritardo*`,
scrivere il nome del fornitore nella barra di ricerca e scegliere la ricerca
per partner: il totale ancora dovuto è in fondo alla colonna.

**Ricerche con il carattere jolly**

Il carattere ``%`` (percento) in un valore di ricerca significa *qualsiasi
testo*. Cercando il partner ``Rossi%Milano`` si trovano *Rossi S.r.l. -
Milano* e *Rossi Mario Milano*, ma non *Rossi S.p.A. - Roma*. Cercando il
numero ``%/2026/%`` si trovano le fatture numerate nel 2026, in qualsiasi
registro.

**Fatture da pagare nel mese**

Scegliere il filtro :version:`10|*Non pagato*;11-12|*Aperta*;13|*Non
pagato*;14|*Non pagata*;15-17|*Non pagato*;*|*Da pagare*`, poi **Raggruppa
per ‣ Data di scadenza ‣ Mese**: ogni gruppo mostra il suo subtotale, cioè
quanto si deve pagare in quel mese. Salvare la ricerca con **Preferiti ‣
Salva la ricerca corrente** per riusarla.
