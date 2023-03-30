#window definition, the structure of the window
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

#notepad_window class
class vinpad_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VinPad")
        self.setWindowIcon(QIcon("VinIcon.png"))

        #setting the minimum size of vinPad
        self.setMinimumSize(400, 400)

        #setting a menubar
        vinBar = self.menuBar()
        vinBar.addMenu(QIcon("files-icon.png"), "File")
        vinBar.addMenu(QIcon("task-edit-icon.png"), "Edit")
        vinBar.addMenu(QIcon("font-height-outline-icon.png"), "Format")
        vinBar.addMenu(QIcon("stack-icon.png"), "View")
        vinBar.addMenu(QIcon("book-question-icon.png"), "Help")
