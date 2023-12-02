import datetime

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDateEdit, QComboBox, QPushButton, QLabel, QListWidget

from calsec import utils, config, db, func
from calsec.models import Incident
from calsec.widgets import DictionaryTableModel


class MainWindow(QtWidgets.QMainWindow):
    datumIncidentaDE : QDateEdit
    kategorijaIncidentaCB: QComboBox
    vnesiIncidentPB: QPushButton
    incidentiLW: QListWidget
    tepsL: QLabel
    thssL: QLabel
    spsL: QLabel
    tnppsL: QLabel
    oimtbiL: QLabel

    def __init__(self):

        super(MainWindow, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi(utils.getPath(__file__, 'gui.ui'), self)  # Load the .ui file

        self.datumIncidentaDE.setDate(datetime.date.today())
        for key, value in config.TipIncidenta.__dict__.items():
            if not key.startswith("__") and isinstance(value, str):
                self.kategorijaIncidentaCB.addItem(value)

        self.vnesiIncidentPB.clicked.connect(self.vnesiIncident)
        self.update()
        self.izracun()

    def update(self):
        print("update")
        db.update()
        self.incidentiLW.clear()
        for inc in db.incidenti:
            self.incidentiLW.addItem(f"Datum: '{inc.datum}', Kategorija: {inc.kategorija}")
        self.izracun()

    def vnesiIncident(self):
        inc = Incident(
            datum=self.datumIncidentaDE.date().toPyDate(),
            kategorija=self.kategorijaIncidentaCB.currentText()
        )
        db.addIncident(inc)
        self.update()

    def izracun(self):
        emailIncidents = Incident.countByMonth(db.incidenti)
        endPointIncidents = Incident.countByMonth(db.incidenti)
        dateOfIncidents = [ele.datum for ele in db.incidenti]

        teps = func.TEPS(
            Resultmeasure=(config.tepsMaxMesaure - Incident.averageByMonth(db.incidenti))/(config.tepsMaxMesaure - config.tepsMinMesaure),
            Wmeasure=config.tepsWmesaure,
            C = config.tepsC,

        )
        tnpps = func.TNPPS(
            Resultmeasure=[
                func.TEPS_OLMCMW(emailIncidents),
                func.TEPS_OLMCMD_SD(endPointIncidents),
            ],
            Wmeasure=config.tnppsWmesaure,
            C=config.tnppsC,
        )
        oimtbi = func.OIMTBI(
            I=dateOfIncidents
        )

        sps = func.SPS(
            Tmeasure=config.spsTmesaure,
            Wmesaure =config.spsWmeasure,
            ResultMTBI=oimtbi,
        )
        thss = func.THSS(
            Resultmeasure=(config.thssMaxMesaure - Incident.averageByMonth(db.incidenti) )/(config.thssMaxMesaure - config.thssMinMesaure),
            Wmeasure = config.thssWmeasure,
            C = config.thssC
        )

        self.tnppsL.setText(f"TNPPS: {round(tnpps, 1)}")
        self.spsL.setText(f"SPS: {round(sps, 1)}")
        self.oimtbiL.setText(f"OIMTBI: {round(oimtbi,1)}")
        self.tepsL.setText(f"TEPS: {round(teps, 1)}")
        self.thssL.setText(f"THSS: {round(thss, 1)}")

def start(argv):
    app = QtWidgets.QApplication(argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()