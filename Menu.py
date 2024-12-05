import pygame
from Constantes import *
from Funciones import *


pygame.init()


lista_botones = crear_lista_botones(4,TAMAÑO_BOTON,'boton_2.png')

# for i in range(4):
#     boton = {}
#     boton['superficie'] = pygame.image.load('boton_2.png')
#     boton['superficie'] = pygame.transform.scale(boton['superficie'],TAMAÑO_BOTON)
#     boton['rectangulo'] = boton['superficie'].get_rect()
#     # no se usa fill
#     #boton['superficie'].fill(COLOR_VERDE)
#     lista_botones.append(boton)

# mi_superficie_fondo = pygame.image.load('fondo_arg.jpeg')
# mi_superficie_fondo = pygame.transform.scale(mi_superficie_fondo,(VENTANA))

mi_superficie_fondo = cargar_imagen('fondo_arg.jpeg',VENTANA)

def mostar_menu(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    pygame.display.set_caption('MENU')
    retorno = 'menu'

    #Gestiono los Eventos
    # Actualizacion del juego

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        if evento.type == pygame.MOUSEBUTTONDOWN:
            CLICK_SONIDO.play()
            for i in range(len(lista_botones)):
                if lista_botones[i]['rectangulo'].collidepoint(evento.pos):
                    if i == BOTON_JUGAR:
                        print('Le hizo click a jugar')
                        retorno = 'jugar'
                    elif i == BOTON_CONFIG:
                        print('le hizo click a configuraciones')
                        retorno = 'configuraciones'
                    elif i == BOTON_RANKINGS:
                        print('Le hizo click a rankings')
                        retorno = 'rankings'
                    elif i == BOTON_SALIR:
                        print('Le hizo click a salir')
                        retorno = 'salir'

    # Dibujar pantalla

    pantalla.blit(mi_superficie_fondo,(0,0))
    
    lista_botones[BOTON_JUGAR]['rectangulo'] = pantalla.blit(lista_botones[BOTON_JUGAR]['superficie'],(300,155))
    lista_botones[BOTON_CONFIG]['rectangulo'] = pantalla.blit(lista_botones[BOTON_CONFIG]['superficie'],(300,225))
    lista_botones[BOTON_RANKINGS]['rectangulo'] = pantalla.blit(lista_botones[BOTON_RANKINGS]['superficie'],(300,295))
    lista_botones[BOTON_SALIR]['rectangulo'] = pantalla.blit(lista_botones[BOTON_SALIR]['superficie'],(300,365))
    
    mostrar_texto(lista_botones[BOTON_JUGAR]['superficie'],'JUGAR',(80,15),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_CONFIG]['superficie'],'CONFIGURACION',(50,15),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_RANKINGS]['superficie'],'RANKINGS',(80,15),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_SALIR]['superficie'],'SALIR',(80,15),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(pantalla,'MENU',(300,30),FUENTE_MENU,COLOR_NEGRO)

    return retorno

