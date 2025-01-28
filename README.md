Pythonkurs README:

Pythonkurset går og 2,5 dager og ganske intensivt. Av erfaring er det litt spredning i forhåndskunnskaper på elevene. Derfor vil det være endel ekstra materiale for de som vil bryne seg på vanskerligere oppgaver. For å løse ekstra oppgavene vil man ofte måtte søke informasjon selv på internett. 
Vi har ikke løsningsforslag for ekstra oppgavene.

Vi kommer til å gå igjennom presentasjonene i fellesskap, og oppgavene gjøres individuelt. 

Presentasjoner ligger i presentasjoner/
- Disse presentasjonene er "notebooks" for Jupyter lab som skal brukes i kurset.
- Kan også se presentasjonene i html-form (I disse kan ikke kodesnippets kjøres) i presentasjoner/html hvis man ikke vil se de i Jupyter
- Oppgaver finner man underveis i presentasjonene/

Løsningsforslag ligger i løsningsforslag/
- Det vil bli gitt ut løsningsforslag underveis i kurset.
- Noen oppgaver er løst i notebooks og andre som script

Nyttige script som blir brukt underveis i scriptet ligger i mappa script/

Kurset kan klones med git hvis du har git installert 
git clone git@github.com:Emanon79/python-kurs.git
Eller lastes ned som zip
https://github.com/Emanon79/python-kurs/archive/refs/heads/main.zip

Start med å lese "01 - Introduksjon". Der står det også hva man skal starte med (litt mer detaljert), men for å komme i gang:

Last ned Python 3.13 fra https://www.python.org/downloads/ 
Har du allerede python i litt eldre versjon (3.12, 3.11,3.10,3.9) vil det også fungere fint.

På Linux:
Python er som regel forhånds installert på Linux. Det kan også installeres med pakkemanageren "sudo apt install python3 python3-pip". Da får du som regel en litt eldre versjon, feks. 3.12,3.11,3.10 eller 3.9, men disse kan også brukes fint)

En bestemt versjon av Python installeres slik:
```sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update 
sudo apt install python3.13
```


På Windows:
- Åpne cmd og kjør: "py --version" Verifiser at den sier "Python 3.13.x" Py launcher er den foretrukkede måten å kjøre python på i Windows. 
- Legger man inn python i Windows in miljøvariabel %PATH% vil "python --version" fungere. 
- Hver gang man ser "python" i presentasjonene og oppgavene kan dette byttes ut med "py" eller "py -3" på Windows for å bruke py launcher istedenfor.

På Linux:
- Åpne terminalen og skriv "python3 --version" (evt. kan det hende din distro har kalt versjon 3 av python for "python")
- Verifiser at den sier "Python 3.13.x .. " etc.

For å bruke Jupyter lab og åpne notebookene (.ipynb-filene):
- Installer pakker evt. spesifiser de direkte
  - pip install -r requirements.txt
evt:
  - pip install Flask jupyterlab requests fastapi uvicorn typer

Hvis pip ikke funker (på Windows) bytt ut pip med "py -3 -m pip":
- py -m pip install -r requirements.txt

Vi har tidligere brukt virtuelle miljøer i kurset (for å installere pakker osv.), men for å unngå å skape forvirring så går vi ikke gjennom dette.
Dere kan helt fint bruke dette selv, hvis det er noe dere pleier. På linux kan man source bin/source\_venv.sh med en requirements-fil som argument
for å få et venv med nødvendige pakker installert: 'source bin/source\_venv.sh requirements.txt'

##### Installer og kjør Jupyterlab
Jupyter lab / notebook er et GUI i nettleseren man kan bruke for å kjøre Pythonkode mer interaktivt enn i et script.
Her kan man kjøre snippets med kode og få resultater tilbake.
Vi kommer til å bruke dette i kurset, og alle presentasjoner er notebooks!
```bash
pip install jupyterlab (Hvis ikke allerede installert i forrige steg)
jupyter lab
```
Hvis dette ikke fungerer, bytt ut "jupyter" med `python3 -m jupyter`
```bash
python3 -m jupyter lab
```
evt. med py launcher for Windows:
```bash
py -m jupyter lab
```

Du skal nå få opp et nytt vindu i nettleseren din. Her kan man se presentasjoner osv.
