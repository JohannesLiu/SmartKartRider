"""
# -*- coding:utf-8 -*-
@Project : SmartKartRider
@File : deploy.py.py
@Author : Johan
@Time : 10/28/2022 12:06 AM

"""
import os

os.system("python ./clean.py")
os.system("git add -A")
os.system('git commit -m "update')
os.system("git push")