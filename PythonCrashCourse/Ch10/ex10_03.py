'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 1:15 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex10_03.py
 @Software: PyCharm
'''

def count_word(filename):
    filename += '.txt'
    try:
        with open(filename) as file:
            contents = file.read()
    except:
        message = 'Can not found the file ' + filename
        print(message)
    else:
        num = len(contents.split())
        print(filename + ' has ' + str(num) + ' words.')

booklist = ['alice','little_women','moby_dick','HarryPoter']
for book in booklist:
    count_word(book)