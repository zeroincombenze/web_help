.. _new_record_rc:

Come inserire un'imposta per l'inversione contabile
---------------------------------------------------

Nell'inversione contabile l'IVA non è addebitata dal fornitore: l'acquirente
integra il documento con l'IVA e la registra sia a credito sia a debito. La
natura dell'operazione è una tra *[N6.1] ... [N6.9]*. Il pacchetto *Italia*
carica, per ogni natura, le imposte di entrambi i lati:

.. list-table::
   :header-rows: 1

   * - Natura
     - Operazione
     - Riferimento legislativo dell'imposta di vendita
   * - N6.1
     - Materiali di scarto e di recupero
     - art.74, comma 7-8, D.P.R. 633/1972
   * - N6.2
     - Oro (*N6.2b*: investimenti in oro)
     - art.17, comma 5, D.P.R. 633/1972
   * - N6.3
     - Subappalto edilizia
     - art.17, comma 6, lett. a, D.P.R. 633/1972
   * - N6.4
     - Investimenti in edilizia (fabbricati)
     - art.17, comma 6, lett. a-bis, D.P.R. 633/1972
   * - N6.5
     - Cellulari
     - art.17, comma 6, lett. b, D.P.R. 633/1972
   * - N6.6
     - Elettronica
     - art.17, comma 6, lett. c, D.P.R. 633/1972
   * - N6.7
     - Servizi edilizia
     - art 17, comma 6, lett. a-ter, D.P.R. 633/1972
   * - N6.8
     - Energia
     - art.17, comma 6, lett. d-bis, d-ter, d-quater, D.P.R. 633/1972

* **Imposte di vendita** *0% IC N6.1* ... *0% IC N6.8*: 0% sulle fatture del
  fornitore che vende in inversione contabile, con la natura e il riferimento
  legislativo della tabella (per N6.9 *Inversione contabile - altri casi* non
  ce n'è: duplicarne una e scegliere la natura).
* **Imposte di acquisto**, una per ogni aliquota e natura: *22% IC N6.3*,
  *10% IC N6.3*, *5% IC N6.3*, *4% IC N6.3*... Solo *22% IC N6.7* e *10% IC
  N6.7* (e la vendita *0% IC N6.7*) sono attive quando il pacchetto viene
  installato: attivare le altre come in *Come attivare un'imposta del
  pacchetto*.
* **Imposte di acquisto fuori dall'Italia**: *22% S IC* (servizi) e *22% M IC*
  (merci) e lo stesso per 10%, 5% e 4% (quelle allo 0% hanno natura N1),
  usate per gli acquisti dalla UE dalla posizione fiscale *Intra-Comunitario*,
  e *22% M Deposito*, per le merci in un deposito IVA.

Le imposte di acquisto hanno due righe *dell'imposta* nella tabella
**Ripartizione per fatture** (e nei rimborsi, con i segni opposti): +100% sul
conto *Credito IVA* e -100% sul conto *Debito IVA*, con le griglie imposta
della sezione VJ del report IVA. Così il totale della fattura fornitore non
cambia e l'IVA è sia a credito sia dovuta.

#. Aprire **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Imposte**, cercare
   ``IC`` e attivare le imposte delle nature e delle aliquote usate.
#. Aprire l'imposta di acquisto, ad es. *22% IC N6.3*, e controllare il
   :field:`Tipo imposta <type_tax_use>` (*Acquisti*), le due righe della
   scheda **Definizione** e il :field:`Gruppo imposta <tax_group_id>` (*IVA
   22%*).
#. Per una nuova aliquota o natura duplicare l'imposta di acquisto più
   vicina: le due righe della ripartizione sono copiate. Cambiare il nome,
   l'importo e le griglie imposta quando cambia la natura, e fare lo stesso
   per la tabella dei rimborsi: le stesse righe nello stesso ordine.
#. Per le vendite in inversione contabile duplicare l'imposta *0% IC N6.x*,
   impostare :field:`Esenzione <l10n_it_exempt_reason>` e :field:`Riferimento
   legislativo <l10n_it_law_reference>` e scegliere l'imposta sulle righe
   fattura.
#. Posizione fiscale: il pacchetto ha *Subappalto Edilizia - IC*, che
   sostituisce *22% S* con *22% IC N6.3* (e 10%, 5%, 4%) sugli acquisti e
   *0%* con *0% IC N6.3* sulle vendite. Per le altre nature aggiungere le
   righe a una posizione fiscale simile.
#. Integrazione della fattura: Odoo non crea un secondo documento. La fattura
   fornitore con un'imposta di inversione contabile è essa stessa
   l'autofattura: una volta registrata, il pulsante [`Invia a SDI`] la invia
   allo SdI con il tipo documento scelto dalle griglie imposta (TD16 per
   l'inversione contabile interna, TD17 per i servizi dall'estero, TD18 per le
   merci dalla UE, TD19 per le merci in un deposito IVA). Una fattura con
   imposte dell'inversione contabile estera non può mescolare servizi e merci:
   Odoo non trova il tipo documento, quindi usare una fattura per ciascuno,
   con l':field:`Ambito imposta <tax_scope>` giusto.


**Scelta del tipo TD**

La funzione ``_l10n_it_edi_get_document_type`` scorre la tabella
``_l10n_it_edi_document_type_mapping``. Usa la prima riga i cui criteri
corrispondono tutti:

.. list-table::
   :header-rows: 1

   * - TD
     - Caso
     - Criteri di corrispondenza
   * - TD16
     - Inversione contabile interna
     - VJ6, VJ7, VJ8, da VJ12 a VJ17
   * - TD17
     - Servizi dall'estero
     - VJ3, servizi
   * - TD18
     - Merci UE
     - VJ9, merci, partner in UE
   * - TD19
     - Merci in Italia / deposito IVA
     - VJ3, merci, goods_in_italy
   * - TD28
     - San Marino
     - paese del partner SM
