import sqlite3
import csv
import os

# 1. Conectar a la base de datos
conexion = sqlite3.connect("fantasy_data.sqlite3")
cursor = conexion.cursor()

# 2. Diccionario con los archivos CSV y el nombre de tabla que queremos asignarles
archivos_csv = {
    "data/league_data.csv": "leagues",
    "data/performance_data.csv": "performances",
    "data/team_player_data.csv": "team_player",
    "data/team_data.csv": "teams"
}

# 3. Recorrer cada archivo e importarlo automáticamente
for ruta_archivo, nombre_tabla in archivos_csv.items():
    # Verificar primero si el archivo existe para evitar errores colaterales
    if not os.path.exists(ruta_archivo):
        print(f"⚠️ Advertencia: No se encontró el archivo {ruta_archivo}, se saltará.")
        continue

    print(f"Procesando {ruta_archivo}...")

    with open(ruta_archivo, "r", encoding="utf-8") as archivo_csv:
        lector = csv.reader(archivo_csv)
        
        # Leer la primera fila (los encabezados)
        columnas = next(lector)
        
        # Eliminar la tabla si ya existía para evitar duplicar datos al re-ejecutar
        cursor.execute(f"DROP TABLE IF EXISTS {nombre_tabla}")
        
        # Crear la tabla dinámicamente usando los encabezados
        columnas_sql = ", ".join([f"[{col}] TEXT" for col in columnas])
        cursor.execute(f"CREATE TABLE {nombre_tabla} ({columnas_sql})")
        
        # Insertar todos los registros del CSV
        signos_interrogacion = ", ".join(["?"] * len(columnas))
        cursor.executemany(f"INSERT INTO {nombre_tabla} VALUES ({signos_interrogacion})", lector)
        
        print(f"  └─ ¡Tabla '{nombre_tabla}' creada e importada con éxito!")

# Guardar los cambios finales y cerrar la conexión
conexion.commit()
conexion.close()

print("\n🎉 ¡Todos los archivos CSV se han cargado correctamente a 'fantasy_data.sqlite3'!")
