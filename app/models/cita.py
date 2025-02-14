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
        cursor.execute('SELECT * FROM citas WHERE paciente_id = ? AND fecha = ? AND hora = ?',
                       (paciente_id, fecha, hora))
        return cursor.fetchone() is not None 