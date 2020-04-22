'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 7:29 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ship.py
 @Software: PyCharm
'''

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''管理飞船的大部分行为'''

    def __init__(self,screen,settings):
        '''飞船初始化'''
        super(Ship,self).__init__()
        self.screen = screen

        #加载飞机图像并获得外接矩阵
        self.image = pygame.image.load('ship.bmp')
        self.image = pygame.transform.scale(self.image,(50,100))
        self.rect  = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.setting = settings
        #飞机移动标志
        self.moving_right = False
        self.moving_left  = False
        self.moving_up = False
        self.moving_down = False

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom
        #飞船 存储成小数
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        self.y = float(self.rect.y)

    def center_ship(self):
        #飞船底部居中刷新
        self.center = self.screen_rect.centerx
        self.y = self.screen_rect.bottom - self.rect.height

    def blitme(self):
        '''在指定地点绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        #根据移动标志决定是否移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.setting.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.y = self.y