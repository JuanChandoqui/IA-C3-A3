from PyQt5.QtWidgets import QMainWindow

from View.Ui_home_view import Ui_MainWindow

class HomeViewController(QMainWindow):
    def __init__(self):
        super(HomeViewController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
