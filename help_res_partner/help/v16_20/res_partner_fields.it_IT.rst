.. _fields:

Campi principali
~~~~~~~~~~~~~~~~

* :field:`Tipologia indirizzo <type>` (solo persone): *Contatto*, *Indirizzo
  fattura*, *Indirizzo di consegna*, *Altro indirizzo*\ :version:`16|,
  *Indirizzo privato*`. Un *Contatto* condivide l'indirizzo della sua
  azienda.
* :field:`Partita IVA <vat>`: verificata secondo le regole della nazione
  (e online con *Verificare le partite IVA*); Odoo avvisa se un altro
  partner ha la stessa.
* :field:`Posizione lavorativa <function>` e :field:`titolo <title>` di una
  persona.
* :field:`Telefono <phone>`, :field:`cellulare <mobile>`, :field:`e-mail
  <email>` e :field:`sito web <website>`.
* :field:`Lingua <lang>`: lingua dei documenti e delle e-mail inviati al
  contatto (visibile con più lingue installate).
* :field:`Etichette <category_id>`: etichette libere per classificare i
  contatti.
* Scheda **Vendite e acquisti**: :field:`addetto vendite <user_id>`,
  :field:`riferimento <ref>`, :field:`ID azienda <company_registry>`,
  :field:`settore <industry_id>`; con Vendite, Acquisti o Fatturazione anche
  termini di pagamento, listino prezzi e posizione fiscale.
* Scheda **Fatturazione** (con Fatturazione installata): conti bancari e
  conti di credito e di debito.
* Scheda **Note interne**: :field:`note <comment>` visibili solo agli utenti.
