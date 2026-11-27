"""
Casos de prueba con los datos recogidos en la observación de campo
(mesa de partes de la Municipalidad Distrital de Chorrillos, octubre de 2026).
Ejecutar con: python pruebas_campo.py
"""

from validaciones import validar_documento, validar_fecha, validar_folios, validar_texto, verificar_requisitos
from operaciones import registrar_expediente, buscar_por_codigo, ordenar_por_codigo, actualizar_estado

aprobadas = 0
casos = 0


def caso(codigo, descripcion, obtenido, esperado):
    global aprobadas, casos
    casos += 1
    correcto = obtenido == esperado
    if correcto:
        aprobadas += 1
    print(codigo, "CORRECTO" if correcto else "FALLA   ", "|", descripcion, "| obtenido:", obtenido)


expedientes = []

print("== Casos normales ==")
c1 = registrar_expediente(expedientes, "20510983662", "Corporacion Textil Unidos SAC", "INSPECCION TECNICA ITSE",
                          "Establecimiento comercial", "MEDIO", "16/10/2026", "30")
caso("P01", "Registro de la solicitud ITSE de Corporación Textil Unidos SAC", c1, "EXP-2026-0001")
c2 = registrar_expediente(expedientes, "20615197310", "Khanz Care Group S.A.C.", "LICENCIA NUEVA",
                          "Consultorio odontologico", "MEDIO", "20/08/2026", "12")
caso("P02", "Registro de la licencia de Khanz Care Group S.A.C.", c2, "EXP-2026-0002")
caso("P03", "Búsqueda por código en minúsculas", buscar_por_codigo(expedientes, "exp-2026-0002"), 1)
expedientes.reverse()
ordenar_por_codigo(expedientes)
caso("P04", "Ordenamiento por código", [e[0] for e in expedientes], ["EXP-2026-0001", "EXP-2026-0002"])
actualizar_estado(expedientes, 1, "APROBADO")
caso("P05", "Archivo de expediente aprobado en estante y caja",
     actualizar_estado(expedientes, 1, "ARCHIVADO", "3", "12"), "Estado actualizado a ARCHIVADO.")

print("== Casos de error ==")
caso("P06", "RUC con un dígito omitido (2051098366)", validar_documento("2051098366"), False)
caso("P07", "RUC con la letra O en lugar de cero (2O510983662)", validar_documento("2O510983662"), False)
caso("P08", "Fecha inexistente 31/09/2026", validar_fecha("31/09/2026"), False)
caso("P09", "Fecha 29/02/2026 en año no bisiesto", validar_fecha("29/02/2026"), False)
caso("P10", "Expediente con cero folios", validar_folios("0"), False)
caso("P11", "Razón social con punto y coma", validar_texto("Corporacion Textil; Unidos SAC"), False)
caso("P12", "Solicitud de riesgo medio sin ficha RUC",
     verificar_requisitos("MEDIO", [True, True, True, False, True]), ["Ficha RUC"])
caso("P13", "Búsqueda de un código inexistente", buscar_por_codigo(expedientes, "EXP-2026-0099"), -1)
caso("P14", "Archivo de un expediente que aún no se resuelve", actualizar_estado(expedientes, 0, "ARCHIVADO", "1", "1"),
     "Solo se archivan expedientes aprobados o denegados.")
caso("P15", "Cambio de estado de un expediente ya archivado", actualizar_estado(expedientes, 1, "OBSERVADO"),
     "Un expediente archivado no puede cambiar de estado.")

print("Resultado:", aprobadas, "de", casos, "casos correctos")
