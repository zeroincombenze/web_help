.. _new_record:

Come inserire un nuovo record
-----------------------------

#. Aprire **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Piano dei conti** e
   premere [`Nuovo`]: in cima all'elenco si apre una riga. I conti esistono
   solo dopo aver scelto un pacchetto di *Localizzazione fiscale*, vedere
   *Come configurare*.
#. Scrivere il :field:`codice <code>`, ad es. ``101000``: solo lettere, cifre
   e punti, unico nell'azienda. Il nuovo codice è controllato quando il conto
   è salvato.
#. Scrivere il :field:`nome conto <name>`, ad es. *Attività correnti*, poi
   scegliere la :field:`tipologia <account_type>`. Se si lascia vuota, la
   tipologia e le etichette sono copiate dal conto con il codice subito
   precedente a quello nuovo.
#. Lasciare o cambiare l'interruttore *Consentire riconciliazione*: è attivo
   per i conti di credito e di debito e non può essere attivo per i conti di
   banca e cassa, carta di credito e fuori bilancio; lasciarlo spento per gli
   altri conti, salvo che si riconcilino le loro righe (ad es. un conto
   transitorio).
#. Salvare la riga, poi premere il pulsante con la freccia a fine riga (*Apri
   nella vista modulo*) per compilare gli altri campi della maschera: le
   :field:`Imposte predefinite <tax_ids>`, le :field:`Etichette <tag_ids>`, i
   :field:`Registri autorizzati <allowed_journal_ids>` e, con più valute, la
   :field:`Valuta del conto <currency_id>`.
#. Il record è salvato automaticamente quando lo si lascia; premere l'icona
   della nuvola accanto al breadcrumb per salvare subito.

Un altro conto si crea da uno esistente con l'icona dell'ingranaggio ‣
**Duplica**: il codice è aumentato fino a uno libero e il nome riceve
*(copia)*.
