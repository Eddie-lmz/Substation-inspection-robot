# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 935)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.page2 = QtWidgets.QWidget(self.centralwidget)
        self.page2.setGeometry(QtCore.QRect(150, 60, 571, 741))
        self.page2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.page2.setObjectName("page2")
        self.label_37 = QtWidgets.QLabel(self.page2)
        self.label_37.setGeometry(QtCore.QRect(30, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page2)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 20, 51, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.page2)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(150, 20, 331, 31))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_5 = QtWidgets.QSlider(self.page2)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(150, 90, 331, 31))
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page2)
        self.lineEdit_6.setGeometry(QtCore.QRect(500, 90, 51, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_38 = QtWidgets.QLabel(self.page2)
        self.label_38.setGeometry(QtCore.QRect(20, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.horizontalSlider_6 = QtWidgets.QSlider(self.page2)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(150, 160, 331, 31))
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page2)
        self.lineEdit_7.setGeometry(QtCore.QRect(500, 160, 51, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_39 = QtWidgets.QLabel(self.page2)
        self.label_39.setGeometry(QtCore.QRect(20, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.line_9 = QtWidgets.QFrame(self.page2)
        self.line_9.setGeometry(QtCore.QRect(0, 220, 571, 16))
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_40 = QtWidgets.QLabel(self.page2)
        self.label_40.setGeometry(QtCore.QRect(70, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.page2)
        self.label_41.setGeometry(QtCore.QRect(370, 250, 141, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.green_right_2 = QtWidgets.QPushButton(self.page2)
        self.green_right_2.setGeometry(QtCore.QRect(210, 390, 61, 61))
        self.green_right_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/camerarighticon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.green_right_2.setIcon(icon)
        self.green_right_2.setIconSize(QtCore.QSize(70, 70))
        self.green_right_2.setFlat(True)
        self.green_right_2.setObjectName("green_right_2")
        self.green_buttom_2 = QtWidgets.QPushButton(self.page2)
        self.green_buttom_2.setGeometry(QtCore.QRect(120, 470, 61, 61))
        self.green_buttom_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("picture/camerabuttomicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.green_buttom_2.setIcon(icon1)
        self.green_buttom_2.setIconSize(QtCore.QSize(70, 70))
        self.green_buttom_2.setFlat(True)
        self.green_buttom_2.setObjectName("green_buttom_2")
        self.green_left_2 = QtWidgets.QPushButton(self.page2)
        self.green_left_2.setGeometry(QtCore.QRect(30, 390, 61, 61))
        self.green_left_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("picture/cameralefticon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.green_left_2.setIcon(icon2)
        self.green_left_2.setIconSize(QtCore.QSize(70, 70))
        self.green_left_2.setFlat(True)
        self.green_left_2.setObjectName("green_left_2")
        self.green_top_2 = QtWidgets.QPushButton(self.page2)
        self.green_top_2.setGeometry(QtCore.QRect(120, 300, 61, 61))
        self.green_top_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("picture/cameratopicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.green_top_2.setIcon(icon3)
        self.green_top_2.setIconSize(QtCore.QSize(70, 70))
        self.green_top_2.setFlat(True)
        self.green_top_2.setObjectName("green_top_2")
        self.yellow_top_2 = QtWidgets.QPushButton(self.page2)
        self.yellow_top_2.setGeometry(QtCore.QRect(410, 300, 71, 61))
        self.yellow_top_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.yellow_top_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("picture/robottopicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yellow_top_2.setIcon(icon4)
        self.yellow_top_2.setIconSize(QtCore.QSize(70, 70))
        self.yellow_top_2.setFlat(True)
        self.yellow_top_2.setObjectName("yellow_top_2")
        self.yellow_left_2 = QtWidgets.QPushButton(self.page2)
        self.yellow_left_2.setGeometry(QtCore.QRect(330, 380, 71, 71))
        self.yellow_left_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.yellow_left_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("picture/robotlefticon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yellow_left_2.setIcon(icon5)
        self.yellow_left_2.setIconSize(QtCore.QSize(80, 80))
        self.yellow_left_2.setFlat(True)
        self.yellow_left_2.setObjectName("yellow_left_2")
        self.yellow_buttom_2 = QtWidgets.QPushButton(self.page2)
        self.yellow_buttom_2.setGeometry(QtCore.QRect(410, 470, 71, 71))
        self.yellow_buttom_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.yellow_buttom_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("picture/robotbuttomicon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yellow_buttom_2.setIcon(icon6)
        self.yellow_buttom_2.setIconSize(QtCore.QSize(80, 80))
        self.yellow_buttom_2.setFlat(True)
        self.yellow_buttom_2.setObjectName("yellow_buttom_2")
        self.yellow_right_2 = QtWidgets.QPushButton(self.page2)
        self.yellow_right_2.setGeometry(QtCore.QRect(490, 380, 61, 71))
        self.yellow_right_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.yellow_right_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("picture/robotrighticon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yellow_right_2.setIcon(icon7)
        self.yellow_right_2.setIconSize(QtCore.QSize(80, 80))
        self.yellow_right_2.setFlat(True)
        self.yellow_right_2.setObjectName("yellow_right_2")
        self.line_10 = QtWidgets.QFrame(self.page2)
        self.line_10.setGeometry(QtCore.QRect(280, 230, 20, 341))
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.page2)
        self.line_11.setGeometry(QtCore.QRect(0, 560, 291, 16))
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.page2)
        self.line_12.setGeometry(QtCore.QRect(290, 560, 281, 16))
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.label_42 = QtWidgets.QLabel(self.page2)
        self.label_42.setGeometry(QtCore.QRect(200, 590, 171, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.plus_2 = QtWidgets.QPushButton(self.page2)
        self.plus_2.setGeometry(QtCore.QRect(120, 640, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.plus_2.setFont(font)
        self.plus_2.setObjectName("plus_2")
        self.minus_2 = QtWidgets.QPushButton(self.page2)
        self.minus_2.setGeometry(QtCore.QRect(330, 640, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.minus_2.setFont(font)
        self.minus_2.setObjectName("minus_2")
        self.label = QtWidgets.QLabel(self.page2)
        self.label.setGeometry(QtCore.QRect(-60, -50, 741, 341))
        self.label.setStyleSheet("border-image: url(:/image/picture/page2_seticon.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.page2)
        self.label_3.setGeometry(QtCore.QRect(51, 100, 61, 31))
        self.label_3.setStyleSheet("border-image: url(:/image/picture/distanceicon.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page2)
        self.label_4.setGeometry(QtCore.QRect(110, 380, 81, 81))
        self.label_4.setStyleSheet("border-image: url(:/image/picture/cameraicon.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page2)
        self.label_5.setGeometry(QtCore.QRect(340, 310, 211, 211))
        self.label_5.setStyleSheet("border-image: url(:/image/picture/robot_c.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.label.raise_()
        self.label_37.raise_()
        self.lineEdit_5.raise_()
        self.horizontalSlider_4.raise_()
        self.horizontalSlider_5.raise_()
        self.lineEdit_6.raise_()
        self.label_38.raise_()
        self.horizontalSlider_6.raise_()
        self.lineEdit_7.raise_()
        self.label_39.raise_()
        self.line_9.raise_()
        self.label_40.raise_()
        self.label_41.raise_()
        self.green_right_2.raise_()
        self.green_buttom_2.raise_()
        self.green_left_2.raise_()
        self.green_top_2.raise_()
        self.yellow_top_2.raise_()
        self.yellow_left_2.raise_()
        self.yellow_buttom_2.raise_()
        self.yellow_right_2.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.line_12.raise_()
        self.label_42.raise_()
        self.plus_2.raise_()
        self.minus_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 90, 41, 51))
        self.label_2.setStyleSheet("border-image: url(:/image/picture/angleicon.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_37.setText(_translate("MainWindow", "云台转动角度"))
        self.label_38.setText(_translate("MainWindow", "机器人运动距离"))
        self.label_39.setText(_translate("MainWindow", "机器人转动角度"))
        self.label_40.setText(_translate("MainWindow", "机器人云台控制"))
        self.label_41.setText(_translate("MainWindow", "机器人机体控制"))
        self.label_42.setText(_translate("MainWindow", "相机焦距和倍率调节"))
        self.plus_2.setText(_translate("MainWindow", "+"))
        self.minus_2.setText(_translate("MainWindow", "-"))
import resource_rc
