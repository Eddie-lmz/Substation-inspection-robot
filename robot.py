from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.Qt import *
import sys
import Main
class Ui_Form(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(400, 394)
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(130, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 M")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setLineWidth(1)
        self.label.setIndent(14)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Widget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 80, 241, 198))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(13)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setMaxLength(32775)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setIndent(1)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setIndent(2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 R")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(90, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 M")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(232, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 M")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(Widget.close)  # type: ignore
        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "学生信息管理系统"))
        self.label.setText(_translate("Widget", "登录信息系统"))
        self.label_2.setText(_translate("Widget", "账号："))
        self.label_3.setText(_translate("Widget", "密码："))
        self.label_4.setText(_translate("Widget", "主机："))
        self.label_5.setText(_translate("Widget", "端口号："))
        self.label_6.setText(_translate("Widget", "数据库："))
        self.pushButton.setText(_translate("Widget", "登录"))
        self.pushButton_2.setText(_translate("Widget", "退出"))

class Main(QDialog, Ui_Form):
    def __init__(self):
        super(Main, self).__init__()
        super().__init__()
        self.setFixedSize(490, 394)  # 禁止拖动
        self.setWindowIcon(
            QtGui.QIcon(r"C:\Users\86159\Desktop\my dear\0087fPGGgy1h5ue8uxji4j31o00xxtak.jpg"))  # 设置窗体标题图标
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # 禁用最大化

        # 背景图片
        image = QtGui.QPixmap()
        image.load(r"C:\Users\86159\Desktop\my dear\0087fPGGgy1h5ue8uxji4j31o00xxtak.jpg")
        bg = QtGui.QPalette()
        bg.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(bg)
        self.setAutoFillBackground(True)
        self.setupUi(self)
        self.setWindowTitle('成绩管理系统')
        self.pushButton.clicked.connect(self.login)
    def login(self):
        gl_db = self.lineEdit_5.text()
        gl_host = self.lineEdit_3.text()
        gl_pwd = self.lineEdit_2.text()
        gl_user = self.lineEdit.text()
        gl_port = self.lineEdit_4.text()
        if gl_user == 'root' and gl_pwd == '12345678':
            if gl_db == 'student' and gl_host == '127.0.0.1':
                self.close()
                self.index_ui = Main.MainWindow()
                self.index_ui.show()
            else:
                QMessageBox.critical(self, '警告', '数据库name或IP地址错误', QMessageBox.Yes)
        else:
            QMessageBox.critical(self, '警告', '密码或账号错误', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)  #
    # app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())