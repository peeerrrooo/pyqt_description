import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._initUI()

    def _initUI(self):
        self.label = QLabel('Hello', self)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
        self.setGeometry(0, 0, 100, 100)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    sys.exit(app.exec_())
