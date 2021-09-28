import sys
from PyQt5 import QtWidgets
from QtMMD.Gui import Gui

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

