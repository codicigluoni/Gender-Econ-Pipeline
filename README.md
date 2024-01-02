# Gender-Econ-Pipeline
Gendere Econ Pipeline è un progetto che coinvolge tecniche di programmazione e interpretazione dati con l'obiettivo di visualizzare graficamente la percentuale di donne nei vari livelli di carriera studentesca e accademica in ambito economico-statistico.

## Introduzione 
Tramite l'interrogazione di banche dati [USTAT](http://ustat.miur.it/) (Ufficio Statistico - Ministero dell'Università e della Ricerca) e l'utilizzo di librerie Python, tra cui [Matplotlib](https://matplotlib.org/), il codice in questione elabora per gli anni richiesti la percentuale e il valore assoluto di donne per sei livelli di carriera studentesca e accademica: Laurea Triennale, Laurea Magistrale, Dottorato (_Implementazione subordinata alla disponibilità prossima dei relativi dati_), Ricercatrice, Professoressa Associata, Professoressa Ordinaria.
I valori calcolati  vengono disposte su un grafico in cui l'asse x rappresenta i livelli di carriera e l'asse y il livello precentuale (o valori assoluti), con una linea che intersechi questi valori per ogni anno preso in considerazione.
I graifici assemblati vengono poi mostrati sulla pagina relativa alla Commissione di Genere della Società Italiana di Economia [(SIE)](https://www.siecon.org/it/chi-siamo/organizzazione/commissioni/commissione-di-genere/dati).<br />

Di seguito un esempio:<br/>
<p align="center">
<img src="https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/12124f73edca7de522f44e5c00d1c1653ab4d177/graph.png" width=50% height=50%>
<img src="https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/ccaf00bbf809623e5861a633c372caaa6f5ab08a/graph_abs.png" width=50% height=50%>
</p>

## Risorse
Come appena anticipato, i dati necessari al progetto vengono estratti da banche dati USTAT, in particolare dalla sezione [Open Data](https://ustat.miur.it/opendata) -> Università e, rispettivamente per carriera studentesca e accademica, -> Studenti o -> Personale.
I campi necessari all'elaborazione in questione, con suddivisione per categoria di analisi e link al database, sono:
- [Studenti](http://dati.ustat.miur.it/dataset/iscritti/resource/373294ff-b051-4ec1-996f-e52078640279?filters=ClasseNUMERO%3AL-33%7CClasseNUMERO%3ALM-56): Anno, Genere (maschile/femminile), Classe di Laurea (Triennale/Magistrale e Tipo di Corso), Numero Iscritti;
* [Personale Accademico](http://dati.ustat.miur.it/dataset/dati-per-bilancio-di-genere/resource/92f2008d-958f-4e9c-ae5c-7a3dd418cd57?filters=AREA_SD%3A13%20-%20Scienze%20economiche%20e%20statistiche%7CAREA_GEO%3AITALIA): Anno, Genere (maschile/femminile), Area Scientifico Disciplinare (Scienze economiche e statistiche), Codice Ateneo (Aggregato o Singolo), Qualifica (Ricercatore/P. Associato/P. Ordinario), Numero Personale Attivo;
+ [Dottorandi](http://dati.ustat.miur.it/dataset/formazione-post-laurea/resource/dc36643d-3f1c-47ea-9748-79c4f2f174e1): _In attesa che le variabili di interesse vengano rese disponibili_

## Struttura Codice
Il codice, contenuto per la maggior parte nel file [Gender_Econ_Pipeline_Git.py](https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/main/Gender_Econ_Pipeline_Git.py), si struttura in quattro sezioni:
1. Enviroment Set Up
2. Previous Analysis Check
3. Data Analysis
4. Graphic Plot <br/>

Inoltre, per semplice questione di ordine, due funzioni sono definite in un file esterno, nominato [functions_Git.py](https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/main/functions_Git.py).<br/>
Fondamentali per il funzionamento del codice sono i tre file generati una volta che questo viene eseguito: [graph.png](https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/main/graph.png), [graph_abs.png](http://dati.ustat.miur.it/dataset/formazione-post-laurea/resource/dc36643d-3f1c-47ea-9748-79c4f2f174e1) e [years.csv](https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/main/years.csv) (in questa repository sono presenti tre esempi *[Da sostituire ogni qualvolta il codice venisse aggiornato]* ). Viene inoltre salvato i file [fulldata.csv](https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/main/fulldata.csv) e [fulldata_abs.csv](https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/ccaf00bbf809623e5861a633c372caaa6f5ab08a/fulldata_abs.csv) contenenti i dati elaborati mostrati nei grafici.

### Enviroment Set Up
Nella prima parte del codice vengono fatte due richieste JSON all'API dei database USTAT: il [database relativo al personale accademico](http://dati.ustat.miur.it/api/3/action/datastore_search?resource_id=92f2008d-958f-4e9c-ae5c-7a3dd418cd57) viene filtrato secondo Area Scientifico Disciplinare, ```AREA_SD```, (13 - Scienze economiche e statistiche) e Codice Ateneo, ```CODICE_ATENEO```, (TTTTT, che rappresenta il dato aggregato), mentre il [database relativo agli studenti](http://dati.ustat.miur.it/api/3/action/datastore_search?resource_id=373294ff-b051-4ec1-996f-e52078640279) viene filtrato secondo le classi di laurea,```ClasseNUMERO```, (L-33, laurea triennale in scienze economiche e statistiche. ed L-56, laurea magistrale in scienze economiche), ponendo come numero limite di risultati ```limit=10000``` per non incorrere nel rischio di scartare elementi di interesse. I dati estratti vengono salvati rispettivamente in ```data_academic``` e ```data_stud```. <br/>
Istruzioni riassuntive per la ricerca dei database in questione possono essere consultate a questo [link](http://dati.ustat.miur.it/api/3/action/help_show?name=datastore_search), mentre istruzioni approfondite sull'API utilizzata da USTAT sono presenti a questo [link ](https://docs.ckan.org/en/latest/maintaining/datastore.html#making-a-data-api-request).<br/>
<br/>
Vengono poi calcolati tramite il ricorso alla funzione esterna ```yr_interval()``` nel file [functions_Git.py](https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/main/functions_Git.py) gli anni per cui può essere eseguito il programma. Viene quindi calcolata l'intersezione degli anni presenti nei database in analisi in modo da assicurarsi la consistenza delle operazioni successive. <br/>
Il numero di anni per cui si vuole procedere con l'analisi può essere modificato a piacimento tramite la modifica della variabile ```req_yr```: nel caso fosse necessaria la visualizzazione di un numero di anni maggiore di 4, andranno aggiunti di conseguenza i relativi casi ```if```. <br/>
È stata aggiunta la costruzione ```key=lambda x:abs(x-[...]``` per identificare l'anno più "vicino" a quello richiesto per ovviare alla mancanza nel database di un determinato anno, nonostante questa evenienza non dovesse presentarsi per la natura stessa dei dati utilizzati.<br/>
Per esempio, dati rispettivamente l'anno meno recente e l'anno più recente quali 2012 e 2021, nella visualizzazione dei dati per 3 anni viene identificato come terzo anno quello equidistante dai due tramite ```(int(min(list_intersection) + (max(list_intersection)-min(list_intersection))/2))```, che rende in questo caso il valore 2016. Nel caso in cui l'anno 2016 non fosse presente in tutte le strutture dati, l'anno comune più vicino sarebbe selezionato.
### Previous Analysis Check
La seconda sezione consiste essenzialmente nel controllo che i dati per gli anni richiesti siano già stati calcolati o meno. In altre parole, se i database USTAT non sono stati aggiornati e la variabile ```req_yr``` non è stata modificata dall'ultima volta in cui il codice è stato eseguito, un ulteriore esecuzione del codice riporterebbe gli stessi dati, risultando quindi inutile.<br/>
<br/>
Ogni volta che il codice viene completamente eseguito viene creato il file [years.csv](https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/main/years.csv) contenente gli anni per cui i dati sono stati elaborati: nel caso in cui il file non sia presente oppure se gli anni calcolati nella sezione precedente e contenuti in ```Years``` fossero diversi da quelli presenti in ```years.csv``` il codice viene eseguito nel suo intero. Se gli anni corrispondono, l'esecuzione del codice termina.
### Data Analysis
Nel caso in cui fosse la prima volta che il codice viene eseguito, e quindi ```years.csv``` risultasse inesistente, oppure fossero disponibili nuovi anni da analizzare, il codice inizia ad analizzare i dati e i nuovi anni che verranno analizzati vengono salvati in un file csv nominato ```years.csv```, andando eventualmente a sostiture il file vecchio.<br/>
Per ogni categoria d'interesse viene quindi calcolato il numero di individui totale per ogni anno e il numero di individui di genere femminile per ogni anno, così da poter calcolare le percentuali e i valori assoluti. Per esempio le percentuali, per studenti e personale accademico, vengono salvate rispettivamente in ```pg_stud_matrix``` e ```pg_staff_matrix```, matrici a due dimensioni dalla forma:
<p>
<img src="https://github.com/codicigluoni/Gender-Econ-Pipeline/assets/45213049/ff5e91d3-f2ea-48f0-b3e6-e67bb04f29d0" width=22% height=22%>
<img src="https://github.com/codicigluoni/Gender-Econ-Pipeline/assets/45213049/55f3e83b-63e1-41d1-b2fb-87cbb349dabc" width=30% height=30%> 
</p> <br/>


Il significato della notazione %f_"categoria"<sub>n</sub> nelle matrici è: percentuale di presenza femminile nella categoria in questione nell'anno n.
Le percentuali calcolate vengono quindi passate alla funzione ```pl0t_th1s_gr4ph()```, la quale verrà approfondita nella prossima sezione, e vengono unite per essere salvati come file excel in ```fulldata.csv```.
Ragionamento equivalente vale per i valori assoluti.

### Graphic Plot
In conclusione vengono chiamate le funzioni esterne ```pl0t_th1s_gr4ph()``` e ```pl0t_th1s_gr4ph_abs()```, definite nel file [functions_Git.py](https://github.com/codicigluoni/Gender-Econ-Pipeline/blob/main/functions_Git.py), che tramite la libreria [Matplotlib](https://matplotlib.org/) ha il compito  di generare un grafico partendo dai valori calcolati. Per una futura modifica dei grafici si consiglia la consultazione della [Guida Utenti](https://matplotlib.org/stable/users/index) e la ricerca di esempi su [Stack Overflow](https://stackoverflow.com/questions/tagged/matplotlib): per esempio, gli stili per le linee sono ben consultabili [qui](https://stackoverflow.com/questions/13359951/is-there-a-list-of-line-styles-in-matplotlib).<br/>
Il ciclo ```for``` viene quindi utilizzato per formare la lista di dati relativi all'asse y. Nel codice, ```y``` viene creata come un array (una sola riga) per poi aggiungere tramite ```np.vstack()``` tante righe quanti sono gli anni analizzati. Questa struttura è stata creata in modo che il codice possa essere dinamico e quindi poter rappresentare diversi numeri di anni semplicemente modificando ```req_yr``` come spiegato [in precedenza](https://github.com/codicigluoni/Gender-Econ-Pipeline/edit/main/README.md#enviroment-set-up). È importante notare che nel caso in cui si volesse rappresentare un numero di anni maggiore di 4, sarà necessario premurarsi che i vettori contenenti gli stili e i colori per le linee, rispettivamente ```CB_color_cycle``` e ```linestyle_str```, siano abbastanza popolati da poter supportare il numero di anni richiesto: in altre parole, se la rappresentazione dovrà contenere i dati per 7 anni, allora i vettori appena citati dovranno avere rispettivamente 7 e 6 elementi (lo stile della linea rappresentante l'anno più recente è di default "solid" e non è specificato nel codice né incluso in ```linestyle_str```).<br/>
Quando ```plt.plot(x,y[j]...``` viene eseguito, il primo elemento di ```x``` viene associato al primo elemento di ```y[j]``` e avanzando in questo senso viene composta la linea del grafico per l'anno in posizione ```j``` in ```Years```.
Una volta terminato il ciclo for, ```y``` avrà la seguente forma:
<p align="center">
<img src="https://github.com/codicigluoni/Gender-Econ-Pipeline/assets/45213049/44910297-6530-49ec-b614-73471d67f543" width=40% height=40%>
</p> <br/>

Le ultime linee del codice fanno riferimento a specifiche del grafico, facilmente e liberamente modificabili leggendo direttamente i commenti del codice stesso.



