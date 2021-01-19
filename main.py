# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:59:15 2020

@author: Ozaki
"""

import pygame
import sys
from hall import Hall
from livingroom import Livingroom
from privateroom import Privateroom
from item_base import Item_Base


def main():
    width = 1280
    height = 1024
    pygame.init()
    screen = pygame.display.set_mode((width + 80, height))
    clock = pygame.time.Clock()
    
    lock_flag = [False, False, False, False, False, False]
    
    item_get = [False, False, False, False]
    item_use = [False, False, False, False]
    item_ctrl = Item_Base(screen, item_get, item_use, width, height)
    
    room_state = 0
    room_ctrl = [Hall(screen, lock_flag, item_get, item_use),
                 Livingroom(screen, lock_flag, item_get, item_use),
                 Privateroom(screen, lock_flag, item_get, item_use)]
    
    while True:

        """ マウスカーソル位置 """
        x, y = pygame.mouse.get_pos()
        room_ctrl[room_state].pos_event(x, y)
        
        """ クリックイベント，キーイベント """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if x < width:
                    room_ctrl[room_state].click_event(x, y)
                else:
                    item_ctrl.click_event(int(y / 64))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    room_state = (room_state - 1) % -3
                elif event.key == pygame.K_RIGHT:
                    room_state = (room_state + 1) % 3
                elif event.key == pygame.K_a:
                    lock_flag[0] = not lock_flag[0]
                elif event.key == pygame.K_b:
                    lock_flag[1] = not lock_flag[1]
                elif event.key == pygame.K_c:
                    lock_flag[2] = not lock_flag[2]
                elif event.key == pygame.K_d:
                    lock_flag[3] = not lock_flag[3]
                elif event.key == pygame.K_e:
                    lock_flag[4] = not lock_flag[4]
                elif event.key == pygame.K_f:
                    lock_flag[5] = not lock_flag[5]
                elif event.key == pygame.K_0:
                    item_get[0] = not item_get[0]
                    item_use[0] = False
                elif event.key == pygame.K_1:
                    item_get[1] = not item_get[1]
                    item_use[1] = False
                elif event.key == pygame.K_2:
                    item_get[2] = not item_get[2]
                    item_use[2] = False
                elif event.key == pygame.K_3:
                    item_get[3] = not item_get[3]
                    item_use[3] = False

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        """ 処理 """
        room_ctrl[room_state].do()
        item_ctrl.do()
        
        """ 描画 """
        screen.fill((0, 0, 0))
        room_ctrl[room_state].draw()
        item_ctrl.draw()
        pygame.display.update()
        
        clock.tick(30)
        
        
if __name__ == '__main__':
    main()
