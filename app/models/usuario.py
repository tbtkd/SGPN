from flask_login import UserMixin
from datetime import datetime
from app import db_orm

class Usuario(db_orm.Model, UserMixin):
    __tablename__ = 'usuarios'
    
    id = db_orm.Column(db_orm.Integer, primary_key=True)
    username = db_orm.Column(db_orm.String(50), nullable=False)
    password_hash = db_orm.Column(db_orm.String(256), nullable=False)
    nombre = db_orm.Column(db_orm.String(50), nullable=True)
    email = db_orm.Column(db_orm.String(120), nullable=True)
    cedula_profesional = db_orm.Column(db_orm.String(30), nullable=True)
    rol = db_orm.Column(db_orm.String(20), default='nutriologa')
    apellido_paterno = db_orm.Column(db_orm.String(50), nullable=True)
    apellido_materno = db_orm.Column(db_orm.String(50), nullable=True)

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

    @staticmethod
    def get(user_id):
        return Usuario.query.get(int(user_id))

    @staticmethod
    def find_by_username(username):
        return Usuario.query.filter_by(username=username).first()

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)
