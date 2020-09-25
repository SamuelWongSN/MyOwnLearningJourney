# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice03.py 
@time: 2020/09/25
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习3：打印如下所示的三角形图案。
str = ''
for i in range(5):
    str += '*'
    print(str)

for i in range(5):
    str = ''
    str += ' ' * (4 - i)
    str += '*' * (1 + i)
    print(str)

for i in range(5):
    str = ''
    str += ' ' * (4 - i)
    str += '*' * (2*i + 1)
    print(str)