import sqlite3

conn = sqlite3.connect('instance/sgpn_nutricion.db')
cursor = conn.cursor()

cursor.execute("SELECT id, fecha FROM valoracion_antropometrica")
for row in cursor.fetchall():
    print(row)

conn.close()
