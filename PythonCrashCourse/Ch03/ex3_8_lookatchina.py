# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:46:45 2020

@author: 思侬
"""

world_list = ['chongqing','shanghai','beijing','tianjin','wuhan']
print(world_list)

print(sorted(world_list))   #打印排序好的列表
print(world_list)           #检查列表顺序是否变化
print(sorted(world_list,reverse=True))  #打印反向排序好的列表
print(world_list)                       #检查列表学列是否变化

world_list.reverse()    #倒置列表
print(world_list)       #检查列表顺序
world_list.reverse()    #再倒置一遍
print(world_list)       #检查列表顺序

world_list.sort()       #排序列表
print(world_list)       #检查
world_list.sort(reverse=True)   #反排序
print(world_list)               #检查