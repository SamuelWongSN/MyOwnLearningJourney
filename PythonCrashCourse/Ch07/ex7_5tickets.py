'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 7:58 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex7_5tickets.py
 @Software: PyCharm
'''

app = ''
flag = True
while flag:
    app = input("Please input your age,input 'quit' to quit: ")
    if app == 'quit':
        flag = False
    else:
        app = int(app)
        if app<3:
            print("Free")
        elif app >= 3 and app < 12:
            print("10d")
        elif app >= 12:
            print("15d")