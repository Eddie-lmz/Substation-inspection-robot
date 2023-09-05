# Substation-inspection-robot
Hello, this is a substation robot project that I (Eddie) completed independently when I was at the Intelligent Systems Research Institute of Wuhan University of Science and Technology. I produced a soft article, which mainly used YOLOV7 and GUI design and some visual algorithms.
！！！The purpose of this project is to control the movement of the four-axis steering wheel substation inspection robot and automatically identify the dial through the host computer software.

After downloading the project, run Main.py directly to open the software.
You can get
![登录](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/5fe100c4-5d2a-4636-8ab0-982c04f26e90)
After logging in, you can get
![主界面](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/adb6027c-4265-4967-972b-c5dce00d522e)
Afterwards you can interact with the controls of the interface to implement the functionality
The following is a schematic diagram of the function operation of each part
![连接网络2](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/022e1e73-794e-4faa-a714-a50fd0e34406)    
![云台运动执行](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/226d67ad-29e7-42af-a723-fa27fd8081e6)
![地盘控制执行](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/caffcd3a-cdcb-4487-935a-47656d384f99)
![放大](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/9f363e4f-a0e0-4440-a8b2-d1604d40e469)  ![放大2](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/09db5394-66ab-4d8a-a68b-334b18ffa9b7)
![表二2](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/fb32547b-8ef8-41ce-9125-c090fa1995cc)    ![表一结果](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/a3354521-565f-40f3-a4c8-171b23ea2255)


The following is the flow chart of the software
![ruan1](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/b762cd6e-3065-4093-ba4e-b3d176abaa64)
![ruan2](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/c6fc28f4-6f2d-4525-a898-5c058ffc5d2a)

具体使用方法：
一、 机器人端：
     使 用 者 在 使 用 本 系 统 前 ， 需 将 单 片 机 程 序 烧 录 进 机 器 人 车 身 的 STM32F407VET6 控制板中，单片机接线按照杜邦线上的标签接。
     使用前需要将机器人云台上的海康相机接上路由器；如果需要实现大范围巡检，需要可移动便携路由器。
二、 PC 端：
     硬件接好之后，使用者如需使用本系统的数据库功能，可按照以下步骤，不需要则可跳过。
     1. 安装 MySQL 8.0。
     2. 设置数据库登录信息，用户名默认、登入密码：123456、端口默认。
     3. 进入 MySQL 8.0 Command Line Client 数据库命令窗口，创建名称为robot 的数据库。
     点击 变电站巡检机器人调试包_2023 中的 Main.exe – 快捷方式
     会弹出黑色窗口，运行稍等几秒，如遇没有黑窗反应，可按一下回车键。
     几秒后，会弹出系统登陆界面；登陆界面注意如下：
     账号：robot （也可更改但需要改代码）
     密码：123456Aa（这里的密码为连接海康相机，获取数据流权限密码，也可用于在 400 密码重置助手中查询设备状态）
     IP：192.168.31.70（这里的 ip 是指海康相机 ip，需要和机器人所存于同一网段下，实验室 1204 的局域网 ip 为 192.168.31.69。如需在其他局域网下巡检，需要在 400 密码重置助手中修改）
     端口：8266（esp8266 的连接端口号）
     数据库：robot（为创建的数据库名称）
     点击登陆后则进入系统主界面，可以参考变电站指针巡检自动读数机器人说 明书操作。

三、 注意事项：
本项主要针对使用过程中可能出现的问题。
![image](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/8fd051cd-2c2b-4078-847f-8178b5a7e1fb) 出现上图所示问题，点击允许访问。
由于本系统一次只能检测一个表盘，所以使用者需要再打开摄像头，等待巡检结果出现后，点击关闭摄像头按钮，再打开摄像头继续巡检。
如果使用场景发生变化或者使用者想要自定义一些摄像头连接、数据库、esp8266 参数，可在以下代码处更改。
![image](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/04b36a4c-11dd-4244-bd1e-05b60f4c3d2b)
![image](https://github.com/Eddie-lmz/Substation-inspection-robot/assets/144076931/ddd421a5-6660-4fd7-a6df-aff49929b484)

Finally
The substation inspection robot project started from July 1, 2022 to March 1, 2023. I am very grateful to my undergraduate supervisor for giving me such an opportunity to get in touch with scientific research projects, and to my brothers and sisters for their help.
