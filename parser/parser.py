# parser.py
#
# written by yuxq in 2018/9/15. all rights reserved.


from curriculum import *
from utils import *
from requester.request_postgrad import query_postgrad_data
import os
import csv
import sys
import json
import datetime

UG_ONLY = False
# NO_SUMMER = True


sys.path.append('../requester')

start_year = int(input("Input the year when the term started >>> "))
term = int(input(
    "Input the term code (1 = autumn or 2 = spring + summer) >>> "))

current_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.abspath(os.path.join(
    current_path, "../csv_data/%d_%d_%d.csv" % (start_year, start_year + 1, term)))
json_path = os.path.abspath(os.path.join(
    current_path, "../json_output/%d_%d_%d.json" % (start_year, start_year + 1, term)))
summer_json_path = os.path.abspath(os.path.join(
    current_path, "../json_output/%d_%d_3.json" % (start_year, start_year + 1)))
# print(current_path)
# print(csv_path)
# input()

course_list = []
with open(csv_path, "r", encoding="utf-8") as raw_file:
    lines = csv.reader(raw_file)

    for line in lines:
        if line[0] == 'yxmc':
            # 第一个表头不要读。里面没信息
            continue
        cur = Curriculum()
        for i in range(len(line)):
            line[i] = sanitize(line[i])
        if len(line) == 15:
            try:
                cur.generate_arrangement(line[7])
                cur.holder_school = line[0]
                cur.teacher_name = line[1]
                cur.teacher_title = line[2]
                cur.title_name = line[3]
                cur.identifier = line[4]
                cur.learn_hour = int(line[5])
                cur.credit_score = float(line[6])
                cur.notes = line[8]
                cur.term = term
                cur.school_year = start_year
                cur.target_grade = int(line[9])
                cur.school_year = int(line[10][:4])
                cur.judge_term(int(line[11]))
                cur.student_number = int(line[12])
            except:
                # 遇到坏的了
                # 这次的 csv 里第 2981 行就是坏的 😠
                continue
            else:
                pass
        course_list.append(cur)
        # cur.print_me()
        print('.', end='')
    print("完成，一共解析了 %d 枚课程数据。" % (len(course_list)))
    # while True:
    #     x = int(input("Pick one to see >>> "))
    #     if x < len(course_list):
    #         course_list[x].print_me()
    #     else:
    #         break
    # print(line)
    # for cur in course_list:
    #     cur.print_me()
raw_file.close()

data = {
    'data': []
}

data_summer = {
    'data': []
}

for i in course_list:
    part = {}
    part['identifier'] = i.identifier
    part['holder_school'] = i.holder_school
    part['name'] = i.title_name
    part['year'] = i.school_year
    part['term'] = i.term
    part['target_grade'] = i.target_grade
    part['teacher'] = i.teacher_name
    part['teacher_title'] = i.teacher_title
    part['credit'] = i.credit_score
    part['start_week'] = i.start_week
    part['end_week'] = i.end_week
    part['odd_week'] = []
    part['even_week'] = []
    for comp in i.odd_week:
        part['odd_week'].append({
            'week_day': comp.week_day,
            'start_from': comp.start_lesson,
            'end_at': comp.end_lesson,
            'classroom': comp.classroom
        })
    for comp in i.even_week:
        part['even_week'].append({
            'week_day': comp.week_day,
            'start_from': comp.start_lesson,
            'end_at': comp.end_lesson,
            'classroom': comp.classroom
        })
    part['student_number'] = i.student_number

    if i.term == 3:
        data_summer['data'].append(part)
    else:
        data['data'].append(part)


if not UG_ONLY:
    for curric in query_postgrad_data(start_year, term):
        data['data'].append(curric)

data['generate_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if not NO_SUMMER:
    if term == 2:
        if not UG_ONLY:
            for curric_summer in query_postgrad_data(start_year, 3):
                data_summer['data'].append(curric_summer)
        data_summer['generate_time'] = datetime.datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S')


with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)
json_file.close()

if len(data_summer['data']) != 0:
    with open(summer_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_summer, json_file, ensure_ascii=False)
    json_file.close()
