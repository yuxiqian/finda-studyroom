# parser.py
#
# written by yuxq in 2018/9/15. all rights reserved.


import os
import csv
import json

from utils import *
from curriculum import *

start_year = int(input("Input the year when the term started >>> "))
term = int(input("Input the term code (1 = autumn or 2 = spring) >>> "))

current_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.abspath(os.path.join(current_path, "../csv_data/%d_%d_%d.csv" % (start_year, start_year + 1, term)))
json_path = os.path.abspath(os.path.join(current_path, "../json_output/%d_%d_%d.json" % (start_year, start_year + 1, term)))
# print(current_path)
# print(csv_path)
# input()

course_list = []
with open(csv_path, "r", encoding = "utf-8") as raw_file:
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
        print('.', end = '')
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

data = {'data': []}
for i in course_list:
    part = {}
    part['identifier'] = i.identifier
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
    part['name'] = i.title_name
    part['teacher'] = i.teacher_name
    part['teacher_title'] = i.teacher_title
    part['student_number'] = i.student_number
    part['year'] = i.school_year
    part['credit'] = i.credit_score
    data['data'].append(part)


with open(json_path, 'w', encoding = 'utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False)
json_file.close()
