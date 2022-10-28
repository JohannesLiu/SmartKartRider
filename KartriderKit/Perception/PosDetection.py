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

from Utils.CVTools import cvDebugOut
from Vision.Detector import ShapeDetector
from Utils.Geometry import angle_between_vectors, direction_of_traingle
from KartriderKit.__init__ import ROOTPATH, RAW_DATA_PATH
import glob

from Vision.Filter import hsvFilter

class PosDetection:
    def __init__(self):
       self.up_norm = np.array([0, -1])
    def PosEstimationOnSmallMap(self, img_path, region = (80, 110, 85, 115), target_size = (100, 100), OutPutPath = ROOTPATH + "/Data/Debug/ArrowInSmallMap"):
        img = cv2.imread(img_path)
        img = cv2.resize(img[region[0]:region[1], region[2]:region[3]], target_size)
        lower = np.array([80, 80, 120])  # BGR
        upper = np.array([120, 255, 255])
        _, mask, _ = hsvFilter(img, lower, upper)
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        sd = ShapeDetector()
        if len(cnts) == 1:
            c = cnts[0]
            shape, train_points = sd.detect(c)
            train_points = train_points.reshape(len(train_points), -1)
            if len(train_points) == 3:
                k_dir_vet = direction_of_traingle(train_points)

                print(shape)
                result = angle_between_vectors(k_dir_vet, self.up_norm)
            else:
                print("No Triangle Detection! "+ img_path)
                cvDebugOut(OutPutPath, img)
                result = 0.0
        else:
            print("No Triangle Detection! " + img_path)
            cvDebugOut(OutPutPath, img)
            result = 0.0
        return result

if __name__ == "__main__":
    img_path_list = glob.glob(ROOTPATH+ '/raw_data/US/SmallMap/*.*', recursive=True)
    # print(img_path_list)
    pd = PosDetection()
    for i in range(len(img_path_list)):
        print(img_path_list[i])
        # img = cv2.imread(img_path_list[i])
        print(pd.PosEstimationOnSmallMap(img_path_list[i]))
