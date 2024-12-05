import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
ANCHO = 800
ALTO = 600
VENTANA = (ANCHO,ALTO)
FPS = 60

TAMAÑO_PREGUNTA = (350,150)
TAMAÑO_RESPUESTA = (260,60)
TAMAÑO_BOTON = (250,60)
CUADRO_TEXTO = (350,90)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (60,60)
TAMAÑO_BOTON_CONFIG = (700,60)
TAMAÑO_OPCION = (300,150)
TAMAÑO_BOTON_OPCION = (20,20)
TAMAÑO_BOTON_RANKINGS = (500,55)

FUENTE_PPAL = pygame.font.SysFont('Impact',60)
FUENTE_50 = pygame.font.SysFont("Arial Narrow",50)
FUENTE_40 = pygame.font.SysFont("Arial Narrow",40)
FUENTE_32 = pygame.font.SysFont("Arial Narrow",32)
FUENTE_30 = pygame.font.SysFont("Arial Narrow",30)
FUENTE_25 = pygame.font.SysFont("Arial Narrow",25)
FUENTE_22 = pygame.font.SysFont("Arial Narrow",22)
FUENTE_MENU = pygame.font.SysFont('Comic Sans MS',80)


CLICK_SONIDO = pygame.mixer.Sound("menu-button.mp3")
CLICK_ERROR = pygame.mixer.Sound("error-choice.mp3")
CLICK_CORRECTO = pygame.mixer.Sound('correct-choice.mp3')
CLICK_JUEGO = pygame.mixer.Sound('click_ppal.mp3')


BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3