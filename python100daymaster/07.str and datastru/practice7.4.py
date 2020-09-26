# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice7.4.py 
@time: 2020/09/26
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。

def max2(list):
    x1, x2 = (list[0], list[1]) if list[0]>list[1] else (list[1], list[0])
    for i in range(2, len(list)):
        if list[i] > x1:
            x2 = x1
            x1 = list[i]
        elif list[i] > x2:
            x2 = list[i]
    return x1, x2

def main():
    list = [3, 45, 3, 23, 2, 52, 12, 423, 4324]
    x1, x2 = max2(list)
    print(x1, x2)

if __name__ == '__main__':
    main()