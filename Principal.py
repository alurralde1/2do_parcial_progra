import pygame
from Constantes import *
from Funciones import *
from Menu import *
from juego import *
from Pantalla_principal import *
from Rankings import *
from Configuracion import *
from Terminado import *

# Inicializamos el juego
pygame.init()

# Creamos el icono de mi juego
pygame.display.set_caption('Preguntados futbolero')
icono = pygame.image.load('icono_futbol.png')
pygame.display.set_icon(icono)

#Configuramos la pantalla
pantalla = pygame.display.set_mode(VENTANA)

#Creo un reloj
clock = pygame.time.Clock()

datos_juego = {'puntuacion': 0,'vidas': 3,'usuario':'','volumen_musica': 5,'respuestas_correctas': 0,'tiempo_juego': 100,'Puntuacion_acierto': 100,'Puntuacion_error':25}

ventana_actual = 'pantalla_principal'

pygame.mixer.init()
bandera_musica = False

corriendo = True
#Bucle principal
while corriendo:

    # Manejo de eventos
    # Actualizar juego
    # Se dibuja los elementos en pantalla

    cola_eventos = pygame.event.get()
    clock.tick(FPS)

    if ventana_actual == 'pantalla_principal':
        ventana_actual = mostar_pantalla_principal(pantalla,cola_eventos)
    elif ventana_actual == 'menu':
        ventana_actual = mostar_menu(pantalla,cola_eventos)
    elif ventana_actual == 'jugar':
        if bandera_musica == False:
            porcentaje_coma = datos_juego['volumen_musica'] / 100
            pygame.mixer.music.load('musica.mp3')
            pygame.mixer.music.set_volume(porcentaje_coma)
            pygame.mixer.music.play(-1)
            bandera_musica = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego) 
    elif ventana_actual == 'configuraciones':
        ventana_actual = mostrar_configuracion(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == 'rankings':
        ventana_actual = mostrar_puntuaciones(pantalla,cola_eventos)
    elif ventana_actual == 'terminando':
        pygame.mixer.music.stop()
        bandera_musica= False
        ventana_actual = mostrar_juego_terminado(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == 'salir':
        print('SALIENDO DEL JUEGO')
        corriendo = False
    
    pygame.display.flip()
pygame.quit()





