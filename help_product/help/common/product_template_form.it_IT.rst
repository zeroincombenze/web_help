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

Un prodotto è qualsiasi cosa l'azienda vende, acquista o tiene in magazzino.
Il :field:`tipo di prodotto <type>` distingue le merci **Consumabile** e
**Prodotto Stoccabile** da un **Servizio**; :field:`Può essere venduto
<sale_ok>` e :field:`Può essere acquistato <purchase_ok>` decidono dove viene
proposto. Un prodotto può avere più **varianti** (ad es. taglie e colori),
costruite dai suoi attributi; le schede mostrano i dati delle applicazioni
installate: vendite, acquisti, magazzino e fatturazione.

.. help-include:: product_fields.rst

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
