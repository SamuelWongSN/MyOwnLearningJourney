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
from time import sleep



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
def check_play_button(stats,play_button,mouse_x,mouse_y,bullets,aliens,ship,setting,screen,sb):
    '''单击按钮，开始游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if not stats.game_active and button_clicked:
        #重置游戏信息
        stats.reset_stats()
        setting.initialize_dynamic_setting()
        stats.game_active = True
        #清空外星人、子弹列表
        bullets.empty()
        aliens.empty()
        #重置记分牌
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ship()
        #创建新外星人，飞船
        create_fleet(setting,screen,ship,aliens)
        ship.center_ship()
        #隐藏光标
        pygame.mouse.set_visible(False)
def check_high_score(stats,sb):
    '''看看有没有诞生最高分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score
def check_events(setting,screen,ship,bullets,stats,play_button,aliens,sb):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,setting,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,bullets,aliens,ship,setting,screen,sb)

def fire_bullets(setting,screen,ship,bullets):
    if len(bullets) < setting.bullet_allowed:
        new_bullet = bullet.Bullet(setting, screen, ship)
        bullets.add(new_bullet)
def check_bullet_alien_collision(setting,screen,ship,aliens,bullets,stats,sb):
    # 检测是否有子弹消灭敌人
    # 如果是，同时删除子弹和敌人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += setting.alien_point*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    # 如果没敌人了，就删除子弹再搞一手敌人
    if len(aliens) == 0:
        bullets.empty()
        stats.level += 1
        sb.prep_level()
        setting.increase_speed()
        create_fleet(setting, screen, ship, aliens)
def update_bullets(setting,screen,ship,aliens,bullets,stats,sb):
    '''更新子弹位置，删除小时子弹'''
    #更新子弹位置
    bullets.update()
    #删除已消失子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #检查击杀且刷新敌人
    check_bullet_alien_collision(setting,screen,ship,aliens,bullets,stats,sb)

def get_number_alien_x(setting,alien_width):
    '''计算每行出多少个外星人'''
    available_space_x = setting.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x
def get_number_alien_y(setting,ship_height,alien_height):
    '''计算能够出多少行外星人'''
    available_space_y = setting.screen_height - 3 * alien_height-ship_height
    number_alien_y = int(available_space_y / (2 * alien_height))
    return number_alien_y

def create_alien(setting,screen,aliens,alien_number,row_number):
    '''创建一个外星人并放在当前行'''
    alien = Alien(setting,screen)
    alien.x = alien.rect.width + 2*alien.rect.width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)
def create_fleet(setting,screen,ship,aliens):
    '''创建外星人群'''
    #创建一个外星人并计算可容纳多少外星人
    alien = Alien(setting, screen)
    number_alien_x = get_number_alien_x(setting,alien.rect.width)
    number_alien_y = get_number_alien_y(setting,ship.rect.height,
                                                alien.rect.height)
    #创建第一行外星人
    for row_number in range(number_alien_y):
        for alien_number in range(number_alien_x):
            create_alien(setting, screen, aliens, alien_number,
                         row_number)

def check_fleet_edges(setting,aliens):
    '''到边缘时，降落且换方向'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(setting,aliens)
            break

def change_fleet_direction(setting,aliens):
    '''将外星人下移且换方向'''
    for alien in aliens.sprites():
        alien.rect.y += setting.fleet_drop_speed
    setting.fleet_direction *= -1

def update_aliens(setting,screen,ship,aliens,bullets,stats,sb):
    '''更新外星人所有位置'''
    check_fleet_edges(setting,aliens)
    for alien in aliens.sprites():
        alien.update()
    #检查有无外星人到达底部
    check_alien_bottom(setting,stats,screen,ship,aliens,bullets)
    #检测外星人有无和飞船碰上
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(setting,stats,aliens,bullets,screen,ship,sb)

def ship_hit(setting,stats,aliens,bullets,screen,ship,sb):
    '''飞船被撞了'''
    if stats.ship_left > 0:
        # 少一条命
        stats.ship_left -= 1
        sb.prep_ship()

        # 清空外星人、子弹列表
        aliens.empty()
        bullets.empty()
        # 创建新外星人和飞船
        create_fleet(setting, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_alien_bottom(setting,stats,screen,ship,aliens,bullets):
    '''检查是否有外星人到达底部'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞到一样处理
            ship_hit(setting,stats,aliens,bullets,screen,ship)
            break


def update_screen(settings,screen,ship,aliens,bullets,stats,play_button,sb):
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
    #显示记分牌
    sb.show_score()
    #如果游戏未开始或已结束，绘制按钮
    if not stats.game_active:
        play_button.draw_button()
    #最近绘制屏幕可见
    pygame.display.flip()
