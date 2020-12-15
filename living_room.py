# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:26:36 2020

@author: Ozaki
"""

import pygame
from room_base import Room_Base

class Living_Room(Room_Base):
    def __init__(self, screen, lock_flag):
        super().__init__(screen, lock_flag)
        self.img_room = pygame.image.load("res/living_room/room.png")
        self.img_tv = pygame.image.load("res/living_room/tv_box.png")
        self.img_sofa = pygame.image.load("res/living_room/zoom_sofa.png")
        self.zoom_tv = False
        self.zoom_sofa = False
        
    def click_event(self, x, y):
        if self.zoom_tv == False and self.zoom_sofa == False:
            if 592 < x < 630 and 305 < y < 356:
                self.zoom_tv = True
            elif 367 < x < 463 and 518 < y < 576:
                self.zoom_sofa = True
        elif self.zoom_tv == True:
            if x < 285 or y < 224 or 537 < x or 404 < y:
                self.zoom_tv = False
        elif self.zoom_sofa == True:
            if x < 254 or y < 372 or 579 < x or 584 < y:
                self.zoom_sofa = False
                
    
    def draw(self):
        self.screen.blit(self.img_room, [0, 0])
        
        if self.zoom_tv == True:
            self.screen.blit(self.img_tv, [285, 224])
        elif self.zoom_sofa == True:
            self.screen.blit(self.img_sofa, [254, 372])
            
