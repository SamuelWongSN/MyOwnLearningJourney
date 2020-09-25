# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice06.py 
@time: 2020/09/25
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 输出100以内所有的素数。
n = int(input('Please input an integer:'))
list = []
for i in range(n):
    flag = 1
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flag = 0
            break
    if flag:
        list.append(i)
print(list)