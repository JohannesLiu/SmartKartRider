"""
# -*- coding:utf-8 -*-
@Project : SmartKartRider
@File : Geometry.py
@Author : Johan
@Time : 10/27/2022 11:08 PM

"""
import math

def angle_of_vector(v1, v2):
    pi = math.pi
    vector_prod = v1[0] * v2[0] + v1[1] * v2[1]
    length_prod = math.sqrt(pow(v1[0], 2) + pow(v1[1], 2)) * math.sqrt(pow(v2[0], 2) + pow(v2[1], 2))
    cos = vector_prod * 1.0 / (length_prod * 1.0 + 1e-6)
    return (math.acos(cos) / pi) * 180