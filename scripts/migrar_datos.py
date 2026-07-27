import sqlite3
from datetime import datetime
from sqlalchemy import text
from app import create_app, db_orm as db
from app.models.usuario import Usuario
from app.models.paciente import Paciente

def migrar():
    app = create_app()
    
    # Ruta a la base de datos antigua
    OLD_DB_PATH = 'instance/pacientes.db' 
    
    try:
        old_conn = sqlite3.connect(OLD_DB_PATH)
        old_conn.row_factory = sqlite3.Row
        cursor = old_conn.cursor()
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos antigua: {e}")
        return

    with app.app_context():
        # Limpiar tablas antes de migrar para evitar conflictos
        db.drop_all()
        db.create_all()
        
        try:
            # 1. Migrar Usuarios
            cursor.execute("SELECT * FROM usuarios")
            usuarios_old = cursor.fetchall()
            for u in usuarios_old:
                u_dict = dict(u)
                usuario = Usuario(
                    id=u_dict['id'],
                    nombre=u_dict.get('nombre', ''),
                    apellido=f"{u_dict.get('apellido_paterno', '')} {u_dict.get('apellido_materno', '')}".strip(),
                    email=u_dict.get('email', ''),
                    password_hash=u_dict['password_hash'],
                    cedula_profesional=u_dict.get('cedula_profesional'),
                    rol=u_dict.get('rol', 'nutriologa')
                )
                db.session.add(usuario)
            db.session.commit()
            print(f"Usuarios: {len(usuarios_old)} transferidos.")

            # 2. Migrar Pacientes
            cursor.execute("SELECT * FROM pacientes")
            pacientes_old = cursor.fetchall()
            for p in pacientes_old:
                p_dict = dict(p)
                
                # Convertir fecha_nacimiento a objeto date
                fecha_nac = p_dict.get('fecha_nacimiento')
                if isinstance(fecha_nac, str):
                    try:
                        fecha_nac = datetime.strptime(fecha_nac, '%Y-%m-%d').date()
                    except ValueError:
                        fecha_nac = None
                
                paciente = Paciente(
                    id=p_dict['id'],
                    nombre=p_dict.get('nombre', ''),
                    apellido=f"{p_dict.get('apellido_paterno', '')} {p_dict.get('apellido_materno', '')}".strip(),
                    fecha_nacimiento=fecha_nac,
                    sexo=p_dict.get('genero'),
                    telefono=p_dict.get('telefono'),
                    email=p_dict.get('correo'),
                    estatus=p_dict.get('status', 'activo')
                )
                db.session.add(paciente)
            db.session.commit()
            print(f"Pacientes: {len(pacientes_old)} transferidos.")

            # 3. Migrar Citas
            cursor.execute("SELECT * FROM citas")
            citas_old = cursor.fetchall()
            for c in citas_old:
                db.session.execute(
                    text("INSERT INTO citas (id, paciente_id, fecha, hora, estado) VALUES (:id, :paciente_id, :fecha, :hora, :estado)"),
                    {'id': c['id'], 'paciente_id': c['paciente_id'], 'fecha': c['fecha'], 'hora': c['hora'], 'estado': c['estado']}
                )
            db.session.commit()
            print(f"Citas: {len(citas_old)} transferidos.")

            # 4. Migrar Pagos
            cursor.execute("SELECT * FROM pagos")
            pagos_old = cursor.fetchall()
            for p in pagos_old:
                db.session.execute(
                    text("INSERT INTO pagos (id, paciente_id, fecha_pago) VALUES (:id, :paciente_id, :fecha_pago)"),
                    {'id': p['id'], 'paciente_id': p['paciente_id'], 'fecha_pago': p['fecha_pago']}
                )
            db.session.commit()
            print(f"Pagos: {len(pagos_old)} transferidos.")

            # 5. Migrar Historial Clínico
            cursor.execute("SELECT * FROM historial_clinico")
            historial_old = cursor.fetchall()
            for h in historial_old:
                db.session.execute(
                    text("""INSERT INTO historial_clinico (id, paciente_id, cirugias, padecimientos, medicamentos, suplementos, enfermedades_previas, enfermedades_actuales, tipo_actividad_fisica, frecuencia_actividad_fisica, tiempo_actividad_fisica, numero_comidas_diarias, alimentos_normales, alimentos_no_gustados) 
                       VALUES (:id, :paciente_id, :cirugias, :padecimientos, :medicamentos, :suplementos, :enfermedades_previas, :enfermedades_actuales, :tipo_actividad_fisica, :frecuencia_actividad_fisica, :tiempo_actividad_fisica, :numero_comidas_diarias, :alimentos_normales, :alimentos_no_gustados)"""),
                    dict(h)
                )
            db.session.commit()
            print(f"Historial Clínico: {len(historial_old)} transferidos.")

            # 6. Migrar Valoración Antropométrica
            cursor.execute("SELECT * FROM valoracion_antropometrica")
            valoraciones_old = cursor.fetchall()
            for v in valoraciones_old:
                db.session.execute(
                    text("""INSERT INTO valoracion_antropometrica (id, paciente_id, numero_cita, fecha, estatura, peso, imc, grasa, cintura, torax, brazo, cadera, pierna, pantorrilla, tension_arterial, frecuencia_cardiaca, bicep, tricep, suprailiaco, subescapular, femoral, porcentaje_grasa, ultima_dieta) 
                       VALUES (:id, :paciente_id, :numero_cita, :fecha, :estatura, :peso, :imc, :grasa, :cintura, :torax, :brazo, :cadera, :pierna, :pantorrilla, :tension_arterial, :frecuencia_cardiaca, :bicep, :tricep, :suprailiaco, :subescapular, :femoral, :porcentaje_grasa, :ultima_dieta)"""),
                    dict(v)
                )
            db.session.commit()
            print(f"Valoración Antropométrica: {len(valoraciones_old)} transferidos.")
            
        except Exception as e:
            db.session.rollback()
            print(f"Error durante la migración: {e}")
        finally:
            old_conn.close()

if __name__ == '__main__':
    migrar()
