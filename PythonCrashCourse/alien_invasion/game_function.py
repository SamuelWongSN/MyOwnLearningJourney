'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 8:54 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : game_function.py
 @Software: PyCharm
'''

import sys
import pygame

import bullet
from alien import Alien

def fire_bullets(setting,screen,ship,bullets):
    if len(bullets) < setting.bullet_allowed:
        new_bullet = bullet.Bullet(setting, screen, ship)
        bullets.add(new_bullet)

def check_keydown_event(event,setting,screen,ship,bullets):
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(setting,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_event(event,ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
def check_events(setting,screen,ship,bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,setting,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)

def update_bullets(bullets):
    '''更新子弹位置，删除小时子弹'''
    #更新子弹位置
    bullets.update()
    #删除已消失子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(setting,screen,aliens):
    '''创建外星人群'''
    #创建一个外星人，并计算一行可容纳多少外星人
    #外星人间距为外星人宽度
    alien = Alien(setting,screen)
    alien_width = alien.rect.width
    available_space_x = setting.screen_width - 2*alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    #创建第一行外星人
    for alien_number in range(number_alien_x):
        alien = Alien(setting,screen)
        alien.rect.x = alien_width + 2 *alien_width *alien_number
        aliens.add(alien)


def update_screen(settings,screen,ship,aliens,bullets):
    '''更新屏幕图像、切换到新屏幕'''
    #每次更新重绘屏幕
    screen.fill(settings.bg_color)
    #绘制飞船
    ship.blitme()
    #绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    #绘制外星人
    aliens.draw(screen)
    #最近绘制屏幕可见
    pygame.display.flip()
