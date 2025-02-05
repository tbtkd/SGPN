from app.db import get_db, query_db
from datetime import datetime

class Paciente:
    @staticmethod
    def crear(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad):
        db = get_db()
        db.execute(
            'INSERT INTO pacientes (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad)
        )
        db.commit()

    @staticmethod
    def obtener_todos():
        return query_db('''
            SELECT p.*, 
                   (SELECT fecha_pago FROM pagos WHERE paciente_id = p.id ORDER BY fecha_pago DESC LIMIT 1) as ultimo_pago
            FROM pacientes p
        ''')

    @staticmethod
    def obtener_por_id(id):
        return query_db('SELECT * FROM pacientes WHERE id = ?', [id], one=True)

    @staticmethod
    def actualizar(id, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad, status):
        db = get_db()
        db.execute(
            'UPDATE pacientes SET nombre = ?, apellido_paterno = ?, apellido_materno = ?, fecha_nacimiento = ?, telefono = ?, correo = ?, ciudad = ?, estatus = ? WHERE id = ?',
            (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad, status, id)
        )
        db.commit()

    @staticmethod
    def actualizar_estatus(paciente_id, status):
        db = get_db()
        db.execute('UPDATE pacientes SET estatus = ? WHERE id = ?', (status, paciente_id))
        db.commit()

