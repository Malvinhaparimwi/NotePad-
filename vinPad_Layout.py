#window definition, the structure of the window
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

#notepad_window class
class vinpad_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VinPad")
        self.setWindowIcon(QIcon("VinIcon.png"))

        #etting the minimum size of vinPad
        self.setMinimumSize(400, 400)