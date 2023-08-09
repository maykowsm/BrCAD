import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Parametros de inicialização
width = 1080    
height = 700
fps = 60


#Consfigurações de inicialização
window_surface= pygame.display.set_mode((width, height), flags= pygame.NOFRAME )
pygame.display.set_caption("Exemplo Pygame com Botões")

clk = pygame.time.Clock()

while True:
   
   clk.tick(fps)

