import sqlite3

def update_db():
    db = sqlite3.connect('pacientes.db')
    cursor = db.cursor()
    
    # Verificar columnas actuales
    cursor.execute("PRAGMA table_info(usuarios)")
    columns = [info[1] for info in cursor.fetchall()]
    
    # Verificar qué columnas faltan
    missing = []
    if 'nombre' not in columns: missing.append("nombre")
    if 'apellido_paterno' not in columns: missing.append("apellido_paterno")
    if 'apellido_materno' not in columns: missing.append("apellido_materno")
    if 'email' not in columns: missing.append("email")
    if 'cedula_profesional' not in columns: missing.append("cedula_profesional")
    if 'rol' not in columns: missing.append("rol")
    
    if missing:
        print(f"Actualizando tabla usuarios, faltan: {missing}")
        try:
            if 'nombre' in missing: cursor.execute("ALTER TABLE usuarios ADD COLUMN nombre TEXT DEFAULT 'Aurora'")
            if 'apellido_paterno' in missing: cursor.execute("ALTER TABLE usuarios ADD COLUMN apellido_paterno TEXT DEFAULT 'Ángeles'")
            if 'apellido_materno' in missing: cursor.execute("ALTER TABLE usuarios ADD COLUMN apellido_materno TEXT DEFAULT 'Pérez'")
            if 'email' in missing: cursor.execute("ALTER TABLE usuarios ADD COLUMN email TEXT DEFAULT 'aurora@clinica.com'")
            if 'cedula_profesional' in missing: cursor.execute("ALTER TABLE usuarios ADD COLUMN cedula_profesional TEXT")
            if 'rol' in missing: cursor.execute("ALTER TABLE usuarios ADD COLUMN rol TEXT DEFAULT 'nutriologa'")
            
            # Migrar datos si existía la columna 'apellido'
            if 'apellido' in columns:
                cursor.execute("UPDATE usuarios SET apellido_paterno = apellido")
            
            cursor.execute("UPDATE usuarios SET email = 'aurora@clinica.com' WHERE email IS NULL")
            db.commit()
            print("Tabla usuarios actualizada exitosamente.")
        except Exception as e:
            print(f"Error al actualizar: {e}")
    else:
        print("La tabla usuarios ya está actualizada.")
    
    db.close()

if __name__ == '__main__':
    update_db()
