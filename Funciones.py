from Constantes import *
import random
import pygame


def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    
def mezclar_lista(lista:list) -> None:
    """
    mezclo la lista ingresada como parametro
    Args:
        lista (list): recibe la lista a mezclar
    """
    random.shuffle(lista)

def verificar_respuesta(datos_juego:dict,pregunta_actual:dict,respuesta:int) -> bool:
    """
    verifica la respuesta si es correcta o no ingresada por el usuario
    Args:
        datos_juego (dict): recibe como parametro el diccionario
        pregunta_actual (dict): recibe como parametro la pregunta 
        respuesta (int): recibe como parametro la respuesta correcta

    Returns:
        bool: retorna True si es correcta y False si no lo es
    """
    if pregunta_actual["respuesta_correcta"] == respuesta:
        datos_juego["puntuacion"] += datos_juego['Puntuacion_acierto']
        datos_juego['respuestas_correctas'] += 1

        if datos_juego['respuestas_correctas'] % 5 == 0:
            datos_juego['vidas'] += 1
            datos_juego['tiempo_juego'] += 10
        retorno = True
    else:
        #SIN PUNTOS NEGATIVOS
        datos_juego['respuestas_correctas'] = 0
        if datos_juego["puntuacion"] > datos_juego['Puntuacion_error']:
            datos_juego["puntuacion"] -= datos_juego['Puntuacion_error']
        
        #CON PUNTOS NEGATIVOS
        #datos_juego["puntuacion"] -= PUNTUACION_ERROR
        if datos_juego['vidas'] > 0:
            datos_juego["vidas"] -= 1
        retorno = False

    return retorno
    

# FUNCIONES PROPIAS CREADAS PARA PEDIR LOS BOTONES Y CARGAR IMAGEN

def cargar_imagen(ruta: str,tamaño: str) -> pygame.surface.Surface:
    """
    funcion que crea una imagen siendo una superficie
    Args:
        ruta (str): recibe la ruta de la imagen a cargar
        tama (_type_): recibe el tamaño a transformar la imagen

    Returns:
        pygame.surface.Surface:retorna la superficie 
    """

    imagen = pygame.image.load(ruta)
    return pygame.transform.scale(imagen,tamaño)


def crear_boton(ruta: str,tamaño: str)-> dict :
    """
    funcion que me crea un boton siendo una superficie
    Args:
        ruta (str): recibe la ruta de la imagen a crgar
        tama (_type_): recibe el tamano a transformar la imagen

    Returns:
        dict: retorna un diccionario que tiene la superfice y el rectangulo de un boton
    """
    boton = {}
    # boton_salida['superficie'] = pygame.image.load('imagen_boton.png')
    # boton_salida['superficie'] = pygame.transform.scale(boton_salida['superficie'],CUADRO_TEXTO)
    boton['superficie'] = cargar_imagen(ruta,tamaño)
    boton['rectangulo'] = boton['superficie'].get_rect()

    return boton

def crear_lista_botones(cantidad: int, tamaño: str,ruta: str)-> list:
    """
    funcion que crea una lista de botones siendo superficies
    Args:
        cantidad (int): recibe la cantidad de botones que necesita
        tama (_type_): recibe el tamano de los botones
        ruta (str): recibe la imagen a cargar

    Returns:
        list: retorna la lista de la superficie de botones
    """
    lista_botones = []

    for i in range(cantidad):
        boton = crear_boton(ruta,tamaño)
        lista_botones.append(boton)

    return lista_botones

def iniciar_musica(ruta: str,volumen: float) :
    pygame.mixer.init()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.play(-1)

def reiniciar_datos(datos_juego: dict) -> None:
    """
    funcion que me reinicia los datos
    Args:
        datos_juego (dict): recibe los datos y los harcodea a como estaban al inicio
    """

    datos_juego.update({'puntuacion': 0,'vidas': 3,'usuario':'','volumen_musica': 10,'respuestas_correctas': 0,'tiempo_juego': 100,'Puntuacion_acierto': 100,'Puntuacion_error':25})
    
