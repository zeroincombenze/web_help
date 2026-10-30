.. _new_record:

Nuovo record
------------

#. Aprire **Vendite ‣ Vendite ‣ Prodotti**, **Acquisti ‣ Acquisto ‣ Prodotti**
   o **Magazzino ‣ Controllo inventario ‣ Prodotti** e premere **Crea**.
#. Digitare il :field:`nome prodotto <name>` (obbligatorio) e spuntare
   :field:`Può essere venduto <sale_ok>` e/o :field:`Può essere acquistato
   <purchase_ok>`.
#. In **Informazioni Generali** scegliere il :field:`tipo di prodotto <type>` e
   la :field:`categoria interna <categ_id>`, digitare il :field:`riferimento
   interno <default_code>`, il :field:`codice a barre <barcode>`, il
   :field:`prezzo di vendita <list_price>` e il :field:`costo
   <standard_price>`, e le unità di misura.
#. In **Vendite** scegliere il :field:`metodo di fatturazione
   <invoice_policy>`.
#. In **Inventario** scegliere le rotte e, sotto **Fornitori**, premere
   **Aggiungi voce** per aggiungere ogni fornitore con prezzo, quantità minima
   e tempo di consegna.
#. In **Fatturazione** controllare le imposte cliente e fornitore.
#. Per venderlo in più versioni (impostazione *Varianti Prodotto*), nella
   scheda **Varianti** aggiungere una riga per ogni attributo (ad es.
   *Taglia*) con i suoi valori (*S, M, L*): Odoo crea una variante per ogni
   combinazione al salvataggio.
#. Premere **Salva**.
