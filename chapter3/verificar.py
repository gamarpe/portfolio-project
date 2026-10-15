import sqlite3

# 1. Conectar a la base de datos local
conexion = sqlite3.connect("fantasy_data.sqlite3")
cursor = conexion.cursor()


def contar_filas(consulta, descripcion):
    """Función auxiliar para ejecutar el conteo e imprimirlo limpiamente"""
    cursor.execute(consulta)
    resultado = cursor.fetchone()[0]  # Trae el primer valor (el conteo)
    print(f"{descripcion}: {resultado}")


print("--- VERIFICACIÓN DE REGISTROS CARGADOS ---")

# 2. Sustitución de cada comando de la imagen del autor:

# sqlite> select count(*) from player;
contar_filas("SELECT COUNT(*) FROM players", "Total de jugadores (players)")

# sqlite> select count(*) from performance;
contar_filas(
    "SELECT COUNT(*) FROM performances", "Total de rendimientos (performances)"
)

# sqlite> select count(*) from performance where last_changed_date > '2024-04-01';
# Nota: Usamos corchetes [last_changed_date] por seguridad debido al formato de columnas del CSV
contar_filas(
    "SELECT COUNT(*) FROM performances WHERE [last_changed_date] > '2024-04-01'",
    "Rendimientos con fecha posterior a 2024-04-01",
)

# sqlite> select count(*) from league;
contar_filas("SELECT COUNT(*) FROM leagues", "Total de ligas (leagues)")

# sqlite> select count(*) from team;
contar_filas("SELECT COUNT(*) FROM teams", "Total de equipos (teams)")

# 3. Cerrar la conexión de forma segura
conexion.close()
