# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020
@author: rufiy
"""

import pygame
from room_base import Room_Base
from password_input import PassInput

class Livingroom(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
        self.img_room = pygame.image.load("res/livingroom/living_complete.png")
        self.img_key = pygame.image.load("res/livingroom/key_in_safe.png")
        self.img_safe = pygame.image.load("res/livingroom/close_safe.png")
        self.img_picture = pygame.image.load("res/livingroom/picture2.png")
        self.img_fridge = pygame.image.load("res/livingroom/fridge_zoom2.png")
        self.img_pin = pygame.image.load("res/livingroom/pin2.png")
        self.img_leftarrow = pygame.image.load("res/livingroom/left_arrow.png")
        self.img_rightarrow = pygame.image.load("res/livingroom/right_arrow.png")
        self.picture = False
        self.zoom = False
        self.pin = False
        self.key = False
        self.next_room = 1
        self.passinput = PassInput(screen, lock_flag, item_get, item_use)
        
    def click_event(self, x, y):
        
        #金庫をクリック(閉まっている)するとキーパッドを拡大表示する
        if self.pin == False and self.picture == True:
            if 602 < x < 636 and 292 < y < 339:
                self.pin = True
                
        #キーパッド以外をクリックすることでキーパッドが消える
        elif self.pin == True and not (661 < x < 877 and 155 < y < 363):
            self.pin = False
            
        #パスワード入力 クラス呼び出し
        if self.pin == True:
            if 661 < x < 877 and 155 < y < 363:
                self.passinput.click_event(x, y)
                self.passinput.do()
                
        #金庫が開いたとき
        if self.lock_flag[0] == True:
            if 600 < x < 619 and 301 < y < 329:
                self.key = True
                self.item_get[2] = True
            
        #絵画をクリック
        if 597 < x < 642 and 244 < y < 335 and self.picture == False: 
            self.picture = True
            
        
        #冷蔵庫をクリックするとズーム、冷蔵庫以外をクリックでズームを解除
        if 400 < x < 478 and 289 < y < 472:
            self.zoom = True
        elif not (400 < x < 478 and 289 < y < 472):
            self.zoom = False
            
        #部屋移動
        #hallへ
        if 63 < x < 109 and 263 < y < 413:
            self.next_room = 0
        #privateroomへ
        if 960 < x < 1002 and 294 < y < 445:
            self.next_room = 2
        
            
    def draw(self):
        #livingroom表示
        self.screen.blit(self.img_room, [0, 0])
        
        #部屋移動の矢印表示
        self.screen.blit(self.img_leftarrow, [63, 263])
        self.screen.blit(self.img_rightarrow, [960, 294])
        
        #絵画を表示
        if self.picture == False:
            self.screen.blit(self.img_picture, [590, 292])
            
        #絵画がなくなると閉じた金庫を表示
        if self.picture == True and self.lock_flag[0] == False:
            self.screen.blit(self.img_safe, [586, 289])
            
        #金庫がクリックされるとキーパッド表示
        if self.pin == True and self.lock_flag[0] == False:
            self.screen.blit(self.img_pin, [658, 150])
            
        #金庫が開いた場合
        if self.lock_flag[0] == True and self.key == False:
             self.screen.blit(self.img_key, [593, 301])
            
        #冷蔵庫
        if self.zoom == True:
            self.screen.blit(self.img_fridge, [163, 154])
            
            
    def next_state(self):
        next = self.next_room
        self.next_room = 1
        return next