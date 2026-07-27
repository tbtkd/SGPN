from app import db_orm as db
from datetime import datetime, timedelta
from app.db import query_db

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(50), nullable=False)
    apellido_materno = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    telefono = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='activo')
    
    # Importación diferida para evitar error de resolución de nombres
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def valoraciones(self):
        from app.models.valoracion import Valoracion
        return Valoracion.query.filter_by(paciente_id=self.id).all()

    @staticmethod
    def crear(nombre, apellido_paterno, apellido_materno, genero, fecha_nacimiento, telefono, correo, ciudad):
        try:
            nuevo_paciente = Paciente(
                nombre=nombre,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                genero=genero,
                fecha_nacimiento=datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date(),
                telefono=telefono,
                correo=correo,
                ciudad=ciudad
            )
            db.session.add(nuevo_paciente)
            db.session.commit()
            return True, "Paciente creado exitosamente"
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def contar_activos():
        return Paciente.query.filter_by(status='activo').count()

    @staticmethod
    def calcular_crecimiento_mensual():
        # Implementación básica: contar pacientes creados en el mes actual
        inicio_mes = datetime.utcnow().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        return Paciente.query.filter(Paciente.fecha_registro >= inicio_mes).count()

    @staticmethod
    def contar_en_seguimiento():
        # Asumimos que 'en seguimiento' es un estatus o lógica específica
        return Paciente.query.filter_by(status='seguimiento').count()

    @staticmethod
    def buscar(busqueda, status='activo'):
        query = Paciente.query.filter_by(status=status)
        if busqueda:
            query = query.filter(
                (Paciente.nombre.contains(busqueda)) |
                (Paciente.apellido_paterno.contains(busqueda)) |
                (Paciente.apellido_materno.contains(busqueda))
            )
        return query.all()

    @staticmethod
    def obtener_por_id(id):
        return Paciente.query.get(id)

    @staticmethod
    def actualizar(id, nombre, apellido_paterno, apellido_materno, genero, fecha_nacimiento, telefono, correo, ciudad, status):
        paciente = Paciente.query.get(id)
        if paciente:
            paciente.nombre = nombre
            paciente.apellido_paterno = apellido_paterno
            paciente.apellido_materno = apellido_materno
            paciente.genero = genero
            paciente.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
            paciente.telefono = telefono
            paciente.correo = correo
            paciente.ciudad = ciudad
            paciente.status = status
            db.session.commit()

    @staticmethod
    def actualizar_estatus(id, status):
        paciente = Paciente.query.get(id)
        if paciente:
            paciente.status = status
            db.session.commit()

    @staticmethod
    def obtener_sin_valoracion_reciente(dias=30):
        # Implementación placeholder
        return []

    @staticmethod
    def obtener_proximos(fecha=None):
        # Implementación placeholder
        return []

    @staticmethod
    def obtener_pendientes_por_agendar():
        # Pacientes cuya última cita haya sido anterior a su última valoración
        # O que no tengan cita futura
        query = '''
            SELECT p.id, p.nombre, p.apellido_paterno, p.apellido_materno,
                   MAX(c.fecha) as ultima_cita,
                   (JULIANDAY('now') - JULIANDAY(MAX(c.fecha))) as dias_transcurridos
            FROM pacientes p
            LEFT JOIN citas c ON p.id = c.paciente_id
            GROUP BY p.id
            HAVING MAX(c.fecha) < DATE('now', '-30 days') OR MAX(c.fecha) IS NULL
        '''
        return query_db(query, [])

    @staticmethod
    def obtener_sin_valoracion_reciente(dias=30):
        # Pacientes cuya última cita haya sido mayor a 30 días desde su última valoración
        fecha_limite = (datetime.now() - timedelta(days=dias)).strftime('%Y-%m-%d')
        query = '''
            SELECT p.id, p.nombre, p.apellido_paterno, p.apellido_materno, 
                   MAX(v.fecha) as ultima_valoracion,
                   (JULIANDAY('now') - JULIANDAY(MAX(v.fecha))) as dias_transcurridos
            FROM pacientes p
            JOIN valoracion_antropometrica v ON p.id = v.paciente_id
            GROUP BY p.id
            HAVING MAX(v.fecha) < ?
        '''
        return query_db(query, [fecha_limite])

    @staticmethod
    def obtener_pendientes_reagendamiento():
        # Implementación placeholder
        return []
