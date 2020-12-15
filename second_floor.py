# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:53:29 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Second_Floor(Room_Base):
    def __init__(self, screen, lock_flag):
        super().__init__(screen, lock_flag)
        self.img_room = pygame.image.load("res/second_floor/room.png")
        self.zoom_tv = False
        
    def click_event(self, x, y):
        if 0 < x < 800:
            self.zoom_tv = True
            
    def draw(self):
        self.screen.blit(self.img_room, [0, 0])
