# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:01:09 2023

@author: Lanis
"""

import pygame
from Player import Player
from Bullet import Bullet
import random

# 定義屏幕寬高
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)

white = (255, 255, 255)
gray = (200, 200, 200)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
pygame.init()

# 背景相關
background_offset_x = 400#random.randint(-2000, 2000)
background_offset_y = 300#random.randint(-2000, 2000)
grid_size = 50  # 網格大小

# 子彈相關
bullet_radius = 8
bullets_left_click = []  # 存儲 (bullet_x, bullet_y, dx, dy)
bullets_click_site = [] 
target_x, target_y = pygame.mouse.get_pos()

# 創建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

# 創建精靈群組
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 創建玩家
player = Player(background_offset_x,background_offset_y,all_sprites)
all_sprites.add(player)

running = True
game_over = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 按下滑鼠左鍵發射子彈
            if not game_over:
                
                keys = pygame.key.get_pressed()
                mouse_buttons = pygame.mouse.get_pressed()
                
                both_button_pressed = mouse_buttons[2]  
                left_button_pressed = mouse_buttons[0]   # 左鍵的狀態

                
                bullet_x1, bullet_y1 = window_size[0] // 2, window_size[1] // 2

                target_x, target_y = pygame.mouse.get_pos()
                dx1 = target_x - bullet_x1
                dy1 = target_y - bullet_y1
                magnitude = (dx1 ** 2 + dy1 ** 2) ** 0.5
                dx1 /= magnitude
                dy1 /= magnitude
                # bullets_click_site.append((background_offset_x, background_offset_y))
                # bullets_left_click.append((bullet_x1, bullet_y1, dx1 * 15, dy1 * 15))
                
                if both_button_pressed:
                    weapon = 3
                    player.shoot(bullets,dx1,dy1, 1000,weapon)
                elif left_button_pressed:
                    weapon = 0
                    player.shoot(bullets,dx1,dy1, 1000,weapon)
                    
       
   
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # 按下滑鼠右鍵發射子彈
            if not game_over:
                
                keys = pygame.key.get_pressed()
                mouse_buttons = pygame.mouse.get_pressed()
                
                left_button_pressed = mouse_buttons[0]
             
                bullet_x1, bullet_y1 = window_size[0] // 2, window_size[1] // 2

                target_x, target_y = pygame.mouse.get_pos()
                dx1 = target_x - bullet_x1
                dy1 = target_y - bullet_y1
                magnitude = (dx1 ** 2 + dy1 ** 2) ** 0.5
                dx1 /= magnitude
                dy1 /= magnitude
                # bullets_click_site.append((background_offset_x, background_offset_y))
                # bullets_left_click.append((bullet_x1, bullet_y1, dx1 * 15, dy1 * 15))
                if left_button_pressed:
                    weapon = 4
                    player.shoot(bullets,dx1,dy1, 1000,weapon)
                else:
                    weapon = 2
                    player.shoot(bullets,dx1,dy1, 1000,weapon)
                   

                    


                
                

        
    

    # 繪製背景
    screen.fill((0, 0, 0))
    # 更新背景偏移量
    background_offset_x = player.background_offset_x
    background_offset_y = player.background_offset_y
    
    # 繪製背景網格
    for x in range(background_offset_x % grid_size, window_size[0], grid_size):
        pygame.draw.line(screen, blue, (x, 0), (x, window_size[1]))
    for y in range(background_offset_y % grid_size, window_size[1], grid_size):
        pygame.draw.line(screen, blue, (0, y), (window_size[0], y))

    # 繪製玩家圓形（在畫面中心）
    # pygame.draw.circle(window, blue, (window_size[0] // 2, window_size[1] // 2), 25)

    # 繪製生命次數
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f"Lives: {player.health}", True, white)
    location_text = font.render(f"location: {player.background_offset_x, player.background_offset_y}", True, white)
    # Mouse_text = font.render(f"Mouse: {target_x, target_y}", True, white)
    screen.blit(lives_text, (10, 10))
    screen.blit(location_text, (10, 40))
    # window.blit(Mouse_text, (10, 70))
    
    # # 更新窗口偏移量，以限制在指定的范围内
    # background_offset_x = max(-3000, min(3000, background_offset_x))
    # background_offset_y = max(-3000, min(3000, background_offset_y))

    
# 繪製子彈
    for bullet in bullets:
        bullet.background_offset_x = player.background_offset_x
        bullet.background_offset_y = player.background_offset_y
        screen.blit(bullet.image, bullet.rect)
        
    # 繪製所有精靈
    all_sprites.update()
    all_sprites.draw(screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
