#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : macgyver.py, classes.py, constantes.py, macgyverlaby + images
"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
window = pygame.display.set_mode((corner_window, corner_window))

#BOUCLE PRINCIPALE
carryon = 1
while carryon:  
  #Chargement et affichage de l'écran d'accueil
  home = pygame.image.load(image_home).convert()
  window.blit(home, (0,0))

  #Rafraichissement
  pygame.display.flip()

  #On remet ces variables à 1 à chaque tour de boucle
  carryon_game = 1
  carryon_home = 1

  #BOUCLE D'ACCUEIL
  while carryon_home:
  
    #Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)
  
    for event in pygame.event.get():
    
      #Si l'utilisateur quitte, on met les variables 
      #de boucle à 0 pour n'en parcourir aucune et fermer
      if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
        carryon_home = 0
        carryon_game = 0
        carryon = 0
        #Variable de choix du niveau
        choice = 0
        
      elif event.type == KEYDOWN:       
        #Lancement du niveau 1
        if event.key == K_F1:
          carryon_home = 0 #On quitte l'accueil
          choice = 'macgyverlaby'    #On définit le niveau à charger
      
    

  #on vérifie que le joueur a bien fait un choix de niveau
  #pour ne pas charger s'il quitte
  if choice != 0:
    #Chargement du fond
    empty = pygame.image.load(image_empty).convert()

    #Génération d'un niveau à partir d'un fichier
    level = Level(choice)
    level.generate()
    level.display(window)

    

        
  #BOUCLE DE JEU
  while carryon_game:
  
    #Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)
  
    
          
              
      
    #Affichages aux nouvelles positions
    window.blit(empty, (0,0))
    level.display(window)
    
    pygame.display.flip()
