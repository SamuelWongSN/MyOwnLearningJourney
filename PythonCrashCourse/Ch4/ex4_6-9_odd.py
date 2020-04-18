# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:34:04 2020

@author: 思侬
"""

ji = list(range(1,20,2))
for j in ji:
    print(j)
    
bei3 = list(range(3,20,3))
for b in bei3:
    print(b)
print('\n')

cube = []
for i in range(1,11):
    cube.append(i ** 3)
for i in cube:
    print(i)
# 搞一手三次方列表

cube2 = [i**3 for i in range(1,11)]
print(cube2)
# 应用列表解析有点东西奥