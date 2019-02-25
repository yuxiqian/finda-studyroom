# request_postgrad.py
#
# written by yuxq in 2018. all rights reserved.

import re
import os
import json
import urllib
import requests


from electsysApi import login, shared


import electsysApi.login as login
import electsysApi.manip as manip
import electsysApi.shared as shared
import electsysApi.modules as modules
import getpass

log = login.Login()


username = input("jAccount ID: >>> ")
password = getpass.getpass("jAccount Password: >>> ")

log.get_captcha(display=True, on_screen=True)
captcha = input("Input Captcha: >>> ")


print("Login Response: ")
s = log.attempt(username, password, captcha)

if s == None:
    print("服务器提了一个问题")
    exit(1)

# s 要不是 None，就是我们的内容 Session 了

# 等会儿，喘口气
# input()
