Non serve configurazione. Le pagine sono ricostruite all'avvio del server
quando cambia una sorgente di aiuto; un editor dell'aiuto può forzarlo con
**Ricostruisci tutte le pagine** in *Aiuto > Editor dell'aiuto > Pagine di aiuto*.

Ogni utente interno legge l'aiuto. Chi lo modifica si imposta nella scheda
utente (*Impostazioni > Utenti*, campo **Aiuto contestuale** nella sezione
*Applicazione*):

* vuoto: nessuna modifica, l'aiuto è solo letto;
* **Utente**: modifica le pagine di aiuto con priorità minore di 64 e le loro
  regole. Modificando una pagina con priorità 64 o più, ad es. una pagina di
  un modulo (96), se ne crea una copia con la priorità predefinita (32) e si
  modifica la copia: avendo priorità più alta, è mostrata al posto
  dell'originale;
* **Sistema**: modifica tutte le pagine di aiuto, come prima.

Il campo imposta anche il livello degli amministratori: partono come
**Sistema** (all'installazione del modulo, o se lo avevano già prima di
questa versione) e possono essere abbassati a **Utente** o a nessuna
modifica. Un utente reso amministratore in seguito non ha un livello di aiuto
predefinito.

Nessuno dei due livelli richiede diritti di amministratore: hanno la sezione *Editor
dell'aiuto* nella barra a sinistra del menu **Aiuto** (pagine, regole,
domande poste) e il pulsante **Modifica** della finestra di aiuto.

I video inseriti nelle pagine di aiuto sono letti dalla cartella del parametro
di sistema ``web_help_video_path`` (predefinito ``~/Video``, la home
dell'utente che esegue Odoo), sottocartelle comprese; si cambia in
*Impostazioni > Tecnico > Parametri di sistema*.
