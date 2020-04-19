'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 6:27 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex6_9-10.py
 @Software: PyCharm
'''

people = {'sam':['a','c','g'],'jj':'b','andrew':['e','c']}
for person in people:
    print(person)
    for word in people[person]:
        print(word)
    print('\n')