import pygame
from Constantes import *
from Funciones import *


pygame.init()


mi_superficie_fondo = cargar_imagen('imagen_res.jpg',VENTANA)

boton_salida = crear_boton('imagen_boton.png',TAMAÑO_BOTON)

boton_comienzo = crear_boton('boton_2.png',TAMAÑO_RESPUESTA)



def mostar_pantalla_principal(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    pygame.display.set_caption('MI PRIMER JUEGO')
    retorno = 'pantalla_principal'

    #Gestiono los Eventos
    # Actualizacion del juego

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            print('Cerro la ventana')
            retorno = 'salir'
        if evento.type == pygame.MOUSEBUTTONDOWN:
            #CLICK_SONIDO.play()
            if boton_salida['rectangulo'].collidepoint(evento.pos):
                print('Le hizo click a salir')
                retorno = 'salir'
            if boton_comienzo['rectangulo'].collidepoint(evento.pos):
                print('Se inicio el juego')
                CLICK_JUEGO.play()
                retorno = 'menu'
    # Dibujar pantalla
    
    
    pantalla.blit(mi_superficie_fondo,(0,0))
    
    boton_comienzo['rectangulo'] = pantalla.blit(boton_comienzo['superficie'],(280,300))
    boton_salida['rectangulo'] = pantalla.blit(boton_salida['superficie'],(500,530))
    
    mostrar_texto(boton_comienzo['superficie'],'PRESIONE PARA COMENZAR',(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(boton_salida['superficie'],'SALIR DEL JUEGO',(50,20),FUENTE_25,COLOR_BLANCO)  
    mostrar_texto(pantalla,'CAMPEONES DEL SABER',(130,190),FUENTE_PPAL,COLOR_NEGRO)

    return retorno

