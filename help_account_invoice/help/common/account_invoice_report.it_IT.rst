.. _report:

Stampe ed esportazione
----------------------

.. help-version:: <13

   * **Fatture**: il PDF della fattura. Stamparlo con
     :version:`10|**Stampare**;11|**Stampa fattura**;*|**Invia e stampa**` o
     dal menu **Stampa**, anche dalla lista dopo aver selezionato le fatture.
     Dopo la validazione il PDF è salvato come allegato e ristampato
     identico.\ :version:`>=11| **Fatture senza pagamento** stampa lo stesso
     PDF senza i pagamenti ricevuti.`
   * :version:`10|**Invia per Email**;11|**Inviare per e-mail**;*|**Invia e
     stampa**` allega il PDF all'email; il messaggio resta nel chatter della
     fattura.
     :version:`12|**Anteprima** mostra la fattura come la vede il cliente nel
     portale.`
   * Analisi fatture: :version:`10|**Fatturazione ‣ Rendiconti ‣ Business
     intelligence ‣ Fatture**;11|**Fatturazione ‣ Rendicontazione ‣ Gestione ‣
     Fatture**;*|**Fatturazione ‣ Rendicontazione ‣ Amministrazione ‣
     Fatture**` mostra gli importi fatturati per periodo, partner, prodotto o
     addetto vendite, come grafico o tabella pivot.

.. help-version:: >=13

   * :version:`<18|**Fatture**;*|**PDF fattura**`: il PDF della fattura.
     Stamparlo dal menu **Stampa**\ :version:`>=17| (sotto l'icona
     dell'ingranaggio accanto al nome del record)`, :version:`<18|con **Invia
     e stampa**;*|con **Stampa**`, o dalla lista dopo aver selezionato le
     fatture. Dopo la conferma il PDF è salvato come allegato e ristampato
     identico.
   * :version:`13|**Fatture senza pagamento**;<18|**Fatture senza
     pagamenti**;*|**PDF senza pagamento**`: lo stesso PDF senza i pagamenti
     ricevuti, dal menu **Stampa**.
   * :version:`<18|**Invia e stampa**;*|**Invia**` allega il PDF all'email; il
     messaggio resta nel chatter della fattura. **Anteprima** mostra la
     fattura come la vede il cliente nel portale.
   * Analisi fatture: :version:`13|**Fatturazione ‣ Rendicontazione ‣
     Amministrazione ‣ Fatture**;*|**Fatturazione ‣ Rendicontazione ‣ Gestione
     ‣ Analisi fatture**` mostra gli importi fatturati per periodo, partner,
     prodotto o addetto vendite, come grafico o tabella pivot.

* Per ottenere un file delle fatture, selezionarli nella vista elenco, poi
  :version:`<=16|**Azione ‣ Esporta**;*|**Azioni ‣ Esporta**`: scegliere i
  campi e il formato (xlsx o csv). Vedere *Importare ed esportare dati* nella
  pagina **Pronto** dell'aiuto.

.. help-version:: 17

   * Per ottenere i documenti di più fatture in un unico file, selezionare le
     fatture clienti confermate nella vista elenco, poi **Azioni ‣ Esporta
     ZIP**: un file ZIP contiene il PDF e gli altri documenti legali di ogni
     fattura.

.. help-version:: >=18

   .. help-if:: module = l10n_it_edi

      * Per ottenere le fatture elettroniche in un unico file, selezionare le
        fatture nella vista elenco, poi **Stampa ‣ XML FatturaPA**: una
        fattura dà il suo file XML, più fatture danno un file ZIP
        (*invoices.zip*) con l'XML di ciascuna. Le fatture senza fattura
        elettronica sono ignorate. **Stampa ‣ PDF** fa lo stesso con i PDF.

   .. help-if:: module = l10n_it_edi_extension

      * Per caricare fatture elettroniche prodotte fuori da Odoo (ad es. da un
        altro software, o scaricate dal portale Fatture e Corrispettivi
        dell'Agenzia delle Entrate), mettere i file XML o P7M in un file ZIP,
        poi **Fatturazione ‣ Fornitori ‣ File importazione e-fattura**:
        caricare lo ZIP e premere **Importa file**. Ogni fattura elettronica
        diventa una fattura cliente o una fattura fornitore, secondo che
        l'azienda sia il venditore o l'acquirente, con la fattura elettronica
        allegata; un file con più fatture dà una fattura per ciascuna. Alla
        fine è mostrata la lista delle fatture importate. I file che non sono
        XML o P7M sono ignorati ed elencati in un'attività *Da fare*
        dell'utente. Se un file con lo stesso nome è già stato importato, non
        è importato nulla e un errore indica il file.
