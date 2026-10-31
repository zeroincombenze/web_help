.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

.. help-version:: <13

   * :field:`Valori attributo <attribute_value_ids>`: ciò che definisce la
     variante, ad es. *L* e *Rosso*.

.. help-version:: >=13

   * :field:`Valori attributo <product_template_attribute_value_ids>`: ciò che
     definisce la variante, ad es. *L* e *Rosso*.

* :field:`Riferimento interno <default_code>` e :field:`codice a barre
  <barcode>`: ogni variante ha i propri.
* :field:`Prezzo di vendita <lst_price>`: il prezzo di vendita del prodotto più
  i prezzi extra dei valori attributo; di sola lettura quando il prodotto ha
  più varianti.
* :field:`Costo <standard_price>`, :field:`peso <weight>` e :field:`volume
  <volume>`: ogni variante ha i propri.
* Magazzino: i pulsanti della quantità disponibile e prevista contano solo la
  quantità di questa variante.
