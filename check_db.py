import sqlite3

def check_db():
    db = sqlite3.connect('pacientes.db')
    cursor = db.cursor()
    
    # Verificar columnas reales
    cursor.execute("PRAGMA table_info(usuarios)")
    columns = [info[1] for info in cursor.fetchall()]
    print(f"Columnas en tabla usuarios: {columns}")
    
    # Verificar datos
    cursor.execute("SELECT * FROM usuarios LIMIT 1")
    row = cursor.fetchone()
    print(f"Fila de ejemplo: {row}")
    
    db.close()

if __name__ == '__main__':
    check_db()
