'''
 # -*- coding: utf-8 -*-
 @Time    : 4/22/2020 3:20 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : game_stats.py
 @Software: PyCharm
'''

class GameStats():
    '''跟踪游戏的统计信息'''

    def __init__(self,setting):
        '''初始化统计信息'''
        self.setting = setting
        self.high_score = 0
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        '''初始化在游戏中变化的统计信息'''
        self.ship_left = self.setting.ship_limit
        self.score = 0
        self.level = 1
