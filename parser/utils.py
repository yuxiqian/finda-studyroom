# utils.py
#
# written by yuxq in 2018/9/15. all rights reserved.

def sanitize(string):
    return string.replace(' ', '')

def han_to_int(string):
    if string == "一":
        return 1
    if string == "二":
        return 2
    if string == "三":
        return 3
    if string == "四":
        return 4
    if string == "五":
        return 5
    if string == "六":
        return 6
    if string == "日":
        return 7
    return 0
