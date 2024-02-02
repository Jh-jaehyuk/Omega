import csv
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox, QMainWindow, QDesktopWidget

class SignUpForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('회원가입 양식')
        self.resize(300, 300)

        layout = QVBoxLayout()

        # 입력 필드 생성
        self.name = QLineEdit(self)
        self.name.setPlaceholderText('이름')
        layout.addWidget(self.name)

        self.userid = QLineEdit(self)
        self.userid.setPlaceholderText('아이디')
        layout.addWidget(self.userid)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText('비밀번호')
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)

        self.birthdate = QLineEdit(self)
        self.birthdate.setPlaceholderText('생년월일 (YYYY-MM-DD)')
        layout.addWidget(self.birthdate)

        self.school = QLineEdit(self)
        self.school.setPlaceholderText('학교')
        layout.addWidget(self.school)

        self.nickname = QLineEdit(self)
        self.nickname.setPlaceholderText('별명')
        layout.addWidget(self.nickname)

        # 회원가입 버튼
        self.button = QPushButton('회원가입', self)
        self.button.clicked.connect(self.sign_up)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def sign_up(self):
        # 입력 값 가져오기
        name = self.name.text()
        userid = self.userid.text()
        password = self.password.text()
        birthdate = self.birthdate.text()
        school = self.school.text()
        nickname = self.nickname.text()

        # 중복 검사 및 저장
        if self.check_duplicates(userid, nickname):
            QMessageBox.warning(self, '회원가입 실패', '아이디 또는 별명이 이미 사용 중입니다.')
        else:
            self.save_to_csv(name, userid, password, birthdate, school, nickname)
            QMessageBox.information(self, '회원가입 성공', '성공적으로 회원가입되었습니다.')

    def check_duplicates(self, userid, nickname):
        try:
            with open('users.csv', 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.reader(file)
                for row in reader:
                    if userid == row[1] or nickname == row[5]:  # 아이디와 별명 컬럼 확인
                        return True
        except FileNotFoundError:
            pass  # 파일이 없는 경우 중복 없음으로 처리
        return False

    def save_to_csv(self, name, userid, password, birthdate, school, nickname):
        file_exists = os.path.isfile('users.csv')
        with open('users.csv', 'a', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['이름', '아이디', '비밀번호', '생년월일', '학교', '별명'])  # 열 이름 쓰기
            writer.writerow([name, userid, password, birthdate, school, nickname])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('오메가 수학전문학원')
        self.resize(200, 150)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)

        self.openSignUpFormButton = QPushButton('회원가입', self.centralWidget)
        self.openSignUpFormButton.clicked.connect(self.openSignUpForm)
        layout.addWidget(self.openSignUpFormButton)

    def openSignUpForm(self):
        self.signUpForm = SignUpForm()
        self.signUpForm.show()


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
