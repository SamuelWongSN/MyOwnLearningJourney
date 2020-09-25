# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice02.py 
@time: 2020/09/25
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
n = int(input('Please input a positive integer:'))
m = int(input('Please input a positive integer:'))
multi = m * n
while n:
    if n > m:
        n, m = m, n
    temp = n
    n = m - n
    m = temp
print(m, int(multi/m))