'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 7:48 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex7_4piiza.py
 @Software: PyCharm
'''
opp = ''
flag = True
while flag:
    if opp != 'quit':
        opp = input("Please input your prefer: ")
        print("ok,we already put "+opp+" on your pizza.")
    else:
        flag = False