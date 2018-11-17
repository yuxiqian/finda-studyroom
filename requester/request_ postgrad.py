# request.py
#
# written by yuxq long time ago. all rights reserved.

import os
import requests
import urllib
from time import sleep

queryUrl = "http://www.yjs.sjtu.edu.cn:81/epstar/web/outer/KKBJ_CX/kkbj.jsp"


campuses = ["闵行校区", "徐汇校区", "卢湾校区", "法华校区", "七宝校区", "外地", "上海市精神卫生中心", "临港校区"]


session = requests.session()

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'Origin': 'http://www.yjs.sjtu.edu.cn:81',
    'Referer': 'http://www.yjs.sjtu.edu.cn:81/epstar/web/outer/KKBJ_CX/kkbj.jsp',
    'Cookie': 'JSESSIONID=0000UqAEWXcf_vrb0A9Uy1ZMc0V:17qdn95g8; _ga=GA1.3.455915496.1542005190; _gid=GA1.3.1091877750.1542378982; UM_distinctid=166a5472d9c312-0bf988bbaf46f88-3e636f4c-13c680-166a5472da00'
}

session.headers.update(headers)


fresh_page = session.get(queryUrl).text

postParams = {}
postParams['XQDM'] = "201809"
postParams['xiaoqu'] = 1
# postParams['skyy'] = ""
postParams['YXDM'] = "000000"
# postParams['KCDM'] = ""

print("Params: ")
print(postParams)

session.post(queryUrl, data=postParams)

sleep(2)

requestUrl = session.get(queryUrl)

print(requestUrl.text)
