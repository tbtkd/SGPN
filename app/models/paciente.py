from app.db import get_db, query_db
from datetime import datetime
import sqlite3

class Paciente:
    @staticmethod
    def crear(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad):
        """
        Crea un nuevo paciente en la base de datos
        Args:
            nombre (str): Nombre del paciente
            apellido_paterno (str): Apellido paterno del paciente
            apellido_materno (str): Apellido materno del paciente
            fecha_nacimiento (str): Fecha de nacimiento del paciente
            telefono (str): Teléfono del paciente
            correo (str): Correo electrónico del paciente
            ciudad (str): Ciudad del paciente
        Returns:
            bool: True si el paciente se registró exitosamente, False en caso contrario
            str: Mensaje de éxito o error
        """
        try:
            db = get_db()
            db.execute(
                '''INSERT INTO pacientes (
                    nombre, apellido_paterno, apellido_materno, fecha_nacimiento, 
                    telefono, correo, ciudad, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 'activo')''',
                [nombre, apellido_paterno, apellido_materno, fecha_nacimiento, 
                 telefono, correo, ciudad]
            )
            db.commit()
            return True, "Paciente registrado exitosamente"
        except sqlite3.IntegrityError:
            db.rollback()
            return False, "El correo electrónico ya está registrado"
        except Exception as e:
            db.rollback()
            return False, str(e)

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
        """
        Actualiza los datos de un paciente
        Args:
            id (int): ID del paciente
            nombre (str): Nombre del paciente
            apellido_paterno (str): Apellido paterno
            apellido_materno (str): Apellido materno
            fecha_nacimiento (str): Fecha de nacimiento
            telefono (str): Teléfono
            correo (str): Correo electrónico
            ciudad (str): Ciudad
            status (str): Estado del paciente (activo/inactivo)
        """
        try:
            db = get_db()
            db.execute('''
                UPDATE pacientes 
                SET nombre = ?, apellido_paterno = ?, apellido_materno = ?, 
                    fecha_nacimiento = ?, telefono = ?, correo = ?, ciudad = ?, 
                    status = ?
                WHERE id = ?
            ''', [nombre, apellido_paterno, apellido_materno, fecha_nacimiento,
                  telefono, correo, ciudad, status, id])
            db.commit()
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def actualizar_estatus(paciente_id, status):
        """
        Actualiza el estado de un paciente
        Args:
            paciente_id (int): ID del paciente
            status (str): Nuevo estado (activo/inactivo)
        """
        try:
            db = get_db()
            db.execute('UPDATE pacientes SET status = ? WHERE id = ?', 
                      [status, paciente_id])
            db.commit()
        except Exception as e:
            db.rollback()
            raise e

    @staticmethod
    def buscar(busqueda, status='activo'):
        """
        Busca pacientes por nombre o apellidos
        Args:
            busqueda (str): Término de búsqueda
            status (str): Estado del paciente (activo/inactivo)
        Returns:
            list: Lista de pacientes que coinciden con la búsqueda
        """
        if busqueda:
            return query_db('''
                SELECT * FROM pacientes 
                WHERE (nombre LIKE ? OR apellido_paterno LIKE ? OR apellido_materno LIKE ?)
                AND status = ?
                ORDER BY nombre
                ''',
                [f'%{busqueda}%', f'%{busqueda}%', f'%{busqueda}%', status])
        else:
            return query_db('SELECT * FROM pacientes WHERE status = ? ORDER BY nombre', [status])