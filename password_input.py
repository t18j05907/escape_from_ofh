# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:00:19 2021

@author: haruo
"""

from room_base import Room_Base

class PassInput(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
        self.i = 0
        self.v = 0
        self.enter = False
        
        
    def click_event(self, x, y):
        """9を入力"""
        if 799 < x < 837 and 275 < y < 288:
            self.i = 9
            self.v = self.v * 10 + self.i
            
        """8を入力"""
        if 757 < x < 795 and 275 < y < 288:
            self.i = 8
            self.v = self.v * 10 + self.i
            
        """7を入力"""
        if 714 < x < 753 and 275 < y < 288:
            self.i = 7
            self.v = self.v * 10 + self.i
            
        """6を入力"""
        if 799 < x < 837 and 244 < y < 257:
            self.i = 6
            self.v = self.v * 10 + self.i
            
        """5を入力"""
        if 757 < x < 795 and 244 < y < 257:
            self.i = 5
            self.v = self.v * 10 + self.i
            
        """4を入力"""
        if 714 < x < 753 and 244 < y < 257:
            self.i = 4
            self.v = self.v * 10 + self.i
            
        """3を入力"""
        if 799 < x < 837 and 213 < y < 226:
            self.i = 3
            self.v = self.v * 10 + self.i
            
        """2を入力"""
        if 757 < x < 795 and 213 < y < 226:
            self.i = 2
            self.v = self.v * 10 + self.i
            
        """1を入力"""
        if 714 < x < 757 and 213 < y < 226:
            self.i = 1
            self.v = self.v * 10 + self.i
        """0を入力"""
        if 757 < x < 795 and 307 < y < 319:
            self.i = 0
            self.v = self.v * 10 + self.i
            
        """エンター(#)を入力"""
        if 799 < x < 837 and 307 < y < 319:
            self.enter = True
            
        """リセット(c)を入力"""
        if 714 < x < 753 and 307 < y < 319:
            self.v = 0
            
    def do(self):
        if self.enter == True:
            if self.v == 315:
                self.lock_flag[0] = True
                self.enter = False
            elif self.v > 99 and self.i != 315:
                self.v = 0
                self.enter = False