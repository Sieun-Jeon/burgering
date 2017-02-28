from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLineEdit, QSplitter, QVBoxLayout, QGridLayout
)

from burgering import Patty


class BgrSplitter(QSplitter):
    def __init__(self):
        super(BgrSplitter, self).__init__()

        self.setHandleWidth(4)

        self.left_panel = BgrLeftPanel()
        self.center_panel = BgrCenterPanel()
        self.right_panel = BgrRightPanel()

        self.addWidget(self.left_panel)
        self.addWidget(self.center_panel)
        self.addWidget(self.right_panel)


class BgrLeftPanel(QWidget):
    def __init__(self):
        super(BgrLeftPanel, self).__init__()

        self.set_layout()

    def set_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(BgrPattyList())
        layout.addWidget(BgrBurgerCrl())

        self.setLayout(layout)
        
        
class BgrCenterPanel(QWidget):
    def __init__(self):
        super(BgrCenterPanel, self).__init__()
      
        
class BgrRightPanel(QWidget):
    def __init__(self):
        super(BgrRightPanel, self).__init__()


class BgrPattyList(QWidget):
    def __init__(self):
        super(BgrPattyList, self).__init__()

        p = Patty()
        p.title = {'default': 'test'}
        p.type = 'm'

        self.patty_list = [p, p, p, p]
        self.set_layout()
        self.populate_patty()

    def set_layout(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(1)

        self.setMinimumWidth(150)
        self.setLayout(layout)

    def populate_patty(self):
        layout = self.layout()

        for p in self.patty_list:
            layout.addWidget(self.build_pattywidget(p))
            layout.setContentsMargins(0, 0, 0, 0)

    def build_pattywidget(self, patty):
        name = patty.title['default']
        color = {
            'm': '#115511'
        }.get(patty.type, '#101010')

        p_widget = PattyWidget(name, color)

        return p_widget


class BgrBurgerCrl(QWidget):
    def __init__(self):
        super(BgrBurgerCrl, self).__init__()

        self.set_layout()


    def set_layout(self):
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignTop)

        search = QLineEdit('검색')
        burn_button = QPushButton('패티 굽기')
        mart_button = QPushButton('패티 마트')

        layout.addWidget(search, 0, 0, 1, 2)
        layout.addWidget(burn_button, 1, 0)
        layout.addWidget(mart_button, 1, 1)

        self.setLayout(layout)


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