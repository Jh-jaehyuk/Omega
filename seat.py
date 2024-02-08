import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox, QGridLayout, QWidget, QLabel
from PyQt5.QtCore import Qt


class SeatSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # super().__init__()을 통해 부모 클래스의 생성자를 호출하고, initUI 메서드를 호출하여 UI를 초기화

    def initUI(self):
        self.setWindowTitle('좌석 선택기')
        self.setGeometry(400, 400, 800, 600)

        # 그리드 레이아웃 설정
        self.gridLayout = QGridLayout()

        # 그리드 레이아웃의 간격 설정
        self.gridLayout.setSpacing(10)  # 모든 간격을 10으로 설정

        # "좌석배치도" 라벨 추가
        self.gridLayout.addWidget(QLabel('Title:'), 0, 0)

        self.titleLabel = QLabel('좌석배치도')
        self.titleLabel.setAlignment(Qt.AlignCenter)  # 문구를 가운데 정렬
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 4)  # 라벨을 그리드의 맨 위에 배치


        # 좌석 배치 구성
        seatPositions = [(1, 1), (1, 2), (1, 3),  # 위에 3개
                         (2, 0), (2, 1), (2, 2), (2, 3),  # 가운데 4개
                         (3, 1), (3, 2), (3, 3),
                         (4, 0), (4, 1), (4, 2), (4, 3)]  # 가장 아래에 3개


        self.seats = [QPushButton(f'좌석 {i+1}') for i in range(30)]

        for pos, seat in zip(seatPositions, self.seats):
            self.gridLayout.addWidget(seat, *pos)
            seat.clicked.connect(self.seatClicked)


        # 입력 필드 설정
        self.inputField = QLineEdit(self)
        self.inputField.setPlaceholderText('좌석 번호 입력')
        self.inputField.returnPressed.connect(self.highlightSeat)
        self.gridLayout.addWidget(self.inputField, 9, 0, 1, 4)  # 입력 필드를 그리드의 맨 아래에 배치

        # 위젯 설정 및 레이아웃 적용
        self.widget = QWidget()
        self.widget.setLayout(self.gridLayout)
        self.setCentralWidget(self.widget)

    def seatClicked(self):
        button = self.sender()
        QMessageBox.information(self, "좌석 선택", f"{button.text()}가 선택되었습니다.")

    def highlightSeat(self):
        seatNumber = int(self.inputField.text()) - 1
        if 0 <= seatNumber < len(self.seats):
            self.seats[seatNumber].setStyleSheet('QPushButton {background-color: yellow; color: black;}')
        else:
            QMessageBox.warning(self, "경고", "잘못된 좌석 번호입니다.")
        self.inputField.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SeatSelector()
    ex.show()
    sys.exit(app.exec_())