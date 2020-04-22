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
        #初始化游戏静态设置
        #初始化屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color     = (230, 230, 230)
        #飞船设置
        self.ship_limit = 3
        #子弹设置
        self.bullet_width = 3
        self.bullet_heigh = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        #升级参数
        self.speed_scale = 1.1
        self.score_scale = 1.5
        #初始化游戏动态设置
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        '''初始化动态变量'''
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.bullet_speed_factor = 1
        # 1为右移，-1为左移
        self.fleet_direction = 1
        self.alien_point = 50

    def increase_speed(self):
        '''提速！！！'''
        self.ship_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.fleet_drop_speed *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale

        self.alien_point = int(self.alien_point * self.score_scale)