"""
# -*- coding:utf-8 -*-
@Project : SmartKartRider
@File : PosDetection.py
@Author : Johan
@Time : 10/27/2022 11:07 PM

"""
import math
import cv2
import imutils
import numpy as np

from Utils.CVTools import ShapeDetector
from Utils.Geometry import angle_of_vector
from KartriderKit.__init__ import ROOTPATH, RAW_DATA_PATH
from datetime import datetime
import glob

def PosEstimationOnSmallMap(img_path, region = (80, 110, 85, 115), target_size = (100, 100), OutPutPath = ROOTPATH + "/Data/Debug/SmallMap"):
    img = cv2.imread(img_path)
    img = cv2.resize(img[region[0]:region[1], region[2]:region[3]], target_size)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([80, 80, 120])  # BGR
    upper = np.array([120, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    # res = cv2.bitwise_and(img, img, mask=mask)
    # canny = cv2.Canny(mask, 50, 50)
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()
    if len(cnts) == 1:
        c = cnts[0]
        # 计算轮廓的中心，然后仅使用轮廓检测形状的名称
        M = cv2.moments(c)
        # cX = int((M["m10"] / M["m00"]))
        # cY = int((M["m01"] / M["m00"]))
        shape, train_points = sd.detect(c)
        train_points = train_points.reshape(len(train_points), -1)
        # 将轮廓(x, y)坐标乘以调整比例，然后在图像上绘制轮廓和形状的名称
        # cv2.drawContours(img, [c], -1, (0, 255, 0), 1)
        # cv2.putText(img, "0", (train_points[0, 0] - 3, train_points[0, 1]), cv2.FONT_HERSHEY_SIMPLEX,
        #             0.2, (255, 255, 255), 1)
        #
        # cv2.putText(img, "1", (train_points[1, 0] - 3, train_points[1, 1]), cv2.FONT_HERSHEY_SIMPLEX,
        #             0.2, (255, 255, 255), 1)
        #
        # cv2.putText(img, "2", (train_points[2, 0] - 3, train_points[2, 1]), cv2.FONT_HERSHEY_SIMPLEX,
        #             0.2, (255, 255, 255), 1)
        if len(train_points) == 3:
            k_left_vet_index, k_up_vet_index = np.argmin(train_points.reshape(len(train_points), -1), axis=0)
            k_right_vet_index = np.argmax(train_points.reshape(len(train_points), -1), axis=0)[0]
            k_left_vet = train_points[k_left_vet_index]
            k_right_vet = train_points[k_right_vet_index]
            k_up_vet = train_points[k_up_vet_index]
            k_mid_down_vet = (k_right_vet + k_left_vet) / 2
            k_dir_vet = k_up_vet - k_mid_down_vet
            up_norm = np.array([0, -1])
            print(shape)
            result = angle_of_vector(k_dir_vet, up_norm)
        else:
            print("No Triangle Detection! "+ img_path)
            cv2.imwrite(OutPutPath + "/" + str(datetime.now()).replace(" ","").replace(":","-") + ".png", img)
            result = 0.0
    else:
        print("No Triangle Detection! " + img_path)
        cv2.imwrite(OutPutPath + "/" + str(datetime.now()).replace(" ","").replace(":","-") + ".png", img)
        result = 0.0
    return result

if __name__ == "__main__":
    img_path_list = glob.glob(ROOTPATH+ '/raw_data/US/SmallMap/*.*', recursive=True)
    # print(img_path_list)
    for i in range(len(img_path_list)):
        print(img_path_list[i])
        # img = cv2.imread(img_path_list[i])
        print(PosEstimationOnSmallMap(img_path_list[i]))
