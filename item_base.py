# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:18:34 2020

@author: rufiy
"""

import pygame

class Item_Base:
    def __init__(self, screen, item_get, item_use, w, h):
        self.img_item = [pygame.image.load("res/common/item_daruma.png"),
                         pygame.image.load("res/common/item_karender.png"),
                         pygame.image.load("res/common/item_key.png"),
                         pygame.image.load("res/common/item_speaker.png")]
        self.screen = screen
        self.item_get = item_get
        self.item_use = item_use
        self.w = w
        self.h = h
        self.cnt = 0
        self.target_face = 0
        self.img_target = pygame.image.load("res/common/target.png")
        """ 36 x 36 に縮小 """
        for i, item in enumerate(self.img_item):
            self.img_item[i] = pygame.transform.scale(item, (36, 36))

    
    def click_event(self, id):
        idx_list = self.true_index(self.item_get)
        if id < len(idx_list):
            self.item_use[idx_list[id]] = not self.item_use[idx_list[id]]
    
    
    def do(self):
        self.cnt = (self.cnt + 1) % 24
        self.target_face = int(self.cnt / 3)
        

    def draw(self):
        for i, id in enumerate(self.true_index(self.item_get)):
            self.screen.blit(self.img_item[id], [self.w+22, 22 + 64*i])
            if self.item_use[id] == True:
                self.screen.blit(self.img_target, [self.w+8, 8 + 64*i],
                                 area=[64*self.target_face, 0, 64, 64])
    
    
    def true_index(self, lst):
        return [i for i, x in enumerate(lst) if x == True]