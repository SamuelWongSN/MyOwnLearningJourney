'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 12:06 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex9_1213.py
 @Software: PyCharm
'''

from collections import OrderedDict

favourite_language = OrderedDict()
favourite_language['Adam'] = 'C'
favourite_language['Betty'] = 'Python'
favourite_language['Cathy'] = 'Go'
favourite_language['Doom'] = 'C'

print(favourite_language)
for key, value in favourite_language.items():
    print(key + " likes " + value)

from random import randint
x = randint(1,6)
print(x)