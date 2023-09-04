import cv2
import os
import math
import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans
import time


def K_means(img):
    data = img.reshape((-1, 3))
    data = np.float32(data)

    # 定义终止条件 (type,max_iter,epsilon)
    criteria = (cv2.TERM_CRITERIA_EPS +
                cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # 设置初始中心的选择
    # flags = cv2.KMEANS_RANDOM_CENTERS
    flags = cv2.KMEANS_PP_CENTERS

    # K-Means聚类 聚集成4类
    compactness, labels, centers = cv2.kmeans(data, 2, None, criteria, 10, flags)

    # 图像转换回uint8二维类型
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    dst = res.reshape((img.shape))
    return dst


# 对K_means聚类分割后的图像进行值分割转成二值图像阈
def Thresh_and_blur(img):
    (_, thresh) = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)

    return thresh


def open_img(img):
    kernel = np.ones(shape=[4, 4], dtype=np.uint8)
    erode_appearance = cv2.morphologyEx(img, cv2.MORPH_CLOSE,  # 容纳腐蚀，膨胀等操作的函数
                                              kernel=kernel)
    return erode_appearance


def Gauss_img(img):
    Gauss_appearance = cv2.GaussianBlur(img,(5,5),1)         #高斯平滑处理(具体用法见文件)
    return  Gauss_appearance


def Canny(img):
    canny =cv2.Canny(img,50,200)    #边缘检测
    return canny



# 霍夫圆检测
def Hough_circle(img,original_img):
    circles = cv2.HoughCircles(
        img, cv2.HOUGH_GRADIENT, 1, 255, param1=50, param2=35, minRadius=10, maxRadius=500)

    font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体样式
    if circles is not None:  # 如果识别出圆
        for circle in circles[0]:
            #  获取圆的坐标与半径
            circle_x = int(circle[0])
            circle_y = int(circle[1])
            circle_r = int(circle[2])
            cv2.circle(original_img, (circle_x, circle_y), circle_r, (255, 255, 255), 3)  # 标记圆
            cv2.circle(original_img, (circle_x, circle_y), 3, (255, 255, 255), -1)  # 标记圆心
            text = 'x:  ' + str(circle_x) + ' y:  ' + str(circle_y)
            cv2.putText(original_img, text, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA, 0)  # 显示圆心位置
    return circle_x,circle_y



def walk(original_img):
        pic_k = K_means(original_img)
        thresh = Thresh_and_blur(pic_k)
        erode = open_img(thresh)
        gauss = Gauss_img(erode)
        canny = Canny(gauss)
        # cv2.waitKey(0)
        center_x,center_y = Hough_circle(canny,original_img)
        center = [center_x,center_y]
        return original_img,center




if __name__ == '__main__':
    # img = cv2.imread("./8.jpg")
    # n,m = img.shape[:2]
    # print(n,m)
    # print(img[n-1][m-1])
    img = cv2.imread("type2.jpg")
    img,center = walk(img)
    cv2.imshow("Hough",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

