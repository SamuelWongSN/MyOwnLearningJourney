'''
 # -*- coding: utf-8 -*-
 @Time    : 4/20/2020 5:56 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex9_3.py
 @Software: PyCharm
'''

class Restaurant():
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
        self.numb = 0

    def describe(self):
        print("This restaurant's name is "+self.name+',cost is '+self.cost)
    def open(self):
        print("The restaurant is opening.")
    def set_numb(self,num):
        self.numb = num
    def increase_numb(self,add):
        self.numb += add

res = Restaurant('jj',45)
print(res.numb)
res.set_numb(6)
print(res.numb)
res.increase_numb(5)
print(res.numb)