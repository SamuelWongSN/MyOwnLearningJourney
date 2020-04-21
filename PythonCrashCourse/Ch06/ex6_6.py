'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 5:54 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex6_6.py
 @Software: PyCharm
'''

poll = {'AmazingJ':True,'Betty':False,'Cryin':True}
for name in poll.keys():
    if poll[name]:
        print(name + ', Thank you baby.')
    else:
        print(name + ', How dare you')