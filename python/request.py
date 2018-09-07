import os
import requests
import urllib
from lxml import etree

queryUrl = 'http://electsysq.sjtu.edu.cn/ReportServer/Pages/ReportViewer.aspx?%2fExamArrange%2fLessonArrangeForOthers&rs:Command=Render'
exportUrl = 'http://electsysq.sjtu.edu.cn/ReportServer/Reserved.ReportViewerWebControl.axd?ExecutionID=2ibmxcr501ukz5zds2ky1v55&ControlID=a45be4edf6064ca6ae8056a78811be9a&Culture=2052&UICulture=4&ReportStack=1&OpType=Export&FileName=LessonArrangeForOthers&ContentDisposition=OnlyHtmlInline&Format='

format = ["XML", "CSV", "TIFF", "MHTML", "EXCEL"]
buildings = ["闵行上院", '闵行中院', '闵行下院', "闵行东上院", '闵行东中院', '闵行东下院']

currentPath = os.path.dirname(os.path.abspath(__file__))
cachePath = os.path.join(currentPath, "cache")

session = requests.session()

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }

session.headers.update(headers)


fresh_page = session.get(queryUrl).text

fresh_html = etree.HTML(fresh_page)

# query 页面里面藏有三个隐藏字段，Post 的时候要一并发过去。

view_state = fresh_html.xpath('//*[@id="__VIEWSTATE"]/@value')
view_state_generator = fresh_html.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')
event_validation = fresh_html.xpath('//*[@id="__EVENTVALIDATION"]/@value')

postParams = {}

postParams['__VIEWSTATE'] = view_state
postParams['__VIEWSTATEGENERATOR'] = view_state_generator
postParams['__EVENTTARGET'] = ''
postParams['__EVENTARGUMENT'] = ''
postParams['__EVENTVALIDATION'] = event_validation
postParams['ReportViewerControl$ctl00$ctl03$ddValue']: 3
# 这个参数代表了学年。目前 1 代表 2018 - 2019 学年。

postParams['ReportViewerControl$ctl00$ctl05$ddValue']: 2
# 这个参数代表学期。一样，3 代表暑期小学期查出来是空的。

postParams['ReportViewerControl$ctl00$ctl07$ddValue']: 1
postParams['ReportViewerControl$ctl00$ctl09$txtValue']: ''
postParams['ReportViewerControl$ctl00$ctl11$txtValue']: ''
postParams['ReportViewerControl$ctl00$ctl13$ddValue']: 1
postParams['ReportViewerControl$ctl00$ctl15$txtValue']: ''
postParams['ReportViewerControl$ctl00$ctl17$txtValue']: ''
postParams['ReportViewerControl$ctl00$ctl19$txtValue']: '闵行上院'
postParams['ReportViewerControl$ctl00$ctl00']: '查看报表'
postParams['ReportViewerControl$ctl01$ctl05$ctl00']: '选择格式'
postParams['ReportViewerControl$ctl04']: ''
postParams['ReportViewerControl$ctl05']: ''
postParams['ReportViewerControl$ctl06']: 1
postParams['ReportViewerControl$ctl07']: 'false'
postParams['ReportViewerControl$ctl08']: 'false'

print("Params: ")
print(postParams)

session.post(queryUrl, data = postParams)

requestUrl = session.get(exportUrl + format[0])
print("writing xml to file...")
with open(cachePath, "wb") as f:
    f.write(requestUrl.content)
f.close()
