from app.db import get_db, query_db
from datetime import datetime

class ValoracionAntropometrica:
    @staticmethod
    def crear(paciente_id, datos):
        db = get_db()
        try:
            # Obtener el siguiente número de cita automáticamente si no se proporciona
            if 'numero_cita' not in datos or not datos['numero_cita']:
                datos['numero_cita'] = ValoracionAntropometrica.obtener_ultimo_numero_cita(paciente_id)
            
            db.execute('''
                INSERT INTO valoracion_antropometrica (
                    paciente_id, numero_cita, fecha, estatura, peso, imc, grasa,
                    cintura, torax, brazo, cadera, pierna, pantorrilla,
                    tension_arterial, frecuencia_cardiaca,
                    bicep, tricep, suprailiaco, subescapular, femoral, porcentaje_grasa,
                    ultima_dieta
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                paciente_id, datos['numero_cita'], datos['fecha'], datos.get('estatura'),
                datos.get('peso'), datos.get('imc'), datos.get('grasa'), datos.get('cintura'),
                datos.get('torax'), datos.get('brazo'), datos.get('cadera'), datos.get('pierna'),
                datos.get('pantorrilla'), datos.get('tension_arterial'), 
                datos.get('frecuencia_cardiaca'),
                datos.get('bicep'), datos.get('tricep'), datos.get('suprailiaco'),
                datos.get('subescapular'), datos.get('femoral'),
                datos.get('porcentaje_grasa'), datos.get('ultima_dieta')
            ))
            db.commit()
            return True, "Valoración antropométrica registrada correctamente."
        except Exception as e:
            db.rollback()
            return False, f"Error al registrar la valoración antropométrica: {str(e)}"

    @staticmethod
    def actualizar(valoracion_id, datos):
        db = get_db()
        try:
            db.execute('''
                UPDATE valoracion_antropometrica SET
                fecha = ?, estatura = ?, peso = ?, imc = ?, grasa = ?,
                cintura = ?, torax = ?, brazo = ?, cadera = ?, pierna = ?,
                pantorrilla = ?, bicep = ?, tricep = ?, suprailiaco = ?,
                subescapular = ?, femoral = ?, porcentaje_grasa = ?, ultima_dieta = ?
                WHERE id = ?
            ''', (
                datos['fecha'], datos['estatura'], datos['peso'], datos['imc'],
                datos['grasa'], datos['cintura'], datos['torax'], datos['brazo'],
                datos['cadera'], datos['pierna'], datos['pantorrilla'],
                datos['bicep'], datos['tricep'], datos['suprailiaco'],
                datos['subescapular'], datos['femoral'], datos['porcentaje_grasa'],
                datos.get('ultima_dieta', ''), valoracion_id
            ))
            db.commit()
            return True, "Valoración antropométrica actualizada correctamente."
        except Exception as e:
            db.rollback()
            return False, f"Error al actualizar la valoración antropométrica: {str(e)}"

    @staticmethod
    def obtener_ultima_por_paciente(paciente_id):
        return query_db('''
            SELECT * FROM valoracion_antropometrica
            WHERE paciente_id = ?
            ORDER BY numero_cita DESC
            LIMIT 1
        ''', [paciente_id], one=True)
        
    @staticmethod
    def obtener_por_paciente(paciente_id):
        return query_db('''
            SELECT * FROM valoracion_antropometrica
            WHERE paciente_id = ?
            ORDER BY fecha DESC
        ''', [paciente_id])

    @staticmethod
    def obtener_ultima_valoracion(paciente_id):
        return query_db('''
            SELECT * FROM valoracion_antropometrica
            WHERE paciente_id = ?
            ORDER BY fecha DESC
            LIMIT 1
        ''', [paciente_id], one=True)

    @staticmethod
    def obtener_todas():
        return query_db('''
            SELECT va.*, p.nombre, p.apellido_paterno, p.apellido_materno
            FROM valoracion_antropometrica va
            JOIN pacientes p ON va.paciente_id = p.id
            ORDER BY va.fecha DESC
        ''')

    @staticmethod
    def obtener_por_id(valoracion_id):
        return query_db('SELECT * FROM valoracion_antropometrica WHERE id = ?', [valoracion_id], one=True)

    @staticmethod
    def actualizar_ultima_dieta(paciente_id, ultima_dieta):
        db = get_db()
        try:
            ultima_valoracion = ValoracionAntropometrica.obtener_ultima_por_paciente(paciente_id)
            if ultima_valoracion:
                db.execute('''
                    UPDATE valoracion_antropometrica
                    SET ultima_dieta = ?
                    WHERE id = ?
                ''', (ultima_dieta, ultima_valoracion['id']))
                db.commit()
                return True, "Última dieta actualizada correctamente."
            else:
                return False, "No se encontró una valoración para actualizar."
        except Exception as e:
            db.rollback()
            return False, f"Error al actualizar la última dieta: {str(e)}"