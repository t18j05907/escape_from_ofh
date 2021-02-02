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
        self.img_rightarrow = pygame.image.load("res/privateroom/right_arrow.png")
        self.img_underarrow = pygame.image.load("res/privateroom/under_arrow.png")
        self.img_hint_shelf = pygame.image.load("res/privateroom/hint_shelf.png")
        self.img_gameover = pygame.image.load("res/privateroom/game_over.png")
        self.shelf = False
        self.hint_shelf = False
        self.wallpaper = False
        self.speaker = False
        self.gameover = False
        self.next_room = 2
        
        
    def click_event(self, x, y):
        #ロックされた場所をクリック
        if 864 < x < 936 and 206 < y < 285:
            #スピーカーを持っていたら
            if self.item_use[0] == False and self.item_use[1] == False and self.item_use[2] == False and self.item_use[3] == True:
                #棚をあける
                self.lock_flag[2] == True
                #使用したアイテムを消す
                self.item_get[3] = False
                self.item_use[3] = False
                self.shelf = True
                
        #ロックされた場所(脱出口)をクリック
        if 44 < x < 290 and 249 < y < 636:
            #鍵を持っていたら
            if self.item_use[0] == False and self.item_use[1] == False and self.item_use[2] == True and self.item_use[3] == False:
                #扉が開く
                self.lock_flag[1] = True
                #使用したアイテムを消す
                self.item_get[2] = False
                self.item_use[2] = False
                self.next_room = 3
        
        #壁紙をクリックすると剝がれる
        if 547 < x < 621 and 341 < y < 422:
            self.wallpaper = True
        
        #スピーカーを取得
        if 375 < x < 428 and 563 < y < 644:
            self.speaker = True
            self.item_get[3] = True
        
        #電気をクリックすると暗くなってゲームオーバー
        if 547 < x < 680 and 130 < y < 189:
            self.item_get[0] = False
            self.item_get[1] = False
            self.item_get[2] = False
            self.item_get[3] = False
            self.gameover = True
            
        #机の上にあるヒントをクリックすると拡大表示
        if 662 < x < 677 and 571 < y < 580:
            self.hint_shelf = True
            
        elif self.hint_shelf == True and not (662 < x < 677 and 571 < y < 580):
            self.hint_shelf = False
        
        #部屋移動
        #hallへ
        if 971 < x < 1017 and 337 < y < 491 and self.gameover == False:
            self.next_room = 0
        #livingroomへ    
        if 448 < x < 607 and 670 < y < 718 and self.gameover == False:
            self.next_room = 1
            
            
    def draw(self):
        #privateroomを表示
        self.screen.blit(self.img_room, [0, 0])
        #部屋移動の矢印を表示
        self.screen.blit(self.img_rightarrow, [971, 377])
        self.screen.blit(self.img_underarrow, [448, 670])
        
        #棚の扉を表示
        if self.shelf == False:
            self.screen.blit(self.img_shelf, [864,206])
        #壁紙を表示    
        if self.wallpaper == False:
            self.screen.blit(self.img_wallpaper, [547,341])
        #スピーカーを表示    
        if self.speaker == False:
            self.screen.blit(self.img_speaker, [375,563])
        #ヒントを拡大表示
        if self.hint_shelf == True:
            self.screen.blit(self.img_hint_shelf, [408,411])
        #ゲームオーバーの画像を表示    
        if self.gameover == True:
            self.screen.blit(self.img_gameover, [0, 0])
            
            
    def next_state(self):
        next = self.next_room
        self.next_room = 2
        return next