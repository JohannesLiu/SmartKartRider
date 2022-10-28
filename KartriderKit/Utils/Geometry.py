"""
# -*- coding:utf-8 -*-
@Project : SmartKartRider
@File : Geometry.py
@Author : Johan
@Time : 10/27/2022 11:08 PM

"""
import math

import numpy as np


def angle_between_vectors(v1, v2):
    pi = math.pi
    vector_prod = v1[0] * v2[0] + v1[1] * v2[1]
    length_prod = math.sqrt(pow(v1[0], 2) + pow(v1[1], 2)) * math.sqrt(pow(v2[0], 2) + pow(v2[1], 2))
    cos = vector_prod * 1.0 / (length_prod * 1.0 + 1e-6)
    return (math.acos(cos) / pi) * 180


def direction_of_traingle(points):
    k_left_vet_index, k_up_vet_index = np.argmin(points.reshape(len(points), -1), axis=0)
    k_right_vet_index = np.argmax(points.reshape(len(points), -1), axis=0)[0]
    k_left_vet = points[k_left_vet_index]
    k_right_vet = points[k_right_vet_index]
    k_up_vet = points[k_up_vet_index]
    k_mid_down_vet = (k_right_vet + k_left_vet) / 2
    k_dir_vet = k_up_vet - k_mid_down_vet
    return k_dir_vet