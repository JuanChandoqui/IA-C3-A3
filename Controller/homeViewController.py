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
        self.ui.label_errorDepartamento.setVisible(False)
        self.fillLocations()
        self.ui.pushButton_consultarPrecio.clicked.connect(self.consultPrice)
        self.ui.pushButton_mostrarGrafica.clicked.connect(self.showGraphic)

    
    def fillLocations(self):
        listLocation = ['COMITAN', 'TUXTLA GUTIERREZ', 'SAN CRISTOBAL DE LAS CASAS']
        listProperties = ['CASA', 'DEPARTAMENTO']
        self.ui.comboBox_listaUbicaciones.addItems(listLocation)
        self.ui.comboBox_listaPropiedades.addItems(listProperties)

    def consultPrice(self):
        location = self.ui.comboBox_listaUbicaciones.currentText()
        propertyType = self.ui.comboBox_listaPropiedades.currentText()
        squareMeter = double(self.ui.doubleSpinBox_metrosCuadrados.text())
        rooms = int(self.ui.spinBox_numHabitaciones.text())
        bathrooms = int(self.ui.spinBox_numBanios.text())

        if(location == 'COMITAN' and propertyType == 'DEPARTAMENTO'):
            self.ui.label_errorDepartamento.setVisible(True)
            self.ui.pushButton_mostrarGrafica.setVisible(False)  
        else:
            if(location == 'TUXTLA GUTIERREZ'):
                location = 0
            elif(location == 'SAN CRISTOBAL DE LAS CASAS'):
                location = 1
            elif(location == 'COMITAN'):
                location = 2
            
            if(propertyType == 'CASA'):
                propertyType = 0
            elif(propertyType == 'DEPARTAMENTO'):
                propertyType = 1

            print(f'location: {location}, propertyType: {propertyType}, rooms: {rooms} ,bathrooms: {bathrooms} ,squareMeter: {squareMeter}')
            
            precio = f'$1000000' #TODO: implementar el predict de la red neuronal
            trainLoss = [1,2,3,4,5,6,7,8] #TODO: LIST OF TRAIN LOSS
            
            self.ui.label_errorDepartamento.setVisible(False)
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
