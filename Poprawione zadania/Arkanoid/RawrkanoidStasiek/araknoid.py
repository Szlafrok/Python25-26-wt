import pygame
from platforma import Platforma
from kulka import *
from BRYK import *

from setup import *




pygame.init()
pygame.font.init()

lives = 3
level = 0
font = pygame.font.SysFont('Consolas', 24)

bricks = pygame.sprite.Group() # bricks, nie 'brick' - nazewnictwo ma znaczenie!

LEVEL_0 = [
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def dodaj_bryksy():
    poziom = LEVEL_0

    for row in range(7): # były zamienione miejscami "row" i "column"
        for column in range(10):
            bryk_state =  poziom[row][column]
            if bryk_state != 0:
                bryk = brick(32 + column * 96, 32 + row * 48, bryk_state)
                bricks.add(bryk) # brakowało dodania bryka do grupy cegiełek

dodaj_bryksy()
                




SZEROKOSC_EKRANU =1024
WYSOKOSC_EKRANU = 800
# bryk = brick() Niepotrzebne ;P
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load(f'{IMAGE_PATH}/background.png')
 
platforma = Platforma()
kulka = Kulka() 

gra_dziala = True

while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            elif zdarzenie.key == pygame.K_a or zdarzenie.key == pygame.K_LEFT:
                platforma.ruszaj_platforma(-1)
            elif zdarzenie.key == pygame.K_d or zdarzenie.key == pygame.K_RIGHT:
                platforma.ruszaj_platforma(1)
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        platforma.ruszaj_platforma(-1)
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        platforma.ruszaj_platforma(1)




    kulka.aktualizuj(platforma, bricks) # było 'bryk' zamiast bricks
    platforma.aktualizuj()
    bricks.update() # było 'bryk' zamiast bricks


    if kulka.przegrana:
        lives - 1
        if lives <= 0:
            break
        kulka.zresetuj_pozycje
        platforma.zresetuj_pozycje




    ekran.blit(obraz_tla, (0,0))
 
    ekran.blit(platforma.obraz, platforma.rect)
    ekran.blit(kulka.obraz, kulka.rect)

    for bryk in bricks: # nie możesz użyć tej samej nazwy w dwóch miejscach w 'for'
        # + niepoprawne nazwy
        ekran.blit(bryk.image, bryk.rect)


    text = font.render(f'Życia: {lives}', False, (255, 255, 255))
    ekran.blit(text, (16, 16))

    pygame.display.flip()
    zegar.tick(30)
 
 
pygame.quit()