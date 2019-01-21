# grabber.py
#
# written by yuxq in 2018/9/15. all rights reserved.


from utils import *
from post_graduate import query_postgrad_data
import os
import csv
import sys
import json
import datetime

UG_ONLY = False


sys.path.append('../requester')

start_year = int(input("Input the year when the term started >>> "))
term = int(input("Input the term code (1 = autumn or 2 = spring + summer) >>> "))


data = {
    'ug': [],
    'pg': []
}

data_summer = {
    'ug': [],
    'pg': []
}


if not UG_ONLY:
    for curric in query_postgrad_data(start_year, term):
        data['pg'].append(curric)

data['generate_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if term == 2:
    if not UG_ONLY:
        for curric_summer in query_postgrad_data(start_year, 3):
            data_summer['pg'].append(curric_summer)
    data_summer['generate_time'] = datetime.datetime.now().strftime(
        '%Y-%m-%d %H:%M:%S')
