import pygame
from Constantes import *
from Funciones import *
from Funciones_archivos import *

pygame.init()

# Crea el botón de "Volver"
boton_volver = crear_boton('boton_atras.png', TAMAÑO_BOTON_VOLVER)

# Crea la lista de botones
lista_botones = crear_lista_botones(10, TAMAÑO_BOTON_RANKINGS, 'boton_2.png')

# Carga la imagen de fondo para los rankings
superficie_fondo_rankings = cargar_imagen('fondo_rankings.jpg', VENTANA)

# Lee el archivo JSON de partidas (presumiblemente contiene una lista de diccionarios)
# lista_json = leer_jsson('partidas')
# lista_ordenada = ordenar_lista_por_criterio(lista_json,'Puntuacion')

def mostrar_puntuaciones(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]):
    retorno = "rankings"

    lista_json = leer_jsson('partidas')
    lista_ordenada = ordenar_lista_por_criterio(lista_json,'Puntuacion')

    # Maneja los eventos
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"

    # Dibuja el fondo
    pantalla.blit(superficie_fondo_rankings, (0, 0))

    # Dibuja el botón "Volver"
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"], (10, 10))

    # Muestra el texto principal
    mostrar_texto(pantalla, "TOP 10 RANKINGS", (300, 20), FUENTE_50, COLOR_NEGRO)
    mostrar_texto(pantalla, 'PUESTO                NOMBRE               PUNTUACION', (210, 90), FUENTE_30, COLOR_NEGRO)

    # Muestra los botones con la información
    for i, boton in enumerate(lista_botones):
        # Calcula la posición vertical del botón
        y_altura_inicial = 100  # Altura inicial
        espacio = 40    # Espacio entre botones
        y_pos = y_altura_inicial + i * espacio  # Ajusta la posición de cada botón

        # Dibuja el botón
        boton['rectangulo'] = pantalla.blit(boton['superficie'], (180, y_pos))

        # Muestra el texto dentro del botón (nombre, puntuación)
        if i < len(lista_ordenada):  # Asegúrate de no exceder el límite de la lista
            jugador = lista_ordenada[i]  # Obtener el diccionario del jugador
            nombre = jugador['nombre']
            puntuacion = jugador['Puntuacion']

            # Muestra el texto dentro del botón
            mostrar_texto(
                pantalla,
                f"    {i + 1:<3}                           {nombre:^20}                           {puntuacion:^5}",
                (200, y_pos + 15),  # Ajusta las coordenadas para centrar el texto
                FUENTE_22,
                COLOR_NEGRO
            )

    # Muestra el texto de "Volver"
    mostrar_texto(boton_volver["superficie"], "", (10, 10), FUENTE_22, COLOR_BLANCO)

    return retorno