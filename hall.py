# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Hall(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
        self.img_room = pygame.image.load("res/hall/hall_sol.png")
        self.img_daruma = pygame.image.load("res/hall/item_daruma.png")
        self.img_karender = pygame.image.load("res/hall/item_karender.png")
        self.img_leftarrow = pygame.image.load("res/hall/left_arrow.png")
        self.daruma = False
        self.karender = False
        self.next_room = 0
        
    def click_event(self, x, y):
        #クリックするとダルマを獲得
        if 842 < x < 899 and 284 < y < 341:
            self.daruma = True
            self.item_get[0] = True
        #カレンダーをはがすことができる
        if 336 < x < 363 and 221 < y < 333:
            self.karender = True
            self.item_get[1] = True
        #livingroomに移動    
        if 387 < x < 431 and 298 < y < 452:
            self.next_room = 1
        #privateroomに移動    
        if 485 < x < 530 and 293 < y < 453:
            self.next_room = 2
            
    def draw(self):
        #hall表示
        self.screen.blit(self.img_room, [0, 0])
        #部屋移動の矢印を表示
        self.screen.blit(self.img_leftarrow, [387, 284])
        self.screen.blit(self.img_leftarrow, [485, 293])
        #ダルマを表示
        if self.daruma == False:
            self.screen.blit(self.img_daruma, [851,264])
        #カレンダーを表示    
        if self.karender == False:
            self.screen.blit(self.img_karender, [336,221])
            
    
    def next_state(self):
        next = self.next_room
        self.next_room = 0
        return next
                 