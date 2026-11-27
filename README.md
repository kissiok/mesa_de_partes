# Mesa de partes digital: licencias de funcionamiento

Prototipo en Python para registrar, validar, buscar, ordenar y almacenar los expedientes de licencias de funcionamiento de la Municipalidad Distrital de Chorrillos.

Curso: Fundamentos de Programación (CIIN1205P), Universidad Privada del Norte.

## Requisitos

- Python 3.8 o superior.
- MySQL 8 con MySQL Workbench (opcional). Sin MySQL el programa trabaja solo con el archivo de texto.
- Conector de MySQL para Python:

```
pip install mysql-connector-python
```

## Preparar la base de datos

1. Abrir `mesa_partes.sql` en MySQL Workbench y ejecutarlo completo (botón del rayo).
2. En `base_datos.py`, escribir la contraseña de MySQL en `CONFIGURACION["password"]`.

## Cómo ejecutar

```
python main.py
```

Pruebas de las funciones y pruebas con los datos recogidos en campo:

```
python pruebas.py
python pruebas_campo.py
```

## Estructura

| Archivo | Contenido |
|---|---|
| `main.py` | Menú principal y opciones del sistema |
| `validaciones.py` | Validación de RUC o DNI, fecha (con años bisiestos), folios, texto y requisitos por nivel de riesgo |
| `operaciones.py` | Registro, búsqueda secuencial, ordenamiento por burbuja, estados y listado |
| `archivo.py` | Guardado y carga de expedientes en `expedientes.txt` |
| `base_datos.py` | Guardado y carga de expedientes en MySQL |
| `mesa_partes.sql` | Script de la base de datos para MySQL Workbench |
| `pruebas.py` | Pruebas de las funciones con casos simples |
| `pruebas_campo.py` | Casos de prueba con los datos de la observación de campo |

Los expedientes se guardan siempre en `expedientes.txt` (un expediente por línea, datos separados por punto y coma) y, si hay conexión, también en la tabla `expediente` de MySQL.
