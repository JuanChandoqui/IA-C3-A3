import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from Controller.homeViewController import HomeViewController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    homeApp = HomeViewController()
    homeApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')