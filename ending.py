# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:23:51 2020

@author: Ozaki
"""

import pygame
from room_base import Room_Base

class Ending(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        self.screen = screen
        self.lock_flag = lock_flag
        self.item_get = item_get
        self.item_use = item_use
        self.img_escape = pygame.image.load("res/privateroom/escape_pr.png")
        self.next_room = 3
    
    
    def pos_event(self, x, y):
        pass
    
    
    def click_event(self, x, y):
        pass
    
    
    def key_event(self, key):
        pass
    
    
    def next_state(self):
        return 3
    
    
    def do(self):
        pass
    
    
    def draw(self):
        if self.lock_flag[1] == True:
           self.screen.blit(self.img_escape, [0, 0])
