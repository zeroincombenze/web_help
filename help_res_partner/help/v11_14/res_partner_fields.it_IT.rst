.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

* :field:`Tipo azienda <company_type>`: *Persona* o *Azienda*.
* :field:`Azienda <parent_id>`: l'azienda a cui appartiene una persona.
* :field:`Tipologia indirizzo <type>` (sui contatti di un'azienda):
  *Contatto*, :version:`11|*Indirizzo fatturazione*, *Indirizzo di
  Spedizione* o *Altro Indirizzo*;12|*Indirizzo fattura*, *Indirizzo di
  spedizione* o *Altro indirizzo*;*|*Indirizzo fattura*, *Indirizzo di
  consegna*, *Altro indirizzo* o *Indirizzo privato*`; ordini e fatture
  scelgono l'indirizzo giusto in base al tipo.
* Indirizzo: via, :field:`città <city>`, :field:`provincia <state_id>`,
  :field:`CAP <zip>` e :field:`nazione <country_id>`.
* :field:`Partita IVA <vat>` (con il modulo *base_vat*): il numero di
  identificazione fiscale, controllato secondo il formato della nazione.
* :field:`Telefono <phone>`, :field:`cellulare <mobile>` ed :field:`email
  <email>`: l'email è usata per inviare documenti e messaggi.
* :field:`Etichette <category_id>`: etichette libere per classificare e
  filtrare.
* :field:`Lingua <lang>`: la lingua dei documenti e delle email inviati al
  contatto.
* Scheda :version:`11|**Vendite & Acquisti**;*|**Vendite e acquisti**`:
  :field:`addetto vendite <user_id>`, :field:`riferimento interno <ref>`, il
  listino e i termini di pagamento.
* Scheda **Fatturazione**: termini di pagamento cliente e fornitore, posizione
  fiscale, conti di credito e debito, conti bancari.

.. help-version:: <=12

   * :field:`È un cliente <customer>` ed :field:`È un fornitore <supplier>`
     (scheda **Vendite e acquisti**) scelgono dove il contatto è proposto.
