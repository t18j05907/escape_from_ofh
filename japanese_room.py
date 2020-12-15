# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:51:44 2020

@author: Ozaki
"""

import pygame
from room_base import Room_Base

class Japanese_Room(Room_Base):
    def __init__(self, screen, lock_flag):
        super().__init__(screen, lock_flag)
        self.img_room = pygame.image.load("res/japanese_room/room.png")
        self.img_scroll = pygame.image.load("res/japanese_room/hanging_scroll.png")
        self.img_safe = pygame.image.load("res/japanese_room/close_safe.png")
        self.upscroll = False
        
    def click_event(self, x, y):
        if 243 < x < 388 and 194 < y < 324:
            self.upscroll = not self.upscroll
            
    def draw(self):
        self.screen.blit(self.img_room, [0, 0])
        
        if self.lock_flag[3] == False:
            self.screen.blit(self.img_safe, [455, 216])
        if self.upscroll == False:
            self.screen.blit(self.img_scroll, [243, 194])
