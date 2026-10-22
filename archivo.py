"""
Módulo de persistencia.
Guarda y carga los expedientes en un archivo de texto.
Cada línea es un expediente y sus campos se separan con punto y coma.
"""

import os

NOMBRE_ARCHIVO = "expedientes.txt"
SEPARADOR = ";"
CAMPOS = 10  # código, documento, razón social, trámite, giro, riesgo, fecha, folios, estado, ubicación


def guardar_expedientes(expedientes, nombre_archivo=NOMBRE_ARCHIVO):
    """Escribe todos los expedientes en el archivo, uno por línea."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for expediente in expedientes:
            linea = SEPARADOR.join(str(dato) for dato in expediente)
            archivo.write(linea + "\n")


def cargar_expedientes(nombre_archivo=NOMBRE_ARCHIVO):
    """Lee el archivo y devuelve la lista de expedientes. Si no existe, devuelve una lista vacía."""
    expedientes = []
    if not os.path.exists(nombre_archivo):
        return expedientes
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            datos = linea.split(SEPARADOR)
            if len(datos) == CAMPOS:
                datos[7] = int(datos[7])  # folios
                expedientes.append(datos)
    return expedientes
