'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 12:43 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex10_02.py
 @Software: PyCharm
'''

file_name = 'pi_million_digits.txt'
with open(file_name) as file:
    lines = file.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[-50:])
print(len(pi_string))
if '970612' in pi_string:
    print("niubi")
print(pi_string.find('970612'))
print(pi_string[912234:912240])
