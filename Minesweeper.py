from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys


class Minesweeper(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('hui.ui', self)
        self.setWindowTitle('Minesweeper')

        self.start_btn.clicked.connect(self.enable_all)

        [btn.clicked.connect(self.run) for btn in self.btn_gr.buttons()]

    #add dialog window
    def enable_all(self):
        for btn in self.btn_gr:
            btn.enable()


app = QApplication(sys.argv)
ex = Minesweeper()
ex.show()
sys.exit(app.exec_())
