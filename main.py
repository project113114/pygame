import pygame as pg
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((720,320))
running = True
background =(225,0,0)
pg.display.set_caption('game')
while running:
  screen.fill((background))
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
  pg.display.update()
pg.quit()

