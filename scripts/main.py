"""
# -*- coding:utf-8 -*-
@Project : SmartKartRider
@File : main.py.py
@Author : Johan
@Time : 10/20/2022 12:35 AM

"""
import cv2
import glob
import numpy as np
import os
import matplotlib.pyplot as plt

from win32gui import GetWindowText, GetForegroundWindow, GetWindowRect, FindWindow
import pyscreenshot as ImageGrab
import time
import os
from IPython.display import display, clear_output
import datetime

'''
# if the foreground window is as the same as desired_window, then this script will capture your current screen and check current scenario.
# which is faster than capture screenshot using Nox.
'''
WORKPATH = "D:/GameProjects/Kartrider/SmartKartRider"
desired_window = "BlueStacks App Player"
os.chdir(WORKPATH)
print(os.popen('adb devices').read())