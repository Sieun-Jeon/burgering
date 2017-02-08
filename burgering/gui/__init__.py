import sys

from PyQt5.QtCore import QRect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class BgrMainWindow(QMainWindow):
    def __init__(self):
        super(BgrMainWindow, self).__init__()

        self.set_layout()
        self.show()

    def set_layout(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Burgering')

        self.setCentralWidget(BgrSplitter())


class BgrSplitter(QSplitter):
    def __init__(self):
        super(BgrSplitter, self).__init__()

        self.setHandleWidth(4)

        patty_list = BgrPattyList()
        patty_list1 = BgrPattyList()

        self.addWidget(patty_list)
        self.addWidget(patty_list1)


class BgrPattyList(QWidget):
    def __init__(self):
        super(BgrPattyList, self).__init__()

        self.patty_list = []
        self.set_layout()

    def set_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(1)

        for p in self.patty_list:
            layout.addWidget(self.build_pattywidget(p))

        layout.setContentsMargins(0, 0, 0, 0)

        self.setStyleSheet("background-color:white;")
        self.setLayout(layout)

    def build_pattywidget(self, patty):
        p_widget = PattyWidget(patty.name, patty.color)

        return p_widget


class PattyWidget(QWidget):
    def __init__(self, name, color):
        super(PattyWidget, self).__init__()

        self.color = QColor(color)
        self.name = name

        self.set_layout()

    def set_layout(self):
        self.setFixedHeight(70)

    def paintEvent(self, e):
        painter = QPainter()

        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.color)

        patty_rect = QRect(2, 2, self.frameGeometry().width()-4, self.frameGeometry().height()-4)
        painter.drawRoundedRect(patty_rect, 20, 30)

        painter.drawText(patty_rect, Qt.AlignCenter, self.name)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = BgrMainWindow()

    sys.exit(app.exec_())
