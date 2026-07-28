from app import db_orm as db
from datetime import datetime

class Cita(db.Model):
    __tablename__ = 'citas'
    
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id', ondelete='CASCADE'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    estado = db.Column(db.String(20), default='pendiente')
    
    paciente = db.relationship('Paciente', backref=db.backref('citas', lazy=True))

    @staticmethod
    def crear(paciente_id, fecha, hora):
        try:
            nueva_cita = Cita(
                paciente_id=paciente_id,
                fecha=datetime.strptime(fecha, '%Y-%m-%d').date(),
                hora=datetime.strptime(hora, '%H:%M').time() if len(hora) == 5 else datetime.strptime(hora, '%H:%M:%S').time(),
                estado='pendiente'
            )
            db.session.add(nueva_cita)
            db.session.commit()
            return True, "Cita creada exitosamente"
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def obtener_siguiente_cita(paciente_id):
        hoy = datetime.now().date()
        return Cita.query.filter(
            Cita.paciente_id == paciente_id,
            Cita.fecha >= hoy
        ).order_by(Cita.fecha.asc(), Cita.hora.asc()).first()

    @staticmethod
    def obtener_citas_del_dia(fecha=None):
        if not fecha:
            fecha = datetime.now().date()
        elif isinstance(fecha, str):
            fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        return Cita.query.filter_by(fecha=fecha, estado='pendiente').order_by(Cita.hora.asc()).all()

    @staticmethod
    def es_horario_disponible(fecha, hora, excluir_cita_id=None):
        fecha_dt = datetime.strptime(fecha, '%Y-%m-%d').date()
        hora_dt = datetime.strptime(hora, '%H:%M').time() if len(hora) == 5 else datetime.strptime(hora, '%H:%M:%S').time()
        
        query = Cita.query.filter_by(fecha=fecha_dt, hora=hora_dt)
        if excluir_cita_id:
            query = query.filter(Cita.id != excluir_cita_id)
        
        existente = query.first()
        return existente is None
