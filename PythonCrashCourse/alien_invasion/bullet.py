'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 11:02 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : bullet.py
 @Software: PyCharm
'''


import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''子弹类'''
    def __init__(self,setting,screen,ship):
        '''在飞船所处位置创建子弹'''
        super(Bullet,self).__init__()
        self.screen = screen

        #在（0，0）处创建一个子弹，再移动
        self.rect = pygame.Rect(0,0,setting.bullet_width,setting.bullet_heigh)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #用小数储存位置
        self.y = float(self.rect.y)

        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        '''更新子弹的位置'''
        #子弹向上移动
        self.y -= self.speed_factor
        #更新子弹位置
        self.rect.y = self.y


    def draw_bullet(self):
        '''绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)