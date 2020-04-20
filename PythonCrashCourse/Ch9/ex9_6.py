'''
 # -*- coding: utf-8 -*-
 @Time    : 4/20/2020 6:37 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex9_6.py
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


class icecreamstand(Restaurant):
    def __init__(self,name,cost):
        super().__init__(name,cost)
        self.favourite = ['apple','banana','orange']
    def show_taste(self):
        print("we have these taste: ")
        for taste in self.favourite:
            print("-"+taste)
ice = icecreamstand('jj','dd')
ice.show_taste()
print(ice.name)
