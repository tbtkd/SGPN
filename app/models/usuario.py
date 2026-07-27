from flask_login import UserMixin
from app.db import get_db
from werkzeug.security import check_password_hash

class Usuario(UserMixin):
    def __init__(self, id, username, password_hash, nombre, apellido_paterno, apellido_materno, email, cedula_profesional=None, rol='nutriologa'):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.email = email
        self.cedula_profesional = cedula_profesional
        self.rol = rol

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute('SELECT * FROM usuarios WHERE id = ?', (int(user_id),)).fetchone()
        if user:
            return Usuario(user['id'], user['username'], user['password_hash'], user['nombre'], user['apellido_paterno'], user['apellido_materno'], user['email'], user['cedula_profesional'], user['rol'])
        return None

    @staticmethod
    def find_by_username(username):
        db = get_db()
        user = db.execute('SELECT * FROM usuarios WHERE username = ?', (username,)).fetchone()
        if user:
            return Usuario(user['id'], user['username'], user['password_hash'], user['nombre'], user['apellido_paterno'], user['apellido_materno'], user['email'], user['cedula_profesional'], user['rol'])
        return None

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
