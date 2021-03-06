# Telegram-bot

Tramite la libreria python-telegram-bot abbiamo realizzato un bot che permette di sfruttare il terzo modello trainato durante l'esercitazione sul machine learning.

Il modello ha performato in maniera eccellente quindi ho pensato di vedere come reagisse con immagini scattate da cellulare anche grossolanamente.

Il file [Relazione_machine_learning.ipynb](Relazione_machine_learning.ipynb) permette, se caricato su qualsiasi servizio compatibile coi IPython Notebook ( Si consiglia Google Colaboratory ), di effettuare il train del modello così da avere anche la possibilità di avere un modello personale.

Il file [bot.py](bot.py) contiene le funzioni principali per far funzionare il bot.   
Tramite la funzione image_handler raccoglie l'immagine che gli viene mandata.  
Effettua un salvataggio in locale della stessa, la rinomina con un numero random da 0 a 100000 e l'username del mittente per evitare che si creino immagini con lo stesso nome.   
Una volta rinominata utilizza la funzione [*recognition()*](rec_catdog.py#15) che è dichiarata nel file [rec_catdog.py](rec_catdog.py).

La funzione restituisce il risultato e una predizione numerica, ma viene utilizzata semplicemente per dare un po' di verve al bot.

Le altre funzioni utilizzate sono di test e non di interesse per il nostro scopo.

In [rec_catdog.py](rec_catdog.py) ritroviamo alcuni degli import mostrati nella parte configurativa della relazione.  
Impostiamo le grandezze dell' immagine  accettata dal modello, lo carichiamo tramite load_model.  
Definita la funzione convertiamo l'immagine in modo che sia compatibile col mnodello e traimte il predict effettuiamo la predizione.  
Come descritto precedentemente restituiamo la valutazione e il valore numerico.

# Installazione
Creare un bot su telegram e ottenere il token per utilizzarlo.
Prerequisiti: Avere Python:3.7.9, pip e virtualenv installati.

`git clone https://github.com/TheTrash/telegram-bot.git`

`virtualenv telegram-bot`

`cd telegram-bot`

Attivare il virtualenv:
- Linux: `source ./bin/activate`  
- Windows: `Scripts\activate`

Creare un file *token.txt* ed inserire il token ottenuto su telegram all'interno del file

`pip install -r requirements.txt`

*Attenzione, tensorflow su Windows potrebbe richiedere di installare pacchetti aggiuntivi manualmente*

per avviare il bot: `python bot.py`  
`Ctrl+c` per chiuderlo

Ed ecco attivo il bot