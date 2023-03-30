#Title  : VinTeck Customized Notepad    #
#Author : Haparimwi Malvin Munashe      #
#_______________________________________#

#using PyQt5 framework
from PyQt5.QtWidgets import QApplication
import sys

#using my defined "notepad_structure"
from vinPad_Layout import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    vinPad = vinpad_window()
    vinPad.show()