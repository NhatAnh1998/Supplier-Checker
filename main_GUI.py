import sys
from PySide6.QtWidgets import QApplication
from main_controller import Controlller

class MainWindow(QApplication):

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.controller = Controlller()
        self.controller.show()


if __name__ == '__main__':

    app = MainWindow(sys.argv)
    sys.exit(app.exec())

