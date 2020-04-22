'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 6:31 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : alien_invasion.py
 @Software: PyCharm
'''

'''
 @思侬的第一个游戏 alien invasion
 @version 1.0
'''


import pygame
from pygame.sprite import Group

import settings
import game_function
import ship
import game_stats
import button
import scoreboard

def run_game():
    #初始化游戏并新建一个屏幕对象
    pygame.init()
    #初始化设置
    setting = settings.Settings()
    #初始化屏幕
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    #创建统计信息、记分牌
    stats = game_stats.GameStats(setting)
    sb = scoreboard.ScoreBoard(setting,screen,stats)
    #创建开始按钮
    play_button = button.Button(setting,screen,'Play')
    #创建一艘飞船、一个子弹编组、一个外星人编组
    ai_ship = ship.Ship(screen,setting)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    game_function.create_fleet(setting,screen,ai_ship,aliens)

    #开始游戏循环
    while True:

        #监视键盘和鼠标事件
        game_function.check_events(setting,screen,ai_ship,bullets,stats,play_button,aliens,sb)
        #有命的情况下刷新
        if stats.game_active:
            ai_ship.update()
            game_function.update_bullets(setting, screen, ai_ship, aliens, bullets,stats,sb)
            game_function.update_aliens(setting, screen, ai_ship, aliens,bullets,stats,sb)
        #每次循环重新绘制屏幕
        game_function.update_screen(setting,screen,ai_ship,aliens,bullets,stats,play_button,sb)

run_game()