# Mesa de partes digital: licencias de funcionamiento

Prototipo en Python para registrar, validar, buscar, ordenar y almacenar los expedientes de licencias de funcionamiento de la Municipalidad Distrital de Chorrillos.

Curso: Fundamentos de Programación (CIIN1205P), Universidad Privada del Norte.

## Requisitos

Python 3.8 o superior. No usa librerías externas.

## Cómo ejecutar

```
python main.py
```

Para ejecutar las pruebas de casos simples:

```
python pruebas.py
```

## Estructura

| Archivo | Contenido |
|---|---|
| `main.py` | Menú principal y opciones del sistema |
| `validaciones.py` | Validación de RUC o DNI, fecha, folios y requisitos por nivel de riesgo |
| `operaciones.py` | Registro, búsqueda secuencial, ordenamiento por burbuja, estados y listado |
| `archivo.py` | Guardado y carga de expedientes en `expedientes.txt` |
| `pruebas.py` | Pruebas de las funciones con casos simples |

Los expedientes se guardan en `expedientes.txt`, un expediente por línea y sus datos separados por punto y coma.
