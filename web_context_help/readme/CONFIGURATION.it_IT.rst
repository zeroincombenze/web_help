Non serve configurazione. Le pagine sono ricostruite all'avvio del server quando
cambia una sorgente di aiuto; un editor dell'aiuto può forzarlo con
**Ricostruisci tutte le pagine** in *Aiuto > Editor dell'aiuto > Pagine di
aiuto*.

Livello di aiuto degli utenti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ogni utente interno legge l'aiuto. Il livello di aiuto di un utente si imposta
nella scheda utente (*Impostazioni > Utenti*, campo **Aiuto contestuale** nella
sezione *Accessi applicazione*):

* vuoto: nessuna modifica, l'aiuto è solo letto;
* **Nessun aiuto**: l'aiuto non è mostrato all'utente: niente pulsante |sos|
  nelle viste, niente menu **Aiuto**, e le pagine di aiuto sono rifiutate;
* **Utente**: modifica le pagine di aiuto con priorità minore di 64 e le loro
  regole. Modificando una pagina con priorità 64 o più, ad es. una pagina di un
  modulo (96), se ne crea una copia con la priorità predefinita (32) e si
  modifica la copia: avendo priorità più alta, è mostrata al posto
  dell'originale;
* **Sistema**: modifica tutte le pagine di aiuto.

I livelli **Utente** e **Sistema** non richiedono diritti di amministratore:
hanno, aprendo l'app **Aiuto**, il menu *Editor dell'aiuto* nella barra in alto
(pagine, regole, domande poste) e il pulsante [`Modifica`] della finestra di
aiuto.

Il campo imposta anche il livello degli amministratori: partono come **Sistema**
(all'installazione del modulo, o se lo avevano già prima di questa versione) e
possono essere abbassati a **Utente**, a nessuna modifica o a **Nessun aiuto**.
Un utente reso amministratore in seguito non ha un livello di aiuto predefinito.

Video
~~~~~

I video inseriti nelle pagine di aiuto sono letti dalla cartella del parametro
di sistema ``web_help_video_path`` (predefinito ``~/Video``, la home dell'utente
che esegue Odoo), sottocartelle comprese; si cambia in *Impostazioni > Tecnico >
Parametri di sistema*.
