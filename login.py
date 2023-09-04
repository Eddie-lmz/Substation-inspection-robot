# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(929, 733)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(420, 100, 441, 491))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(500, 130, 281, 51))
        self.frame.setStyleSheet("#frame{\n"
"    color: rgb(85, 0, 255);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 191, 28))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 M")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"    border:none;\n"
"}\n"
"#pushButton:focus{\n"
"    color: rgb(207, 207, 207);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(210, 0, 51, 41))
        self.label_3.setStyleSheet("image: url(:/image/roboticon1.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 100, 340, 490))
        self.label.setStyleSheet("border-image: url(:/image/WUST.jpg);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 110, 31, 31))
        self.pushButton_3.setStyleSheet("border:none;")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/logouticon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(430, 200, 411, 371))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:10px;")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 80, 301, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:10px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 140, 301, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:10px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 200, 301, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:10px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 260, 301, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:10px;")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 320, 171, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 M")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    background-color: rgb(149, 149, 149);\n"
"    color: rgb(255, 255, 255);\n"
"    border:3px solid rgb(149, 149, 149);\n"
"    border-radius:8px;\n"
"}\n"
"#pushButton_2:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(149, 149, 149);\n"
"}\n"
"#pushButton_2:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(220, 320, 51, 31))
        self.label_4.setStyleSheet("image: url(:/image/enterkeyicon.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 110, 31, 31))
        self.pushButton_4.setStyleSheet("border:none;")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("picture/iconshide.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(43, 33))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "变电站巡检机器人系统"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  账号："))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  密码："))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "  IP："))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "  端口："))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "  数据库："))
        self.pushButton_2.setText(_translate("Form", "登录"))
import resource_rc
