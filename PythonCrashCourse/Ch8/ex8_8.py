'''
 # -*- coding: utf-8 -*-
 @Time    : 4/19/2020 9:40 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex8_8.py
 @Software: PyCharm
'''

def make_album(singer,name):
    return {'singer':singer,'name':name}

while True:
    print("Please input your favourite singer and album name.")
    singer = input("singer: ")
    name   = input("album name: ")

    print(make_album(singer,name))

    flag = input("Continue?")
    if flag.lower() == 'n':
        break