import csv
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox, QMainWindow, QDialog
from collections import defaultdict

import menu
from menu import MainWindow as MW


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("로그인 화면")
        self.resize(300, 300)

        layout = QVBoxLayout()

        # 입력 필드 생성
        self.userid = QLineEdit(self)
        self.userid.setPlaceholderText('아이디')
        layout.addWidget(self.userid)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText('비밀번호')
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)

        # 로그인 버튼
        self.button = QPushButton('로그인', self)
        self.button.clicked.connect(self.login)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def loadDatabase(self):
        self.data = defaultdict(str)
        if not os.path.exists('./users.csv'):
            open('users.csv', 'w')
            return self.data

        f = open('users.csv', 'r')

        while True:
            tmp = f.readline().split(',')
            if tmp[0] == '':
                break

            id, pw = tmp[1], tmp[2]
            if id == '아이디':
                continue

            self.data[id] = pw

        return self.data

    def login(self):
        userid = self.userid.text()
        password = self.password.text()
        data = self.loadDatabase()
        flag = False

        if not userid or not password:
            if not userid:
                QMessageBox.warning(self, "로그인 실패", "아이디를 입력하세요.")

            else:
                QMessageBox.warning(self, "로그인 실패", "비밀번호를 입력하세요.")

        elif data[userid] == password:
            flag = True
            QMessageBox.information(self, "로그인 성공", "로그인 되었습니다!")

        elif data[userid] == '':
            QMessageBox.warning(self, "로그인 실패", "존재하지 않는 아이디입니다.")

        elif data[userid] != password:
            QMessageBox.warning(self, "로그인 실패", "잘못된 비밀번호입니다")

        else:
            QMessageBox.warning(self, "로그인 실패", "ERRORRRRR!!!")

        if flag:
            self.close()
            self.second = menu.MainWindow()
            self.second.show()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("오메가 수학전문학원")
        self.resize(200, 150)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)

        self.openLoginFormButton = QPushButton("로그인", self.centralWidget)
        self.openLoginFormButton.clicked.connect(self.openLoginForm)
        layout.addWidget(self.openLoginFormButton)


    def openLoginForm(self):
        self.loginForm = LoginForm()
        self.loginForm.show()


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
