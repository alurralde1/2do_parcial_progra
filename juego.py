import pygame
from Funciones import *
from Funciones_archivos import *
from Constantes import *


pygame.init()


carta_pregunta = crear_boton('fondo_pregunta.png',TAMAÑO_PREGUNTA)

cartas_respuestas = crear_lista_botones(4,TAMAÑO_RESPUESTA,'boton_respuessta.png')

mis_superficie_fondo= cargar_imagen('juego_menu.jpeg',VENTANA)

opcion_correcta = cargar_imagen('correcto.png',TAMAÑO_RESPUESTA)
opcion_incorrecta = cargar_imagen('cerrar.png',TAMAÑO_RESPUESTA)

imagen_fondo_pregunta = cargar_imagen('fondo_pregunta.png',TAMAÑO_PREGUNTA)
imagen_fondo_respuesta = cargar_imagen('boton_respuessta.png',TAMAÑO_RESPUESTA)


lista_preguntas = []

if not leer_csv_preguntas(lista_preguntas,'Preguntas'):
    print('Error al leer el archivo csv de las preguntas')


indice = 0
mezclar_lista(lista_preguntas)
bandera_respuesta = False

tiempo_juego = pygame.USEREVENT
pygame.time.set_timer(tiempo_juego,1000)



def mostrar_juego(pantalla: pygame.Surface,cola_eventos: list[pygame.event.Event],datos_juego: dict)-> str:
    global indice
    global bandera_respuesta

    retorno = "jugar"

    pregunta_actual = lista_preguntas[indice]
    
    if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False
        
    # carta_pregunta["superficie"].fill(COLOR_ROJO)
    # for i in range(len(cartas_respuestas)):
    #     cartas_respuestas[i]["superficie"].fill(COLOR_AZUL)

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == tiempo_juego:
            datos_juego['tiempo_juego'] -= 1
            if datos_juego['tiempo_juego'] == 0 or datos_juego['vidas'] <= 0:
                retorno = 'terminando'
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    print(f"LE DIO CLICK A LA RESPUESTA : {respuesta_seleccionada}")
                    
                    if verificar_respuesta(datos_juego,pregunta_actual,respuesta_seleccionada):
                        print("RESPUESTA CORRECTA")
                        #Ustedes van a manejar una imagen para esto
                        cartas_respuestas[i]["superficie"].blit(opcion_correcta,(0,0))
                        CLICK_CORRECTO.play()
                    else:
                        print("RESPUESTA INCORRECTA") 
                        #Ustedes van a manejar una imagen para esto
                        cartas_respuestas[i]["superficie"].blit(opcion_incorrecta,(0,0))
                        CLICK_ERROR.play()
                    
                    indice +=1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    
                    bandera_respuesta = True

    

    mostrar_texto(carta_pregunta["superficie"],pregunta_actual["pregunta"],(10,40),FUENTE_30,COLOR_NEGRO)

    for i in range(len(cartas_respuestas)):
        mostrar_texto(cartas_respuestas[i]["superficie"],pregunta_actual[f"respuesta_{i+1}"],(50,20),FUENTE_22,COLOR_BLANCO)
    # mostrar_texto(cartas_respuestas[0]["superficie"],pregunta_actual["respuesta_1"],(50,20),FUENTE_22,COLOR_BLANCO)
    # mostrar_texto(cartas_respuestas[1]["superficie"],pregunta_actual["respuesta_2"],(50,20),FUENTE_22,COLOR_BLANCO)
    # mostrar_texto(cartas_respuestas[2]["superficie"],pregunta_actual["respuesta_3"],(50,20),FUENTE_22,COLOR_BLANCO)
    # mostrar_texto(cartas_respuestas[3]['superficie'],pregunta_actual["respuesta_4"],(50,20),FUENTE_22,COLOR_BLANCO)

    pantalla.blit(mis_superficie_fondo,(0,0))

    pantalla.blit(carta_pregunta["superficie"],(200,100))
      
    cartas_respuestas[0]["rectangulo"] = pantalla.blit(cartas_respuestas[0]["superficie"],(250,245))#r1
    cartas_respuestas[1]["rectangulo"] = pantalla.blit(cartas_respuestas[1]["superficie"],(250,315))#r2
    cartas_respuestas[2]["rectangulo"] = pantalla.blit(cartas_respuestas[2]["superficie"],(250,385))#r3
    cartas_respuestas[3]["rectangulo"] = pantalla.blit(cartas_respuestas[3]["superficie"],(250,455))#r3

    carta_pregunta["superficie"].blit(imagen_fondo_pregunta, (0, 0))
    for carta in cartas_respuestas:
        carta["superficie"].blit(imagen_fondo_respuesta, (0, 0))

    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_BLANCO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['vidas']}",(10,40),FUENTE_25,COLOR_BLANCO)
    mostrar_texto(pantalla,f'SEGUNDOS: {datos_juego["tiempo_juego"]}',(300,10),FUENTE_25,COLOR_BLANCO)

    return retorno