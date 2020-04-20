'''
 # -*- coding: utf-8 -*-
 @Time    : 4/20/2020 3:56 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex9_1-2.py
 @Software: PyCharm
'''


class Restaurant():
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost

    def describe(self):
        print("This restaurant's name is "+self.name+',cost is '+self.cost)
    def open(self):
        print("The restaurant is opening.")

bb = Restaurant('Sanjiao','12')
cc = Restaurant('qimin','3')
dd = Restaurant('sdfs','45')
bb.describe()
cc.describe()
dd.describe()