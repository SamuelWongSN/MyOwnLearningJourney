'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 6:12 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex6_7.py
 @Software: PyCharm
'''

samuel = {'high':171,'weigh':79,'hobby':'art'}
jj = {'high':178,'weigh':83,'hobby':'yoyo'}
andrew = {'high':174,'weigh':60,'hobby':'teach'}
# 建立三个字典

people = [samuel,jj,andrew]
# 列表嵌套字典

for person in people:
    print(person)