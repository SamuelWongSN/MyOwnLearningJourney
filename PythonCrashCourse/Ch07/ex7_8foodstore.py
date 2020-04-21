'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 8:32 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex7_8foodstore.py
 @Software: PyCharm
'''

sandwish_orders = ['beef','pork','banana','milk']
finished_sandwich = []
# 一个订单列表 一个完成列表

while sandwish_orders:                              # 列表不为空
    current_sandwich = sandwish_orders.pop();       # pop出最后一个元素
    print("I make your "+current_sandwich+" sandwich!");
    finished_sandwich.append(current_sandwich)      # 添加到完成列表
print("All orders have finished.:P")