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
        self.daruma = False
        self.karender = False
        
    def click_event(self, x, y):
        if 1075 < x < 1142 and 399 < y < 484:
            self.daruma = not self.daruma
        
        if 422 < x < 450 and 315 < y < 470:
            self.karender = not self.karender
            
    def draw(self):
        self.screen.blit(self.img_room, [0, 0])

        if self.daruma == False:
            self.screen.blit(self.img_daruma, [1075,399])
            
        if self.karender == False:
            self.screen.blit(self.img_karender, [422,315]) 
            
            
    def next_state(self):
        return 0