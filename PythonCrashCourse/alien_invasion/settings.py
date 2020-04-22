'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 7:02 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : settings.py
 @Software: PyCharm
'''

class Settings():
    '''存储 alien invasion 中的所有设置'''

    def __init__(self):
        '''初始化游戏设置'''

        #初始化屏幕设置
        self.screen_width = 1200
        self.screen_heigh = 800
        self.bg_color     = (230, 230, 230)
        #飞船移动速度设置
        self.ship_speed_factor = 1.5
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_heigh = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3