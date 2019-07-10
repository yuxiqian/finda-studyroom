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

def gen_classroom(string):
    if len(string.strip()) == 0 or string == '.':
        return "不安排教室"
    minhang_token = ["上院", "中院", "下院", "东上院", "东中院", "东下院", "包图", "逸夫楼"]
    xuhui_token = ["教一楼", "徐汇中院", "新上院", "工程馆", "Med-X实验室"]
    if '(' in string or string == '不安排教室':
        return string
    for k in minhang_token:
        if string[:len(k)] == k:
            return "闵行 (%s/%s)" % (k, string)
    for x in xuhui_token:
        if string[:len(x)] == x:
            return "徐汇 (%s/%s)" % (x, string)
    print("Undetected Campus for %s" % string)
    return string