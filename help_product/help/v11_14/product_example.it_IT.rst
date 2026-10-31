.. _example:

Esempi
------

**Una maglietta in 3 taglie e 2 colori**

#. Attivare :version:`11|*Attributi e Varianti*;12|*Varianti e
   opzioni*;*|*Varianti*` in **Vendite ‣ Configurazione ‣ Impostazioni**.
#. Creare il prodotto *Maglietta*, nella scheda
   :version:`<=14|**Varianti**;*|**Attributi & varianti**` aggiungere *Taglia*
   con *S, M, L* e *Colore* con *Bianco, Rosso*, poi **Salva**: Odoo crea 6
   varianti.
#. Impostare un prezzo extra di 2,00 su *Rosso* con :version:`11|**Prezzi
   Variante**;12-14|**Configura varianti**;*|**Configura** sulla riga
   *Colore*`: le magliette rosse costano 2,00 in più.

**Un servizio di installazione fatturato a lavoro fatto**

Creare il prodotto di tipo *Servizio*, selezionare *Può essere venduto* e
scegliere la politica di fatturazione *Quantità consegnate*: la quantità da
fatturare è quella indicata come consegnata sulla riga dell'ordine.

**Acquistato a scatole da 12, venduto a pezzi**

Con l'impostazione *Unità di misura*, impostare *Unità* come unità di misura e
*Dozzine* come unità di misura d'acquisto: gli ordini di acquisto contano
dozzine, magazzino e vendite contano pezzi.
