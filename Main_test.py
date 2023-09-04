from PyQt5 import QtWidgets
import robot_interface
import tcp_part
import socket
import sys
import torch
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2,os,random
random.seed(0)
import torch
import numpy as np
from models.experimental import attempt_load
from utils.general import  non_max_suppression,scale_coords
from utils.datasets import  letterbox
from utils.plots import plot_one_box
from HaiKang import change_zoom,change_color
import threading
import time
from cluster import walk

class MainWindow(tcp_part.TCPLogic):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.client_socket_list = list()
        self.another = None
        self.link = False

        self.timer = QtCore.QTimer()

        # 打开软件时默认获取本机ip
        self.click_get_ip()
        # self.connect()
        self.connect()
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
        ip_camera_url = 'rtsp://admin:123456Aa@192.168.31.70/Streaming/Channels/2'
        self.cap = cv2.VideoCapture(ip_camera_url)
        change_color(brightness=80, contrast=50, saturation=50)
        print('IP摄像头是否开启： {}'.format(self.cap.isOpened()))
        self.timer.start(50)

    def video_buton_close(self):
        self.timer.stop()
        self.cap.release()

    def show_viedo(self):
        global focus
        global cluster
        global img_cluster
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
                        img_clock = self.img[int(xyxy[1]):int(xyxy[3]),int(xyxy[0]):int(xyxy[2])]
                        if (img_cluster):
                            cv2.imwrite("type1.jpg", img_clock)
                            img_cluster = False
                            focus = True
                        plot_one_box(xyxy, self.img, color=self.colors[int(cls)], line_thickness=1)
                        # if(img_cluster):
                        #     cv2.imwrite("type1.jpg",img_clock)
                        #     img_cluster = False
                        #     focus = True
                        # if(cluster):
                        #     cluster_clock,center = walk(self.img)
                        #     cv2.imwrite("clock.jpg",cluster_clock)
                        #     cluster = False
            threading.Thread(target=clock_show, daemon=True).start()
            QtImg = QtGui.QImage(self.img.data,
                                   self.img.shape[1],
                                   self.img.shape[0],
                                   self.img.shape[1] * 3,
                                   QtGui.QImage.Format_BGR888)
            jpg_out = QtGui.QPixmap(QtImg).scaled(
                  self.picture_output1.width(), self.picture_output1.height())
            self.picture_output1.setPixmap(jpg_out)


def clock_show():
    global focus
    if (focus):
        im0 = cv2.imread("type1.jpg")
        im0 = cv2.resize(im0,(400,400))
        canny,center = walk(im0)

        focus = False



if __name__ == '__main__':
    focus = False
    cluster = False
    img_cluster = True
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())