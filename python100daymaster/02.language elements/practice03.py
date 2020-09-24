# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice03.py 
@time: 2020/09/24
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
year = int(input('Please input the year:'))
is_leap = year % 4 == 0 and year % 100 != 0\
          or year % 400 == 0
print(is_leap)