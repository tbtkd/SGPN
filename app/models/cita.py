import sqlite3
from app.db import get_db

class Cita:
    def __init__(self, paciente_id, fecha, hora, estado='pendiente'):
        self.paciente_id = paciente_id
        self.fecha = fecha
        self.hora = hora
        self.estado = estado

    @staticmethod
    def crear(paciente_id, fecha, hora):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO citas (paciente_id, fecha, hora, estado) VALUES (?, ?, ?, ?)',
                       (paciente_id, fecha, hora, 'pendiente'))
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def existe_cita(paciente_id, fecha, hora):
        db = get_db()
        cursor = db.cursor()
        if hora is not None:
            cursor.execute('SELECT id FROM citas WHERE paciente_id = ? AND fecha = ? AND hora = ?', (paciente_id, fecha, hora))
        else:
            cursor.execute('SELECT id FROM citas WHERE paciente_id = ? AND fecha = ?', (paciente_id, fecha))
        return cursor.fetchone()  # Devuelve el ID de la cita si existe, o None si no existe

    @staticmethod
    def obtener_por_id(cita_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM citas WHERE id = ?', (cita_id,))
        return cursor.fetchone()  # Devuelve la cita si existe 