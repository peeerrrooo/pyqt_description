import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout,
                             QLabel, QSlider)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._initUI()

    def _initUI(self):
        self.label = QLabel('Change Slider', self)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.valueChanged.connect(self._handleChangeSlider)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)

        self.setLayout(self.layout)
        self.show()

    def _handleChangeSlider(self, value):
        self.label.setText(str(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    sys.exit(app.exec_())
