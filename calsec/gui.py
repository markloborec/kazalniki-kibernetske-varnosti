from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDateEdit, QComboBox, QPushButton, QTableWidget, QLabel

from calsec import utils



class MainWindow(QtWidgets.QMainWindow):
    datumIncidentaDE : QDateEdit
    kategorijaIncidentaCB: QComboBox
    vnesiIncidentPB: QPushButton
    incidentiTW: QTableWidget
    tepsL: QLabel
    thssL: QLabel
    spsL: QLabel
    tnppsL: QLabel
    oimtbiL: QLabel





    def __init__(self):

        super(MainWindow, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi(utils.getPath(__file__, 'gui.ui'), self)  # Load the .ui file






def start(argv):
    app = QtWidgets.QApplication(argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()