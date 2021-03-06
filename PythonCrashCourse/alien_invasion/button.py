'''
 # -*- coding: utf-8 -*-
 @Time    : 4/22/2020 4:20 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : button.py
 @Software: PyCharm
'''

import pygame.font

class Button():
    '''按钮类'''
    def __init__(self,setting,screen,msg):
        '''初始化按钮属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #设置按钮尺寸及其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('arial', 48)
        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #按钮标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        '''将msg渲染到按钮上，并居中'''
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''填充按钮，绘制文字'''
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)