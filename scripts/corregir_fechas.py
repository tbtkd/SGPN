import sqlite3

conn = sqlite3.connect('instance/sgpn_nutricion.db')
cursor = conn.cursor()

# Actualizar fechas vacías a NULL
cursor.execute("UPDATE valoracion_antropometrica SET fecha = NULL WHERE fecha = '' OR fecha IS NULL;")
conn.commit()

print("Registros corregidos:", cursor.rowcount)
conn.close()
