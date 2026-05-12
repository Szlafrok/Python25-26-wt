import random
import pygame 
from setup import *
SZEROKOSC = 1024
WYSOKOSC = 800

vec = pygame.math.Vector2

class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super(Kulka, self).__init__()
        self.obraz = pygame.image.load(f'{IMAGE_PATH}/ball.png')  
        self.r = 16
        self.przegrana = False
        self.zresetuj_pozycje()


    def zresetuj_pozycje(self):                                     
        self.wspolrzedne = vec(SZEROKOSC/2, WYSOKOSC-140)
        self.rect = self.obraz.get_rect(center=self.wspolrzedne)
        self.wektor = vec(0, -10)
        self.kat = random.randrange(-30, 30)
        self.wektor.rotate_ip(self.kat)
        self.przegrana = False


    def aktualizuj(self, platforma, bryks):

        self.wspolrzedne += self.wektor
        self.rect.center = self.wspolrzedne
        self.sprawdz_kolizje(platforma, bryks)


    def sprawdz_kolizje(self, platforma, bryks):    
        if self.rect.x <= 0:
            self.wektor.x *= -1
        if self.rect.right >= SZEROKOSC:
            self.wektor.x *= -1         # hmmmm...
        if self.rect.top <= 0:
            self.wektor.y *= -1
        if self.rect.bottom >= WYSOKOSC:
            self.przegrana = True

        if self.rect.colliderect(platforma.rect):
            self.wektor.y *= -1
            self.wektor.x += platforma.porusza_sie * 5
            if self.wektor.x < -10: self.wektor.x = -10
            if self.wektor.x > 10: self.wektor.x = 10 # literówka
        
        for bryk in bryks:
            if self.bryk_kolizja(bryk): # jeden argument za dużo
                bryk.hit()
                break
    

    


    def bryk_kolizja(self, bryk):
        # Jeśli korzystasz z nazwy 'rect', to korzystaj z nazwy 'rect' a nie 'pozycja' ;)
        dystans_x = abs(self.rect.centerx - bryk.rect.centerx) - bryk.rect.width / 2
        dystans_y = abs(self.rect.centery - bryk.rect.centery) - bryk.rect.height / 2
    
        if dystans_x < self.r and dystans_y < self.r:
            if dystans_y > dystans_x:
                self.wektor.y *= -1 # literówka
            else:
                self.wektor.x *= -1
            return True
        return False