# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

import pygame
import sys
import math

# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# establecer titulo de la ventana
pygame.display.set_caption("Ciudad de hierro")

#definición colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (120, 120, 120)
GRIS_OSCURO = (60, 60, 60)
AZUL = (80, 180, 255)
VERDE = (0, 200, 100)
ROJO = (220, 50, 50)
AMARILLO = (255, 255, 0)
MORADO = (180, 0, 255)
NARANJA = (255, 140, 0)
