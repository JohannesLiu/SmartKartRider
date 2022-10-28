"""
# -*- coding:utf-8 -*-
@Project : SmartKartRider
@File : clean.py
@Author : Johan
@Time : 10/28/2022 12:39 AM

"""
import os
from KartriderKit.__init__ import *
import glob

if __name__ == "__main__":
    remove_list = glob.glob(ROOTPATH + "/Data/debug/*/*.*", recursive= True)
    for item in remove_list:
        os.system("rm " + item)