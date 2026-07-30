from app import db_orm as db
from datetime import datetime, timedelta
from sqlalchemy import text

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

    @property
    def valoraciones(self):
        from app.models.valoracion_antropometrica import ValoracionAntropometrica
        return ValoracionAntropometrica.query.filter_by(paciente_id=self.id).all()

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
        inicio_mes = datetime.utcnow().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        return Paciente.query.filter(Paciente.fecha_registro >= inicio_mes).count()

    @staticmethod
    def contar_en_seguimiento():
        return Paciente.query.filter_by(status='seguimiento').count()

    @staticmethod
    def buscar(busqueda, status='activo'):
        from app.models.valoracion_antropometrica import ValoracionAntropometrica
        from app.models.cita import Cita
        from sqlalchemy import func

        # Subquery para obtener la fecha de la última valoración (o última cita si aplica)
        # Usaremos la fecha de la última valoración antropométrica como referencia de consulta/cita
        subq_val = db.session.query(
            ValoracionAntropometrica.paciente_id,
            func.max(ValoracionAntropometrica.fecha).label('ultima_val')
        ).group_by(ValoracionAntropometrica.paciente_id).subquery()

        query = db.session.query(
            Paciente,
            subq_val.c.ultima_val.label('ultima_consulta')
        ).outerjoin(
            subq_val, Paciente.id == subq_val.c.paciente_id
        ).filter(Paciente.status == status)

        if busqueda:
            query = query.filter(
                (Paciente.nombre.contains(busqueda)) |
                (Paciente.apellido_paterno.contains(busqueda)) |
                (Paciente.apellido_materno.contains(busqueda))
            )

        resultados = query.all()
        
        # Mapear los resultados a un formato que el template espera (dict o objeto con atributo/clave ultima_consulta)
        pacientes_con_consulta = []
        for pac, ultima_val in resultados:
            # Adjuntamos dinámicamente la propiedad ultima_consulta al objeto Paciente
            pac.ultima_consulta = ultima_val
            pacientes_con_consulta.append(pac)

        return pacientes_con_consulta

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
    def obtener_proximos(fecha=None):
        return []

    @staticmethod
    def obtener_pendientes_por_agendar():
        query = text('''
            SELECT p.id, p.nombre, p.apellido_paterno, p.apellido_materno,
                   MAX(c.fecha) as ultima_cita,
                   (JULIANDAY('now') - JULIANDAY(MAX(c.fecha))) as dias_transcurridos
            FROM pacientes p
            LEFT JOIN citas c ON p.id = c.paciente_id
            GROUP BY p.id
            HAVING MAX(c.fecha) < DATE('now', '-30 days') OR MAX(c.fecha) IS NULL
        ''')
        result = db.session.execute(query)
        return result.fetchall()

    @staticmethod
    def obtener_sin_valoracion_reciente(dias=30):
        fecha_limite = (datetime.now() - timedelta(days=dias)).strftime('%Y-%m-%d')
        query = text('''
            SELECT p.id, p.nombre, p.apellido_paterno, p.apellido_materno, 
                   MAX(v.fecha) as ultima_valoracion,
                   (JULIANDAY('now') - JULIANDAY(MAX(v.fecha))) as dias_transcurridos
            FROM pacientes p
            JOIN valoracion_antropometrica v ON p.id = v.paciente_id
            GROUP BY p.id
            HAVING MAX(v.fecha) < :fecha_limite
        ''')
        result = db.session.execute(query, {"fecha_limite": fecha_limite})
        return result.fetchall()

    @staticmethod
    def obtener_pendientes_reagendamiento():
        return []
