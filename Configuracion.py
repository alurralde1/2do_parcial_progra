import pygame
from Constantes import *
from Funciones import *

pygame.init()

boton_suma = crear_boton('boton_suma.png',TAMAÑO_BOTON_VOLUMEN)
boton_resta = crear_boton('boton_resta.png',TAMAÑO_BOTON_VOLUMEN)

boton_suma_dos = crear_boton('boton_suma.png',TAMAÑO_BOTON_VOLUMEN)
boton_resta_dos = crear_boton('boton_resta.png',TAMAÑO_BOTON_VOLUMEN)

boton_suma_tres = crear_boton('boton_suma.png',TAMAÑO_BOTON_VOLUMEN)
boton_resta_tres = crear_boton('boton_resta.png',TAMAÑO_BOTON_VOLUMEN)

boton_suma_cuatro = crear_boton('boton_suma.png',TAMAÑO_BOTON_VOLUMEN)
boton_resta_cuatro = crear_boton('boton_resta.png',TAMAÑO_BOTON_VOLUMEN)

boton_suma_cinco = crear_boton('boton_suma.png',TAMAÑO_BOTON_VOLUMEN)
boton_resta_cinco = crear_boton('boton_resta.png',TAMAÑO_BOTON_VOLUMEN)


boton_volver = crear_boton('boton_atras.png',TAMAÑO_BOTON_VOLVER)

superficie_config = cargar_imagen('config.jpg',VENTANA)
superficie_musica = cargar_imagen('icono_musica.png',TAMAÑO_BOTON_VOLUMEN)
superficie_opcion_uno = cargar_imagen('boton_configuracion.png',TAMAÑO_BOTON_CONFIG)
superficie_opcion_dos = cargar_imagen('boton_configuracion.png',TAMAÑO_BOTON_CONFIG)
superficie_opcion_juego = cargar_imagen('opcion_juego.png',TAMAÑO_BOTON_VOLUMEN)

superficie_etiqueta = cargar_imagen('etiqueta.png',TAMAÑO_OPCION)
superficie_etiqueta2 = cargar_imagen('etiqueta.png',TAMAÑO_OPCION)
superficie_etiqueta3 = cargar_imagen('etiqueta.png',TAMAÑO_OPCION)
superficie_etiqueta4 = cargar_imagen('etiqueta.png',TAMAÑO_OPCION)

def mostrar_configuracion(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    
    retorno = "configuraciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] < 100:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica"] += 5
                else:
                    CLICK_ERROR.play()
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] > 0:
                    CLICK_SONIDO.play()
                    datos_juego["volumen_musica"] -= 5
                else:
                    CLICK_ERROR.play()
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
            elif boton_suma_dos['rectangulo'].collidepoint(evento.pos):
                if datos_juego['Puntuacion_acierto'] < 1000:
                    datos_juego['Puntuacion_acierto'] += 10
                    CLICK_SONIDO.play()
                else:
                    CLICK_ERROR.play()
            elif boton_resta_dos['rectangulo'].collidepoint(evento.pos):
                if datos_juego['Puntuacion_acierto'] > 0:
                    datos_juego['Puntuacion_acierto'] -= 10
                    CLICK_SONIDO.play()
                else:
                    CLICK_ERROR.play()
            elif boton_suma_tres['rectangulo'].collidepoint(evento.pos):
                if datos_juego['Puntuacion_error'] < 500 :
                    datos_juego['Puntuacion_error'] += 5
                    CLICK_SONIDO.play()
                else:
                    CLICK_ERROR.play()
            elif boton_resta_tres['rectangulo'].collidepoint(evento.pos):
                if datos_juego['Puntuacion_error'] > 0:
                    datos_juego['Puntuacion_error'] -= 5
                    CLICK_SONIDO.play()
                else:
                    CLICK_ERROR.play()
            elif boton_suma_cuatro['rectangulo'].collidepoint(evento.pos):
                if datos_juego['vidas'] < 10 :
                    datos_juego['vidas'] += 1
                    CLICK_SONIDO.play()
                else:
                    CLICK_ERROR.play()
            elif boton_resta_cuatro['rectangulo'].collidepoint(evento.pos):
                if datos_juego['vidas'] > 0:
                    datos_juego['vidas'] -= 1
                    CLICK_SONIDO.play()
                else:
                    CLICK_ERROR.play()
            elif boton_suma_cinco['rectangulo'].collidepoint(evento.pos):
                if datos_juego['tiempo_juego'] < 1800 :
                    datos_juego['tiempo_juego'] += 100
                    CLICK_SONIDO.play()
                else:
                    CLICK_ERROR.play()
            elif boton_resta_cinco['rectangulo'].collidepoint(evento.pos):
                if datos_juego['tiempo_juego'] > 0:
                    datos_juego['tiempo_juego'] -= 100
                    CLICK_SONIDO.play()
                else:
                    CLICK_ERROR.play()
    #Aca pueden usar el get_pressed()
    
    pantalla.blit(superficie_config,(0,0))
    pantalla.blit(superficie_opcion_uno,(30,100))
    superficie_opcion_uno.blit(superficie_musica,(600,0))
    pantalla.blit(superficie_opcion_dos,(30,240))
    superficie_opcion_dos.blit(superficie_opcion_juego,(600,0))

    pantalla.blit(superficie_etiqueta,(30,280))
    pantalla.blit(superficie_etiqueta2,(30,350))
    pantalla.blit(superficie_etiqueta3,(30,420))
    pantalla.blit(superficie_etiqueta4,(30,490))

    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(130,170))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(550,170))

    boton_resta_dos["rectangulo"] = pantalla.blit(boton_resta_dos["superficie"],(360,320))
    boton_suma_dos['rectangulo'] = pantalla.blit(boton_suma_dos['superficie'],(650,320))

    boton_resta_tres['rectangulo'] = pantalla.blit(boton_resta_tres['superficie'],(360,390))
    boton_suma_tres['rectangulo'] = pantalla.blit(boton_suma_tres['superficie'],(650,390))

    boton_resta_cuatro['rectangulo'] = pantalla.blit(boton_resta_cuatro['superficie'],(360,465))
    boton_suma_cuatro['rectangulo'] = pantalla.blit(boton_suma_cuatro['superficie'],(650,465))

    boton_resta_cinco['rectangulo'] = pantalla.blit(boton_resta_cinco['superficie'],(360,535))
    boton_suma_cinco['rectangulo'] = pantalla.blit(boton_suma_cinco['superficie'],(650,535))

    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(20,20))
    

    mostrar_texto(boton_volver["superficie"],"",(10,10),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(boton_suma["superficie"],"",(5,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_resta["superficie"],"",(5,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(pantalla,f"{datos_juego['volumen_musica']} ",(350,190),FUENTE_50,COLOR_BLANCO)
    mostrar_texto(superficie_opcion_uno,'VOL. MUSICA:',(10,10),FUENTE_32,COLOR_NEGRO)
    mostrar_texto(pantalla,'CONFIGURACION',(250,50),FUENTE_50,COLOR_NEGRO)
    mostrar_texto(superficie_opcion_dos,'OPCION DE JUEGO:',(10,10),FUENTE_32,COLOR_NEGRO)
    mostrar_texto(superficie_etiqueta,'PUNTOS ACIERTOS:',(15,65),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(pantalla,f'+{datos_juego["Puntuacion_acierto"]}',(510,340),FUENTE_40,COLOR_BLANCO)
    mostrar_texto(superficie_etiqueta2,'PUNTOS ERROR:',(15,65),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(pantalla,f"-{datos_juego['Puntuacion_error']}",(520,410),FUENTE_40,COLOR_BLANCO)
    mostrar_texto(superficie_etiqueta3,'CANTIDAD VIDAS:',(15,65),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(superficie_etiqueta4,'TIEMPO DISPONIBLE:',(15,65),FUENTE_30,COLOR_NEGRO)
    mostrar_texto(pantalla,f'{datos_juego["vidas"]}',(520,480),FUENTE_40,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego['tiempo_juego']} seg.",(510,550),FUENTE_40,COLOR_BLANCO)
    return retorno
