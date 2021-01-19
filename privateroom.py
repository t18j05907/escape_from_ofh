# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Privateroom(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
        self.img_room = pygame.image.load("res/privateroom/perfect_solution_pr.png")
        self.img_shelf = pygame.image.load("res/privateroom/shelf.png")
        self.img_wallpaper = pygame.image.load("res/privateroom/wallpaper.png")
        self.img_speaker = pygame.image.load("res/privateroom/speaker.png")
        self.shelf = False
        self.wallpaper = False
        self.speaker = False
        
        
    def click_event(self, x, y):
        if 1079 < x < 1171 and 279 < y < 373:
            self.shelf = not self.shelf
            
        if 683 < x < 773 and 455 < y < 565:
            self.wallpaper = not self.wallpaper
            
        if 471 < x < 523 and 751 < y < 857:
            self.speaker = not self.speaker
            
            
    def draw(self):
        self.screen.blit(self.img_room, [0, 0])
        
        if self.shelf == False:
            self.screen.blit(self.img_shelf, [1079,279])
            
        if self.wallpaper == False:
            self.screen.blit(self.img_wallpaper, [683,455])
            
        if self.speaker == False:
            self.screen.blit(self.img_speaker, [471,751])
