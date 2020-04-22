'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 11:36 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : test.py
 @Software: PyCharm
'''

import pygame
import sys

def run():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Alien Invasion')
    print('no')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print('yes')


run()