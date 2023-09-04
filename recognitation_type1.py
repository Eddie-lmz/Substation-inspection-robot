import cv2
import numpy as np
import os
import PIL.Image as image

def MedianFilter(img,k=3,padding=None):             #中值滤波函数
    imarray=img
    height = imarray.shape[0]
    width = imarray.shape[1]
    if not padding:
        edge = int((k - 1) / 2)
        if height - 1 - edge <= edge or width - 1 - edge <= edge:
            print("The parameter k is to large.")
            return None
        new_arr = np.zeros((height, width), dtype="uint8")
        for i in range(edge,height-edge):
            for j in range(edge,width-edge):
                new_arr[i, j] = np.median(imarray[i - edge:i + edge + 1, j - edge:j + edge + 1])# 调用np.median求取中值
    return new_arr

# def read_path(file_pathname):
#     #遍历该目录下的所有图片文件
#     imglist = []
#     for filename in os.listdir(file_pathname):
#         img = cv2.imread(file_pathname+'/'+filename)
#         imglist.append(img)
#     return imglist
#     return imglist

def break_template(template,n):
    templatelist = []
    for i in range(n):
        width = 160-((160-20)//n)*(i+1)
        height = 120-((120-20)//n)*(i+1)
        template2 = cv2.resize(template, (width, height))
        templatelist.append(template2)
    return templatelist


def angle_cal(x1,y1,x2,y2):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    if x2 - x1 == 0:
        print
        ("直线是竖直的")
        result = 90
    elif y2 - y1 == 0:
        print
        ("直线是水平的")
        result = 0
    else:
        if(x1 >x2 and y1<y2):     #说明在第一象限
            x = x1 - x2
            y = y2 - y1
            k = y / x
            result = (90 - np.arctan(k) * 57.29577) + 180

        elif(x1 <x2 and y1< y2):  #说明在第二象限
            x = x1 - x2
            y = y2 - y1
            k = -(y / x)
            result =  np.arctan(k) * 57.29577 + 90

        elif(x1 < x2 and y1 > y2): #说明在第三象限
            x = x1 - x2
            y = y2 - y1
            k = y / x
            result = 90 - (np.arctan(k) * 57.29577)

        else:#说明在第四象限
            x = x1 - x2
            y = y2 - y1
            k = -(y/x)
            result = (np.arctan(k) * 57.29577) + 270
            # 计算斜率
    return result



# if __name__ == '__main__':
def template_matching(img,path):
    # val_listfinal = []
    # loc_listfinal = []
    # height_width_list= []
    # img = cv2.imread("./88.jpg")
    img = cv2.resize(img, (640, 480))
    template1 = cv2.imread(path)
    # template_list = read_path("./number")

    # for template in template_list:
        # height, width = template.shape[:2]
        # print(height,width)
    val_list = []
    loc_list = []
    template_gray = cv2.cvtColor(template1,cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))  # 直方图均衡化
    template_gray = clahe.apply(template_gray)
    templatelist = break_template(template_gray, 10)
    # print(len(templatelist))
    for template_compare in templatelist:
        res = cv2.matchTemplate(img, template_compare, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # if(max_val <0.4):
        val_list.append(max_val)
        loc_list.append(max_loc)

    index_max_val = val_list.index(max(val_list))
    if(val_list[index_max_val]<0.90 and val_list[index_max_val]>0.54):
        # val_listfinal.append(val_list[index_max_val])
        # loc_listfinal.append(loc_list[index_max_val])
        if(path == "clock_1/number0.jpg"):
            number = 0
        else:
            number = 1.2
        temp = templatelist[index_max_val]
        height, width = temp.shape[:2]
        # height_width_list.append((width,height))
    # print(height_width_list)
    # print(val_listfinal)
    # index_max_val = val_listfinal.index(max(val_listfinal))
    # print(index_max_val)
    # print(index_max_val)
        top_left = loc_list[index_max_val]
        # height_width = height_width_list[index_max_val]
    # print(top_left)
    #     bottom_right = (top_left[0] + width, top_left[1] + height)
    # print(bottom_right)
    #     cv2.rectangle(img, top_left, bottom_right, 255, 2)
    # # cv2.imwrite("picture.jpg",img)
    #     cv2.imshow("img1", templatelist[index_max_val])
    #     cv2.imshow("img2", img)

    rectangle_center = [top_left[0] + float(width)/2.0,top_left[1] + float(height)/2.0]
    return rectangle_center,number




def Pointer_recognition(img,center,orign_img):
    appearance = img
    path1 = "clock_1/number0.jpg"
    path2 = "clock_1/number2.jpg"
    appearance_gray = cv2.cvtColor(appearance, code=cv2.COLOR_BGR2GRAY)  # 对图像进行灰度处理
    # 110, 255
    clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))  # 直方图均衡化
    imggray = clahe.apply(appearance_gray)
    rtgle1_center, number1 = template_matching(imggray, path1)
    rtgle2_center, number2 = template_matching(imggray, path2)

    dst = cv2.bitwise_not(imggray)  # 图像取反

    # after_img = MedianFilter(dst)        #中值滤波
    # cv2.imshow('lvbo', after_img)

    after_img = cv2.GaussianBlur(dst,(15,15),1)

    kernel = np.ones((2, 2), np.uint8)
    erosion = cv2.erode(after_img, kernel, iterations=1)

    kernel = np.ones(shape=[3, 3], dtype=np.uint8)
    open_appearance = cv2.morphologyEx(erosion, cv2.MORPH_OPEN,  # 容纳腐蚀，膨胀等操作的函数
                                        kernel=kernel)

    ret,dst = cv2.threshold(open_appearance,130,255,cv2.THRESH_BINARY)      #二值化阈值分割(具体用法见文件)

    img_thinning = cv2.ximgproc.thinning(dst, thinningType=cv2.ximgproc.THINNING_ZHANGSUEN)         #细化操作

    img_dilate = cv2.dilate( img_thinning, kernel, iterations = 1)

    minLineLength = 10
    maxLineGap = 200
    lines = cv2.HoughLines( img_dilate, 1, np.pi / 180, 60,maxLineGap,minLineLength)
    for line in lines[0]:
        rho = line[0]  # 第一个元素是距离rho
        theta = line[1]  # 第二个元素是角度theta
        print('distance:' + str(rho), 'theta:' + str(((theta / np.pi) * 180)))
        if (theta > 3 * (np.pi / 3)) or (theta < (np.pi / 2)):  # 从图像边界画出延长直线
            # 该直线与第一行的交点
            pt1 = (int(rho / np.cos(theta)), 0)
            # 该直线与最后一行的焦点
            pt2 = (int((rho - orign_img.shape[0] * np.sin(theta)) / np.cos(theta)), orign_img.shape[0])
            # 绘制一条白线
            cv2.line(orign_img, pt1, pt2, 255, 1)
            # print('theat >180 theta<90')

        else:  # 水平直线
            # 该直线与第一列的交点
            pt1 = (0, int(rho / np.sin(theta)))
            # 该直线与最后一列的交点
            pt2 = (orign_img.shape[1], int((rho - orign_img.shape[1] * np.cos(theta)) / np.sin(theta)))
            # 绘制一条直线
            cv2.line(orign_img, pt1, pt2, 255, 1)

    angle_rtgle1 = angle_cal(rtgle1_center[0], rtgle1_center[1], center[0], center[1])
    angle_rtgle2 = angle_cal(rtgle2_center[0], rtgle2_center[1], center[0], center[1])

    if (number1 == 0 and number2 == 1.2):
        precision = (number2-number1) / (angle_rtgle2 - angle_rtgle1)
        if (precision < 0):
            precision = -precision
        print("精度为{}".format(precision))
        angle = theta - angle_rtgle1
        if (angle >= 0):
            dushu = angle * precision
        else:
            dushu = -(angle * precision)
        print("表的示数为:", str(dushu))
    # else:
    #     precision = 1.0 / (angle_rtgle2 - angle_rtgle1)
    #     if (precision < 0):
    #         precision = -precision
    #     angle = theta - angle_rtgle1
    #     if (angle >= 0):
    #         dushu = angle * precision
    #     else:
    #         dushu = (360 + angle) * precision
    #     if (number1 == 1):
    #         dushu = dushu + 1
    #     else:
    #         dushu = dushu + 2
    #     print("表的示数为:", str(dushu))



    return  orign_img,dushu



if __name__ == '__main__':
    img = cv2.imread("clock_2/type1.jpg")
    Pointer_recognition(img, [321,247])