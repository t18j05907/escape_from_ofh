# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Livingroom(Room_Base):
    def __init__(self, screen, lock_flag):
        super().__init__(screen, lock_flag)
        self.img_room = pygame.image.load("res/livingroom/living_complete.png")
        
    def click_event(self, x, y):
        pass
            
    def draw(self):
        self.screen.blit(self.img_room, [0, 0])
