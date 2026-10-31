.. _new_record:

Come inserire un nuovo record
-----------------------------

#. Aprire il menu prodotti di Vendite, Acquisti o Magazzino e premere **Crea**.
#. Scrivere il :field:`nome del prodotto <name>` (obbligatorio) e selezionare
   :field:`Può essere venduto <sale_ok>` e/o :field:`Può essere acquistato
   <purchase_ok>`.
#. In **Informazioni generali** scegliere la :field:`tipologia prodotto
   <type>` e la :field:`categoria interna <categ_id>`, scrivere il
   :field:`riferimento interno <default_code>`, il :field:`codice a barre
   <barcode>`, il :field:`prezzo di vendita <list_price>` e il :field:`costo
   <standard_price>`, e le unità di misura.
#. In :version:`11|**Vendite**;13|**Vendite**;*|**Vendita**` scegliere la
   :field:`politica di fatturazione <invoice_policy>`.
#. In **Acquisto**, sotto **Fornitori**, premere :version:`11|**Aggiungi
   voce**;*|**Aggiungi una riga**` per aggiungere ogni fornitore con il suo
   prezzo, la quantità minima e il tempo di consegna.
#. In :version:`11|**Inventario**;*|**Magazzino**` scegliere i percorsi; in
   :version:`11|**Fatturazione**;*|**Contabilità**` controllare le imposte
   cliente e fornitore.
#. Per venderlo in più versioni (impostazione delle varianti), nella scheda
   :version:`<=14|**Varianti**;*|**Attributi & varianti**` aggiungere una riga
   per ogni attributo (es. *Taglia*) con i suoi valori (*S, M, L*): Odoo crea
   una variante per ogni combinazione al salvataggio.
#. Premere **Salva**.
