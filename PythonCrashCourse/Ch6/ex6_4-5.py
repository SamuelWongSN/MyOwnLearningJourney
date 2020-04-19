'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 5:43 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex6_4-5.py
 @Software: PyCharm
'''

dictory = {'joke':1,'queen':12,'king':13,'Ace':1}
for key,value in dictory.items():
    print(key + "'s value is " + str(value))
print('\n')
# ex6-5 rivers

river_country = {'nile':'egypt','huang':'china','amazon':'america'}
for river,country in river_country.items():
    print(river + ' in the ' + country)
print('\n')
for river in river_country.keys():
    print(river)
print('\n')
for country in river_country.values():
    print(country)