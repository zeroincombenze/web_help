Non serve configurazione. Le pagine sono ricostruite all'avvio del server
quando cambia una sorgente di aiuto; un editor dell'aiuto può forzarlo con
**Ricostruisci tutte le pagine** in *Aiuto > Editor dell'aiuto > Pagine di aiuto*.

Ogni utente interno legge l'aiuto. Le pagine di aiuto e le loro regole sono
scritte dagli utenti del gruppo **Editor dell'aiuto** (*Impostazioni > Utenti*,
sezione *Aiuto contestuale*), senza diritti di amministratore: hanno la
sezione *Editor dell'aiuto* nella barra a sinistra del menu **Aiuto** (pagine,
regole, domande poste) e il pulsante **Modifica** della finestra di aiuto. Anche gli amministratori sono editor dell'aiuto.

I video inseriti nelle pagine di aiuto sono letti dalla cartella del parametro
di sistema ``web_help_video_path`` (predefinito ``~/Video``, la home
dell'utente che esegue Odoo), sottocartelle comprese; si cambia in
*Impostazioni > Tecnico > Parametri di sistema*.
