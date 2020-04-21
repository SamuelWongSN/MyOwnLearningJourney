'''
 # -*- coding: utf-8 -*-
 @Time    : 4/20/2020 12:06 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex8_9-11.py
 @Software: PyCharm
'''

def show_magicans(magicans):
    '''把魔术师名字打印出来'''
    print('\n')
    for magican in magicans:
        print(magican)


def make_great(magicans):
    '''名字前面加个昵称'''
    for cnt in range(len(magicans)):
        magicans[cnt] = 'The Great '+magicans[cnt]
    return magicans

magic = ['dingding','laobai','bibabo','aohei']
show_magicans(magic)
new_list = make_great(magic[:])     # 调用副本
show_magicans(magic)
show_magicans(new_list)

