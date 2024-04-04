from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QRect

class ToggleWidget(QWidget):
    def __init__(self,windowheight,parentwidth,parentheight,parent=None):
        super().__init__(parent)
        self.parentheight =parentheight
        self.parentwidth=parentwidth
        self.windowheight=windowheight

        # 애니메이션을 적용할 위젯
        self.animated_widget = QWidget(self)
        self.animated_widget.setGeometry(0, self.parentheight, self.parentwidth, self.windowheight)  # 초기 위치 설정
        self.animated_widget.setStyleSheet("background-color: lightgreen;")
        

        # 애니메이션 트리거 버튼
        self.toggle_button = QPushButton("^", self)
        self.toggle_button.clicked.connect(self.toggle_animation)

        self.main_layout = QVBoxLayout(self)
        #self.main_layout.setGeometry(QRect(0, self.parentheight, self.parentwidth, self.windowheight))

        # 레이아웃에 위젯 추가
        self.main_layout.addWidget(self.animated_widget)
        self.main_layout.addWidget(self.toggle_button)

        self.animation = QPropertyAnimation(self.animated_widget, b"geometry")
        self.animation.setDuration(200)  # 200ms 동안 애니메이션 실행

        self.toggle_animation()

    def toggle_animation(self):
        current_geometry = self.animated_widget.geometry()

        # 위젯이 숨겨져 있으면 나타나게, 나타나 있으면 숨기게 애니메이션 설정
        if current_geometry.y() == self.parentheight-self.windowheight:  # 위젯이 숨겨져 있는 경우
            self.animation.setStartValue(QRect(0, self.parentheight-self.windowheight, self.parentwidth, self.windowheight))
            self.animation.setEndValue(QRect(0, self.parentheight, self.parentwidth, self.windowheight))
        else:  # 위젯이 보여지는 경우
            self.animation.setStartValue(QRect(0, self.parentheight, self.parentwidth, self.windowheight))
            self.animation.setEndValue(QRect(0, self.parentheight-self.windowheight, self.parentwidth, self.windowheight))
        self.animation.start()

