# parser.py
#
# written by yuxq in 2018/9/15. all rights reserved.


import os
import csv

from utils import *
from curriculum import *

start_year = int(input("Input the year when the term started >>> "))
term = int(input("Input the term code (1 = autumn or 2 = spring) >>> "))
current_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.abspath(os.path.join(current_path, "../csv_data/%d_%d_%d.csv" % (start_year, start_year + 1, term)))
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
    while True:
        x = int(input("Pick one to see >>> "))
        if x < len(course_list):
            course_list[x].print_me()
        else:
            break
        # print(line)
    # for cur in course_list:
    #     cur.print_me()
