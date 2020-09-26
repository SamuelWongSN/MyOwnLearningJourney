# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice7.5.py 
@time: 2020/09/26
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习5：计算指定的年月日是这一年的第几天。

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def compute_days(date):
    pos1 = date.find('.')
    pos2 = date.rfind('.')
    days_for_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    year = int(date[:pos1-1])
    month = int(date[pos1+1:pos2])
    day = int(date[pos2+1:])

    days = 0
    for i in range(month):
        days += days_for_month[i]
    days += day
    if is_leap(year):
        days += 1
    return days

def main():
    date = input(':')
    days = compute_days(date)
    print(days)

if __name__ == '__main__':
    main()