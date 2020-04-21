'''
 # -*- coding: utf-8 -*-
 @Time    : 4/20/2020 2:23 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : dog.py
 @Software: PyCharm
'''

class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def sit(self):
        print(self.name.title() + " is sitting.")
    def row_over(self):
        print(self.name.title() + ' is rolling over.')

my_dog = Dog('Harry',12)
print("My dog's name is " + my_dog.name.title() + ".")
my_dog.sit()
my_dog.row_over()