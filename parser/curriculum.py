# curriculum.py
#
# written by yuxq in 2018/9/15. all rights reserved.

import re
from utils import *
from copy import deepcopy

class Arrangement:
    # 单次上课的具体参数
    # 一门课可能会在一个学期内包含不同的课程教室组合
    # 由一个 Arrangement 数组来描述
    week_day = 0
    # 星期数。约定使用 1 ～ 7 分别代表周一到周日。

    start_lesson = 0
    # 开始节数

    end_lesson = 0
    # 结束节数（怪怪的）

    classroom = ''
    # 授课教室

    def print_me(self):
        print('\t', end = '')
        print(self.week_day)
        print('\t', end = '')
        print(self.start_week)
        print('\t', end = '')
        print(self.end_week)
        print('\t', end = '')
        print(self.start_lesson)
        print('\t', end = '')
        print(self.end_lesson)
        print('\t', end = '')
        print(self.classroom)
        print()


class Curriculum:

    def __init__(self):
        self.odd_week = []
        # 单周的行课安排

        self.even_week = []
        # 霜周的行课安排

    holder_school = ''
    # 开课院系

    teacher_name = ''
    # 教师名称

    teacher_title = ''
    # 教师职称

    title_name = ''
    # 课程名称

    identifier = ''
    # 课程唯一识别代码

    learn_hour = 0
    # 学时

    credit_score = 0.0
    # 学分

    start_week = 0
    # 起始周数

    end_week = 0
    # 终止周数

    def generate_arrangement(self, raw_arrangement):
        # 生成行课安排 (通过未经处理的字符串)
        arrange_box = raw_arrangement.split('\n')
        # print(arrange_box)

        week_info = [x for x in re.split("行课安排为第|-|周,其中:", arrange_box[0]) if x]
        self.start_week = int(week_info[0])
        self.end_week = int(week_info[1])
        # 搞出来起始周……

        is_odd_but_not_even = True
        is_plain_weekmode = True

        for line in arrange_box[1:]:
            if line == "单周":
                is_odd_but_not_even = True
                is_plain_weekmode = False
                continue
            elif line == "双周":
                is_odd_but_not_even = False
                is_plain_weekmode = False
                continue
            if is_odd_but_not_even:
                if line[:2] == "星期":
                    # 是详细信息里的第一行：日期数
                    # 准备往 odd_week 里写
                    arr = deepcopy(Arrangement())
                    day_info = [x for x in re.split("星期|第|节--第|节", line) if x]
                    # print(day_info)

                    arr.week_day = han_to_int(day_info[0])
                    arr.start_lesson = int(day_info[1])
                    arr.end_lesson = int(day_info[2])
                    self.odd_week.append(arr)
                else:
                    classroom_info = line.split('(')
                    # print(classroom_info)
                    if classroom_info[0][:5] == "不安排教室":
                        self.odd_week[-1].classroom = "不安排教室"
                    else:
                        self.odd_week[-1].classroom = classroom_info[0]

            else:
                if line[:2] == "星期":
                    # 是详细信息里的第一行：日期数
                    # 准备往 even_week 里写
                    arr = Arrangement()
                    day_info = [x for x in re.split("星期|第|节--第|节", line) if x]
                    # print(day_info)

                    arr.week_day = han_to_int(day_info[0])
                    arr.start_lesson = int(day_info[1])
                    arr.end_lesson = int(day_info[2])
                    self.even_week.append(arr)
                else:
                    classroom_info = line.split('(')
                    # print(classroom_info)
                    if classroom_info[0][:5] == "不安排教室":
                        self.even_week[-1].classroom = "不安排教室"
                    else:
                        self.even_week[-1].classroom = classroom_info[0]

        # input()
        # 先等我让我缓一下……

        if is_plain_weekmode:
            self.copy_odd_to_even()
        """
        行课安排为第1-14周,其中:\n单周\n星期三第1节--第2节\n下院213(1-13周)张景新(1-13周)\n星期五第3节--第4节\n下院213(1-13周)张景新(1-13周)\n双周\n星期三第1节--第2节\n下院213(2-14周)张景新(2-14周)
        """


    notes = ''
    # 备注

    target_grade = 0
    # 目标年级

    school_year = 0
    # 学年

    term = 0
    # 学期

    student_number = 0
    # 上课人数

    def copy_odd_to_even(self):
        self.even_week = self.odd_week

    def judge_term(self, term):
        self.term = term
        if "夏季" in self.notes and "学期" in self.notes:
            self.term = 3
        # 教务处暑期小学期是在备注里标明的……绝了

    def print_me(self):
        print(self.title_name)
        print(self.teacher_name)
        print(self.teacher_title)
        print(self.holder_school)
        print(self.identifier)
        print(self.learn_hour)
        print(self.credit_score)
        for i in self.odd_week:
            i.print_me()
        for i in self.even_week:
            i.print_me()
        print(self.notes)
        print(self.target_grade)
        print(self.school_year)
        print(self.term)
        print(self.student_number)
        print()
