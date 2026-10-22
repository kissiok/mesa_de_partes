"""
Módulo de validaciones.
Verifica los datos del expediente antes de registrarlos.
"""

# Requisitos principales según el nivel de riesgo del establecimiento
REQUISITOS_BAJO_MEDIO = [
    "Formato de declaración jurada de licencia de funcionamiento",
    "Reporte de nivel de riesgo del establecimiento",
    "Declaración jurada de cumplimiento de condiciones de seguridad",
    "Ficha RUC",
    "Recibo de pago por derecho de trámite",
]

REQUISITOS_ALTO_MUY_ALTO = [
    "Formato de declaración jurada de licencia de funcionamiento",
    "Reporte de nivel de riesgo del establecimiento",
    "Planos de ubicación, arquitectura y seguridad firmados",
    "Certificado de medición del sistema de puesta a tierra",
    "Plan de seguridad del establecimiento",
    "Ficha RUC",
    "Recibo de pago por derecho de trámite",
]

NIVELES_RIESGO = ["BAJO", "MEDIO", "ALTO", "MUY ALTO"]


def validar_documento(documento):
    """Devuelve True si el documento es un DNI (8 dígitos) o un RUC (11 dígitos)."""
    documento = documento.strip()
    if len(documento) != 8 and len(documento) != 11:
        return False
    for caracter in documento:
        if caracter < "0" or caracter > "9":
            return False
    return True


def validar_fecha(fecha):
    """Devuelve True si la fecha tiene el formato dd/mm/aaaa y valores posibles."""
    partes = fecha.strip().split("/")
    if len(partes) != 3:
        return False
    dia, mes, anio = partes
    if len(dia) != 2 or len(mes) != 2 or len(anio) != 4:
        return False
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return False
    dia, mes, anio = int(dia), int(mes), int(anio)
    dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes < 1 or mes > 12 or anio < 2000:
        return False
    return 1 <= dia <= dias_por_mes[mes - 1]


def validar_folios(folios):
    """Devuelve True si el número de folios es un entero mayor que cero."""
    texto = folios.strip()
    return texto.isdigit() and int(texto) > 0


def validar_texto(texto, minimo=3):
    """Devuelve True si el texto tiene al menos la cantidad mínima de caracteres."""
    return len(texto.strip()) >= minimo


def requisitos_por_riesgo(nivel):
    """Devuelve la lista de requisitos que corresponde al nivel de riesgo."""
    if nivel in ("BAJO", "MEDIO"):
        return REQUISITOS_BAJO_MEDIO
    return REQUISITOS_ALTO_MUY_ALTO


def verificar_requisitos(nivel, respuestas):
    """
    Recibe el nivel de riesgo y una lista de respuestas (True o False),
    una por requisito. Devuelve la lista de requisitos faltantes.
    """
    requisitos = requisitos_por_riesgo(nivel)
    faltantes = []
    for i in range(len(requisitos)):
        if not respuestas[i]:
            faltantes.append(requisitos[i])
    return faltantes
