# utils.py
#
# written by yuxq in 2018 - 2019. all rights reserved.


def sanitize(string):
    return string.replace(' ', '').replace(' ', '')


def remove_nbsp(string):
    return sanitize(string.replace('&nbsp', ''))


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


def generate_term_id(code):
    if code == 1:
        term_code = '3'
    elif code == 2:
        term_code = '12'
    elif code == 3:
        term_code = '16'
    else:
        return None
    return term_code
