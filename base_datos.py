"""
Módulo de base de datos.
Guarda y recupera los expedientes en MySQL con el conector oficial
mysql-connector-python. Si MySQL no está disponible, las funciones
devuelven None o False y el programa sigue trabajando con el archivo de texto.
"""

try:
    import mysql.connector
    CONECTOR_INSTALADO = True
except ImportError:
    CONECTOR_INSTALADO = False

# Datos de conexión: cambiar la contraseña por la de MySQL Workbench
CONFIGURACION = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "mesa_partes_digital",
}

# Posición de cada dato dentro del expediente (igual que en operaciones.py)
CODIGO, DOCUMENTO, RAZON_SOCIAL, TRAMITE, GIRO, RIESGO, FECHA, FOLIOS, ESTADO, UBICACION = range(10)


def conectar():
    """Abre la conexión con MySQL. Devuelve la conexión o None si no se pudo conectar."""
    if not CONECTOR_INSTALADO:
        return None
    try:
        return mysql.connector.connect(**CONFIGURACION)
    except mysql.connector.Error:
        return None


def fecha_a_mysql(fecha):
    """Convierte dd/mm/aaaa en aaaa-mm-dd, el formato del tipo DATE de MySQL."""
    dia, mes, anio = fecha.split("/")
    return anio + "-" + mes + "-" + dia


def fecha_desde_mysql(fecha):
    """Convierte la fecha leída de MySQL al formato dd/mm/aaaa del programa."""
    return fecha.strftime("%d/%m/%Y")


def guardar_expedientes_bd(expedientes):
    """
    Inserta los expedientes nuevos y actualiza el estado y la ubicación de los existentes.
    Devuelve True si se guardaron o False si no hubo conexión.
    """
    conexion = conectar()
    if conexion is None:
        return False
    cursor = conexion.cursor()
    for expediente in expedientes:
        cursor.execute("SELECT id FROM expediente WHERE codigo = %s", (expediente[CODIGO],))
        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO expediente (codigo, documento, razon_social, tramite, giro, riesgo, "
                "fecha_ingreso, folios, estado, ubicacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (expediente[CODIGO], expediente[DOCUMENTO], expediente[RAZON_SOCIAL], expediente[TRAMITE],
                 expediente[GIRO], expediente[RIESGO], fecha_a_mysql(expediente[FECHA]),
                 expediente[FOLIOS], expediente[ESTADO], expediente[UBICACION]))
        else:
            cursor.execute("UPDATE expediente SET estado = %s, ubicacion = %s WHERE codigo = %s",
                           (expediente[ESTADO], expediente[UBICACION], expediente[CODIGO]))
    conexion.commit()
    cursor.close()
    conexion.close()
    return True


def cargar_expedientes_bd():
    """Devuelve la lista de expedientes guardados en MySQL, o None si no hubo conexión."""
    conexion = conectar()
    if conexion is None:
        return None
    cursor = conexion.cursor()
    cursor.execute("SELECT codigo, documento, razon_social, tramite, giro, riesgo, fecha_ingreso, "
                   "folios, estado, ubicacion FROM expediente ORDER BY id")
    expedientes = []
    for fila in cursor.fetchall():
        expediente = list(fila)
        expediente[FECHA] = fecha_desde_mysql(fila[FECHA])
        expedientes.append(expediente)
    cursor.close()
    conexion.close()
    return expedientes
