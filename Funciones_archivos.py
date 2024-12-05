import os
import json
import copy

def crear_diccionario_pregunta(lista_preguntas: list) -> dict:
    """
    funcion que crea un diccionario 
    Args:
        lista_preguntas (list): recibe una lista como parametro

    Returns:
        dict: retorna el diccionario
    """
    pregunta = {}

    pregunta["pregunta"] = lista_preguntas[0]
    pregunta["respuesta_1"] = lista_preguntas[1]
    pregunta["respuesta_2"] = lista_preguntas[2]
    pregunta["respuesta_3"] = lista_preguntas[3]
    pregunta["respuesta_4"] = lista_preguntas[4]
    pregunta["respuesta_correcta"] = int(lista_preguntas[5])
   
    return pregunta

def leer_csv_preguntas(lista: list[dict],ruta: str) -> bool:
    """
    funcion que lee un archivo csv      
    Args:
        lista (list[dict]): recibe la lista a copiar los valores del csv

        ruta (str): recibe la ruta a donde esta ubicada el archivo
    Returns:
        bool: retorna true si logro encontrar el archivo o false si no pudo
    """
    nombre_archivo = ruta

    if os.path.exists(f'{nombre_archivo}.csv'):
        with open(f'{nombre_archivo}.csv', 'r') as file:
            #Falsa lectura
            file.readline()

            for linea in file:
                linea_aux = linea.replace('\n','')
                lista_valores = linea_aux.split(',')
                pregunta = crear_diccionario_pregunta(lista_valores)
                lista.append(pregunta)
        retorno = True
    else:
        retorno = False
    
    return retorno

def deep_copy_listas(lista_preguntas: list[dict]) -> list:
    """
    la funcion crea una copia profunda de la lista para no modificar la original   
    Args:
        lista_preguntas (list[dict]): recibe como parametro la lista a copiar

    Returns:
        list: retorna la lista duplicada
    """
    
    nueva_lista = copy.deepcopy(lista_preguntas)

    return nueva_lista

def ordenar_lista_por_criterio(lista_preguntas: list[dict],criterio: str)-> list:
    """
    funcion que me ordena de menor a mayor segun el criterio pasado por parametro
    Args:
        lista_preguntas (list[dict]): recibe como parametro la lista a ordenar
        criterio (str): recibe como parametro el criteria a evaluar

    Returns:
        list: retorna la lista ordenada
    """

    lista_copiada = deep_copy_listas(lista_preguntas)

    for i in range(len(lista_copiada) - 1):
        for j in range(i + 1, len(lista_copiada)):
            if lista_copiada[i][criterio] < lista_copiada[j][criterio]:
                auxiliar = lista_copiada[i]
                lista_copiada[i] = lista_copiada[j]
                lista_copiada[j] = auxiliar
    
    return lista_copiada


def guardar_datos(nombre,puntuacion: int,fecha):
    """
    funcion que guarda el diccionario que corresponde de cada jugador en un archivo json
    Args:
        nombre (_type_): recibe como parametro el nombre del jugador
        puntuacion (int): recibe como parametro la puntuacion del jugador
        fecha (_type_): _recibe como parametro la fecha del jugador
    """
    datos = {
        'nombre': nombre,
        'Puntuacion': puntuacion,
        'fecha': fecha
    }
    lista = []
    lista = leer_jsson('partidas')
    lista.append(datos)

    with open('partidas.json', 'w') as file:
        json.dump(lista,file,indent=4)



def leer_jsson(nombre_archivo: str) -> list:
    """
    funcion que lee el contenido de un archivo json
    Args:
        nombre_archivo (str): recibe como parametro el nombre del archivo a leer

    Returns:
        list: retorna la lista de diccionarios dada en el archivo json
    """
    if os.path.exists(f'{nombre_archivo}.json'):
        with open(f'{nombre_archivo}.json', 'r') as file:
            try:
                lista = json.load(file)
            except json.JSONDecodeError:
                # Si el archivo está vacío o tiene contenido inválido
                lista = []
        return lista
    else:
        return []

