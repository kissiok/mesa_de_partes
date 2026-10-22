"""
Módulo de operaciones sobre los expedientes.
Cada expediente es una lista con 10 datos y todos se guardan
en una lista de listas (arreglo bidimensional).
"""

# Posición de cada dato dentro del expediente
CODIGO, DOCUMENTO, RAZON_SOCIAL, TRAMITE, GIRO, RIESGO, FECHA, FOLIOS, ESTADO, UBICACION = range(10)

TRAMITES = ["LICENCIA NUEVA", "CAMBIO DE GIRO", "CESE DE ACTIVIDADES", "DUPLICADO DE LICENCIA"]
ESTADOS = ["RECIBIDO", "EN EVALUACION", "OBSERVADO", "APROBADO", "DENEGADO", "ARCHIVADO"]


def generar_codigo(expedientes, anio):
    """Genera el siguiente código correlativo del año, por ejemplo EXP-2026-0001."""
    mayor = 0
    prefijo = "EXP-" + anio + "-"
    for expediente in expedientes:
        if expediente[CODIGO].startswith(prefijo):
            numero = int(expediente[CODIGO][len(prefijo):])
            if numero > mayor:
                mayor = numero
    return prefijo + str(mayor + 1).zfill(4)


def registrar_expediente(expedientes, documento, razon_social, tramite, giro, riesgo, fecha, folios):
    """Crea el expediente con estado RECIBIDO, lo agrega a la lista y devuelve su código."""
    anio = fecha[6:10]
    codigo = generar_codigo(expedientes, anio)
    expediente = [codigo, documento.strip(), razon_social.strip().upper(), tramite,
                  giro.strip().upper(), riesgo, fecha, int(folios), "RECIBIDO", "SIN ARCHIVAR"]
    expedientes.append(expediente)
    return codigo


def buscar_por_codigo(expedientes, codigo):
    """Búsqueda secuencial: devuelve la posición del expediente o -1 si no existe."""
    codigo = codigo.strip().upper()
    for i in range(len(expedientes)):
        if expedientes[i][CODIGO] == codigo:
            return i
    return -1


def ordenar_por_codigo(expedientes):
    """Ordena los expedientes por código con el método de burbuja."""
    n = len(expedientes)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if expedientes[j][CODIGO] > expedientes[j + 1][CODIGO]:
                expedientes[j], expedientes[j + 1] = expedientes[j + 1], expedientes[j]
                intercambio = True
        if not intercambio:
            break
