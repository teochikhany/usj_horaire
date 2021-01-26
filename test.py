import requests
import json


x = "https://etudiant.usj.edu.lb/commonfiles/fullCalendar/fonctions.php?cod_etu=201587&annee=2021&semestre=2&jourMin=2021-01-25"

horaire_site = requests.get(x)


y = json.loads(horaire_site.text)

for ss in y:
    print(ss["start"])
    print(ss["end"])
    print(ss["title"])
    print("====================\n")