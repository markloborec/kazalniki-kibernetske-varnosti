import csv
import datetime
import os.path

from calsec.config import TipIncidenta
from calsec.models import Incident

incidenti: list[Incident] = []

incidentiFile = "incidenti.csv"

def update():
    global incidenti
    incidenti = []

    if not os.path.isfile(incidentiFile):
        print(f"{incidentiFile} ne obstaja!")
        return

    with open(incidentiFile, 'r') as file:
        for ele in  csv.DictReader(file):
            incident = Incident(
                datum= datetime.datetime.strptime(ele['datum'], "%Y-%m-%d").date(),
                kategorija=ele['kategorija']
            )
            incidenti.append(incident)

    print(incidenti)
def save():
    with open(incidentiFile, 'w') as file:
        dw = csv.DictWriter(file, ['datum', 'kategorija'])
        dw.writeheader()
        for inc in incidenti:
            dw.writerow(inc.__dict__)

def addIncident(inc: Incident):
    incidenti.append(inc)
    save()

def searchIncidents(tip: str):
    foundInc = []
    for inc in incidenti:
        if inc.kategorija == tip:
            foundInc.append(inc)
    return foundInc

if __name__ == '__main__':
    incidenti = [
        Incident(datum=datetime.date.today(), kategorija=TipIncidenta.Aktivnost_cloveskih_virov),
        Incident(datum=datetime.date.today(), kategorija=TipIncidenta.Aktivnost_cloveskih_virov),
        Incident(datum=datetime.date.today(), kategorija=TipIncidenta.Aktivnost_cloveskih_virov),
        Incident(datum=datetime.date.today(), kategorija=TipIncidenta.Aktivnost_cloveskih_virov),

    ]

    update()
    update()