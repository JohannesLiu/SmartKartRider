"""
# -*- coding:utf-8 -*-
@Project : SmartKartRider
@File : CVTools.py
@Author : Johan
@Time : 10/27/2022 11:07 PM

"""
import cv2 as cv

class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        # 初始化形状名称并近似轮廓
        shape = "unidentified"
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.10* peri, True)
        # approx = cv.approxPolyDP(c, 0.04 * peri, True)
        # 如果形状是一个三角形，它将有3个顶点
        if len(approx) == 3:
            shape = "triangle"
        # 如果形状有4个顶点，它要么是正方形，要么是矩形
        elif len(approx) == 4:
            # 计算轮廓的包围框，并使用包围框计算高宽比
            (x, y, w, h) = cv.boundingRect(approx)
            ar = w / float(h)
            # 正方形的长宽比大约等于1，否则，形状就是矩形
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        # 如果形状是一个五边形，它将有5个顶点
        elif len(approx) == 5:
            shape = "pentagon"
        # 否则，我们假设形状是一个圆
        else:
            shape = "circle"
        # 返回形状的名称
        return shape, approx