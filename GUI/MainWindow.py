import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from ToggleWidget import ToggleWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Rocket Ground Server Program")
        self.windowwidth=1366
        self.windowheight=1200

        # 메인 위젯 및 레이아웃
        #self.togglewidget = ToggleWidget(400,self.windowwidth,self.windowheight,self)


        self.centralwidget = QWidget();
        self.setCentralWidget(self.centralwidget);
        self.maingridlayout =   QGridLayout(self.centralwidget)
        self.maingridlayout.setHorizontalSpacing=10;
        self.maingridlayout.setVerticalSpacing=10;
        self.maingridlayout.setContentsMargins(10,10,10,10)
        self.maingridlayout.setRowMinimumHeight(0, 50)


        mLabel = QLabel('CommunicationStatus');
        mLabel.setMaximumHeight(50)
        self.maingridlayout.addWidget(mLabel, 0, 0)
        self.maingridlayout.addWidget(QLabel('RocketName'), 0, 1)
        self.maingridlayout.addWidget(QLabel('SensorStatus'), 0, 2)





        self.maingridlayout.addWidget(QLabel('CommunicationLabel'), 1, 0)
        self.maingridlayout.addWidget(QLabel('RocketPositionGraph'), 2, 0)
        self.maingridlayout.addWidget(QLabel('StatusExample1'), 3, 0)
        self.maingridlayout.addWidget(QLabel('SensorGraph1'), 1, 2)
        self.maingridlayout.addWidget(QLabel('SensorGraph2'), 2, 2)
        self.maingridlayout.addWidget(QLabel('SensorGraph3'), 3, 2)
        self.maingridlayout.addWidget(QLabel('RocketImage'), 1, 1,3,1)
        self.maingridlayout.addWidget(QLabel('ChecklistLabel'), 4, 0)
        self.maingridlayout.addWidget(QLabel('ForceButton'), 4, 1)
        self.maingridlayout.addWidget(QLabel('RocketStatusLabel'), 4, 2)

        self.setGeometry(0, 0, self.windowwidth, self.windowheight)



if __name__=="__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    app.exec()

