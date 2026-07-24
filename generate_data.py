import sqlite3
from datetime import datetime, timedelta
import random

def generate_dummy_data():
    db_path = 'pacientes.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Limpiar tablas excepto usuarios
    tables_to_clear = ['valoracion_antropometrica', 'citas', 'pagos', 'historial_clinico', 'pacientes']
    for table in tables_to_clear:
        cursor.execute(f"DELETE FROM {table}")
    
    # Reset autoincrement
    cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('" + "','".join(tables_to_clear) + "')")

    # 2. Generar 20 pacientes activos (con historial completo)
    for i in range(1, 21):
        nombre = f"Paciente_{i}"
        apellido_paterno = f"ApellidoP_{i}"
        apellido_materno = f"ApellidoM_{i}"
        genero = "hombre" if i % 2 == 0 else "mujer"
        
        cursor.execute("""
            INSERT INTO pacientes (nombre, apellido_paterno, apellido_materno, genero, fecha_nacimiento, telefono, correo, ciudad, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nombre, apellido_paterno, apellido_materno, genero, "1990-01-01", f"555000{i:03d}", f"paciente{i}@example.com", "Ciudad de México", "activo"))
        paciente_id = cursor.lastrowid

        # Historial clínico
        cursor.execute("""
            INSERT INTO historial_clinico (paciente_id, cirugias, padecimientos, medicamentos, suplementos, enfermedades_previas, enfermedades_actuales, tipo_actividad_fisica, frecuencia_actividad_fisica, tiempo_actividad_fisica, numero_comidas_diarias, alimentos_normales, alimentos_no_gustados)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (paciente_id, "Ninguna", "Ninguno", "Ninguno", "Ninguno", "Ninguna", "Ninguna", "Caminar", "3 veces por semana", "30 min", 3, "Pollo, Arroz", "Brócoli"))

        # 10 valoraciones, citas y pagos
        for j in range(1, 11):
            dias_atras = (11 - j) * 30
            fecha = (datetime.now() - timedelta(days=dias_atras)).strftime('%Y-%m-%d')
            
            cursor.execute("""
                INSERT INTO valoracion_antropometrica (
                    paciente_id, numero_cita, fecha, estatura, peso, imc, grasa, cintura, torax, 
                    brazo, cadera, pierna, pantorrilla, tension_arterial, frecuencia_cardiaca, 
                    bicep, tricep, suprailiaco, subescapular, porcentaje_grasa
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                paciente_id, j, fecha, 1.70, 75.0, 25.9, 20.0, 80.0, 90.0, 
                30.0, 95.0, 50.0, 35.0, "120/80", 70, 
                10.0, 15.0, 20.0, 25.0, "Normal"
            ))

            cursor.execute("INSERT INTO citas (paciente_id, fecha, hora, estado) VALUES (?, ?, ?, ?)",
                           (paciente_id, fecha, "10:00:00", "completada"))

            cursor.execute("INSERT INTO pagos (paciente_id, fecha_pago) VALUES (?, ?)",
                           (paciente_id, fecha))

    # 3. Generar 13 pacientes inactivos
    for i in range(1, 14):
        nombre = f"Inactivo_{i}"
        apellido_paterno = f"ApellidoP_{i}"
        apellido_materno = f"ApellidoM_{i}"
        genero = "hombre" if i % 2 == 0 else "mujer"
        
        cursor.execute("""
            INSERT INTO pacientes (nombre, apellido_paterno, apellido_materno, genero, fecha_nacimiento, telefono, correo, ciudad, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nombre, apellido_paterno, apellido_materno, genero, "1990-01-01", f"555999{i:03d}", f"inactivo{i}@example.com", "Ciudad de México", "inactivo"))

    # 4. Generar 10 registros para próximas citas
    for i in range(1, 11):
        nombre = f"ProximaCita_{i}"
        apellido_paterno = f"ApellidoP_{i}"
        apellido_materno = f"ApellidoM_{i}"
        genero = "hombre" if i % 2 == 0 else "mujer"
        
        cursor.execute("""
            INSERT INTO pacientes (nombre, apellido_paterno, apellido_materno, genero, fecha_nacimiento, telefono, correo, ciudad, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nombre, apellido_paterno, apellido_materno, genero, "1990-01-01", f"555888{i:03d}", f"proximacita{i}@example.com", "Ciudad de México", "activo"))
        paciente_id = cursor.lastrowid
        
        # Cita futura
        fecha_futura = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
        cursor.execute("INSERT INTO citas (paciente_id, fecha, hora, estado) VALUES (?, ?, ?, ?)",
                       (paciente_id, fecha_futura, "10:00:00", "pendiente"))

    conn.commit()
    conn.close()
    print("Datos dummy generados exitosamente.")

if __name__ == "__main__":
    generate_dummy_data()
