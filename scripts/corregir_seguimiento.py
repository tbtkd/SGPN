import sqlite3

conn = sqlite3.connect('instance/sgpn_nutricion.db')
cursor = conn.cursor()

# Actualizar filas donde fecha_seguimiento_15d sea 'NULL' o NULL o vacío a '1900-01-01'
cursor.execute("UPDATE valoracion_antropometrica SET fecha_seguimiento_15d = '1900-01-01' WHERE fecha_seguimiento_15d = 'NULL' OR fecha_seguimiento_15d IS NULL OR fecha_seguimiento_15d = ''")
conn.commit()

cursor.execute("SELECT id, fecha_seguimiento_15d FROM valoracion_antropometrica LIMIT 10")
for row in cursor.fetchall():
    print(row)

conn.close()
