from signup import *
from login import *
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('오메가 수학전문학원')
        self.resize(200, 150)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)

        self.img = QPixmap('./main_logo.PNG')
        self.label = QLabel(self)
        self.label.setPixmap(self.img)
        self.label.setContentsMargins(10, 20, 10, 20)
        self.label.resize(self.img.width(), self.img.height())
        layout.addWidget(self.label)

        self.openLoginFormButton = QPushButton("로그인", self.centralWidget)
        self.openLoginFormButton.clicked.connect(self.openLoginForm)
        layout.addWidget(self.openLoginFormButton)

        self.openSignUpFormButton = QPushButton('회원가입', self.centralWidget)
        self.openSignUpFormButton.clicked.connect(self.openSignUpForm)
        layout.addWidget(self.openSignUpFormButton)


    def openSignUpForm(self):
        self.signUpForm = SignUpForm()
        self.signUpForm.show()


    def openLoginForm(self):
        self.loginForm = LoginForm()
        self.loginForm.show()


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()