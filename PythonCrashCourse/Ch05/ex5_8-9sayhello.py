'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 3:47 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex5_8-9sayhello.py
 @Software: PyCharm
'''

list1 = ['jj','admin','sn','doinb','Gimgoon']
list2 = []
user_list = list2
if user_list:
    for user in user_list:
        if user == 'admin':
            print('Hello admin,would you like to see me?')
        else:
            print('Hello '+user+',how are you')
else:
    print('you need to find some friends.')