import pygame
import random
#from arkanoid import SZEROKOSC_EKRANU, WYSOKOSC_EKRANU
from setup import *
SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
 
class Platforma(pygame.sprite.Sprite):
    def __init__(self):
        super(Platforma, self).__init__()
        
        self.los = random.randint(1,3)

        if self.los == 1:               # Skin Randomizer
            self.obraz = pygame.image.load(f'{IMAGE_PATH}/pad.png')
        elif self.los == 2:
            self.obraz = pygame.image.load(f'{IMAGE_PATH}/pad1.png')
        else:
            self.obraz = pygame.image.load(f'{IMAGE_PATH}/pad2.png')
        
        self.zresetuj_pozycje()
    
    def zresetuj_pozycje(self):
        self.rect = pygame.Rect(SZEROKOSC_EKRANU/2-70, WYSOKOSC_EKRANU-100, 140, 30)
 
    def ruszaj_platforma(self, wartosc):
        predkosc = 10
        self.porusza_sie = wartosc
        self.rect.move_ip(wartosc*predkosc, 0)
        if self.rect.left < 0: self.rect.x = 0
        if self.rect.right > SZEROKOSC_EKRANU: self.rect.x = SZEROKOSC_EKRANU - 140
    
    def aktualizuj(self):
        self.porusza_sie = 0