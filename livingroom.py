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
        self.img_room = pygame.image.load("res/livingroom/living.png")
        self.img_safe = pygame.image.load("res/livingroom/close_safe.png")
        self.img_picture = pygame.image.load("res/livingroom/picture.png")
        self.img_fridge = pygame.image.load("res/livingroom/fridge_zoom.png")
        self.nopicture = False
        self.lock = False
        
    def click_event(self, x, y):
        if 744 < x < 803 and 386 < y < 456: 
            self.nopicture = not self.nopicture
            
    def draw(self):
        self.screen.blit(self.img_room, [0, 0])

        if self.nopicture_flag[3] == False:
            self.screen.bilt(self.img_picture, [744, 386])
        if self.lock == False:
            self.screen.bilt(self.img_safe, [738, 387])  