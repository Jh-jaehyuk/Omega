import os
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox, \
    QMainWindow, QDialog
from collections import defaultdict
from seat import *


class SeatForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("좌석 선택")
        self.resize(300, 300)

        layout = QVBoxLayout()

        # 선택 메뉴 1 - 좌석 선택



        self.setLayout(layout)

    def seat(self):
        raise NotImplementedError("아직 구현되지 않음.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("메뉴 선택")
        self.resize(200, 150)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)

        self.openSeatFormButton = QPushButton('좌석 선택')
        self.openSeatFormButton.clicked.connect(self.openSeatForm)
        layout.addWidget(self.openSeatFormButton)


    def openSeatForm(self):
        self.seatForm = SeatSelector()
        self.seatForm.show()


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
