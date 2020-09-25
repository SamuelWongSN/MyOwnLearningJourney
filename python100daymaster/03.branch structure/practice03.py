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
from math import sqrt
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a+b > c and a+c > b and b+c > a:
    perimeter = a+b+c
    s = (a+b+c) / 2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print('%.2f, %.2f' % (perimeter, area))
else:
    print('can not be a trangle')