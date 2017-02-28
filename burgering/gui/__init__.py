import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from burgering.gui.widgets import BgrSplitter
from burgering import Patty


class BgrMainWindow(QMainWindow):
    def __init__(self):
        super(BgrMainWindow, self).__init__()

        self.set_layout()
        self.show()

    def set_layout(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(200, 200, 1024, 768)
        self.setWindowTitle('Burgering')

        self.bgr_splitter = BgrSplitter()
        self.setCentralWidget(self.bgr_splitter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BgrMainWindow()

    sys.exit(app.exec_())
