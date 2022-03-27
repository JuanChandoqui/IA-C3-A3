from PyQt5.QtWidgets import QMainWindow
from numpy import double
import matplotlib.pyplot as plt

from View.Ui_home_view import Ui_MainWindow

class HomeViewController(QMainWindow):
    def __init__(self):
        super(HomeViewController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_listaUbicaciones
        self.ui.pushButton_mostrarGrafica.setVisible(False)
        self.fillLocations()
        self.ui.pushButton_consultarPrecio.clicked.connect(self.consultPrice)
        self.ui.pushButton_mostrarGrafica.clicked.connect(self.showGraphic)

    
    def fillLocations(self):
        listLocation = ['Los manguitos', 'Patria nueva', 'El sabinito', 'La garza'] #TODO: implementar la lista de ubicaciones
        self.ui.comboBox_listaUbicaciones.addItems(listLocation)


    def consultPrice(self):
        trainLoss = [1,2,3,4,5,6,7,8] #TODO: LIST OF TRAIN LOSS
        location = self.ui.comboBox_listaUbicaciones.currentText()
        rooms = int(self.ui.spinBox_numHabitaciones.text())
        squareMeter = double(self.ui.doubleSpinBox_metrosCuadrados.text())
        print(f'location: {location}, rooms: {rooms}, squareMeter: {squareMeter}')

        precio = f'$1000000' #TODO: implementar el predict de la red neuronal

        self.ui.label_precio.setText(precio)
        self.ui.pushButton_mostrarGrafica.setVisible(True)
        self.generateGraphic(trainLoss)        


    def generateGraphic(self, listLoss):
        plt.plot(listLoss, label="LOSS")
        plt.legend()
        plt.xlabel("iteraciones")
        plt.ylabel("errores")

    def showGraphic(self):
        plt.show()
