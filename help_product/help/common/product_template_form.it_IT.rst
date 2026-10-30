.. help-page:: product_template_form
   :title: Prodotto
   :model: product.template
   :view-type: form
   :priority: 96

Prodotto
========

.. _description:

Descrizione
-----------

I prodotti sono i beni o i servizi acquistati e venduti da un'azienda.
Possono avere un codice specifico o esserne privi, essere gestiti a magazzino,
tracciati con numeri di serie o numeri di lotto, oppure gestiti senza alcuna
identificazione specifica, e influiscono sulle registrazioni contabili
dell'azienda. Possono avere una data di scadenza ed essere quantificati con
una o più unità di misura. Possono inoltre avere un prezzo di acquisto e/o un
prezzo di vendita. Infine, possono essere gestiti come articoli monolitici
oppure come prodotti con varianti.

In Odoo il :field:`tipo di prodotto <type>` distingue le merci
**Consumabile** e **Prodotto Stoccabile** da un **Servizio**; :field:`Può
essere venduto <sale_ok>` e :field:`Può essere acquistato <purchase_ok>`
decidono dove il prodotto viene proposto. Il :field:`riferimento interno
<default_code>` è il codice, il :field:`costo <standard_price>` e il
:field:`prezzo di vendita <list_price>` sono i prezzi, l':field:`unità di
misura <uom_id>` la quantità. Le schede mostrano i dati delle applicazioni
installate: vendite, acquisti, magazzino (lotti e numeri di serie; date di
scadenza con il modulo *Product Expiry*) e fatturazione (imposte e conti). Le
**varianti** (ad es. taglie e colori) sono costruite dagli attributi del
prodotto.

.. help-include:: product_fields.rst

.. help-include:: product_variants.rst

.. help-include:: product_new.rst

.. help-include:: product_update.rst

.. help-include:: product_configure.rst

.. help-include:: product_report.rst

.. help-include:: product_example.rst

.. _faq:

Domande frequenti
-----------------

.. help-question:: Che differenza c'è tra un prodotto consumabile e uno stoccabile?

   Entrambi sono merci consegnate e ricevute. Odoo conta la quantità in
   possesso solo del *Prodotto Stoccabile* (con Magazzino installato); un
   *Consumabile* è considerato sempre disponibile. Un *Servizio* non viene mai
   consegnato.

.. help-question:: Perché non riesco a cambiare il tipo di prodotto o l'unità di misura?

   Quando il prodotto ha movimenti di magazzino, cambiarli renderebbe errate
   le quantità esistenti: creare invece un nuovo prodotto e archiviare il
   vecchio.

.. help-question:: Perché non riesco a eliminare il prodotto?

   Un prodotto usato da ordini, fatture o movimenti di magazzino non si può
   eliminare: archiviarlo invece con il pulsante **Attivo** in alto a destra.

.. help-question:: Perché il prezzo di vendita non è modificabile?

   Il prodotto ha più varianti: il prezzo di ogni variante è il prezzo di
   vendita del prodotto più il suo prezzo extra, vedere *Modifica record*.

.. help-question::
   :auto:

.. _footer:

Piè di pagina
-------------

Pagina creata il 2026-10-29 12:00 · © 2026 Zeroincombenze srls <https://www.zeroincombenze.it>
