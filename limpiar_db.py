import sqlite3
from datetime import date

def limpiar_fechas_valoracion():
    db_path = 'instance/sgpn_nutricion.db'
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Obtener todas las valoraciones
        cursor.execute("SELECT id, fecha FROM valoracion_antropometrica")
        rows = cursor.fetchall()
        
        for row in rows:
            id_val, fecha_val = row
            # Si la fecha no es una cadena válida (ej. es un entero o nulo), corregir
            if fecha_val is None or not isinstance(fecha_val, str) or len(fecha_val) != 10:
                print(f"[INFO] Corrigiendo fecha para ID {id_val}: {fecha_val}")
                cursor.execute("UPDATE valoracion_antropometrica SET fecha = ? WHERE id = ?", ('1900-01-01', id_val))
        
        conn.commit()
        conn.close()
        print("[ÉXITO] Base de datos limpiada correctamente.")
    except Exception as e:
        print(f"[ERROR] Fallo al limpiar la base de datos: {e}")

if __name__ == "__main__":
    limpiar_fechas_valoracion()
