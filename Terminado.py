import pygame
import json
from datetime import datetime
from Constantes import *
from Funciones import *
from Funciones_archivos import*
pygame.init()

# caja_texto = {}
# caja_texto["superficie"] = pygame.Surface(CUADRO_TEXTO)
# caja_texto["rectangulo"] = caja_texto["superficie"].get_rect()
# caja_texto["superficie"].fill(COLOR_AZUL)

caja_texto = crear_boton('cuadro_terminado.png',(CUADRO_TEXTO))

boton_aceptar = crear_boton('aceptar_terminado.png',(TAMAÑO_BOTON_VOLVER))

nombre = ""#Inmutable

superficie_fondo_terminado = cargar_imagen('fondo_terminado.png',VENTANA)

fecha = datetime.now().strftime('%d-%m-%Y')



def mostrar_juego_terminado(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global nombre
    global fecha
    retorno = "terminando"
    
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_aceptar["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                guardar_datos(nombre, datos_juego['puntuacion'],fecha)
                reiniciar_datos(datos_juego)
                nombre = ''
                retorno = "menu"
        if evento.type == pygame.KEYDOWN:
            letra_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            
            if letra_presionada == "space":
                nombre += " "
            elif letra_presionada == "backspace" and len(nombre) > 0:
                nombre = nombre[:-1]  # Me elimina automaticamente el último
            elif len(letra_presionada) == 1:
                if bloc_mayus != 0:
                    nombre += letra_presionada.upper()
                else:
                    nombre += letra_presionada
                print(nombre)
        elif evento.type == pygame.QUIT:
            retorno = 'salir'
    
    caja_texto['superficie'] = cargar_imagen('cuadro_terminado.png',CUADRO_TEXTO)


    mostrar_texto(caja_texto["superficie"],nombre,(30,30),FUENTE_22,COLOR_BLANCO)
    # pantalla.fill(COLOR_BLANCO)
    
    pantalla.blit(superficie_fondo_terminado,(0,0))

    caja_texto["rectangulo"] = pantalla.blit(caja_texto["superficie"],(230,270))
    boton_aceptar['rectangulo'] = pantalla.blit(boton_aceptar['superficie'],(350,350))


    
    mostrar_texto(pantalla,f"Usted obtuvo: {datos_juego['puntuacion']} puntos",(230,250),FUENTE_40,COLOR_NEGRO)
    
    return retorno
