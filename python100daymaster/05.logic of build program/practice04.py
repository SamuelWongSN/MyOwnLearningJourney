# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice04.py 
@time: 2020/09/25
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 生成斐波那契数列的前20个数。
n = int(input('How many you want:'))
list = []
for i in range(n):
    if i < 2:
        list.append(1)
    else:
        list.append(list[-1] + list[-2])
print(list)

# 生成第n层杨辉三角。
n = int(input('How many you want:'))
list = []
for i in range(n):
    if i > 1:
        for j in range(i-1, 0, -1):
            list[j] = list[j] + list[j-1]
    list.append(1)
print(list)