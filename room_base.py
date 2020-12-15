# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:23:51 2020

@author: Ozaki
"""

class Room_Base:
    def __init__(self, screen, lock_flag):
        self.screen = screen
        self.lock_flag = lock_flag
    
    
    def pos_event(self, x, y):
        pass
    
    
    def click_event(self, x, y):
        pass
    
    
    def next_state(self):
        return 0
    
    
    def do(self):
        pass
    
    
    def draw(self):
        pass
