.. _example:

Esempi
------

**Il cliente vuole le fatture inviate alla sede centrale**

Aprire l'azienda, in **Contatti e indirizzi** premere **Crea**, scegliere
:version:`11|*Indirizzo fatturazione*;*|*Indirizzo fattura*`, scrivere
l'indirizzo della sede e **Salva e chiudi**: i nuovi ordini lo propongono come
indirizzo di fatturazione.

**Una persona passa a un'altra azienda**

Aprire la persona, premere **Modifica**, cambiare l':field:`azienda
<parent_id>` e **Salva**: l'indirizzo e i dati commerciali vengono ora dalla
nuova azienda; i documenti vecchi conservano quelli vecchi.

**Un cliente è stato creato due volte**

Aprire la copia non ancora usata, controllare che non abbia documenti
(pulsanti in alto) ed eliminarla; se ha documenti, archiviarla.

.. help-version:: <=12

   **Un cliente è anche fornitore**

   Selezionare :field:`È un fornitore <supplier>` nella scheda **Vendite e
   acquisti**: lo stesso contatto è proposto su ordini di acquisto e fatture
   fornitore.

.. help-version:: >=13

   **Un cliente è anche fornitore**

   Non c'è niente da impostare: lo stesso contatto si può scegliere su
   documenti di vendita e di acquisto; compare tra i fornitori dopo il suo
   primo ordine di acquisto o fattura fornitore.
