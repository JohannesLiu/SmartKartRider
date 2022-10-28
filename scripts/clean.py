"""
# -*- coding:utf-8 -*-
@Project : SmartKartRider
@File : clean.py
@Author : Johan
@Time : 10/28/2022 12:17 AM

"""
import glob
import os

from KartriderKit.__init__ import *
if __name__ == "__main__":
    remove_file_list = glob.glob(ROOTPATH + "/Data/Debug/*/*.*")
    for item in remove_file_list:
        os.system("rm " + item)