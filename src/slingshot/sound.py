import os.path as path
import pygame

# Set where the sound files are stored
data_dir = path.join("src", "slingshot", "data")

pygame.mixer.init()

# Music
music_track = pygame.mixer.Sound(path.join(data_dir, "Rising.ogg"))

# Interface sounds
test_sound = pygame.mixer.Sound(path.join(data_dir,"confirm.ogg"))
menu_item_hover = pygame.mixer.Sound(path.join(data_dir, "menu_item_hover.wav"))
menu_item_select = pygame.mixer.Sound(path.join(data_dir, "menu_item_select.wav"))

# Game SFX
player_fire = pygame.mixer.Sound(path.join(data_dir, "player_fire_3.wav"))
player_explosion = pygame.mixer.Sound(path.join(data_dir, "explosion_2.wav"))
planet_strike = pygame.mixer.Sound(path.join(data_dir, "explosion_1.wav"))
