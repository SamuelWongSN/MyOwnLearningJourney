# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:40:32 2020

@author: 思侬
"""

pizzas = ['ham','cheese','tomato','pineapple','chicken']
print(pizzas[:3])
print(pizzas[-3:])
print(pizzas[1:4])
# 分别打印前三个，后三个，第二个到第四个

friend_pizzas = pizzas[:]
pizzas.append("beef")
friend_pizzas.append("bug")
print(pizzas)
print(friend_pizzas)
# 各添加一种口味，看看串不串

print("")
buffet = ('noodle','rice','ham','pork','meatball')
for food in buffet:
    print(food)
buffet = ('rice','ham')
print(buffet)