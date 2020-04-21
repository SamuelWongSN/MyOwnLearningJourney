'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 2:37 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex10test.py
 @Software: PyCharm
'''

import json
pi = {'jj':6}
with open('Fnum.json','w') as file:
    json.dump(pi,file)
print(pi)