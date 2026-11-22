.. _configure:

Come configurare
----------------

* Le imposte sono in **Fatturazione ‣ Configurazione ‣ Contabilità ‣
  Imposte**, per gli utenti che vedono il menu **Configurazione**.
* Le imposte di un paese sono caricate dalla localizzazione fiscale:
  **Fatturazione ‣ Configurazione ‣ Impostazioni**, blocco **Localizzazione
  fiscale**, campo *Pacchetto*. Il pacchetto si può scegliere solo finché
  l'azienda non ha registrazioni contabili.
* Nella stessa pagina il blocco **Imposte predefinite** ha i campi *Imposta su
  vendite* e *Imposta su acquisti*: scegliere le imposte proposte sui nuovi
  prodotti (il pacchetto italiano imposta *22%* sulle vendite e *22% M* sugli
  acquisti). Sul prodotto,
  scheda **Informazioni generali**, i campi *Imposte vendite* e *Imposte
  d'acquisto* contengono le imposte di quel prodotto.
* Le **Posizioni fiscali** (**Fatturazione ‣ Configurazione ‣ Contabilità ‣
  Posizioni fiscali**) sostituiscono le imposte dei prodotti: nella scheda
  **Mappatura imposta**, *Imposta su prodotto* è sostituita da *Imposta da
  applicare*. Una posizione si sceglie sul partner, scheda **Fatturazione**,
  gruppo **Informazioni fiscali**, campo *Posizione fiscale*, oppure è
  rilevata automaticamente.
* I **Gruppi imposta** (menu **Fatturazione ‣ Configurazione ‣ Contabilità ‣
  Gruppi imposta**, solo in modalità sviluppatore) impostano i conti del
  totale di ogni imposta e il titolo con cui è stampata.

**Come attivare un'imposta del pacchetto**

#. Aprire **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Imposte** e cercare
   l'imposta per nome o per importo: le imposte archiviate sono nella lista,
   in grigio.
#. Fare clic sull'interruttore **Attivo** della riga.

.. help-if:: module = l10n_it

   **Altri piani dei conti italiani**

   Il modulo ``l10n_it_coa`` (**Italia - Piano dei conti (Zeroincombenze)**)
   porta con sé le proprie imposte, con nomi italiani come *IVA 22% su
   vendite*, *Art. 17ter - split-payment* o *Acq. (RC 22%) N.I. art.17 c.2
   DPR633*, e senza codice natura: i passi sopra per attivare o duplicare
   un'imposta sono gli stessi, i nomi dei capitoli *Come inserire
   un'imposta ...* sono quelli di ``l10n_it``.
