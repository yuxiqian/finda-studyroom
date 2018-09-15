# parser.py
#
# written by yuxq in 2018/9/15. all rights reserved.


import os
import csv
from utils import *

start_year = int(input("Input the year when the term started >>> "))
term = int(input("Input the term code (1 = autumn or 2 = spring) >>> "))
current_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.abspath(os.path.join(current_path, "../csv_data/%d_%d_%d.csv" % (start_year, start_year + 1, term)))
# print(current_path)
# print(csv_path)
# input()
with open(csv_path, "r", encoding = "utf-8") as raw_file:
    lines = csv.reader(raw_file)
    for line in lines:
        for i in line:
            i = sanitize(i)
        print(line)
