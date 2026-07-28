import sqlite3
import os

source_db = 'instance/_sgpn_nutricion.db'
target_db = 'instance/sgpn_nutricion.db'

print(f"Copiando datos desde {source_db} hacia {target_db}...")

if not os.path.exists(source_db):
    print(f"Error: El archivo de origen {source_db} no existe.")
    exit(1)

# Conectar origen y destino
src_conn = sqlite3.connect(source_db)
src_cursor = src_conn.cursor()

tgt_conn = sqlite3.connect(target_db)
tgt_cursor = tgt_conn.cursor()

# Obtener lista de tablas en el origen
src_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
tables = [row[0] for row in src_cursor.fetchall()]

print(f"Tablas encontradas en origen: {tables}")

# Desactivar foreign keys temporalmente para evitar conflictos de orden de inserción
tgt_cursor.execute("PRAGMA foreign_keys = OFF;")

for table in tables:
    try:
        # Obtener datos de la tabla origen
        src_cursor.execute(f"SELECT * FROM {table}")
        rows = src_cursor.fetchall()
        
        if not rows:
            print(f"Tabla {table}: Sin registros para copiar.")
            continue
            
        # Obtener columnas
        src_cursor.execute(f"PRAGMA table_info({table})")
        columns_info = src_cursor.fetchall()
        col_names = [info[1] for info in columns_info]
        
        # Limpiar tabla destino antes de insertar
        tgt_cursor.execute(f"DELETE FROM {table}")
        
        placeholders = ", ".join(["?"] * len(col_names))
        columns_str = ", ".join([f'"{c}"' for c in col_names])
        sql = f"INSERT OR REPLACE INTO {table} ({columns_str}) VALUES ({placeholders})"
        
        tgt_cursor.executemany(sql, rows)
        tgt_conn.commit()
        print(f"Tabla {table}: {len(rows)} registros copiados exitosamente.")
    except Exception as e:
        print(f"Error al copiar la tabla {table}: {e}")
        tgt_conn.rollback()

tgt_cursor.execute("PRAGMA foreign_keys = ON;")
src_conn.close()
tgt_conn.close()
print("¡Proceso de copiado y validación de esquema completado con éxito!")
