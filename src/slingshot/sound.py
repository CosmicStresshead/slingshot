import os.path as path
import pygame

# Set where the sound files are stored
data_dir = path.join("src", "slingshot", "data")

pygame.mixer.init()
pygame.mixer.music.load(path.join(data_dir, "Rising.ogg"))

# Music
music_track = pygame.mixer.Sound(path.join(data_dir, "Rising.ogg"))

# Interface sounds
test_sound = pygame.mixer.Sound(path.join(data_dir,"confirm.ogg"))
menu_item_hover = pygame.mixer.Sound(path.join(data_dir, "blip.wav"))
menu_item_select = pygame.mixer.Sound(path.join(data_dir, "menu_item_select_2.wav"))

# Game SFX
player_fire = pygame.mixer.Sound(path.join(data_dir, "player_fire_2.wav"))
player_fire.set_volume(0.5)
player_explosion = pygame.mixer.Sound(path.join(data_dir, "explosion_2.wav"))
planet_strike = pygame.mixer.Sound(path.join(data_dir, "explosion_1.wav"))
