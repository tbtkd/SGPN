import sqlite3
import os
from datetime import datetime

# Ruta a la base de datos SQLite activa
# Se ajusta para buscar en la ruta especificada por el usuario
db_path = r"C:\Users\Hf\AppData\Local\SistemaPacientes\sgpn_nutricion.db"

if not os.path.exists(db_path):
    print(f"[ERROR] No se encontró la base de datos en: {db_path}")
    # Intentar ruta local como respaldo
    db_path = os.path.join("instance", "sgpn_nutricion.db")
    if not os.path.exists(db_path):
        exit()

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("--- INSPECCIONANDO REGISTROS AFECTADOS EN 'valoracion_antropometrica' ---")

# Obtener todas las columnas de la tabla para identificar cuáles son fechas
cursor.execute("PRAGMA table_info(valoracion_antropometrica)")
columnas = cursor.fetchall()
print("Columnas encontradas:", [col[1] for col in columnas])

# Consultar filas específicas
cursor.execute("SELECT id, fecha FROM valoracion_antropometrica WHERE id IN (10, 11, 12, 13)")
filas = cursor.fetchall()

print("\nValores actuales en las filas 10, 11, 12, 13:")
for fila in filas:
    print(f"ID: {fila[0]} | Valor Fecha: {repr(fila[1])} | Tipo Python: {type(fila[1])}")

# APLICAR SANANEMIENTO DIRECTO
print("\n--- APLICANDO SANANEMIENTO DE FECHAS ---")

# 1. Corregir registros específicos de la lista
fecha_defecto = datetime.now().strftime("%Y-%m-%d")

cursor.execute("""
    UPDATE valoracion_antropometrica 
    SET fecha = ? 
    WHERE (id IN (10, 11, 12, 13) 
       OR fecha IS NULL 
       OR fecha = '' 
       OR fecha = 'None')
       AND fecha != '1900-01-01'
""", (fecha_defecto,))

# 2. Convertir cualquier posible valor numérico/timestamp a formato de fecha texto YYYY-MM-DD
# Nota: SQLite no tiene una función 'typeof' estándar en todas las versiones, 
# pero es soportada en la mayoría de las implementaciones modernas.
try:
    cursor.execute("""
        UPDATE valoracion_antropometrica 
        SET fecha = date(fecha / 1000, 'unixepoch') 
        WHERE typeof(fecha) = 'integer' AND fecha > 1000000000000;
    """)

    cursor.execute("""
        UPDATE valoracion_antropometrica 
        SET fecha = date(fecha, 'unixepoch') 
        WHERE typeof(fecha) = 'integer' AND fecha <= 1000000000000;
    """)
except sqlite3.OperationalError as e:
    print(f"[ADVERTENCIA] Error al intentar convertir timestamps: {e}")

conn.commit()
print(f"[ÉXITO] Filas corregidas. Se asignó '{fecha_defecto}' a las fechas inválidas.")
conn.close()
