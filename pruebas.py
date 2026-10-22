"""
Pruebas de los módulos del prototipo con casos simples.
Ejecutar con: python pruebas.py
"""

import os
from validaciones import validar_documento, validar_fecha, validar_folios, verificar_requisitos
from operaciones import generar_codigo, registrar_expediente, buscar_por_codigo, ordenar_por_codigo, actualizar_estado
from archivo import guardar_expedientes, cargar_expedientes

aprobadas = 0
total = 0


def probar(descripcion, obtenido, esperado):
    global aprobadas, total
    total += 1
    resultado = "CORRECTO" if obtenido == esperado else "FALLA"
    if obtenido == esperado:
        aprobadas += 1
    print(resultado.ljust(9), descripcion)


print("== Validaciones ==")
probar("RUC de 11 dígitos es válido", validar_documento("20510983662"), True)
probar("DNI de 8 dígitos es válido", validar_documento("12345678"), True)
probar("Documento de 10 dígitos es inválido", validar_documento("2051098366"), False)
probar("Documento con letras es inválido", validar_documento("2051098366A"), False)
probar("Fecha 16/10/2026 es válida", validar_fecha("16/10/2026"), True)
probar("Fecha 32/08/2026 es inválida", validar_fecha("32/08/2026"), False)
probar("Fecha con guiones es inválida", validar_fecha("16-10-2026"), False)
probar("30 folios es válido", validar_folios("30"), True)
probar("0 folios es inválido", validar_folios("0"), False)
probar("Requisito faltante detectado", len(verificar_requisitos("MEDIO", [True, True, False, True, True])), 1)

print("== Registro, búsqueda y ordenamiento ==")
lista = []
c1 = registrar_expediente(lista, "20510983662", "Corporacion Textil Unidos SAC", "LICENCIA NUEVA",
                          "Venta de prendas de vestir", "MEDIO", "16/10/2026", "30")
c2 = registrar_expediente(lista, "20615197310", "Khanz Care Group S.A.C.", "LICENCIA NUEVA",
                          "Consultorio odontologico", "MEDIO", "20/08/2026", "12")
probar("Primer código generado es EXP-2026-0001", c1, "EXP-2026-0001")
probar("Segundo código generado es EXP-2026-0002", c2, "EXP-2026-0002")
probar("Búsqueda de código existente", buscar_por_codigo(lista, "exp-2026-0002"), 1)
probar("Búsqueda de código inexistente", buscar_por_codigo(lista, "EXP-2026-0099"), -1)

desordenada = [["EXP-2026-0003"] + [""] * 9, ["EXP-2026-0001"] + [""] * 9, ["EXP-2026-0002"] + [""] * 9]
ordenar_por_codigo(desordenada)
probar("Ordenamiento por código (burbuja)", [e[0] for e in desordenada],
       ["EXP-2026-0001", "EXP-2026-0002", "EXP-2026-0003"])

print("== Estados y archivo ==")
probar("No se archiva un expediente sin resolver", actualizar_estado(lista, 0, "ARCHIVADO", "3", "12"),
       "Solo se archivan expedientes aprobados o denegados.")
actualizar_estado(lista, 1, "APROBADO")
actualizar_estado(lista, 1, "ARCHIVADO", "3", "12")
probar("Ubicación física registrada al archivar", lista[1][9], "ESTANTE 3 - CAJA 12")

guardar_expedientes(lista, "prueba_expedientes.txt")
probar("Los datos se recuperan del archivo", cargar_expedientes("prueba_expedientes.txt"), lista)
os.remove("prueba_expedientes.txt")

print("Resultado:", aprobadas, "de", total, "pruebas correctas")
