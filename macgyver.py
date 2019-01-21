import pygame 
from pygame.locals import *
from constantes import *
from classes import *

pygame.init()

window = pygame.display.set_mode((corner_window, corner_window))

carryon = 1
while carryon:
  home = pygame.image.load(image_home).convert()
  window.blit(home, (0,0))

  pygame.display.flip()

  carryon_home = 1
  carryon_game = 1
  while carryon_home:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():

      if event.type == KEYDOWN:
        if event.key == K_F1:
          carryon_home = 0
          choice = 'macgyverlaby'

  if choice != 0:
    empty = pygame.image.load(image_empty).convert()

    level = Level(choice)
    level.generate()
    level.display(window)

    mac = Character(macgyver, level)


  while carryon_game:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_RIGHT:
          mac.move('right')
        elif event.key == K_LEFT:
          mac.move('left')
        elif event.key == K_UP:
          mac.move('up')
        elif event.key == K_DOWN:
          mac.move('down')    


    window.blit(empty, (0,0))
    level.display(window)
    window.blit(mac.macgyver, (mac.x, mac.y))

    pygame.display.flip()

    if level.structure[mac.box_y][mac.box_x] == 'a':
      carryon_game = 0



