# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice01.py 
@time: 2020/09/26
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 实现计算求最大公约数和最小公倍数的函数。
def fun(x1, x2):
    multi = x1 * x2
    while x1:
        if x1 > x2:
            x1, x2 = x2, x1
        temp = x1
        x1 = x2 - x1
        x2 = temp
    return x2, multi // x2

def main():
    print(fun(215, 86))

if __name__ == '__main__':
    main()