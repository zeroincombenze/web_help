.. _report:

Stampe ed esportazione
----------------------

.. help-version:: <13

   * Analisi fatture: :version:`10|**Fatturazione ‣ Rendiconti ‣ Business
     intelligence ‣ Fatture**;11|**Fatturazione ‣ Rendicontazione ‣ Gestione ‣
     Fatture**;*|**Fatturazione ‣ Rendicontazione ‣ Amministrazione ‣
     Fatture**` mostra gli importi fatturati per periodo, partner o prodotto,
     come grafico o tabella pivot: le fatture fornitore ne fanno parte,
     filtrarle per tipo.

.. help-version:: >=13

   * Analisi fatture: :version:`13|**Fatturazione ‣ Rendicontazione ‣
     Amministrazione ‣ Fatture**;*|**Fatturazione ‣ Rendicontazione ‣ Gestione
     ‣ Analisi fatture**` mostra gli importi fatturati per periodo, partner o
     prodotto, come grafico o tabella pivot: le fatture fornitore ne fanno
     parte, filtrarle per tipo.

* Per ottenere un file delle fatture fornitore, selezionarle nella vista
  elenco, poi :version:`<=16|**Azione ‣ Esporta**;*|**Azioni ‣ Esporta**`:
  scegliere i campi e il formato (xlsx o csv). Vedere *Importare ed esportare
  dati* nella pagina **Pronto** dell'aiuto.

.. help-version:: >=18

   .. help-if:: module = l10n_it_edi_extension

      * Per caricare fatture elettroniche prodotte fuori da Odoo (ad es. da un
        altro software, o scaricate dal portale Fatture e Corrispettivi
        dell'Agenzia delle Entrate), mettere i file XML o P7M in un file ZIP,
        poi **Fatturazione ‣ Fornitori ‣ File importazione e-fattura**:
        caricare lo ZIP e premere [`Importa file`]. Ogni fattura elettronica
        diventa una fattura fornitore (o una fattura cliente, se l'azienda è
        il venditore), con la fattura elettronica allegata; un file con più
        fatture dà un documento per ciascuna. Alla fine è mostrata la lista
        dei documenti importati. I file che non sono XML o P7M sono ignorati
        ed elencati in un'attività *Da fare* dell'utente. Se un file con lo
        stesso nome è già stato importato, non è importato nulla e un errore
        indica il file.
