import pygame
from sys import exit
import os

class samurai(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()

        surface_player_idle = pygame.image.load('assets/player/idle.png').convert_alpha()
        surface_player_attack_1 = pygame.image.load('assets/player/attack_01.png').convert_alpha()
        surface_player_attack_2 = pygame.image.load('assets/player/attack_02.png').convert_alpha()
        
        # Required for sprites
        self.image = surface_player_idle               
        self.rect = self.image.get_rect(midbottom = (150,1000))

        # Attacks
        self.player_attack = [surface_player_attack_1,surface_player_attack_2]
        self.player_attack_index = 0

    def attack(self):
        # self.image = player_attack
        self.player_attack_index += 0.1
        if self.player_attack_index >= len(self.player_attack):
            self.player_attack_index = 0
        self.image = self.player_attack[int(self.player_attack_index)]