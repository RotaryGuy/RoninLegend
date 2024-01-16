import pygame
from sys import exit
import os

class Player(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()

        surface_player_idle = pygame.image.load('assets/player/idle.png').convert_alpha()
        
        # Required for sprites
        self.image = surface_player_idle
        self.rect = self.image.get_rect(midbottom = (80,200))