from flask_login import UserMixin
from app.db import get_db
from werkzeug.security import check_password_hash

class Usuario(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    @staticmethod
    def get(user_id):
        db = get_db()
        # Convertir user_id a int si es necesario, ya que sqlite3 puede devolverlo como string
        user = db.execute('SELECT * FROM usuarios WHERE id = ?', (int(user_id),)).fetchone()
        if user:
            return Usuario(user['id'], user['username'], user['password_hash'])
        return None

    @staticmethod
    def find_by_username(username):
        db = get_db()
        user = db.execute('SELECT * FROM usuarios WHERE username = ?', (username,)).fetchone()
        if user:
            return Usuario(user['id'], user['username'], user['password_hash'])
        return None

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
