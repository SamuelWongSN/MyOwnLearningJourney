'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 8:40 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex7_9pastrami.py
 @Software: PyCharm
'''

sandwish_orders = ['beef','pork','banana','milk','beef','rabbit','beef']
print(sandwish_orders)
print("Opps,Beef have sold out,sorry.")
while 'beef' in sandwish_orders:
    sandwish_orders.remove("beef")
print("There's new order.")
print(sandwish_orders)