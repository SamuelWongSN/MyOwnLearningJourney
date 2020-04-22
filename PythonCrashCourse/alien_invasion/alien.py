'''
 # -*- coding: utf-8 -*-
 @Time    : 4/22/2020 12:51 AM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : alien.py
 @Software: PyCharm
'''

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示单个外星人的类'''
    def __init__(self,setting,screen):
        '''初始化外星人并设置位置'''
        super(Alien,self).__init__()
        self.screen = screen
        self.setting = setting

        #加载外星人图像，并设置rect
        self.image = pygame.image.load('alien.bmp')
        self.image = pygame.transform.scale(self.image, (100,50))
        self.rect  = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        '''撞墙了就返回True'''
        screem_rect = self.screen.get_rect()
        if self.rect.right > screem_rect.right:
            return True
        elif self.rect.left < 0:
            return True

    def update(self):
        '''向右/左移动外星人'''
        self.x += self.setting.alien_speed_factor * \
                  self.setting.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)
