.. _new_record_split:

Come inserire un'imposta per la scissione dei pagamenti
-------------------------------------------------------

Nella scissione dei pagamenti il cliente è una pubblica amministrazione: paga
al fornitore solo l'imponibile e l'IVA va all'erario. Il pacchetto *Italia*
carica, per ogni aliquota, tre imposte:

* *22% SP pos.*, *10% SP pos.*, *5% SP pos.*, *4% SP pos.*: tipo *Nessuno*,
  l'IVA positiva, con le griglie imposta del report IVA e quella della
  scissione dei pagamenti (VE38);
* *22% SP neg.*, *10% SP neg.*, *5% SP neg.*, *4% SP neg.*: tipo *Nessuno*,
  con importo negativo (-22, -10, -5, -4) e :field:`Compresa nel prezzo
  <price_include_override>` *Imponibile*, che annullano l'IVA nel totale della
  fattura;
* *22% SP*, *10% SP*, *5% SP*, *4% SP*: tipo *Vendita*, :field:`Calcolo
  imposta <amount_type>` *Gruppo di imposte*, con le due imposte sopra nella
  tabella **Imposte figlie**: sono queste da scegliere sulle fatture.

La ripartizione delle due figlie registra l'imposta sul conto *IVA c/Split
Payment*; il gruppo imposta dell'imposta di gruppo è *Scissione dei
Pagamenti*. Non modificarle: duplicare l'intero gruppo di tre quando serve
un'altra aliquota.

#. Aprire **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Imposte**, togliere
   i filtri **Vendita** e **Acquisto** e cercare ``SP``: ci sono le dodici
   imposte. Sono attive quando il pacchetto viene installato.
#. Aprire **Fatturazione ‣ Configurazione ‣ Contabilità ‣ Posizioni fiscali**
   e aprire *Scissione dei Pagamenti*: nella scheda **Mappatura imposta**
   *22%* è sostituita da *22% SP*, e così per 10%, 5% e 4%.
#. Sul partner pubblica amministrazione, scheda **Fatturazione**, gruppo
   **Informazioni fiscali**, scegliere la *Posizione fiscale* *Scissione dei
   Pagamenti*. Le fatture del partner prendono le imposte di gruppo.
#. Per un'aliquota non caricata (ad es. 21%) duplicare le tre imposte di
   un'aliquota: cambiare i nomi e gli importi delle due figlie (+21 e -21), il
   :field:`Gruppo imposta <tax_group_id>` di quella positiva (*IVA 21%*), poi
   sull'imposta di gruppo sostituire le :field:`Imposte figlie
   <children_tax_ids>` con le due nuove. Poi aggiungere la riga alla
   *Mappatura imposta* della posizione fiscale.

