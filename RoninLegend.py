import pygame
from sys import exit
import os
from classes import player

os.system('cls')

# Init Pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Ronin Legend')
clock = pygame.time.Clock()

font = pygame.font.Font('font/Pixeltype.ttf', 50)
surface_title = font.render('Ronin Legend', False, (111,196,169))

# Environment
surface_cloud = pygame.image.load('assets/background/clouds.png').convert_alpha()
surface_house = pygame.image.load('assets/background/houses.png').convert_alpha()
surface_road = pygame.image.load('assets/background/road.png').convert_alpha()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  
    
    

    # Draw background
    screen.blit(surface_cloud, (0, 0))
    screen.blit(surface_house, (0, 100))
    screen.blit(surface_road, (0, 200))
    
    # Draw title
    screen.blit(surface_title, (920, 0))

    # Player
    samurai = pygame.sprite.GroupSingle()
    samurai.add(player.Player())
    samurai.draw(screen)

    pygame.display.update()
    clock.tick(60)