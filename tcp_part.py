import robot_interface
from PyQt5 import QtWidgets
import socket
import threading
import sys
import math
import stopThreading
class TCPLogic(robot_interface.MAIN_W):
    def __init__(self):
        super(TCPLogic, self).__init__()
        self.tcp_socket = None
        self.client_th = None
        self.client_socket_list = list()

        self.link = False  # 用于标记是否开启了连接

    def tcp_server_start(self):
        """
        功能函数，TCP服务端开启的方法
        :return: None
        """
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 取消主动断开连接四次握手后的TIME_WAIT状态
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 设定套接字为非阻塞式
        self.tcp_socket.setblocking(False)
        try:
            port = int(self.portdit.text())
            self.tcp_socket.bind(('', port))
        except Exception as ret:
            msg = '请检查端口号\n'
            self.signal_write_msg.emit(msg)
        else:
            self.tcp_socket.listen()
            self.sever_th = threading.Thread(target=self.tcp_server_concurrency)
            self.sever_th.start()
            msg = 'TCP服务端正在监听端口:%s\n' % str(port)
            self.signal_write_msg.emit(msg)

    def tcp_server_concurrency(self):
        """
        功能函数，供创建线程的方法；
        使用子线程用于监听并创建连接，使主线程可以继续运行，以免无响应
        使用非阻塞式并发用于接收客户端消息，减少系统资源浪费，使软件轻量化
        :return:None
        """
        while True:
            try:
                client_socket, client_address = self.tcp_socket.accept()
            except Exception as ret:
                pass
            else:
                client_socket.setblocking(False)
                # 将创建的客户端套接字存入列表,client_address为ip和端口的元组
                self.client_socket_list.append((client_socket, client_address))
                msg = 'TCP服务端已连接IP:%s端口:%s\n' % client_address
                self.signal_write_msg.emit(msg)
            # 轮询客户端套接字列表，接收数据
            for client, address in self.client_socket_list:
                try:
                    recv_msg = client.recv(1024)
                except Exception as ret:
                    pass
                else:
                    if recv_msg:
                        msg = recv_msg.decode('utf-8')
                        msg = '来自IP:{}端口:{}:\n{}\n'.format(address[0], address[1], msg)
                        self.signal_write_msg.emit(msg)
                    else:
                        client.close()
                        self.client_socket_list.remove((client, address))


    def tcp_client_start(self):
        """
        功能函数，TCP客户端连接其他服务端的方法
        :return:
        """
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            address = (str(self.IPEdit.text()), int(self.portdit.text()))
            # ip = "192.168.4.2"
            # address = (str(ip),int(8080))
        except Exception as ret:
            msg = '请检查目标IP，目标端口\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                msg = '正在连接目标服务器\n'
                self.signal_write_msg.emit(msg)
                self.tcp_socket.connect(address)
            except Exception as ret:
                msg = '无法连接目标服务器\n'
                self.signal_write_msg.emit(msg)
            else:
                self.client_th = threading.Thread(target=self.tcp_client_concurrency, args=(address,))
                self.client_th.start()
                msg = 'TCP客户端已连接IP:%s端口:%s\n' % address
                self.signal_write_msg.emit(msg)

    def tcp_client_concurrency(self, address):
        """
        功能函数，用于TCP客户端创建子线程的方法，阻塞式接收
        :return:
        """
        while True:
            recv_msg = self.tcp_socket.recv(1024)
            if recv_msg:
                msg = recv_msg.decode('utf-8')
                msg = '来自IP:{}端口:{}:\n{}\n'.format(address[0], address[1], msg)
                self.signal_write_msg.emit(msg)
            else:
                self.tcp_socket.close()
                # self.reset()
                msg = '从服务器断开连接\n'
                self.signal_write_msg.emit(msg)
                break

    def tcp_Clinet_send(self):
        """
        功能函数，用于TCP服务端和TCP客户端发送消息
        :return: None
        """
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (int(self.cpsend_data_2.toPlainText())).encode('utf-8')
                self.tcp_socket.send(send_msg)
                msg = 'TCP客户端已发送\n'
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)

    def tcp_Server_send(self):
        """
        功能函数，用于TCP服务端和TCP客户端发送消息
        :return: None
        """
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str(self.cpsend_data_2.toPlainText())).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
                msg = 'TCP服务端已发送\n'
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)

    def tcp_searchclock_send(self):
        text = self.sender().text()
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                if (text == "仪表搜索"):
                    send_msg = (str("a")).encode('utf-8')
                elif(text == "结束搜索"):
                    send_msg = (str("b")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
                msg = 'TCP服务端已发送\n'
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)


##--------------------------------------------摄像机云台控制部分--------------------------------------------------------------------------##
    def camera_topmove_Press(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("c")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
                msg = '云台控制已执行\n'
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)
    def camera_topmove_Relase(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("b")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)

    def camera_bottommove_Press(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("d")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
                msg = '云台控制已执行\n'
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)
    def camera_bottommove_Relase(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("b")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)

########----------------------------------------底盘运动控制部分-------------------------------------------------------------------------######
    def wheel_forwardmove_Press(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("e")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
                msg = '底盘控制已执行\n'
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)
    def wheel_forwardmove_Relase(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("b")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)

    def wheel_backmove_Press(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("f")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
                msg = '底盘控制已执行\n'
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)
    def wheel_backmove_Relase(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("b")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)

    def wheel_leftmove_Press(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("g")).encode('utf-8')
                for client, address in self.client_socket_list:
                    client.send(send_msg)
                msg = '底盘控制已执行\n'
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)
    def wheel_leftmove_Relase(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("b")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)

    def wheel_rightmove_Press(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("h")).encode('utf-8')
                for client, address in self.client_socket_list:
                    client.send(send_msg)
                msg = '底盘控制已执行\n'
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)
    def wheel_rightmove_Relase(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("b")).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(send_msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)

    def wheel_leftmove_Press_camera(self):
        try:
            send_msg = (str("g")).encode('utf-8')
            for client, address in self.client_socket_list:
                client.send(send_msg)
        except Exception as ret:
            msg = '发送失败\n'
            self.signal_write_msg.emit(msg)

    def wheel_rightmove_Press_camera(self):
            try:
                send_msg = (str("h")).encode('utf-8')
                for client, address in self.client_socket_list:
                    client.send(send_msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)
########-------------------------------------------------------------------------------------------------------------------------------######
#########-------------------------------------------云台自定义转角度----------------------------------------------------------------------######
    def camera_valuechange(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                if(self.horizontalSlider_4.value() % 10 == 0):
                    send_msg = (str(math.floor(self.horizontalSlider_4.value()/10))).encode('utf-8')
                # if self.comboBox_tcp.currentIndex() == 0:
                    # 向所有连接的客户端发送消息
                    for client, address in self.client_socket_list:
                        client.send(send_msg)
                    msg = '转动{}度\n'.format(self.horizontalSlider_4.value())
                    self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)

    def speed_valuechange(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                if(self.horizontalSlider_6.value() % 100 == 0):
                    print(self.horizontalSlider_6.value())
                    if(self.horizontalSlider_6.value() == 100):
                        send_msg = (str("A")).encode('utf-8')
                    elif(self.horizontalSlider_6.value() == 300):
                        send_msg = (str("B")).encode('utf-8')
                    elif (self.horizontalSlider_6.value() == 500):
                        send_msg = (str("C")).encode('utf-8')
                    elif (self.horizontalSlider_6.value() == 700):
                        send_msg = (str("D")).encode('utf-8')
                    elif (self.horizontalSlider_6.value() == 900):
                        send_msg = (str("E")).encode('utf-8')
                    # elif (self.horizontalSlider_6.value() == 1200):
                    #     send_msg = (str("F")).encode('utf-8')
                    for client, address in self.client_socket_list:
                        client.send(send_msg)
                    msg = '转动速度:{}\n'.format(self.horizontalSlider_6.value())
                    self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)

    def huizheng(self):
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.signal_write_msg.emit(msg)
        else:
            try:
                send_msg = (str("i")).encode('utf-8')
                for client, address in self.client_socket_list:
                    client.send(send_msg)
                msg = '机器人重校准\n'
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)


    def tcp_Client_close(self):
        """
        功能函数，关闭网络连接的方法
        :return:
        """
        try:
            self.tcp_socket.close()
            if self.link is True:
                msg = '已断开网络\n'
                self.signal_write_msg.emit(msg)
        except Exception as ret:
            pass
        try:
            stopThreading.stop_thread(self.client_th)
        except Exception:
            pass

    def tcp_Server_close(self):
        """
                功能函数，关闭网络连接的方法
                :return:
                """
        try:
            for client, address in self.client_socket_list:
                client.close()
            self.tcp_socket.close()
            if self.link is True:
                msg = '已断开网络\n'
                self.signal_write_msg.emit(msg)
        except Exception as ret:
            pass
        try:
            stopThreading.stop_thread(self.sever_th)
        except Exception:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = TCPLogic()
    ui.show()
    sys.exit(app.exec_())
