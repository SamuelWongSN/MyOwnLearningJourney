'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 12:39 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex10_01.py
 @Software: PyCharm
'''

file_name = 'pi_digits.txt'
with open(file_name) as file:
    files = file.read()
    lines = file.readlines()

    print(files)
    for i in files:
        print(i)

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))