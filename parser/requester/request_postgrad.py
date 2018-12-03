# request_postgrad.py
#
# written by yuxq in 2018. all rights reserved.

import re
import os
import json
import urllib
import requests

from lxml import etree
from time import sleep


def parse_leaf(item, params):
    if item.xpath(params) != []:
        return item.xpath(params)[0].text
    else:
        return ""


queryUrl = "http://www.yjs.sjtu.edu.cn:81/epstar/web/outer/KKBJ_CX/kkbj.jsp"


campuses = ["闵行校区", "徐汇校区", "卢湾校区", "法华校区", "七宝校区", "外地", "上海市精神卫生中心", "临港校区"]

campuses_id = ["哈！", "闵行", "徐汇", "卢湾",
               "法华", "七宝", "外地", "上海市精神卫生中心", "临港"]

school_id = ['00000', '01000', '01900', '02000', '03000', '03100', '03200', '03300', '03400', '03500', '03600', '03700', '03900', '05000', '07100', '07200', '08000', '08200', '09000', '09600', '10000', '11000', '12000', '13000', '14000', '15000', '16000', '17000', '18000', '19000', '20000', '21000', '22000', '22100', '23000', '25100', '26000', '27000', '28000', '29000', '29100', '31000', '33000', '34000', '35000',
             '35100', '35200', '36000', '37000', '38000', '39000', '40200', '40400', '41300', '41500', '41600', '41700', '43000', '64000', '65000', '70000', '71000', '71100', '71200', '71900', '72000', '72100', '72200', '72300', '72400', '72500', '72600', '72700', '72800', '72900', '73000', '73100', '73200', '75000', '75100', '75200', '75300', '75400', '75500', '75600', '76000', '78100', '79000', '79100', '79200', '79300', '99999']

han_numbers = ['rua!', '一', '二', '三', '四', '五', '六', '日']

month_tbl = ['pika!', '09', '02', '06']

session = requests.session()

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'Host': 'www.yjs.sjtu.edu.cn:81',
    'Origin': 'http://www.yjs.sjtu.edu.cn:81',
    'Referer': 'http://www.yjs.sjtu.edu.cn:81/epstar/web/outer/KKBJ_CX/kkbj.jsp',
    'Upgrade-Insecure-Requests': '1'
}

session.headers.update(headers)


def query_postgrad_data(start_year, term):
    # start_year = int(input("Input the year when the term started >>> "))
    # term = int(
    #     input("Input the term code (1 = autumn or 2 = spring or 3 = summer >>> "))

    if term != 1:
        start_year += 1

    result_array = []

    for camp in range(1, 9):
        for school in school_id:
            postParams = {'XQDM': str(start_year) + month_tbl[term],
                          'xiaoqu': str(camp),
                          'skyy': '',
                          'YXDM': school,
                          'KCDM': ''
                          }

            # print("Params: ")
            print(postParams)

            sleep(2)
            # Sleep 2 seconds before call .post

            requestUrl = session.post(queryUrl, data=postParams)

            sleep(2)
            # Sleep 2 seconds before call .get
            #

            query_result = etree.HTML(requestUrl.text)

            # print("gotta " + requestUrl.text)
            print("Campus + school has " +
                  str(len(query_result.xpath('//*[@id="table_5"]/tbody/tr'))))

            for item in query_result.xpath('//*[@id="table_5"]/tbody/tr'):
                nod = item.xpath('td[1]/div/a')
                if len(nod) == 0:
                    print("Throw up one piece.")
                    continue

                part = {}
                part['identifier'] = parse_leaf(item, 'td[1]/div/a')

                part['holder_school'] = parse_leaf(item, 'td[7]/div')
                part['name'] = parse_leaf(
                    item, 'td[2]/div/a').split(part['identifier'])[0]
                part['year'] = start_year
                part['term'] = term
                part['target_grade'] = 0
                part['teacher'] = parse_leaf(item, 'td[6]/div/a')
                part['teacher_title'] = ""
                language = parse_leaf(item, 'td[5]/div')
                part['credit'] = float(parse_leaf(item, 'td[4]/div'))

                part['odd_week'] = []
                part['even_week'] = []
                part['notes'] = "授课语言：" + language + \
                    "。" + parse_leaf(item, 'td[12]/div')
                part['student_number'] = int(parse_leaf(item, 'td[10]/div'))

                campus = parse_leaf(item, 'td[8]/div')
                arrangement = parse_leaf(item, 'td[9]/div')

                arrs = arrangement.split(' ')
                for arr in arrs:
                    odd_even_flag = 0
                    if '(单周)' in arr:
                        arr = arr.replace('(单周)', '')
                        print("Marked 单周. arr = " + arr)
                        odd_even_flag = 1
                    elif '(双周)' in arr:
                        arr = arr.replace('(双周)', '')
                        print("Marked 双周. arr = " + arr)
                        odd_even_flag = 2

                    arr_info = [x for x in re.split(
                        "-|周,星期|第|-|节", arr) if x]
                    if len(arr_info) < 6:
                        # print("Throw up " + arr)
                        # Skip this bad loop
                        continue

                    if int(arr_info[0]) + int(arr_info[1]) < 10:
                        part['start_week'] = int(arr_info[0])
                        part['end_week'] = int(arr_info[1])
                    else:
                        part['start_week'] = int(arr_info[0]) + 19
                        part['end_week'] = int(arr_info[1]) + 19

                    if len(arr_info) >= 7:
                        classroom = campus + \
                            arr_info[5] + '-' + '-'.join(arr_info[6:])

                    else:
                        classroom = campus + arr_info[5]
                    print("获得教室 " + classroom)
                    arr = {
                        'week_day': han_numbers.index(arr_info[2]),
                        'start_from': int(arr_info[3]),
                        'end_at': int(arr_info[4]),
                        'classroom': classroom
                    }

                    if odd_even_flag != 2:
                        part['odd_week'].append(arr)

                    if odd_even_flag != 1:
                        part['even_week'].append(arr)

                if part['odd_week'] == [] and part['even_week'] == []:
                    print("Failed to dump " + arrangement)
                    continue
                # print(json.dumps(part, ensure_ascii=False))
                result_array.append(part)
                # print("course + 1")
            print("Finish data grab for %s %s. Now %d counts" %
                  (campuses_id[camp], school, len(result_array)))
    return result_array
