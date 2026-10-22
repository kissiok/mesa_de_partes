"""
Prototipo de mesa de partes digital.
Expedientes de licencias de funcionamiento - Municipalidad Distrital de Chorrillos.
"""

from validaciones import (validar_documento, validar_fecha, validar_folios, validar_texto,
                          requisitos_por_riesgo, verificar_requisitos, NIVELES_RIESGO)
from operaciones import (registrar_expediente, buscar_por_codigo, ordenar_por_codigo,
                         actualizar_estado, listar_expedientes, TRAMITES, ESTADOS)
from archivo import guardar_expedientes, cargar_expedientes

ETIQUETAS = ["Código", "RUC o DNI", "Administrado", "Trámite", "Giro", "Nivel de riesgo",
             "Fecha de ingreso", "Folios", "Estado", "Ubicación física"]


def pedir_dato(mensaje, validar, error):
    """Repite la pregunta hasta que el dato ingresado sea válido."""
    dato = input(mensaje)
    while not validar(dato):
        print("  Error:", error)
        dato = input(mensaje)
    return dato.strip()


def elegir_opcion(titulo, opciones):
    """Muestra una lista numerada y devuelve la opción elegida."""
    print(titulo)
    for i in range(len(opciones)):
        print(" ", i + 1, "-", opciones[i])
    numero = pedir_dato("  Opción: ", lambda x: x.strip().isdigit() and 1 <= int(x) <= len(opciones),
                        "elija un número de la lista.")
    return opciones[int(numero) - 1]


def opcion_registrar(expedientes):
    print("\n--- REGISTRAR EXPEDIENTE ---")
    documento = pedir_dato("RUC o DNI: ", validar_documento, "el DNI debe tener 8 dígitos y el RUC 11.")
    razon = pedir_dato("Razón social o nombre: ", validar_texto, "ingrese al menos 3 caracteres.")
    tramite = elegir_opcion("Tipo de trámite:", TRAMITES)
    giro = pedir_dato("Giro del negocio: ", validar_texto, "ingrese al menos 3 caracteres.")
    riesgo = elegir_opcion("Nivel de riesgo:", NIVELES_RIESGO)
    fecha = pedir_dato("Fecha de ingreso (dd/mm/aaaa): ", validar_fecha, "fecha no válida, use el formato dd/mm/aaaa.")
    folios = pedir_dato("Número de folios: ", validar_folios, "debe ser un número mayor que cero.")

    print("Verificación de requisitos (s/n):")
    respuestas = []
    for requisito in requisitos_por_riesgo(riesgo):
        respuesta = pedir_dato("  " + requisito + ": ", lambda x: x.strip().lower() in ("s", "n"), "responda s o n.")
        respuestas.append(respuesta.lower() == "s")
    faltantes = verificar_requisitos(riesgo, respuestas)
    if len(faltantes) > 0:
        print("Expediente no registrado. Requisitos faltantes:", len(faltantes))
        for requisito in faltantes:
            print("  -", requisito)
        return

    codigo = registrar_expediente(expedientes, documento, razon, tramite, giro, riesgo, fecha, folios)
    guardar_expedientes(expedientes)
    print("Expediente registrado con código", codigo)


def opcion_buscar(expedientes):
    print("\n--- BUSCAR EXPEDIENTE ---")
    posicion = buscar_por_codigo(expedientes, input("Código del expediente: "))
    if posicion == -1:
        print("Expediente no encontrado.")
        return
    for i in range(len(ETIQUETAS)):
        print(" ", ETIQUETAS[i].ljust(18), ":", expedientes[posicion][i])


def opcion_ordenar(expedientes):
    ordenar_por_codigo(expedientes)
    guardar_expedientes(expedientes)
    print("\nExpedientes ordenados por código.")


def opcion_actualizar(expedientes):
    print("\n--- ACTUALIZAR ESTADO ---")
    posicion = buscar_por_codigo(expedientes, input("Código del expediente: "))
    if posicion == -1:
        print("Expediente no encontrado.")
        return
    nuevo = elegir_opcion("Nuevo estado:", ESTADOS[1:])
    estante = caja = ""
    if nuevo == "ARCHIVADO":
        estante = pedir_dato("Estante: ", lambda x: x.strip() != "", "ingrese el estante.")
        caja = pedir_dato("Caja: ", lambda x: x.strip() != "", "ingrese la caja.")
    print(actualizar_estado(expedientes, posicion, nuevo, estante, caja))
    guardar_expedientes(expedientes)


def opcion_listar(expedientes):
    print("\n--- LISTADO DE EXPEDIENTES ---")
    if len(expedientes) == 0:
        print("No hay expedientes registrados.")
        return
    for linea in listar_expedientes(expedientes):
        print(linea)
    print("Total de expedientes:", len(expedientes))


def menu_principal():
    expedientes = cargar_expedientes()
    opcion = ""
    while opcion != "0":
        print("\n===== MESA DE PARTES DIGITAL - LICENCIAS DE FUNCIONAMIENTO =====")
        print("1. Registrar expediente")
        print("2. Buscar expediente por código")
        print("3. Ordenar expedientes por código")
        print("4. Actualizar estado del expediente")
        print("5. Listar expedientes")
        print("0. Guardar y salir")
        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            opcion_registrar(expedientes)
        elif opcion == "2":
            opcion_buscar(expedientes)
        elif opcion == "3":
            opcion_ordenar(expedientes)
        elif opcion == "4":
            opcion_actualizar(expedientes)
        elif opcion == "5":
            opcion_listar(expedientes)
        elif opcion == "0":
            guardar_expedientes(expedientes)
            print("Datos guardados. Fin del sistema.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_principal()
