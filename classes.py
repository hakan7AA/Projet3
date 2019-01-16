"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *

class Level:
  """Classe permettant de créer un niveau"""
  def __init__(self, file):
    self.file = file
    self.structure = 0
  
  
  def generate(self):
    """Méthode permettant de générer le niveau en fonction du fichier.
    On crée une liste générale, contenant une liste par ligne à afficher""" 
    #On ouvre le fichier
    with open(self.file, "r") as file:
      structure_level = []
      #On parcourt les lignes du fichier
      for line in file:
        line_level = []
        #On parcourt les sprites (lettres) contenus dans le fichier
        for sprite in line:
          #On ignore les "\n" de fin de ligne
          if sprite != '\n':
            #On ajoute le sprite à la liste de la ligne
            line_level.append(sprite)
        #On ajoute la ligne à la liste du niveau
        structure_level.append(line_level)
      #On sauvegarde cette structure
      self.structure = structure_level
  
  
  def display(self, window):
    """Méthode permettant d'afficher le niveau en fonction 
    de la liste de structure renvoyée par generer()"""
    #Chargement des images (seule celle d'arrivée contient de la transparence)
    wall = pygame.image.load(image_wall).convert()
    start = pygame.image.load(image_start).convert()
    arrive = pygame.image.load(image_arrive).convert()
    
    #On parcourt la liste du niveau
    num_line = 0
    for line in self.structure:
      #On parcourt les listes de lignes
      num_box = 0
      for sprite in line:
        #On calcule la position réelle en pixels
        x = num_box * size_sprite
        y = num_line * size_sprite
        if sprite == 'm':      #m = Mur
          window.blit(wall, (x,y))
        elif sprite == 'd':      #d = Départ
          window.blit(start, (x,y))
        elif sprite == 'a':      #a = Arrivée
          window.blit(arrive, (x,y))
        num_box += 1
      num_line += 1