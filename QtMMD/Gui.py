import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)
from .Settings import Settings


class Gui(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Math-Magik Designer')
        self.settings = Settings()
        size = self.settings.get_size()
        pos = self.settings.get_pos()
        self.move(pos)
        self.resize(size)
        self.show()

    def quit(self):
        self.settings.write_settings()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   g = Gui()
   app.aboutToQuit.connect(lambda: g.quit())
   sys.exit(app.exec_())
