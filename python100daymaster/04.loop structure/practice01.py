# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice01.py 
@time: 2020/09/25
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习1：输入一个正整数判断是不是素数。
flag = True
num = int(input('Please input an integer:'))
for i in range(2, int(num**0.5)+1):
    if num % i ==0:
        flag = not flag
        break
print(flag)