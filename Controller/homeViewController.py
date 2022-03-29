from PyQt5.QtWidgets import QMainWindow, QWidget
from numpy import double
import matplotlib.pyplot as plt
from Model.red import cargar_modelado

from View.Ui_home_view import Ui_MainWindow

class HomeViewController(QMainWindow):
    def __init__(self):
        super(HomeViewController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_listaUbicaciones
        self.ui.label_errorDepartamento.setVisible(False)
        self.fillLocations()
        self.ui.pushButton_consultarPrecio.clicked.connect(self.consultPrice)
        self.modelo, self.historial = cargar_modelado()
        self.ui.pushButton_mostrarGrafica.clicked.connect(lambda: self.generateGraphic(self.historial),)
        

    
    def fillLocations(self):
        listLocation = ['COMITÁN', 'TUXTLA GUTIÉRREZ', 'SAN CRISTÓBAL DE LAS CASAS']
        listProperties = ['CASA', 'DEPARTAMENTO']
        self.ui.comboBox_listaUbicaciones.addItems(listLocation)
        self.ui.comboBox_listaPropiedades.addItems(listProperties)

    def consultPrice(self):
        location = self.ui.comboBox_listaUbicaciones.currentText()
        propertyType = self.ui.comboBox_listaPropiedades.currentText()
        squareMeter = double(self.ui.doubleSpinBox_metrosCuadrados.text())
        rooms = int(self.ui.spinBox_numHabitaciones.text())
        bathrooms = int(self.ui.spinBox_numBanios.text())

        if(location == 'COMITÁN' and propertyType == 'DEPARTAMENTO'):
            self.ui.label_errorDepartamento.setVisible(True) 
        else:
            if(location == 'TUXTLA GUTIÉRREZ'):
                location = 0
            elif(location == 'SAN CRISTÓBAL DE LAS CASAS'):
                location = 1
            elif(location == 'COMITÁN'):
                location = 2
            
            if(propertyType == 'CASA'):
                propertyType = 0
            elif(propertyType == 'DEPARTAMENTO'):
                propertyType = 1

            print(f'location: {location}, propertyType: {propertyType}, rooms: {rooms} ,bathrooms: {bathrooms} ,squareMeter: {squareMeter}')
            
            valuePrediction = [[location, propertyType, squareMeter, rooms, bathrooms]]
            result = self.modelo.predict(valuePrediction)
            precio = f'${result[0][0]} MXN'

            self.ui.label_errorDepartamento.setVisible(False)
            self.ui.label_precio.setText(precio)   
                   

    def generateGraphic(self, historial):
        plt.plot(historial.history['val_loss'], label='val_loss')
        plt.plot(historial.history['loss'], label='loss')
        plt.xlabel('Número de iteraciones')
        plt.ylabel('Error')
        plt.legend()
        plt.show()
