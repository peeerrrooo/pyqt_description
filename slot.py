import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout,
                             QLabel, QPushButton)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._initUI()

    def _initUI(self):
        self.label = QLabel('Push the Button', self)
        self.button = QPushButton('Push', self)
        self.button.clicked.connect(self._handleClickButton)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
        self.show()

    def _handleClickButton(self):
        self.label.setText('Push Done.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    sys.exit(app.exec_())
