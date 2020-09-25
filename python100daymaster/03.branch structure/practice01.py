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
length = float(input('Please input the length:'))
unit = input('Please input the unit:')

if unit == 'nt':
    len_nt = length
    len_cm = length * 2.54
    print('cm: %.2f cm; nt: %.2f nt' % (len_cm, len_nt))
elif unit == 'cm':
    len_cm = length
    len_nt = length / 2.54
    print('cm: %.2f cm; nt: %.2f nt' % (len_cm, len_nt))
else:
    print('Please input valid unit')
