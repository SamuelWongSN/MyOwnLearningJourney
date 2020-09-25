# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice05.py 
@time: 2020/09/25
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 找出10000以内的完美数。
list = []
for i in range(1, 10001):
    sum = 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            sum += j
            sum += int(i / j)
    if sum == i:
        list.append(i)
print(list)