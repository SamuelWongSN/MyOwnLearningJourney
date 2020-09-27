# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice7.6.py 
@time: 2020/09/26
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习6：打印杨辉三角。

n = int(input(':'))
list = []
for i in range(n):
    if i > 1:
        for j in range(i-1, 0, -1):
            list[j] = list[j]+list[j-1]
    list.append(1)
    print(list)