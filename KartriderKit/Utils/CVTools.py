"""
# -*- coding:utf-8 -*-
@Project : SmartKartRider
@File : CVTools.py
@Author : Johan
@Time : 10/27/2022 11:07 PM

"""
from datetime import datetime

import cv2


def cvDebugOut(OutPutPath, img):
    cv2.imwrite(OutPutPath + "/" + str(datetime.now()).replace(" ", "").replace(":", "-") + ".png", img)
