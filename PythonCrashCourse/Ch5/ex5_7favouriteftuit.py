'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 3:26 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex5_7favouriteftuit.py
 @Software: PyCharm
'''

favourite_fruits = ['dragonfruit','pineapple','pear']
# 喜欢的水果列表
guess_list = ['apple','banana','pear','peach','pineapple','strawberry']
# 猜测的水果列表

for guess_fruit in guess_list:      # 猜测列表里的每个都猜一边冲冲冲
    if guess_fruit in favourite_fruits:
        print('wow,'+ guess_fruit +' is your favourite fruit!')
    # 猜对了就感叹一下
    else:
        print("How dare you don't like " + guess_fruit + " !")
    # 猜错了就指责我

