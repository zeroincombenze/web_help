.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

* :field:`Tipo di azienda <company_type>`: *Persona* o *Azienda*.
* :field:`Azienda <parent_id>`: l'azienda a cui appartiene una persona.
* :field:`Tipo indirizzo <type>` (modalità sviluppatore, sui contatti di
  un'azienda): *Contatto*, *Indirizzo fattura*, *Indirizzo di Spedizione* o
  *Altro Indirizzo*; ordini e fatture scelgono l'indirizzo giusto dal tipo.
* Indirizzo: via, :field:`città <city>`, :field:`provincia <state_id>`,
  :field:`CAP <zip>` e :field:`nazione <country_id>`.
* :field:`Partita IVA <vat>` (con il modulo *base_vat*): il numero di
  identificazione fiscale, controllato secondo il formato della nazione.
* :field:`Telefono <phone>`, :field:`cellulare <mobile>` ed :field:`email
  <email>`: l'email serve per inviare documenti e messaggi.
* :field:`Tag <category_id>`: etichette libere per classificare e filtrare.
* :field:`Lingua <lang>`: la lingua dei documenti e delle email inviate al
  contatto.
* Scheda **Vendite e Acquisti**: :field:`È un cliente <customer>` ed :field:`È
  un fornitore <supplier>` decidono dove il contatto è proposto,
  :field:`commerciale <user_id>`, :field:`riferimento interno <ref>`.
* Scheda **Contabilità** (con Fatturazione installata): condizioni di
  pagamento cliente e fornitore, posizione fiscale, conti di credito e debito,
  conti bancari.
