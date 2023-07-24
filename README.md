# Gender-Econ-Pipeline
Gendere Econ Pipeline è un progetto che coinvolge tecniche di programmazione e interpretazione dati con l'obiettivo di visualizzare graficamente la percentuale di donne nei vari livelli di carriera studentesca e accademica in ambito economico-statistico.

## Introduzione 
Tramite l'interrogazione di banche dati [USTAT](http://ustat.miur.it/) (Ufficio Statistico - Ministero dell'Università e della Ricerca) e l'utilizzo di librerie Python, tra cui [Matplotlib](https://matplotlib.org/), il codice in questione elabora per gli anni richiesti la percentuale di donne per sei livelli di carriera studentesca e accademica: Laurea Triennale, Laurea Magistrale, Dottorato, Ricercatore, Professore Associato, Professore Ordinario.
Le percentuali calcolate vengono disposte su un grafico in cui l'asse x rappresenta i livelli di carriera e l'asse y il livello precentuale, con una linea che intersechi questi valori per ogni anno preso in considerazione.
Il grafico assemblato viene poi mostrato sulla pagina relativa alla Commissione di Genere della Società Italiana di Economica [(SIE)](https://www.siecon.org/it/chi-siamo/organizzazione/commissioni/commissione-di-genere/dati).<br />
Di seguito un esempio: ---------------------- *[Cambiare Immagine]* <br/>
<p align="center">
<img src="https://github.com/codicigluoni/Gender-Econ-Pipeline/assets/45213049/55210b8e-01bb-4c31-94a1-a175c609ac1d" width=50% height=50%>
</p>

## Risorse
Come appena anticipato, i dati necessari al progetto vengono estratti da banche dati USTAT, in particolare dalla sezione Open Data -> Università e, rispettivamente per carriera studentesca e accademica, -> Studenti o -> Personale.
I campi necessari all'elaborazione in questione,con suddivisione per categoria di analisi e link al database, sono:
- [Studenti](http://dati.ustat.miur.it/dataset/iscritti/resource/373294ff-b051-4ec1-996f-e52078640279?filters=ClasseNUMERO%3AL-33%7CClasseNUMERO%3ALM-56): Anno, Genere (maschile/femminile), Classe di Laurea (Triennale/Magistrale e Tipo di Corso), Numero Iscritti
* [Personale Accademico](http://dati.ustat.miur.it/dataset/dati-per-bilancio-di-genere/resource/92f2008d-958f-4e9c-ae5c-7a3dd418cd57?filters=AREA_SD%3A13%20-%20Scienze%20economiche%20e%20statistiche%7CAREA_GEO%3AITALIA): Anno, Genere (maschile/femminile), Area Scientifico Disciplinare (Scienze economiche e statistiche), Codice Ateneo (Aggregato o Singolo), Qualifica (Ricercatore/P. Associato/P. Ordinario), Numero Personale Attivo
+ Dottorandi: 
