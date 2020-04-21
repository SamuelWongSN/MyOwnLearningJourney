'''
 # -*- coding: utf-8 -*-
 @Time    : 4/20/2020 1:06 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex8_12.py
 @Software: PyCharm
'''

def make_sandwich(size,*toppings):
    print("you order a "+str(size)+" size sandwich with these: ")
    for sandwich in toppings:
        print('-'+sandwich)

make_sandwich(12,'beef','pork','milk','apple')