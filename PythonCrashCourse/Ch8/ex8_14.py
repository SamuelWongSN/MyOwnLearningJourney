'''
 # -*- coding: utf-8 -*-
 @Time    : 4/20/2020 1:16 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex8_14.py
 @Software: PyCharm
'''

def make_cars(maker,plat,**infos):
    cars = {}
    cars['maker'] = maker
    cars['plat']  = plat

    for key,value in infos.items():
        cars[key] = value
    return cars

car = make_cars('subaru', 'outback', color='blue', tow_package=True)
print(car)