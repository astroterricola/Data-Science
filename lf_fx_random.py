import pandas as pd
import os
# Funciones propias para reemplazar numpy

def lf_rango(lp_inicio, lp_fin, lp_numero):
    """
    Genera una lista de valores equiespaciados en un rango dado.

    Parámetros:
    - lp_inicio (float): Valor inicial del rango.
    - lp_fin (float): Valor final del rango.
    - lp_numero (int): Número total de valores en el rango.

    Retorna:
    - List[float]: Lista de valores equiespaciados.
    """
    lp_paso = (lp_fin - lp_inicio) / (lp_numero - 1)
    return [lp_inicio + lp_paso * lv_indice for lv_indice in range(lp_numero)]

def lf_media(lv_valores):
    """
    Calcula la media aritmética de una lista de valores.

    Parámetros:
    - lv_valores (List[float]): Lista de valores numéricos.

    Retorna:
    - float: Media aritmética.
    """
    return sum(lv_valores) / len(lv_valores)

def lf_desviacion_estandar(lv_valores):
    """
    Calcula la desviación estándar de una lista de valores.

    Parámetros:
    - lv_valores (List[float]): Lista de valores numéricos.

    Retorna:
    - float: Desviación estándar.
    """
    lv_media = lf_media(lv_valores)
    return (sum((lv_x - lv_media) ** 2 for lv_x in lv_valores) / len(lv_valores)) ** 0.5

def lf_evaluar_polinomio(lp_coeficientes, lp_x):
    """
    Evalúa un polinomio en un punto específico.

    Parámetros:
    - lp_coeficientes (List[float]): Coeficientes del polinomio ordenados de mayor a menor grado.
    - lp_x (float): Valor en el que se evaluará el polinomio.

    Retorna:
    - float: Resultado de la evaluación del polinomio.
    """
    return sum(lv_c * (lp_x ** lv_i) for lv_i, lv_c in enumerate(reversed(lp_coeficientes)))

def lf_evaluar_polinomio_todos(lp_coeficientes, lv_xs):
    """
    Evalúa un polinomio en múltiples puntos.

    Parámetros:
    - lp_coeficientes (List[float]): Coeficientes del polinomio ordenados de mayor a menor grado.
    - lv_xs (List[float]): Lista de valores en los que se evaluará el polinomio.

    Retorna:
    - List[float]: Resultados de la evaluación en cada punto.
    """
    return [lf_evaluar_polinomio(lp_coeficientes, lv_x) for lv_x in lv_xs]

def lf_aleatorios(lp_tamano):
    """
    Genera una lista de valores aleatorios entre 0 y 1.

    Parámetros:
    - lp_tamano (int): Tamaño de la lista.

    Retorna:
    - List[float]: Lista de valores aleatorios.
    """
    return [random.random() for _ in range(lp_tamano)]

def lf_norma(lv_valores):
    """
    Calcula la norma euclidiana de un vector.

    Parámetros:
    - lv_valores (List[float]): Lista de valores representando el vector.

    Retorna:
    - float: Norma euclidiana del vector.
    """
    return sum(lv_x ** 2 for lv_x in lv_valores) ** 0.5
