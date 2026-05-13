# Importar librerías
import pygame
import sys
import math

# Inicializar pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mini Parque Pacman")

# Colores
negro = (0,0,0)
amarillo = (255,255,0)
rojo = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
blanco = (255,255,255)
gris = (120,120,120)
naranja = (255, 165, 0)

# variables auxiliares
PI = math.pi

# Tiempo
clock = pygame.time.Clock()

# Fuente
fuente = pygame.font.SysFont("Arial", 25)

# Bucle principal
while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Fondo
    ventana.fill(negro)

    # Texto
    texto = fuente.render("PARQUE PACMAN", True, blanco)
    ventana.blit(texto, (90,20))

    texto = fuente.render("DYANERIS SÁNCHEZ", True, gris)
    ventana.blit(texto, (100,50))

    # Suelo
    pygame.draw.line(ventana, verde, (0,350), (400,350), 8)

    # Carpa (poligono)
    puntos = [(120,350), (200,220), (280,350)]
    pygame.draw.polygon(ventana, rojo, puntos)

    # Puerta (rectangulo)
    pygame.draw.rect(ventana, azul, (180,300,40,50))

    # Rueda (circulo)
    pygame.draw.circle(ventana, blanco, (320,250), 50, 3)

    # Lineas rueda
    pygame.draw.line(ventana, blanco, (320,200), (320,300), 2)
    pygame.draw.line(ventana, blanco, (270,250), (370,250), 2)

    # Base rueda
    pygame.draw.line(ventana, gris, (300,300), (320,350), 3)
    pygame.draw.line(ventana, gris, (340,300), (320,350), 3)

    # Sol (circulo)
    pygame.draw.circle(ventana, amarillo, (60,60), 30)

    # Arco
    pygame.draw.arc(ventana, naranja, (20,20,80,80), 0, math.pi, 3)

    # Pacman
    pygame.draw.circle(ventana, amarillo, (70,320), 25)

    boca = [(70,320), (95,305), (95,335)]
    pygame.draw.polygon(ventana, negro, boca)

    # Ojo
    pygame.draw.circle(ventana, negro, (70,310), 4)


    # actualizar visualización de la ventana
    pygame.display.flip()

