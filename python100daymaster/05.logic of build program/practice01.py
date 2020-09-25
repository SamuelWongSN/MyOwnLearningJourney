# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice01.py 
@time: 2020/09/25
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
perfect = []
for i in range(100, 1000):
    i_one = i % 10
    i_ten = i // 10 % 10
    i_hun = i // 100

    if i == i_one**3 + i_ten**3 + i_hun**3:
        perfect.append(i)
print(perfect)