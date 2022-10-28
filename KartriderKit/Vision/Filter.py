"""
# -*- coding:utf-8 -*-
@Project : SmartKartRider
@File : Filter.py
@Author : Johan
@Time : 10/28/2022 12:22 AM

"""
import cv2


def hsvFilter(img, lower, upper):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(img, img, mask=mask)
    return hsv, mask, res