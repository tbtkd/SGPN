import sqlite3
from datetime import datetime

def insertar_citas_hoy():
    db_path = 'pacientes.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Obtener 15 IDs de pacientes activos
    cursor.execute("SELECT id FROM pacientes WHERE status = 'activo' LIMIT 15")
    pacientes = cursor.fetchall()

    if not pacientes:
        print("No hay pacientes activos para asignar citas.")
        conn.close()
        return

    fecha_hoy = datetime.now().strftime('%Y-%m-%d')
    
    print(f"Insertando 15 citas para el día {fecha_hoy}...")
    
    for i, (paciente_id,) in enumerate(pacientes):
        # Asignar horas diferentes para cada cita
        hora = f"{9 + (i % 8):02d}:{ (i % 4) * 15:02d}:00"
        cursor.execute("INSERT INTO citas (paciente_id, fecha, hora, estado) VALUES (?, ?, ?, ?)",
                       (paciente_id, fecha_hoy, hora, "pendiente"))

    conn.commit()
    conn.close()
    print("15 citas para hoy insertadas exitosamente.")

if __name__ == "__main__":
    insertar_citas_hoy()
