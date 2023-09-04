from PyQt5 import QtCore, QtGui, QtWidgets
import robot_interface
import tcp_part
import socket
import sys
import torch
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2,os,random
random.seed(0)
import torch
import numpy as np
from models.experimental import attempt_load
from utils.general import  non_max_suppression,scale_coords
from utils.datasets import  letterbox
from utils.plots import plot_one_box
from HaiKang import change_zoom,change_hlc,change_color
import threading
import time
from cluster import walk
import recognitation_type1,recognitation_type2
import json
import pymysql

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(929, 733)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
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
        self.label_3.setStyleSheet("image: url(picture/roboticon1.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 100, 340, 490))
        self.label.setStyleSheet("border-image: url(picture/WUST.jpg);\n"
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
        self.pushButton_3.setShortcut('esc')
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
        self.pushButton_2.setShortcut('enter')
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(220, 320, 51, 31))
        self.label_4.setStyleSheet("image: url(picture/enterkeyicon.jpg);")
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

        self.pushButton_3.clicked.connect(Form.close)  # type: ignore
        self.pushButton_4.clicked.connect(Form.showMinimized)
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



class MainWindow(tcp_part.TCPLogic):
    def __init__(self):
        super(MainWindow, self).__init__()
        global gl_port
        self.client_socket_list = list()
        self.another = None
        self.link = False
        self.portdit.setText(str(gl_port))
        self.timer = QtCore.QTimer()

        # 打开软件时默认获取本机ip
        self.click_get_ip()
        # self.connect()
        self.connect()
        try:
            self.openDefaultData()
        except:
            pass
        self.names = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
                 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
                 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase',
                 'frisbee',
                 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
                 'surfboard',
                 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
                 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
                 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard',
                 'cell phone',
                 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
                 'teddy bear',
                 'hair drier', 'toothbrush']
        self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in self.names]
        self.model = attempt_load("yolov7.pt", map_location="cuda:0")
    def connect(self, ):
        """
        控件信号-槽的设置
        :param : QDialog类创建的对象
        :return: None
        """
        # 如需传递参数可以修改为connect(lambda: self.click(参数))
        super(MainWindow, self).connect()
        self.pushButton_9.clicked.connect(self.click_link)
        self.pushButton_10.clicked.connect(self.click_unlink)
        self.getipbutton.clicked.connect(self.click_get_ip)
        self.clearrev.clicked.connect(self.click_clear)
        self.sendbutton.clicked.connect(self.tcp_Server_send)
        self.pushButton_13.clicked.connect(self.tcp_searchclock_send)
        self.pushButton_14.clicked.connect(self.tcp_searchclock_send)
        self.pushButton_16.clicked.connect(self.inputFile)
        self.outputfile.clicked.connect(self.saveFile)
        self.green_top_2.pressed.connect(self.camera_topmove_Press)
        self.green_top_2.released.connect(self.camera_topmove_Relase)
        self.green_buttom_2.pressed.connect(self.camera_bottommove_Press)
        self.green_buttom_2.released.connect(self.camera_bottommove_Relase)
        self.yellow_top_2.pressed.connect(self.wheel_forwardmove_Press)
        self.yellow_top_2.released.connect(self.wheel_forwardmove_Relase)
        self.yellow_buttom_2.pressed.connect(self.wheel_backmove_Press)
        self.yellow_buttom_2.released.connect(self.wheel_backmove_Relase)
        self.yellow_left_2.pressed.connect(self.wheel_leftmove_Press)
        self.yellow_left_2.released.connect(self.wheel_leftmove_Relase)
        self.yellow_right_2.pressed.connect(self.wheel_rightmove_Press)
        self.yellow_right_2.released.connect(self.wheel_rightmove_Relase)
        self.horizontalSlider_4.valueChanged.connect(self.camera_valuechange)
        self.horizontalSlider_6.valueChanged.connect(self.speed_valuechange)
        self.green_left_2.clicked.connect(self.huizheng)
        # self.timer.timeout.connect(self.show_viedo)
        self.Buton_cameraopen.clicked.connect(self.video_buton_open)
        self.Buton_cameraclose.clicked.connect(self.video_buton_close)
        self.save_picture.clicked.connect(self.picture_cap)
        self.plus_2.clicked.connect(self.jiaoju_plus)
        self.minus_2.clicked.connect(self.jiaoju_minus)
        self.outputfile.clicked.connect(self.saveData)
        self.timer.timeout.connect(self.show_viedo)

    def click_link(self):
        self.tcp_server_start()
        self.link = True
        self.pushButton_10.setEnabled(True)
        self.pushButton_9.setEnabled(False)

    def click_unlink(self):
        """
        pushbutton_unlink控件点击触发的槽
        :return: None
        """
        # 关闭连接
        self.tcp_Server_close()
        self.link = False
        self.pushButton_10.setEnabled(False)
        self.pushButton_9.setEnabled(True)
        self.reset()

    def click_get_ip(self):
        """
        pushbutton_get_ip控件点击触发的槽
        :return: None
        """
        # 获取本机ip
        self.IPEdit.clear()
        my_addr = socket.gethostbyname(socket.gethostname())
        self.IPEdit.setText(str(my_addr))

    def click_clear(self):
        """
        pushbutton_clear控件点击触发的槽
        :return: None
        """
        # 清空接收区屏幕
        self.textBrowser_recv.clear()

    def reset(self):
        """
        功能函数，将按钮重置为初始状态
        :return:None
        """
        self.link = False
        self.client_socket_list = list()
        self.pushButton_10.setEnabled(False)
        self.pushButton_9.setEnabled(True)

    def send(self):
        """
        pushbutton_send控件点击触发的槽
        :return:
        """
        # 连接时根据用户选择的功能调用函数
        # self.tcp_send()

    def video_buton_open(self):
        global Type,gl_host,gl_port,gl_pwd,focus
        focus = True
        ip = str(gl_host)
        pwd = str(gl_pwd)
        # ip_camera_url = 'rtsp://admin:123456Aa@192.168.31.70/Streaming/Channels/2'
        ip_camera_url = 'rtsp://admin:'+ pwd + '@'+ ip +'/Streaming/Channels/2'
        self.cap = cv2.VideoCapture(ip_camera_url)
        print('IP摄像头是否开启： {}'.format(self.cap.isOpened()))
        change_hlc(enabled='True')
        change_color(brightness=60, contrast=50, saturation=100)
        Type = self.type.text()
        self.timer.start(50)

    def video_buton_close(self):
        self.timer.stop()
        self.cap.release()

    def show_viedo(self):
        global focus
        global cluster
        global img_cluster
        global Type,dushu,show_img,start_plot,search
        ret, self.img = self.cap.read()
        if ret:
            image, ratio, death = letterbox(self.img, auto=False)
            image = image.transpose((2, 0, 1))[::-1]
            image = np.expand_dims(image, 0)
            image = np.ascontiguousarray(image)

            im = torch.from_numpy(image).float()
            im /= 255.0

            im = im.cuda()
            with torch.no_grad():
                result = self.model(im)[0]
                result = non_max_suppression(result, 0.5, 0.65)[0]
                result[:, :4] = scale_coords(im.shape[2:], result[:, :4], self.img.shape)

                for *xyxy, conf, cls in result:
                    if self.names[int(cls)] == "clock":
                    # plot_one_box(xyxy, frame, label=label, color=colors[int(cls)], line_thickness=1)
                    #     self.img_clock = self.img[int(xyxy[1]):int(xyxy[3]),int(xyxy[0]):int(xyxy[2])]
                        img_cluster = self.img[int(xyxy[1]):int(xyxy[3]),int(xyxy[0]):int(xyxy[2])]
                        plot_one_box(xyxy, self.img, color=self.colors[int(cls)], line_thickness=1)
                        # if(search):
                        #     xc = (int(xyxy[0]) + int(xyxy[2])) / 2
                        #     yc = (int(xyxy[1]) + int(xyxy[3])) / 2
                        #     if (xc > 340):
                        #         self.wheel_leftmove_Press_camera()
                        #     else:
                        #         self.wheel_backmove_Relase()
                        #     if (xc < 300):
                        #         self.wheel_rightmove_Press_camera()
                        #     else:
                        #         self.wheel_backmove_Relase()

                        if(focus):
                            change_zoom(2,1)
                            focus = False
                            cluster = True
                        # if(cluster):
                        #     cluster_clock,center = walk(self.img)
                        #     cv2.imwrite("clock.jpg",cluster_clock)
                        #     cluster = False
            threading.Thread(target=clock_show, daemon=True).start()
            if(start_plot):
                QtImg = QtGui.QImage(show_img.data,
                                     show_img.shape[1],
                                     show_img.shape[0],
                                     show_img.shape[1] * 3,
                                     QtGui.QImage.Format_BGR888)
                jpg_out = QtGui.QPixmap(QtImg).scaled(
                    self.picture_output2.width(), self.picture_output2.height())
                self.picture_output2.setPixmap(jpg_out)
                self.dushu_line.setText(str(dushu))
                msg = '读数结果为{}\n'.format(dushu)
                self.signal_write_msg.emit(msg)
                self.insert_information(Type,dushu)
                start_plot = False
                search = False

            QtImg = QtGui.QImage(self.img.data,
                                   self.img.shape[1],
                                   self.img.shape[0],
                                   self.img.shape[1] * 3,
                                   QtGui.QImage.Format_BGR888)
            jpg_out = QtGui.QPixmap(QtImg).scaled(
                  self.picture_output1.width(), self.picture_output1.height())
            self.picture_output1.setPixmap(jpg_out)

    def picture_cap(self):
        global camera_flag
        if(camera_flag):
            fileName2, ok2 = QFileDialog.getSaveFileName(self.centralwidget, "图片保存", '', 'Image files (*.jpg *.gif *.png *.jpeg)')
            save_path = fileName2

            if save_path != '':
                screen = QApplication.primaryScreen()
                pix = screen.grabWindow(self.picture_output1.winId())
                pix.save(fileName2)
                msg = '已保存图片到:{}\n'.format(fileName2)
                self.signal_write_msg.emit(msg)
        else:
            msg = '请检查摄像头是否开启\n'
            self.signal_write_msg.emit(msg)


    def jiaoju_plus(self):
        global temp
        temp += 1
        if(temp == 5):
            temp = 1
        if(camera_flag):
            change_zoom(temp, 1)
            msg = '已经调节焦距\n'
            self.signal_write_msg.emit(msg)
        else:
            msg = '请检查摄像头是否开启\n'
            self.signal_write_msg.emit(msg)

    def jiaoju_minus(self):
        if (camera_flag):
            change_zoom(1, 1)
            msg = '已经调节焦距\n'
            self.signal_write_msg.emit(msg)
        else:
            msg = '请检查摄像头是否开启\n'
            self.signal_write_msg.emit(msg)

    def insert_information(self,type,dushu):
        try:
            typec = type
            dushuc = float(dushu)
            if dushuc == '':
                QMessageBox.critical(self, '警告', '类型和读数不能为空')
                exit()
            items = [[typec,dushuc]]
            self.freshTable(items)
        except:
            pass

    def freshTable(self,items):
         '''主界面table刷新模块'''
         for i in range(len(items)):
             item = items[i]
             row = self.tableWidget.rowCount()
             self.tableWidget.insertRow(row)
             for j in range(len(item)):
                 item = QTableWidgetItem(str(items[i][j]))
                 self.tableWidget.setItem(row, j, item)
         msg = '读数完成\n'
         self.signal_write_msg.emit(msg)

    def inputFile(self):
        '''导入信息'''
        try:
            directory1 = QFileDialog.getOpenFileName(None, "选择文件", '', 'json(*.json)')
            # self.signal_write_msg.emit(str(directory1))
            # print(directory1)  # 打印文件夹路径
            path = directory1[0]
            if path != '':
                with open(file=path, mode='r', encoding='utf8') as file:
                    items = json.load(file)['database']
                    self.tableWidget.setRowCount(0)
                    self.tableWidget.clearContents()
                    self.freshTable(items)
        except:
            QMessageBox.critical(self, '警告', '导入文件出错')

    def saveFile(self):
        '''导出信息'''
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", '', 'json(*.json)')
        save_path = fileName2
        if save_path != '':
            items = []
            for i in range(self.tableWidget.rowCount()):
                lis = []
                for g in range(self.tableWidget.columnCount()):  # 此处是7行
                    if self.tableWidget.item(i, g):
                        lis.append(self.tableWidget.item(i, g).text())
                items.append(lis)
            with open(file=save_path, mode='w+', encoding='utf8') as file:
                file.write(json.dumps({"database": items}))

    def saveData(self):
        '''保存默认文件信息'''
        items = []
        for i in range(self.tableWidget.rowCount()):
            lis = []
            for g in range(self.tableWidget.columnCount()):  # 此处是7行
                if self.tableWidget.item(i, g):
                    lis.append(self.tableWidget.item(i, g).text())
            items.append(lis)
            # print(lis)
        conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                               , user='root'  # 用户名
                               , passwd='123456'  # 密码
                               , port=3306  # 端口，默认为3306
                               , db='robot'  # 数据库名称
                               , charset='utf8'  # 字符编码
                               )
        cur = conn.cursor()  # 生成游标对象
        sql = "TRUNCATE robot"  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        for item in items:
            sql = "insert into robot(clock_type,data) values (%s,%s)"
            cur.execute(sql,item)
        conn.commit()
        msg = '保存完成\n'
        self.signal_write_msg.emit(msg)

    def openDefaultData(self):
        '''打开默认文件信息'''

        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        '获取数据库数据后对应格式'
        conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                               , user='root'  # 用户名
                               , passwd='123456'  # 密码
                               , port=3306  # 端口，默认为3306
                               , db='robot'  # 数据库名称
                               , charset='utf8'  # 字符编码
                               )
        cur = conn.cursor()  # 生成游标对象
        sql = "select * from robot"  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        items=cur.fetchall()
        msg = '初始化完成\n'
        self.signal_write_msg.emit(msg)
        # print(items)
        self.freshTable(items)

    def freshTable(self, items):
         '''主界面table刷新模块'''
         for i in range(len(items)):
             item = items[i]
             row = self.tableWidget.rowCount()
             self.tableWidget.insertRow(row)
             for j in range(len(item)):
                 item = QTableWidgetItem(str(items[i][j]))
                 self.tableWidget.setItem(row, j, item)



def clock_show():
     global cluster,img_cluster,Type,show_img,start_plot,dushu
     if (cluster):
         cluster = False
         time.sleep(8)
         cv2.imwrite("clock.jpg", img_cluster)
         try:
             im0_cluster, center = walk(img_cluster)
             if Type == "" or Type == "1":
                show_img, dushu = recognitation_type1.Pointer_recognition(img_cluster, center, im0_cluster)
                cv2.imwrite("clock_show1.jpg", show_img)
                start_plot = True
             if Type == "2":
                show_img, dushu = recognitation_type2.Pointer_recognition(img_cluster, center, im0_cluster)
                cv2.imwrite("clock_show1.jpg", show_img)
                start_plot = True
         except Exception as ret:
             if Type == "" or Type == "1":
                 im0 = cv2.imread("clock_1/type1.jpg")
                 im0_cluster, center = walk(im0)
                 show_img, dushu = recognitation_type1.Pointer_recognition(im0, center, im0_cluster)
                 cv2.imwrite("clock_show.jpg", show_img)
                 start_plot = True
             if Type == "2":
                 im0 = cv2.imread("clock_2/type2.jpg")
                 im0_cluster, center = walk(im0)
                 show_img, dushu = recognitation_type2.Pointer_recognition(im0, center, im0_cluster)
                 cv2.imwrite("clock_show.jpg", show_img)
                 start_plot = True

###------------------------------------------------------------------------------------
# def clock_show():
#     global cluster, img_cluster, Type, show_img, start_plot, dushu
#     if (cluster):
#         cluster = False
#         time.sleep(8)
#         cv2.imwrite("clock.jpg", img_cluster)
#         if Type == "" or Type == "1":
#             Type = "1"
#             im0 = cv2.imread("clock_1/type1.jpg")
#             im0_cluster, center = walk(im0)
#             show_img, dushu = recognitation_type1.Pointer_recognition(im0, center, im0_cluster)
#             cv2.imwrite("clock_show.jpg", show_img)
#             start_plot = True
#         if Type == "2":
#             im0 = cv2.imread("clock_2/type2.jpg")
#             im0_cluster, center = walk(im0)
#             show_img, dushu = recognitation_type2.Pointer_recognition(im0, center, im0_cluster)
#             cv2.imwrite("clock_show.jpg", show_img)
#             start_plot = True



class Main(QDialog, Ui_Form):
    def __init__(self):
        super(Main, self).__init__()
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('变电站巡检机器人系统')
        self.pushButton_2.clicked.connect(self.login)
    def login(self):
        global gl_host,gl_port,gl_pwd
        gl_db = self.lineEdit_5.text()
        gl_host = self.lineEdit_3.text()
        gl_pwd = self.lineEdit_2.text()
        gl_user = self.lineEdit.text()
        gl_port = self.lineEdit_4.text()
        if gl_user == 'robot' :
            if gl_db == 'robot' :
                self.close()
                self.index_ui = MainWindow()
                self.index_ui.show()
            else:
                QMessageBox.critical(self, '警告', '数据库name错误', QMessageBox.Yes)
        else:
            QMessageBox.critical(self, '警告', '密码或账号错误', QMessageBox.Yes)

if __name__ == '__main__':
#--------------------------------main----------------------------------------------------
    focus = True
    cluster = False
    img_cluster = False
    camera_flag = True
    Type = False
    dushu = False
    show_img = False
    start_plot = False
    search = True
    temp = 0
#--------------------------------login----------------------------------------------------
    gl_port = False
    gl_host = False
    gl_pwd = False
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())