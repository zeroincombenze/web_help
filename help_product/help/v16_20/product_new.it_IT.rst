.. _new_record:

Nuovo record
------------

#. Aprire **Vendite ‣ Prodotti ‣ Prodotti** (oppure **Magazzino ‣ Prodotti ‣
   Prodotti**, **Acquisti ‣ Prodotti ‣ Prodotti**) e premere **Nuovo**.
#. Digitare il :field:`nome del prodotto <name>` (obbligatorio) e scegliere la
   **Tipologia prodotto**\ :version:`>=18| (per i beni a magazzino attivare anche
   **Traccia magazzino**)`.
#. Attivare :version:`<=17|**Può essere venduto** e **Può essere
   acquistato**;*|**Vendita** e **Acquisto**` secondo il caso.
#. Impostare il :field:`prezzo di vendita <list_price>`, le imposte e il
   :field:`costo <standard_price>`; scegliere la :field:`categoria <categ_id>`
   e, con l'impostazione *Unità di misura*, l':field:`unità di misura
   <uom_id>`.
#. Digitare il :field:`riferimento interno <default_code>` e il :field:`codice
   a barre <barcode>`, se presenti.
#. Nella scheda **Vendita** scrivere la descrizione per i clienti; nella
   scheda **Acquisto** aggiungere i fornitori con il loro prezzo; nella scheda
   **Magazzino** impostare percorsi, peso e volume.
#. Per un prodotto venduto in più versioni aprire la scheda **Attributi e
   varianti** (impostazione *Varianti*), premere **Aggiungi riga**,
   scegliere l'attributo (es. *Taglia*) e i suoi valori: Odoo crea una
   variante per ogni combinazione.
#. Il record si salva automaticamente quando si esce; premere l'icona della
   nuvola accanto al percorso per salvare subito.
