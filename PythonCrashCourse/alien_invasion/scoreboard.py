'''
 # -*- coding: utf-8 -*-
 @Time    : 4/22/2020 5:28 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : scoreboard.py
 @Software: PyCharm
'''

import  pygame.font
from ship import Ship
from pygame.sprite import Group

class ScoreBoard():
    '''记分牌，显示积分，等级'''
    def __init__(self,setting,screen,stats):
        '''初始化显示得分涉及的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting = setting
        self.stats = stats

        #显示得分时的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        #准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        '''将得分转为一幅渲染的图像'''
        rounded_score = int(round(self.stats.score,-1))
        score_str = 'Score: ' + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,
                            True,self.text_color,
                                self.setting.bg_color)
        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def prep_high_score(self):
        rounded_high_score = int(round(self.stats.high_score,-1))
        high_score_str ='High Score: ' + "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str,
                                    True,self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        self.level_image = self.font.render('Level' + str(self.stats.level),True,self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right -20
        self.level_rect.top = self.score_rect.bottom +10

    def prep_ship(self):
        '''显示还剩下多少艘飞船'''
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.screen,self.setting)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        '''显示分数图像'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)