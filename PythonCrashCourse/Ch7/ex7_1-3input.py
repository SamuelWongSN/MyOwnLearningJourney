'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 6:40 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex7_1-3input.py
 @Software: PyCharm
'''

car = input("Which car would you like? ")
print("Let me see if I can find " + car)
# 汽车问答

table = input("How many people book the table? ")
if int(table) > 8:
    print("Sorry,we have no seat")
else:
    print("Book complicated")
# 预定吃饭问答

num = input("Please input a number to test whether is 10's plus. ")
if int(num) % 10 == 0:
    print("Yes")
else:
    print('No')